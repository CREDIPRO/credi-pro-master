# Agente generador de artículos del blog Credipro

Este documento describe cómo funciona el agente automatizado que genera contenido nuevo para el blog cada semana.

## Resumen

- **Frecuencia:** cada domingo a las 9:00 AM (hora local de México)
- **Volumen:** 5 artículos nuevos por semana **en formato draft** (no se publican automáticamente)
- **Idioma:** español (México)
- **SEO:** todos los artículos incluyen meta tags, palabras clave, schema y FAQ
- **Modelo:** primero generar drafts → tú revisas → tú publicas con un comando

## Audiencias específicas que cubre

El agente rota entre estas 6 audiencias (cada una recibe un artículo aproximadamente cada 3 semanas):

| Código | Audiencia | Foco |
|--------|-----------|------|
| A | SEP / Maestros del magisterio | FOVISSSTE docentes, créditos plaza, ISSSTE para maestros |
| B | ISSSTECALI Baja California — activos | Créditos personales, hipotecarios, salud |
| C | ISSSTECALI Baja California — pensionados | Pensión, créditos retirados, prestaciones |
| D | Ayuntamiento de Tijuana | SUTAT, caja de ahorro, FONACOT, créditos sindicales |
| E | IMSS — trabajadores activos | SNTSS, RJP, préstamos sindicales |
| F | IMSS — pensionados | Modalidad 40, INAPAM, créditos para pensionados |

## Distribución semanal de los 5 artículos

- 2 artículos de audiencia específica (de la tabla arriba, rotando)
- 1 artículo sobre crédito en México (CAT, Buró, FOVISSSTE, INFONAVIT, Condusef)
- 1 artículo sobre educación financiera / ahorro / inversión
- 1 artículo sobre emprendimiento / negocio propio / ingresos extra

## Estructura de carpetas

```
blog/
├── articles.json                      # SOLO publicados (no tocar a mano)
├── articulo.html                      # Redirect a /p/{slug}/
├── index.html                         # Listado del blog
├── generate-static-pages.py           # Genera /p/{slug}/ desde articles.json
├── generate-sitemap.py                # Genera /sitemap.xml
├── publish-drafts.py                  # Mueve drafts → publicado
│
├── p/
│   └── {slug}/
│       └── index.html                 # Página estática de cada artículo
│
├── drafts/                            # ⭐ Drafts pendientes de revisión
│   ├── 2026-05-10/                    # Lote del domingo 10 de mayo
│   │   ├── README.md                  # Resumen del lote para revisar rápido
│   │   ├── drafts.json                # Datos estructurados (los lee publish-drafts.py)
│   │   ├── 01-{slug}.md               # Artículo 1 en formato lectura
│   │   ├── 02-{slug}.md
│   │   ├── 03-{slug}.md
│   │   ├── 04-{slug}.md
│   │   ├── 05-{slug}.md
│   │   ├── facebook-copys.md          # 5 copys para Facebook
│   │   └── image-prompts.md           # 5 prompts para generar imágenes
│   │
│   └── published/                     # Drafts ya publicados (histórico)
│       └── 2026-05-03/
│
├── image-prompts/                     # Prompts publicados (histórico)
└── copys-facebook.md                  # Copys publicados (acumulativo)
```

## Flujo semanal completo

### Domingo 9:00 AM (automático)
El agente genera la carpeta `blog/drafts/YYYY-MM-DD/` con:
- 5 drafts en formato JSON + 5 archivos MD individuales para leer
- Image prompts (puedes empezar a generar imágenes en paralelo)
- Copys de Facebook
- README con tabla resumen

Recibes una notificación con los 5 títulos y las audiencias elegidas.

### Lunes-Sábado (tu revisión)
1. Abre `blog/drafts/YYYY-MM-DD/`
2. Lee `README.md` para ver el resumen
3. Abre cada `01-{slug}.md` ... `05-{slug}.md` y léelos
4. Si quieres cambiar algo:
   - Edita el `.md` directamente y luego edita también `drafts.json` (los datos estructurados)
   - O dile a Claude en chat: *"edita el draft 3 y cambia X por Y"* — Claude actualiza ambos
5. Mientras revisas, puedes ir generando las imágenes con `image-prompts.md`

### Cuando estés listo (manual)
Abre Terminal y desde la raíz del proyecto:

**Publicar TODO el lote:**
```bash
python3 blog/publish-drafts.py 2026-05-10
```

**Publicar solo algunos:**
```bash
python3 blog/publish-drafts.py 2026-05-10 --slugs credito-issstecali-tijuana fondo-emergencia
```

**Ver qué pasaría sin publicar (dry-run):**
```bash
python3 blog/publish-drafts.py 2026-05-10 --dry-run
```

`publish-drafts.py` automáticamente:
1. Asigna ids consecutivos a los drafts
2. Marca destacado=true al PRIMERO de los nuevos (los anteriores destacados pasan a false)
3. Inserta los artículos al INICIO de `articles.json`
4. Regenera todas las páginas estáticas en `/blog/p/`
5. Actualiza `sitemap.xml`
6. Hace APPEND de los copys de Facebook a `copys-facebook.md`
7. Mueve la carpeta de drafts a `drafts/published/`

### Después de publicar
1. Asegúrate de tener las imágenes en `/src/assets/images/blog/{slug}.jpg` (1200x630 px)
2. Sube los cambios al servidor (`git add`, `git commit`, `git push`)
3. Publica los copys de Facebook según la frecuencia que prefieras (recomendado: 1 cada 2 días)

## Cómo modificar la tarea programada

Si quieres cambiar el día, la hora o las audiencias, pídele a Claude en chat:
*"actualiza el agente generar-articulos-blog-credipro y cambia X"*.

## Cómo lanzar el agente fuera del horario

En la barra lateral de la app de Claude, sección **Scheduled**, encuentras la tarea `generar-articulos-blog-credipro`. Click en *Run now*.

## Reglas que el agente respeta

- Nunca repite slugs ya publicados
- Nunca toca articles.json directamente (eso lo hace `publish-drafts.py` después de tu OK)
- Nunca confunde IMSS con ISSSTE/ISSSTECALI (son instituciones distintas)
- Nunca usa logos o texto de instituciones reales en los prompts de imágenes (riesgo legal)
- Para audiencias de Baja California / Tijuana, usa referencias locales reales (Mexicali, Ensenada, Rosarito, Tecate)
