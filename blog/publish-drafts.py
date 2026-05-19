#!/usr/bin/env python3
"""
Publica drafts del blog Credipro.

Flujo:
1. El agente semanal escribe drafts en /blog/drafts/YYYY-MM-DD/
   - drafts.json (datos estructurados)
   - {01..05}-{slug}.md (lectura humana)
   - facebook-copys.md (5 copys de FB)
   - image-prompts.md (5 prompts de imágenes)
2. El usuario revisa los .md
3. Cuando está listo, ejecuta:
       python3 publish-drafts.py YYYY-MM-DD
       # o publicar solo algunos:
       python3 publish-drafts.py YYYY-MM-DD --slugs slug-1 slug-3 slug-5

Lo que hace este script:
- Lee /blog/drafts/<fecha>/drafts.json
- Filtra por slugs (si se especifican)
- Reasigna ids consecutivos a partir del id máximo en articles.json
- Inserta los artículos AL INICIO de articles.json
- Marca destacado=true SOLO al primero de los nuevos; los anteriores destacados pasan a false
- Ejecuta generate-static-pages.py
- Ejecuta generate-sitemap.py
- APPENDS los copys de FB de drafts/<fecha>/facebook-copys.md al final de copys-facebook.md
- Mueve la carpeta drafts/<fecha>/ → drafts/published/<fecha>/

Uso:
    python3 publish-drafts.py 2026-05-10
    python3 publish-drafts.py 2026-05-10 --slugs "credito-issstecali-tijuana" "fondo-emergencia"
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
BLOG = ROOT / "blog"
ARTICLES_JSON = BLOG / "articles.json"
DRAFTS_DIR = BLOG / "drafts"
PUBLISHED_DIR = DRAFTS_DIR / "published"
COPYS_FB = BLOG / "copys-facebook.md"
GEN_STATIC = BLOG / "generate-static-pages.py"
GEN_SITEMAP = BLOG / "generate-sitemap.py"


def main():
    parser = argparse.ArgumentParser(description="Publica drafts del blog")
    parser.add_argument("fecha", help="Fecha del lote, formato YYYY-MM-DD")
    parser.add_argument(
        "--slugs",
        nargs="*",
        help="Slugs específicos a publicar. Si se omite, publica todos los drafts del lote.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra qué se publicaría sin hacer cambios reales",
    )
    args = parser.parse_args()

    week_dir = DRAFTS_DIR / args.fecha
    if not week_dir.exists():
        print(f"❌ No existe la carpeta de drafts: {week_dir}", file=sys.stderr)
        sys.exit(1)

    drafts_json = week_dir / "drafts.json"
    if not drafts_json.exists():
        print(f"❌ No existe {drafts_json}", file=sys.stderr)
        sys.exit(1)

    with open(drafts_json, "r", encoding="utf-8") as f:
        all_drafts = json.load(f)

    # Filtrar por slugs si se especificaron
    if args.slugs:
        wanted = set(args.slugs)
        drafts = [d for d in all_drafts if d.get("slug") in wanted]
        missing = wanted - {d.get("slug") for d in drafts}
        if missing:
            print(f"⚠️  Slugs no encontrados en drafts: {sorted(missing)}", file=sys.stderr)
        if not drafts:
            print("❌ Ninguno de los slugs solicitados existe en los drafts.", file=sys.stderr)
            sys.exit(1)
    else:
        drafts = all_drafts

    print(f"\n📦 Lote: {args.fecha}")
    print(f"📝 Drafts a publicar: {len(drafts)} de {len(all_drafts)}")
    for d in drafts:
        print(f"   - {d.get('slug')}: {d.get('titulo', '')[:60]}")

    if args.dry_run:
        print("\n🟡 DRY RUN — no se hicieron cambios.")
        return

    # Cargar articles.json existente
    with open(ARTICLES_JSON, "r", encoding="utf-8") as f:
        articles = json.load(f)

    # Calcular id máximo y reasignar ids
    max_id = max((a.get("id", 0) for a in articles), default=0)
    next_id = max_id + 1

    # Quitar destacado=true de cualquiera previo
    for a in articles:
        a["destacado"] = False

    # Asignar ids consecutivos a los drafts y marcar el PRIMERO como destacado
    for i, d in enumerate(drafts):
        d["id"] = next_id + i
        d["destacado"] = i == 0

    # Insertar al inicio del array
    new_articles = drafts + articles

    # Guardar articles.json (con backup por si algo sale mal)
    backup = ARTICLES_JSON.with_suffix(".json.bak")
    shutil.copy2(ARTICLES_JSON, backup)
    with open(ARTICLES_JSON, "w", encoding="utf-8") as f:
        json.dump(new_articles, f, ensure_ascii=False, indent=2)

    # Validar que el JSON sea parseable
    try:
        with open(ARTICLES_JSON, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido tras escribir: {e}", file=sys.stderr)
        shutil.copy2(backup, ARTICLES_JSON)
        print("   Restaurado desde backup.", file=sys.stderr)
        sys.exit(1)
    print(f"✅ articles.json actualizado ({len(new_articles)} artículos totales)")

    # Regenerar páginas estáticas
    print("\n🔨 Regenerando páginas estáticas...")
    result = subprocess.run(
        ["python3", str(GEN_STATIC)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("❌ Error en generate-static-pages.py:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)
    print(result.stdout)

    # Regenerar sitemap
    print("\n🗺️  Regenerando sitemap...")
    result = subprocess.run(
        ["python3", str(GEN_SITEMAP)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("❌ Error en generate-sitemap.py:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)
    print(result.stdout)

    # APPEND copys de Facebook al archivo acumulativo (solo de los slugs publicados)
    fb_drafts = week_dir / "facebook-copys.md"
    if fb_drafts.exists():
        published_slugs = {d["slug"] for d in drafts}
        fb_content = fb_drafts.read_text(encoding="utf-8")

        # Si publicamos TODOS los drafts, hacemos append directo
        # Si publicamos solo algunos, filtramos por slugs
        if args.slugs:
            # Parser simple: divide por "## " y mantiene solo los bloques cuyas urls coincidan
            blocks = fb_content.split("\n## ")
            kept = [blocks[0]] if blocks else []  # encabezado
            for b in blocks[1:]:
                if any(s in b for s in published_slugs):
                    kept.append(b)
            fb_content = "\n## ".join(kept)

        with open(COPYS_FB, "a", encoding="utf-8") as f:
            f.write("\n\n")
            f.write(fb_content)
        print(f"✅ Copys de Facebook agregados a {COPYS_FB.name}")

    # Mover drafts publicados a /published/
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    if args.slugs:
        # Solo se publicaron algunos: dejar la carpeta de drafts en su lugar y solo mover los archivos publicados
        # Más simple: solo registramos en un log
        log = PUBLISHED_DIR / "_partial-publishes.log"
        with open(log, "a", encoding="utf-8") as f:
            f.write(f"{args.fecha}: publicados {sorted(published_slugs)}\n")
        print(f"📝 Publicación parcial registrada en {log.name}")
        print(f"   La carpeta {week_dir} sigue ahí — borra manualmente si ya no la necesitas.")
    else:
        # Se publicó todo el lote: mover la carpeta completa
        target = PUBLISHED_DIR / args.fecha
        if target.exists():
            shutil.rmtree(target)
        shutil.move(str(week_dir), str(target))
        print(f"📁 Carpeta de drafts movida a {target}")

    print(f"\n✨ ¡{len(drafts)} artículos publicados!")
    print("\nURLs en vivo (después de subir cambios al servidor):")
    for d in drafts:
        print(f"   https://credipro.com.mx/blog/p/{d['slug']}/")


if __name__ == "__main__":
    main()
