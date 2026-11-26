# CuaderCampo — web de producto

Sitio web estático de **CuaderCampo** (https://cuadercampo.com/), el cuaderno de campo digital cuya aplicación está en https://app.cuadercampo.com/. Misma arquitectura que el sitio de Canary GPS (HTML generado con Python, partials y GitHub Pages) y la identidad de marca **Huerta**.

## Páginas (20 + 404)

Inicio · Funciones (12 módulos) · Para quién (agricultores, cooperativas, asesores, explotaciones con equipo) · Cuaderno digital SIEX · Por cultivo · Ejemplos de uso · Cómo funciona · Planes · Quiénes somos (por qué, qué hacemos, quiénes somos) · Preguntas frecuentes · Contacto · Aviso legal · Privacidad · Cookies · Mapa web. Con `sitemap.xml`, `robots.txt`, `llms.txt`, datos estructurados (Organization, SoftwareApplication, FAQPage, BreadcrumbList) y `404.html`.

Todas las páginas terminan con un formulario de contacto (en *Para cooperativas*, el de alta de cooperativa) que abre el programa de correo con el mensaje redactado. Los botones «Crear cuenta» y «Entrar» llevan a la app (`APP` en `_fuente/datos.py`).

## Identidad (paleta Huerta)

| Color | Hex | Uso |
|---|---|---|
| Bosque | `#234B2C` | Principal, botones, cabeceras |
| Salvia | `#DCE5D0` | Baldosas |
| Crema | `#F3F1E7` | Fondo |
| Terracota | `#8A3B1E` | Avisos y acentos manuscritos |
| Brote | `#7FA35E` | Mapas, checks |
| Agua | `#DCE9E6` | Riego |
| Trigo | `#F1E7CC` | Cosechas |
| Tierra | `#1E2A1F` | Texto, pie |

Tipografías: DM Sans (todo el texto; títulos 800, botones 700) y Dancing Script (solo acentos: logotipo, saludo, nombre de finca). Símbolo: cuaderno abierto con un brote (`assets/simbolo.svg`, `assets/favicon.svg`).

## Cómo editar

Las páginas se generan; no se editan a mano.

- `_fuente/datos.py` — textos: empresa, planes y precios, pasos, funciones, perfiles, cultivos, ejemplos, preguntas frecuentes, quiénes somos.
- `_fuente/config.py` — `GTM_ID` (vacío = sin etiquetas de medición).
- `_fuente/partials/` — `head`, `cabecera`, `pie`, `formulario` y campos.
- `_fuente/generar.py` — compone cada página, incluidas las maquetas de la app (móvil, mapa, validaciones) en HTML/SVG.

```
python3 _fuente/generar.py
```

## Publicación

GitHub Pages (Deploy from a branch, carpeta raíz) con dominio propio `cuadercampo.com` (archivo `CNAME`; el DNS ya apunta a GitHub Pages).

## Pendiente

- Titular, NIF y domicilio en el aviso legal y la privacidad (marcados «pendiente de completar»).
- Correo de contacto: `info@cuadercampo.com`. Confirmar y las rutas exactas de registro/alta en la app.

Planes: CuaderHuerta, CuaderFinca, CuaderExplotación y CuaderCooperativa, con precios finales con IGIC incluido e interruptor mensual/anual (`PLANES` en `_fuente/datos.py`; el anual equivale a dos meses gratis). El asistente de IA por voz y chat es el módulo `asistente` de `FUNCIONES`.
