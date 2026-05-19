# Drafts del 2026-05-17

## Cómo revisar
Abre cada archivo `01-<slug>.md` ... `05-<slug>.md` y léelo. Si quieres cambiar algo, edita el .md o el drafts.json directamente, o pídele a Claude en chat.

## Cómo publicar
- TODO: `python3 blog/publish-drafts.py 2026-05-17`
- SOLO ALGUNOS: `python3 blog/publish-drafts.py 2026-05-17 --slugs slug-1 slug-3`
- DRY RUN (ver qué pasaría): `python3 blog/publish-drafts.py 2026-05-17 --dry-run`

## Tabla de artículos generados

| # | Audiencia | Categoría | Título | Slug |
|---|-----------|-----------|--------|------|
| 1 | C | Créditos de Nómina | Crédito para Pensionados del ISSSTECALI en Baja California: Guía 2026 | credito-pensionados-issstecali-baja-california-2026 |
| 2 | F | Créditos de Nómina | Pensión IMSS Ley 73 vs Ley 97: Todo lo que Debes Saber en 2026 | pension-imss-ley-73-ley-97-credito-pensionados-2026 |
| 3 | general | Crédito en México | Condusef: Cómo Protege tus Derechos como Usuario de Crédito en México | condusef-derechos-consumidor-financiero-mexico-2026 |
| 4 | general | Educación Financiera | Cómo Salir de Deudas si Eres Empleado del Gobierno en México | como-salir-deudas-empleado-gobierno-mexico-2026 |
| 5 | general | Emprendimiento | Cómo Emprender una Tienda en Línea en México Sin Dejar tu Trabajo | negocio-digital-tienda-en-linea-empleado-gobierno-mexico-2026 |

## Audiencias en esta semana

Se eligieron las audiencias **C (ISSSTECALI – Pensionados BC)** y **F (IMSS – Pensionados)** como los 2 artículos audiencia-específica porque:

- **Audiencia C (ISSSTECALI pensionados):** Nunca había sido cubierta en ningún artículo publicado ni en drafts anteriores. Es un segmento relevante en Baja California con necesidades financieras muy específicas.
- **Audiencia F (IMSS pensionados):** Nunca había sido cubierta directamente. El artículo comparativo publicado (credito-nomina-trabajadores-imss-issste-diferencias) tocaba trabajadores *activos*, no pensionados.
- **Audiencias ya cubiertas en semanas recientes:**
  - A (SEP/Magisterio): cubierta el 2026-05-05 (publicado)
  - B (ISSSTECALI activos): cubierta en draft 2026-05-10 (pendiente de publicar)
  - D (Ayuntamiento Tijuana): cubierta en draft 2026-05-10 (pendiente de publicar)
  - E (IMSS trabajadores activos): parcialmente cubierta el 2026-05-05 (publicado)

## Nota sobre draft anterior pendiente
El lote `2026-05-10` todavía no ha sido publicado. Considera publicarlo antes o en paralelo con este lote.

## Imágenes pendientes
Después de aprobar los textos, genera las 5 imágenes con `image-prompts.md` y súbelas a `/src/assets/images/blog/<slug>.jpg` en 1200x630 px.
