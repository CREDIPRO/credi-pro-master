# Drafts del 2026-05-10

## Cómo revisar
Abre cada archivo `01-<slug>.md` ... `05-<slug>.md` y léelo. Si quieres cambiar algo, edita el .md o el drafts.json directamente, o pídele a Claude en chat.

## Cómo publicar
- TODO: `python3 blog/publish-drafts.py 2026-05-10`
- SOLO ALGUNOS: `python3 blog/publish-drafts.py 2026-05-10 --slugs slug-1 slug-3`
- DRY RUN (ver qué pasaría): `python3 blog/publish-drafts.py 2026-05-10 --dry-run`

## Tabla de artículos generados

| # | Audiencia | Categoría | Título | Slug |
|---|-----------|-----------|--------|------|
| 1 | B | Créditos de Nómina | Crédito Personal ISSSTECALI para Trabajadores de Baja California 2026 | credito-personal-issstecali-trabajadores-bc-2026 |
| 2 | D | Créditos de Nómina | Crédito de Nómina para Trabajadores del Ayuntamiento de Tijuana 2026 | credito-nomina-trabajadores-municipales-tijuana-2026 |
| 3 | general | Crédito en México | INFONAVIT vs. FOVISSSTE: ¿Cuál Conviene Más para Comprar Casa en 2026? | como-funciona-credito-infonavit-trabajadores-gobierno-2026 |
| 4 | general | Educación Financiera | Cómo Mejorar tu Score en el Buró de Crédito: Guía Real para México 2026 | como-mejorar-score-buro-credito-mexico-2026 |
| 5 | general | Emprendimiento | Cómo Generar Ingresos Extra Monetizando tus Habilidades en 2026 | como-monetizar-habilidades-ingresos-extra-trabajador-gobierno-2026 |

## Audiencias en esta semana

Se eligieron las audiencias **B (ISSSTECALI – Trabajadores activos BC)** y **D (Ayuntamiento de Tijuana)** como los 2 artículos audiencia-específica porque:

- **Audiencia B (ISSSTECALI activos):** Nunca había sido cubierta en los artículos publicados. Es uno de los segmentos clave de Credipro en Baja California.
- **Audiencia D (Ayuntamiento Tijuana):** Nunca había sido cubierta. Tijuana es el mercado principal y los trabajadores municipales tienen particularidades importantes (SUTAT, caja de ahorro municipal).
- **Audiencias ya cubiertas recientemente:** A (SEP/magisterio) cubierta el 2026-05-05. E (IMSS trabajadores) parcialmente cubierta el 2026-05-05 en el artículo comparativo.
- **Audiencias C y F (ISSSTECALI pensionados e IMSS pensionados)** quedan pendientes para las próximas semanas.

## Imágenes pendientes
Después de aprobar los textos, genera las 5 imágenes con `image-prompts.md` y súbelas a `/src/assets/images/blog/<slug>.jpg` en 1200x630 px.

| # | Nombre de archivo |
|---|-------------------|
| 1 | `credito-personal-issstecali-trabajadores-bc-2026.jpg` |
| 2 | `credito-nomina-trabajadores-municipales-tijuana-2026.jpg` |
| 3 | `como-funciona-credito-infonavit-trabajadores-gobierno-2026.jpg` |
| 4 | `como-mejorar-score-buro-credito-mexico-2026.jpg` |
| 5 | `como-monetizar-habilidades-ingresos-extra-trabajador-gobierno-2026.jpg` |
