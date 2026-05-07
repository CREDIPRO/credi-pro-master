# Prompts de imágenes para el blog CrediPro

Esta carpeta contiene los prompts de imágenes que el agente semanal genera automáticamente cada domingo.

## ¿Cómo funciona?

1. Cada domingo a las 9:00 AM, el agente programado crea un archivo aquí con el formato:
   `prompts-YYYY-MM-DD.md` (ej. `prompts-2026-05-10.md`)
2. El archivo contiene 5 prompts (uno por artículo de la semana) listos para copiar y pegar en cualquier generador de imágenes (Midjourney, DALL·E, Flux, etc.).
3. Cada prompt incluye:
   - El **slug** exacto que debe llevar la imagen como nombre de archivo
   - Una descripción en inglés optimizada para generadores de imágenes
   - Especificación de relación de aspecto (16:9 horizontal) y estilo
   - Notas de paleta de colores de marca CrediPro

## ¿Dónde subir las imágenes una vez generadas?

Las imágenes finales deben colocarse en:
`/src/assets/images/blog/{slug}.jpg`

Donde `{slug}` es exactamente el slug que aparece en el prompt y en `articles.json`.

**Ejemplo:** Si el slug es `como-mejorar-buro-credito-2026`, la imagen debe llamarse:
`/src/assets/images/blog/como-mejorar-buro-credito-2026.jpg`

## Especificaciones técnicas para las imágenes

- **Formato:** JPG (preferido) o WebP
- **Resolución:** **1200 x 630 px exactos** (relación 1.91:1) — esta es la dimensión oficial recomendada por Facebook para mostrar el preview GRANDE en el feed (imagen completa arriba, texto abajo). Si usas otra relación, FB muestra el preview compacto y la imagen se ve pequeña/borrosa.
- **Peso:** menor a 250 KB (comprimir con TinyPNG si es necesario; FB acepta hasta 8 MB pero pesado = lento)
- **Estilo:** fotografía profesional o ilustración moderna, paleta de marca (azul #023047, turquesa #219EBC, ámbar #FFB703)
- **Sin texto sobre la imagen** (el sitio agrega el título encima, además FB castiga imágenes con mucho texto)
