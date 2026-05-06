# Agente generador de artículos del blog CrediPro

Este documento describe cómo funciona el agente automatizado que genera contenido nuevo para el blog cada semana.

## Resumen

- **Frecuencia:** cada domingo a las 9:00 AM (hora local de México)
- **Volumen:** 5 artículos nuevos por semana
- **Audiencia:** mezcla de trabajadores del gobierno (≈3 artículos) y público general mexicano interesado en finanzas, crédito y emprendimiento (≈2 artículos)
- **Idioma:** español (México)
- **SEO:** todos los artículos incluyen meta tags, palabras clave, schema y FAQ (los esquemas se renderizan automáticamente en `articulo.html`)

## Archivos que toca el agente

| Archivo | Acción |
|---|---|
| `blog/articles.json` | Inserta los 5 artículos nuevos al inicio del array |
| `blog/image-prompts/prompts-YYYY-MM-DD.md` | Crea un archivo nuevo con los 5 prompts de imágenes |

El agente **no toca HTML ni JS**, porque `index.html` y `articulo.html` ya leen `articles.json` dinámicamente.

## Flujo semanal del usuario

1. **Domingo 9:00 AM** → el agente corre y genera artículos + prompts.
2. **Domingo / Lunes** → tú abres `blog/image-prompts/prompts-YYYY-MM-DD.md`, copias cada prompt y lo pegas en tu generador de imágenes preferido (Midjourney, DALL·E, Flux, etc.).
3. **Subes las imágenes** a `src/assets/images/blog/` con el nombre exacto del slug (ej. `como-pagar-buro-credito.jpg`).
4. Mientras subes las imágenes, los artículos ya están publicados con un placeholder. Una vez que la imagen real exista en la ruta esperada, automáticamente reemplaza al placeholder (porque la ruta apunta al slug).

## Sobre el placeholder de imágenes

Cuando el agente crea un artículo nuevo, asigna como `imagen` la ruta:

```
../src/assets/images/blog/{slug}.jpg
```

Si **todavía no subes** la imagen real con ese nombre, el navegador mostrará una imagen rota. Para evitar eso, el agente además agrega un atributo `imagenFallback` con la ruta a `../src/assets/images/credi2.jpg` (una imagen genérica de la marca que ya existe). Cuando subas la imagen real con el slug correcto, automáticamente la usa sin que tengas que cambiar nada en el JSON.

## Categorías que rota el agente

- Créditos de Nómina
- Educación Financiera
- Crédito en México
- Emprendimiento
- Ahorro e Inversión
- Sobre CrediPro

## Cómo lanzar el agente manualmente

Si quieres generar artículos antes del próximo domingo:

1. Abre la app de Claude
2. Ve a la sección de **Tareas programadas** o pídele a Claude: *"corre la tarea generar-articulos-blog ahora"*
3. La tarea se ejecuta inmediatamente sin esperar al domingo.

## Cómo modificar la tarea

Si quieres cambiar el día, la hora, los temas o el número de artículos:

1. Pídele a Claude: *"actualiza la tarea programada generar-articulos-blog y cambia X"*
2. Claude buscará la tarea, leerá su prompt actual y aplicará los cambios.

## Ejemplos de temas que el agente puede tocar

- "Cómo mejorar tu Buró de Crédito en 2026"
- "Diferencias entre crédito de nómina e ISSSTE"
- "Cómo emprender un negocio desde casa siendo trabajador del gobierno"
- "Qué es el CAT y por qué importa al pedir crédito"
- "Estrategias de ahorro con la regla 50/30/20"
- "Cómo armar tu fondo de emergencia en 6 meses"
- "Aguinaldo 2026: cómo invertirlo en lugar de gastarlo"
- "FOVISSSTE: requisitos y cómo combinarlo con un crédito"
