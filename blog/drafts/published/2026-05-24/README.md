# Drafts del 2026-05-24

## Cómo revisar
Abre cada archivo `01-<slug>.md` ... `05-<slug>.md` y léelo. Si quieres cambiar algo, edita el .md o el drafts.json directamente, o pídele a Claude en chat.

## Cómo publicar
- TODO: `python3 blog/publish-drafts.py 2026-05-24`
- SOLO ALGUNOS: `python3 blog/publish-drafts.py 2026-05-24 --slugs slug-1 slug-3`
- DRY RUN (ver qué pasaría): `python3 blog/publish-drafts.py 2026-05-24 --dry-run`

## Tabla de artículos generados

| # | Audiencia | Categoría | Título | Slug |
|---|-----------|-----------|--------|------|
| 1 | E (IMSS trabajadores activos) | Créditos de Nómina | Crédito Sindical SNTSS: Guía Completa para Trabajadores del IMSS 2026 | credito-sindical-sntss-trabajadores-imss-2026 |
| 2 | A (SEP / Maestros) | Créditos de Nómina | FOVISSSTE para Maestros: Cómo Obtener Crédito de Vivienda Siendo Docente en 2026 | fovissste-maestros-credito-vivienda-docentes-2026 |
| 3 | general | Crédito en México | FOVISSSTE 2026: Guía Completa para Trabajadores del Gobierno | fovissste-2026-como-funciona-trabajadores-gobierno |
| 4 | general | Educación Financiera | CETES 2026: La Inversión Más Segura para Trabajadores del Gobierno en México | invertir-cetes-trabajador-gobierno-mexico-2026 |
| 5 | general | Emprendimiento | Cómo Registrar tu Negocio en el SAT Siendo Empleado del Gobierno en 2026 | registrar-negocio-sat-empleado-gobierno-mexico-2026 |

## Audiencias en esta semana

**Audiencia E — IMSS trabajadores activos** (artículo 1)
- Nunca había sido cubierta explícitamente como audiencia principal en artículos anteriores. Máxima prioridad.
- Tema elegido: crédito sindical SNTSS, un beneficio real que muchos trabajadores del IMSS desconocen.

**Audiencia A — SEP / Maestros del magisterio** (artículo 2)
- Último artículo: 2026-05-05 (hace 19 días). Ya dentro de la ventana de rotación de 3 semanas.
- Tema elegido: FOVISSSTE para maestros — crédito de vivienda, temática nueva (el artículo anterior era sobre crédito de nómina general).

**Audiencias excluidas esta semana:**
- C (ISSSTECALI pensionados): cubierta hace 7 días — demasiado reciente.
- F (IMSS pensionados): cubierta hace 7 días — demasiado reciente.
- B (ISSSTECALI activos): cubierta hace 14 días — esperar.
- D (Ayuntamiento Tijuana): cubierta hace 14 días — esperar.

## Imágenes pendientes
Después de aprobar los textos, genera las 5 imágenes con `image-prompts.md` y súbelas a `/src/assets/images/blog/<slug>.jpg` en 1200x630 px.

## Notas del lote
- El artículo 3 (FOVISSSTE general) y el artículo 2 (FOVISSSTE maestros) son complementarios pero distintos: uno es la guía general del instrumento, el otro es el enfoque específico para docentes. No se solapan en términos de audiencia ni keyword principal.
- El artículo 4 (CETES) cubre por primera vez el tema de inversión en valores gubernamentales, que no había sido abordado en artículos anteriores.
- El artículo 5 (SAT + negocio) es distinto a los artículos de emprendimiento previos (negocio desde casa, tienda en línea, monetizar habilidades) — este aborda el aspecto fiscal/legal.
