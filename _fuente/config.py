# -*- coding: utf-8 -*-
"""Configuración de etiquetado del sitio (único punto de edición).

El sitio es HTML estático generado con `python3 _fuente/generar.py`, sin
GitHub Actions: los valores se escriben en las páginas al regenerarlas.
"""

# Google Tag Manager. Vacío = sin etiquetas de medición. Al rellenarlo con el ID
# del contenedor (GTM-XXXXXXX) se añade en <head> y tras <body> en todas las páginas.
# Antes de activarlo, añade un banner de consentimiento de cookies.
GTM_ID = ''
