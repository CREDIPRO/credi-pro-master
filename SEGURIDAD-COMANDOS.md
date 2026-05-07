# 🚨 Resolver alerta de GitHub: API keys expuestas

Sigue estos comandos en orden. Abre tu Terminal en macOS, copia y pega cada comando uno a uno.

## ¿Qué pasó?

Un archivo llamado `512.html` se subió por error a `src/assets/images/blog/`. Era una página HTML guardada de Google Docs/Drive (parece un documento "Bonos por alcance de..."). Cuando guardas una página de Google Docs como HTML, Google embebe sus propias API keys internas en el código. GitHub detectó esas keys y por eso te llegaron las 20 alertas.

**Importante:** esas keys NO son tuyas. Son keys internas de Google. No tienes acceso para "rotarlas" ni costo asociado a ellas — son de la infraestructura de Google. Pero igual hay que sacarlas del repo para que GitHub deje de marcarlas.

## Paso 1 — Asegúrate de estar en la carpeta del proyecto

```bash
cd ~/Documents/credi-pro-master
```

## Paso 2 — Confirma que el archivo ya no está y revisa los cambios

```bash
ls src/assets/images/blog/512.html 2>&1
git status
```

Lo primero debe responder "No such file or directory". Lo segundo debe mostrar el archivo borrado y los nuevos archivos creados (gitignore, sitemap, etc.).

## Paso 3 — Quitar archivos basura del index de git

Los `.DS_Store` ya estaban versionados y los borramos. También sacamos del index los archivos antiguos que no deberían estar:

```bash
git rm --cached -r --ignore-unmatch '**/.DS_Store' 2>/dev/null
git rm --cached --ignore-unmatch 'src/assets/images/blog/512.html' 2>/dev/null
```

## Paso 4 — Hacer commit del cambio

```bash
git add .gitignore
git add -A
git commit -m "security: eliminar 512.html con API keys expuestas + .DS_Store + agregar .gitignore"
```

## Paso 5 — Reescribir la historia de git para borrar las keys del pasado

**Esto es lo más importante.** Borrar el archivo del HEAD no es suficiente: GitHub sigue mostrando el secreto si está en algún commit anterior. Hay que reescribir la historia.

La forma más fácil: usa `git filter-repo` (es la herramienta recomendada por GitHub).

### Instalar git-filter-repo (una sola vez)

```bash
brew install git-filter-repo
```

Si no tienes Homebrew, instálalo primero:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Reescribir la historia

```bash
# Asegúrate de que tu working tree esté limpio
git status

# Hacer un backup local por si algo sale mal (recomendado)
cd ~/Documents
cp -r credi-pro-master credi-pro-master-BACKUP-$(date +%Y%m%d)
cd credi-pro-master

# Eliminar el archivo de toda la historia de git
git filter-repo --invert-paths --path src/assets/images/blog/512.html --force
```

## Paso 6 — Force push al repo remoto

```bash
git push origin --force --all
git push origin --force --tags
```

⚠️ **Importante:** este `--force` reescribe lo que está en GitHub. Si trabajas con más personas en este repo, avísales antes para que hagan un fresh clone después; sus copias locales quedarán desfasadas.

## Paso 7 — Cerrar las alertas en GitHub

1. Ve a tu repo: https://github.com/CREDIPRO/credi-pro-master
2. Click en la pestaña **Security** (o el ícono de escudo arriba)
3. Click en **Secret scanning alerts**
4. Por cada una de las 20 alertas:
   - Click en la alerta
   - Marca como **"Revoked"** o **"Won't fix"** (estas keys no son tuyas, no las puedes revocar — usa "Won't fix" con la nota: "Google internal API keys from a Google Docs HTML export, not customer keys, file removed and history rewritten")

## Paso 8 — Verifica

```bash
# Buscar si todavía hay keys de Google en cualquier commit del proyecto
git log --all --full-history -- src/assets/images/blog/512.html
# Debe responder vacío

# Buscar el patrón en TODA la historia
git rev-list --all | xargs git grep "AIza" 2>/dev/null | head
# Debe responder vacío
```

## Si algo sale mal

Tienes el backup en `~/Documents/credi-pro-master-BACKUP-YYYYMMDD/`. Para restaurar:

```bash
cd ~/Documents
rm -rf credi-pro-master
cp -r credi-pro-master-BACKUP-YYYYMMDD credi-pro-master
```

Luego dime qué pasó y lo arreglamos.

---

## Resumen rápido (si ya sabes git)

```bash
cd ~/Documents/credi-pro-master
git rm --cached -r --ignore-unmatch '**/.DS_Store' 2>/dev/null
git add -A
git commit -m "security: eliminar 512.html + .DS_Store + agregar .gitignore"

# instalar filter-repo si no lo tienes
brew install git-filter-repo

# reescribir historia
git filter-repo --invert-paths --path src/assets/images/blog/512.html --force

# force push
git push origin --force --all

# luego cerrar las 20 alertas en GitHub Security tab como "won't fix"
```
