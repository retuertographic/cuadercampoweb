# -*- coding: utf-8 -*-
"""Genera el sitio estático de CuaderCampo (cuadercampo.com).

Uso:  python3 _fuente/generar.py
"""
import json
import os
import re
from html import escape, unescape

from datos import (EMPRESA, APP, PENDIENTE, PLANES, PLAN_DESTACADO, PRUEBA_DIAS, PASOS, FUNCIONES,
                   TONOS, SOLUCIONES, CULTIVOS, EJEMPLOS, FAQ_GENERAL, POR_QUE, QUE_HACEMOS, VALORES,
                   HISTORIA, EQUIPO)
from config import GTM_ID

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANIO = 2026
BASE = EMPRESA['base_url']

# ---------------------------------------------------------------- Iconos (trazo, 24×24)
_P = {
    'mail': '<path d="M3.5 6h17v12h-17z"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    'pin': '<path d="M12 21s6.5-6 6.5-11a6.5 6.5 0 1 0-13 0C5.5 15 12 21 12 21Z"/><circle cx="12" cy="10" r="2.4"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'flecha': '<path d="M5 12h13"/><path d="m12.5 5.5 6.5 6.5-6.5 6.5"/>',
    'abajo': '<path d="m6.5 9.5 5.5 5 5.5-5"/>',
    'arriba': '<path d="M12 19V6"/><path d="m5.5 12.5 6.5-6.5 6.5 6.5"/>',
    'check': '<path d="m4.5 12.5 4.5 4.5 10.5-10.5"/>',
    'mas': '<path d="M12 5v14M5 12h14"/>',
    'mapa': '<path d="m3.5 6 5.5-2 6 2 5.5-2v14l-5.5 2-6-2-5.5 2z"/><path d="M9 4v14M15 6v14"/>',
    'brote': '<path d="M12 21v-9"/><path d="M12 12c0-4.5 3-7.5 7.5-7.5 0 4.5-3 7.5-7.5 7.5Z"/><path d="M12 15c0-3.5-2.4-6-6-6 0 3.5 2.4 6 6 6Z"/>',
    'matraz': '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/>',
    'gota-hoja': '<path d="M12 3.5s5.5 6 5.5 10a5.5 5.5 0 0 1-11 0c0-4 5.5-10 5.5-10Z"/><path d="M12 18.5v-5l2.5-2.5"/>',
    'agua': '<path d="M12 3.5s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11Z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
    'cesta': '<path d="M3.5 10h17l-2 10h-13z"/><path d="m8 10 3-6M16 10l-3-6"/><path d="M9 14v3M12 14v3M15 14v3"/>',
    'azada': '<path d="M5 21 15 11"/><path d="M13 5.5 18.5 11l2-2c-1-2.5-3-4.5-5.5-5.5z"/>',
    'cajas': '<path d="M3.5 12h8v8.5h-8zM12.5 12h8v8.5h-8zM8 3.5h8V12H8z"/>',
    'personas': '<circle cx="9" cy="8" r="3"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><path d="M15.5 5.3a3 3 0 0 1 0 5.4M17.5 19a5.5 5.5 0 0 0-2.5-4.6"/>',
    'insignia': '<circle cx="12" cy="9" r="5.5"/><path d="m9 13.8-1.5 7.2 4.5-2.5 4.5 2.5-1.5-7.2"/><path d="m10 9 1.5 1.5 3-3"/>',
    'edificio': '<path d="M4 21V8l8-4.5L20 8v13"/><path d="M2.5 21h19"/><path d="M8.5 21v-6h7v6M8.5 11h1M14.5 11h1"/>',
    'sello': '<path d="M12 3.2 19 6v6c0 4.4-3 7.6-7 8.8-4-1.2-7-4.4-7-8.8V6Z"/><path d="m9 12 2 2 4-4"/>',
    'escudo': '<path d="M12 3.2 19 6v6c0 4.4-3 7.6-7 8.8-4-1.2-7-4.4-7-8.8V6Z"/><rect x="9" y="10.5" width="6" height="5" rx="1"/><path d="M10.2 10.5V9a1.8 1.8 0 0 1 3.6 0v1.5"/>',
    'tractor': '<circle cx="7" cy="16" r="4"/><circle cx="18" cy="17.5" r="2.5"/><path d="M5 12V5.5h6l2 6.5h6v5"/><path d="M11 16h4.5"/>',
    'oliva': '<path d="M5 19c4-1 9-6 14-14"/><ellipse cx="9.5" cy="10.5" rx="2.6" ry="3.8" transform="rotate(-35 9.5 10.5)"/><ellipse cx="15.5" cy="14" rx="2.2" ry="3.2" transform="rotate(-60 15.5 14)"/>',
    'uva': '<circle cx="9" cy="10" r="2.2"/><circle cx="13.5" cy="10" r="2.2"/><circle cx="11.2" cy="14" r="2.2"/><circle cx="11.2" cy="18" r="2.2"/><path d="M11.5 7.8V4.5c1.5 0 3 .5 4 1.5"/>',
    'citrico': '<circle cx="12" cy="13" r="7"/><path d="M12 6V3.5c2 0 3.5 1 4 2.5"/><path d="M12 13 7.5 9.5M12 13l4.5-3.5M12 13v6"/>',
    'manzana': '<path d="M12 7.5c-3-2-7-.5-7 4.5 0 4.5 3 8.5 5 8.5 1 0 1.3-.5 2-.5s1 .5 2 .5c2 0 5-4 5-8.5 0-5-4-6.5-7-4.5Z"/><path d="M12 7.5V4M12 5.5c1-1.5 2.5-2 4-2"/>',
    'hoja': '<path d="M5 19C5 10 10 5 19.5 4.5 19 14 14 19 5 19Z"/><path d="M5 19 13 11"/>',
    'espiga': '<path d="M12 21V8"/><path d="M12 8c-2-1-2.5-3-2-5 2 .5 3 2.5 2 5Zm0 0c2-1 2.5-3 2-5-2 .5-3 2.5-2 5Z"/><path d="M12 13c-2.5-.5-3.5-2.5-3.5-4.5 2.2.3 3.5 2 3.5 4.5Zm0 0c2.5-.5 3.5-2.5 3.5-4.5-2.2.3-3.5 2-3.5 4.5Z"/><path d="M12 18c-2.5-.5-3.5-2.5-3.5-4.5 2.2.3 3.5 2 3.5 4.5Zm0 0c2.5-.5 3.5-2.5 3.5-4.5-2.2.3-3.5 2-3.5 4.5Z"/>',
    'almendra': '<path d="M12 3.5c4 3 6 7 6 10.5a6 6 0 0 1-12 0c0-3.5 2-7.5 6-10.5Z"/><path d="M12 7c-1 3-1 7 0 12"/>',
    'palmera': '<path d="M12 21c0-5 .5-9 1.5-12"/><path d="M13.5 9C11 6 7.5 5.5 4.5 7M13.5 9c1-3.5 4-5 7-4.5M13.5 9c3 0 5.5 1.5 6.5 4.5M13.5 9C10.5 9.5 8 11.5 7.5 14.5"/><path d="M8 21h9"/>',
    'info': '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5"/><path d="M12 7.8v.1"/>',
    'pregunta': '<circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.5a2.5 2.5 0 1 1 3.4 2.3c-.6.3-1 .8-1 1.5v.4"/><path d="M12 16.6v.1"/>',
    'etiqueta': '<path d="M3.5 12.5V4h8.5l8.5 8.5-8.5 8.5z"/><circle cx="8" cy="8.5" r="1.3"/>',
    'llave': '<circle cx="8" cy="15" r="4"/><path d="m11 12 8.5-8.5"/><path d="m16.5 6.5 2.5 2.5M14 9l2 2"/>',
    'regalo': '<path d="M4 11h16v9.5H4zM3 7.5h18V11H3z"/><path d="M12 7.5v13"/><path d="M12 7.5C10 7.5 7.5 6.5 8 4.5s4 0 4 3Zm0 0c2 0 4.5-1 4-3s-4 0-4 3Z"/>',
    'reloj': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    'doc': '<path d="M6 3.5h8l4 4v13H6z"/><path d="M14 3.5v4h4"/><path d="M9 12h6M9 15.5h6"/>',
    'engranaje': '<circle cx="12" cy="12" r="3"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"/>',
    'movil': '<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>',
    'aviso': '<path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>',
    'corazon': '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.3 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10Z"/>',
    'estrella': '<path d="m12 3.5 2.6 5.5 6 .8-4.4 4.2 1.1 6-5.3-2.9-5.3 2.9 1.1-6L3.4 9.8l6-.8z"/>',
    'descarga': '<path d="M12 4v11"/><path d="m7 10.5 5 5 5-5"/><path d="M4.5 19.5h15"/>',
    'cuaderno': '<path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/><path d="M12 7v14"/>',
    'whatsapp': '<path d="M4.5 19.5 5.6 16A8 8 0 1 1 8.4 18.7z"/><path d="M9.2 8.6c.3 2.9 2.3 5 5.2 5.6l1.2-1.3-1.8-1-.8.7c-1-.5-1.8-1.3-2.3-2.3l.7-.8-1-1.8z"/>',
    'microfono': '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0"/><path d="M12 17.5V21M8.5 21h7"/>',
    'chat': '<path d="M4 5.5h16v11H9l-5 4z"/><path d="M8 10h8M8 13h5"/>',
    'chispa': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><path d="m12 8 1.5 2.5L16 12l-2.5 1.5L12 16l-1.5-2.5L8 12l2.5-1.5z"/>',
    'firma': '<path d="M3 17c3 0 4-8 6-8s0 8 2 8 3-4 4.5-4 1 3 2.5 3h3"/><path d="M3 21h18"/>',
}


def ico(nombre):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % _P[nombre])


def e(s):
    return escape(s, quote=True)


# ---------------------------------------------------------------- Marca
def simbolo(tam=44, completo=True):
    """Símbolo de CuaderCampo: cuaderno abierto con un brote (manual de marca)."""
    extra = ('<path d="M48 32v36" stroke="#234B2C" stroke-width="3" stroke-linecap="round"/>'
             '<path d="M48 56c0-8-5-13-13-14 0 8 5 13 13 14z" fill="#A9C48A"/>') if completo else ''
    lineas = ('<path d="M27 58c7-2 13-2 18 1M51 59c5-3 11-3 18-1" stroke="#C9BFA6" stroke-width="2" '
              'stroke-linecap="round" fill="none"/>') if completo and tam >= 40 else ''
    return ('<svg class="simbolo" width="%d" height="%d" style="width:%dpx;height:%dpx" viewBox="0 0 96 96" aria-hidden="true">'
            '<rect width="96" height="96" rx="26" fill="#234B2C"/>'
            '<path d="M20 66c9-4 19-4 28 2 9-6 19-6 28-2V30c-9-4-19-4-28 2-9-6-19-6-28-2z" fill="#F3F1E7"/>'
            '%s<path d="M48 50c0-11 7-18 17-19 0 11-7 18-17 19z" fill="#7FA35E"/>%s</svg>') % (tam, tam, tam, tam, extra, lineas)


def logo(claro=False):
    cls = ' claro' if claro else ''
    return ('%s<span class="marca%s"><span class="marca-c">Cuader</span><span class="marca-s">Campo</span></span>'
            % (simbolo(44), cls))


# ---------------------------------------------------------------- Partials
PARTIALS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'partials')
_cache = {}
_RE_ICO = re.compile(r'\{\{\s*ico:([a-z-]+)\s*\}\}')
_RE_VAR = re.compile(r'\{\{\s*([a-z_]+)\s*\}\}')


def parcial(nombre, **ctx):
    if nombre not in _cache:
        with open(os.path.join(PARTIALS, nombre + '.html'), encoding='utf-8') as f:
            _cache[nombre] = f.read().rstrip('\n')
    html = _RE_ICO.sub(lambda m: ico(m.group(1)), _cache[nombre])

    def var(m):
        if m.group(1) not in ctx:
            raise KeyError('Falta «%s» en el partial %s.html' % (m.group(1), nombre))
        return str(ctx[m.group(1)])
    html = _RE_VAR.sub(var, html)
    if '{{' in html:
        raise ValueError('Marca sin resolver en el partial %s.html' % nombre)
    return html


COMUN = dict(email=EMPRESA['email'], whatsapp=EMPRESA['whatsapp'], app_entrar=APP['entrar'], app_crear=APP['crear'], prueba=PRUEBA_DIAS)

# ---------------------------------------------------------------- Menú
NAV = [
    ('index', 'Inicio'),
    ('funciones', 'Funciones'),
    ('para-quien', 'Para quién'),
    ('cuaderno-digital-siex', 'SIEX'),
    ('como-funciona', 'Cómo funciona'),
    ('planes', 'Planes'),
    ('quienes-somos', 'Quiénes somos'),
    ('preguntas-frecuentes', 'FAQ'),
    ('contacto', 'Contacto'),
]


# ---------------------------------------------------------------- Datos estructurados
def datos_estructurados(url, cuerpo, extra=None):
    grafo = [{
        '@type': 'Organization', '@id': BASE + '#org', 'name': 'CuaderCampo', 'url': BASE,
        'logo': BASE + 'assets/icono-512.png', 'image': BASE + 'assets/og.png', 'email': EMPRESA['email'],
        'slogan': EMPRESA['lema'],
        'description': 'Cuaderno de campo digital para agricultores y cooperativas, preparado para el SIEX.',
        'areaServed': {'@type': 'Country', 'name': 'España'},
    }, {
        '@type': 'WebSite', '@id': BASE + '#web', 'url': BASE, 'name': 'CuaderCampo',
        'inLanguage': 'es', 'publisher': {'@id': BASE + '#org'},
    }, {
        '@type': 'WebPage', '@id': url, 'url': url, 'inLanguage': 'es',
        'isPartOf': {'@id': BASE + '#web'}, 'about': {'@id': BASE + '#app'},
    }]
    migas = ld_migas(url, cuerpo)
    if migas:
        grafo.append(migas)
        grafo[2]['breadcrumb'] = {'@id': migas['@id']}
    grafo += extra or []
    datos = json.dumps({'@context': 'https://schema.org', '@graph': grafo}, ensure_ascii=False)
    return '<script type="application/ld+json">%s</script>' % datos.replace('</', '<\\/')


def ld_migas(url, cuerpo):
    m = re.search(r'<div class="crumbs">(.*?)</div>', cuerpo)
    if not m:
        return None
    pasos = [(BASE + h, unescape(t)) for h, t in re.findall(r'<a href="([^"#]+)">([^<]+)</a>', m.group(1))]
    pasos.append((url, unescape(re.sub(r'<[^>]+>', '', m.group(1).rsplit('</span>', 1)[-1]))))
    return {'@type': 'BreadcrumbList', '@id': url + '#migas', 'itemListElement': [
        {'@type': 'ListItem', 'position': i, 'name': n, 'item': u} for i, (u, n) in enumerate(pasos, 1)]}


def ld_app():
    ofertas = []
    for clave, nombre, _para, mensual, anual, _inc in PLANES:
        if clave == 'cooperativa':
            continue
        for periodo, (precio, _suf, _txt) in (('mensual', mensual), ('anual', anual)):
            if clave == 'huerta' and periodo == 'anual':
                continue
            ofertas.append({'@type': 'Offer', 'name': '%s (%s)' % (nombre, periodo),
                            'price': precio.replace(' €', '').replace(',', '.'), 'priceCurrency': 'EUR',
                            'description': 'Precio por mes con impuestos incluidos, facturación %s' % periodo,
                            'url': BASE + 'planes.html'})
    return {
        '@type': 'SoftwareApplication', '@id': BASE + '#app', 'name': 'CuaderCampo',
        'applicationCategory': 'BusinessApplication', 'applicationSubCategory': 'Cuaderno de campo agrícola',
        'operatingSystem': 'Web, Android, iOS (aplicación web instalable)', 'url': APP['entrar'],
        'description': 'Cuaderno de campo digital conforme al SIEX: recintos SIGPAC, plantaciones, tratamientos, fertilización, riego, cosechas e inventario para agricultores y cooperativas.',
        'image': BASE + 'assets/og.png', 'inLanguage': 'es', 'publisher': {'@id': BASE + '#org'},
        'featureList': [f[3] for f in FUNCIONES],
    }


def ld_faq(lista):
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': r}} for q, r in lista]}


# ---------------------------------------------------------------- Esqueleto
def pagina(slug, titulo, descripcion, cuerpo, activo=None, form=True, ld=None, form_kw=None):
    url = BASE + ('' if slug == 'index' else slug + '.html')
    nav_items = ''.join(
        '<li><a href="%s.html"%s>%s</a></li>' % (
            s, ' class="active" aria-current="%s"' % ('page' if s == slug else 'true') if s == activo else '', n)
        for s, n in NAV)
    li = lambda s, i, n: '<li><a href="%s.html">%s<span>%s</span></a></li>' % (s, ico(i), n)
    prod_links = ''.join(li(*x) for x in [
        ('funciones', 'cuaderno', 'Funciones'), ('cuaderno-digital-siex', 'sello', 'Cuaderno digital SIEX'),
        ('como-funciona', 'engranaje', 'Cómo funciona'), ('planes', 'etiqueta', 'Planes'),
        ('cultivos', 'brote', 'Por cultivo'), ('ejemplos', 'estrella', 'Ejemplos de uso')])
    sol_links = ''.join(li(s['slug'], s['ico'], s['nombre']) for s in SOLUCIONES)
    emp_links = ''.join(li(*x) for x in [
        ('quienes-somos', 'personas', 'Quiénes somos'), ('preguntas-frecuentes', 'pregunta', 'Preguntas frecuentes'),
        ('contacto', 'mail', 'Contacto')]) + \
        '<li><a href="%s" rel="noopener">%s<span>Entrar en la app</span></a></li>' % (APP['entrar'], ico('llave'))
    if form:
        cuerpo += form_contacto(**(form_kw or {}))
    if slug == '404':
        enlaces_seo = '<meta name="robots" content="noindex">'
        jsonld = ''
    else:
        enlaces_seo = '<link rel="canonical" href="%s">\n<meta property="og:url" content="%s">' % (url, url)
        jsonld = datos_estructurados(url, cuerpo, ld)
    gtm_head = gtm_body = ''
    if GTM_ID:
        gtm_head = ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
                    "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
                    "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
                    "})(window,document,'script','dataLayer','%s');</script>" % GTM_ID)
        gtm_body = ('<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%s" height="0" width="0" '
                    'style="display:none;visibility:hidden"></iframe></noscript>' % GTM_ID)
    html = '\n'.join([
        parcial('head', titulo=e(titulo), descripcion=e(descripcion), og_img=BASE + 'assets/og.png',
                enlaces_seo=enlaces_seo, jsonld=jsonld, gtm_head=gtm_head),
        parcial('cabecera', nav_items=nav_items, logo=logo(), gtm_body=gtm_body, **COMUN),
        '', '<main id="contenido" tabindex="-1">', cuerpo, '</main>',
        parcial('pie', prod_links=prod_links, sol_links=sol_links, emp_links=emp_links, anio=ANIO,
                logo_claro=logo(claro=True), **COMUN),
    ]) + '\n'
    return re.sub(r'\n{3,}', '\n\n', html)


def form_contacto(titulo='¿Hablamos de tu finca?',
                  texto='Cuéntanos qué cultivas, cuántas hectáreas llevas o qué necesita tu cooperativa. Te respondemos personas, no un robot, y te ayudamos a dar de alta tu primera finca.',
                  asunto='Consulta desde la web', boton='Enviar por WhatsApp', ancla='escribenos', campos='contacto'):
    if campos == 'contacto':
        opc = ''.join('<option>%s</option>' % o for o in
                      ['Agricultor o agricultora', 'Cooperativa o SAT', 'Técnico de cooperativa', 'Explotación grande'])
        html_campos = parcial('campos-contacto', opciones=opc)
    else:
        html_campos = parcial('campos-cooperativa')
    return parcial('formulario', titulo=titulo, texto=texto, asunto=asunto, boton=boton, ancla=ancla,
                   campos=html_campos, **COMUN)


# ---------------------------------------------------------------- Bloques
def page_head(titulo, texto, migas, antetitulo=None, acciones=''):
    m = '<a href="index.html">Inicio</a>'
    for href, txt in migas[:-1]:
        m += '<span>/</span><a href="%s">%s</a>' % (href, txt)
    m += '<span>/</span>' + migas[-1][1]
    ante = '<span class="eyebrow">%s</span>\n  ' % antetitulo if antetitulo else ''
    acc = '\n  <div class="actions">%s</div>' % acciones if acciones else ''
    return f'''<div class="page-head"><div class="wrap">
  <div class="crumbs">{m}</div>
  {ante}<h1>{titulo}</h1>
  <p>{texto}</p>{acc}
</div>{surcos()}</div>'''


def surcos(alto=False):
    """Borde inferior en forma de lomas de cultivo, en dos capas: una loma de Brote
    y, delante, el Crema de la sección siguiente (así el corte se lee como paisaje)."""
    clase = 'surcos surcos-alto' if alto else 'surcos'
    return ('<svg class="%s" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M0 62C180 18 380 14 600 44s420 50 600 18 200-34 240-30v88H0z" fill="#A9C48A" fill-opacity=".55"/>'
            '<path d="M0 92c200-38 420-44 660-18s440 34 620 6c70-11 130-14 160-12v52H0z" fill="#F3F1E7"/>'
            '</svg>') % clase


def cabeza(ante, titulo, texto=''):
    p = '<p>%s</p>' % texto if texto else ''
    return f'<div class="section-head"><span class="eyebrow-dark">{ante}</span><h2>{titulo}</h2>{p}</div>'


def pasos(lista, clase='g3'):
    items = ''.join(
        '<div class="paso"><span class="paso-n">%02d</span><h3>%s</h3><p>%s</p></div>' % (i + 1, t, d)
        for i, (t, d) in enumerate(lista))
    return '<div class="grid %s pasos">%s</div>' % (clase, items)


def faq(lista):
    return '<div class="faq">' + ''.join(
        '<details class="faq-item"><summary>%s%s</summary><div class="faq-r"><p>%s</p></div></details>'
        % (q, ico('abajo'), r) for q, r in lista) + '</div>'


def btn(href, txt, clase='btn-primary', icono=None, externo=False):
    ext = ' rel="noopener"' if externo else ''
    return '<a class="btn %s" href="%s"%s>%s%s</a>' % (clase, e(href), ext, ico(icono) if icono else '', txt)


def btn_crear(txt='Crear cuenta gratis', clase='btn-primary'):
    return btn(APP['crear'], txt, clase, 'mas', externo=True)


def btn_entrar(txt='Entrar en mi cuaderno', clase='btn-ghost'):
    return btn(APP['entrar'], txt, clase, 'llave', externo=True)


def panel(titulo, texto, botones):
    return f'''<section class="tight"><div class="wrap"><div class="panel">
  <h2>{titulo}</h2>
  <p>{texto}</p>
  <div class="actions">{botones}</div>
</div></div></section>'''


def baldosa(f, enlace=True):
    fid, icono, tono, nombre, resumen = f[:5]
    clase = ' oscura' if tono == 'bosque' else ''
    href = 'funciones.html#' + fid
    tag_a, tag_c = ('<a class="baldosa%s" href="%s" style="--tono:%s">' % (clase, href, TONOS[tono]), '</a>') if enlace \
        else ('<div class="baldosa%s" style="--tono:%s">' % (clase, TONOS[tono]), '</div>')
    return f'{tag_a}<span class="b-ico">{ico(icono)}</span><h3>{nombre}</h3><p>{resumen}</p>{tag_c}'


def tarjeta_solucion(s, mini=False):
    p = '' if mini else '<p>%s</p>' % s['resumen']
    return f'''<a class="card sol" href="{s['slug']}.html">
  <span class="ico">{ico(s['ico'])}</span>
  <span class="sol-ante">{s['antetitulo']}</span>
  <h3>{s['nombre']}</h3>{p}
  <span class="more">Ver cómo te ayuda {ico('flecha')}</span>
</a>'''


def ejemplos(lista):
    out = []
    for slug, icono, etiqueta, titulo, texto in lista:
        out.append(f'''<figure class="historia">
  <figcaption>{ico(icono)}<span>{etiqueta}</span></figcaption>
  <h3>{titulo}</h3>
  <blockquote>{texto}</blockquote>
</figure>''')
    return '<div class="grid historias">' + ''.join(out) + '</div>'


def nombre_plan(nombre):
    """CuaderHuerta → «Cuader» en DM Sans 800 + «Huerta» manuscrito, como el logotipo."""
    return '<span class="pn"><span class="pn-c">Cuader</span><span class="pn-s">%s</span></span>' % nombre[len('Cuader'):]


def selector_periodo():
    """Interruptor mensual/anual; site.js lo activa y cambia los precios (sin JS queda oculto y se ve el mensual)."""
    return ('<div class="periodo" role="group" aria-label="Periodo de facturación" hidden>'
            '<button type="button" data-periodo="mensual" aria-pressed="true">Mensual</button>'
            '<button type="button" data-periodo="anual" aria-pressed="false">Anual <span class="ahorro">2 meses gratis</span></button>'
            '</div>')


def tarjetas_planes(compacto=False):
    out = []
    for clave, nombre, para, mensual, anual, incluye in PLANES:
        top = clave == PLAN_DESTACADO
        cls = ' plan-top' if top else ''
        reco = '<span class="plan-reco">El más elegido</span>' if top else ''
        lista = incluye[:5] if compacto else incluye
        items = ''.join('<li>%s<span>%s</span></li>' % (ico('check'), x) for x in lista)
        # Sin precios publicados: cada plan lleva a la consulta.
        boton = btn('#escribenos', 'Hacer consulta', 'btn-primary' if top else 'btn-ghost', 'mail')
        out.append(f'''<div class="plan{cls}">{reco}
  <h3>{nombre_plan(nombre)}</h3>
  <p class="plan-para">{para}</p>
  <ul class="plan-lista">{items}</ul>
  {boton}
</div>''')
    return ('<div class="planes-zona"><div class="grid g4 planes">%s</div>'
            '<p class="note-inline nota-precios">Escríbenos y te preparamos el precio del plan que mejor encaja con tu finca o tu cooperativa.</p></div>'
            % ''.join(out))


def relacionados(slugs):
    titulos = {
        'funciones': ('cuaderno', 'Funciones', 'Todo lo que puedes anotar y controlar.'),
        'cuaderno-digital-siex': ('sello', 'Cuaderno digital SIEX', 'Qué cambia y cómo te prepara CuaderCampo.'),
        'como-funciona': ('engranaje', 'Cómo funciona', 'De la cuenta al cuaderno oficial, en seis pasos.'),
        'planes': ('etiqueta', 'Planes', 'Un plan para cada finca, sin permanencia.'),
        'para-quien': ('personas', 'Para quién', 'Agricultores, cooperativas, técnicos y explotaciones grandes.'),
        'cultivos': ('brote', 'Por cultivo', 'Olivar, viñedo, cítricos, frutales, huerta y más.'),
        'ejemplos': ('estrella', 'Ejemplos de uso', 'Así se usa CuaderCampo en fincas distintas.'),
        'quienes-somos': ('corazon', 'Quiénes somos', 'Por qué hacemos CuaderCampo.'),
        'preguntas-frecuentes': ('pregunta', 'Preguntas frecuentes', 'Respuestas claras a las dudas de siempre.'),
        'para-cooperativas': ('edificio', 'Para cooperativas', 'Todas las fincas de tus socios en un panel.'),
    }
    cards = ''.join(f'''<a class="card rel" href="{s}.html"><span class="ico">{ico(titulos[s][0])}</span><h3>{titulos[s][1]}</h3><p>{titulos[s][2]}</p><span class="more">Ver {ico('flecha')}</span></a>''' for s in slugs)
    return f'''<section><div class="wrap">
  <div class="section-head"><span class="eyebrow-dark">Sigue leyendo</span><h2>También te puede interesar</h2></div>
  <div class="grid g3">{cards}</div>
</div></section>'''


# ---------------------------------------------------------------- Maquetas de la app
def maqueta_movil():
    def tile(icono, nombre, dato, tono):
        return (f'<div class="m-tile" style="--tono:{TONOS[tono]}">{ico(icono)}'
                f'<b>{nombre}</b><small>{dato}</small></div>')
    return f'''<div class="mock-phone" role="img" aria-label="Pantalla de CuaderCampo en el móvil: panel de la finca con tratamientos, riego, cosechas e inventario">
  <div class="mock-screen">
    <div class="m-top">{simbolo(26, False)}<span class="m-word"><b>Cuader</b><i>Campo</i></span><span class="m-avatar">MC</span></div>
    <p class="m-saludo">¡Buenos días!</p>
    <p class="m-finca">Finca Los Olivos</p>
    <div class="m-chips"><span class="chip chip-coop">Coop. Norte</span><span class="chip chip-aviso">Plazo activo</span></div>
    <div class="m-grid">
      {tile('matraz', 'Tratamientos', '3 este mes', 'salvia')}
      {tile('agua', 'Riego', '12.400 m³', 'agua')}
      {tile('cesta', 'Cosechas', '18.250 kg', 'trigo')}
      {tile('cajas', 'Inventario', '14 lotes', 'brote')}
    </div>
    <div class="m-aviso">{ico('aviso')}<span><b>Carnet fitosanitario</b> de J. Pérez caduca en 21 días</span></div>
    <div class="m-boton">{ico('mas')}Anotar</div>
  </div>
</div>'''


def maqueta_mapa():
    return f'''<div class="mock-map" role="img" aria-label="Mapa de la finca con recintos SIGPAC dibujados">
  <svg viewBox="0 0 420 300" aria-hidden="true">
    <rect width="420" height="300" fill="#E9E4D2"/>
    <path d="M0 210 C90 190 160 240 260 220 S380 180 420 190 V300 H0Z" fill="#DCE9E6"/>
    <path d="M40 30 L190 18 L205 120 L60 140Z" fill="#7FA35E" fill-opacity=".55" stroke="#234B2C" stroke-width="2"/>
    <path d="M205 22 L370 30 L380 128 L218 118Z" fill="#A9C48A" fill-opacity=".6" stroke="#234B2C" stroke-width="2"/>
    <path d="M62 146 L206 126 L222 200 L80 214Z" fill="#F1E7CC" stroke="#234B2C" stroke-width="2"/>
    <path d="M222 124 L382 134 L370 196 L236 202Z" fill="#7FA35E" fill-opacity=".35" stroke="#234B2C" stroke-width="2" stroke-dasharray="6 5"/>
    <g fill="#234B2C" opacity=".35">{''.join('<circle cx="%d" cy="%d" r="2.4"/>' % (x, y) for x in range(70, 190, 16) for y in range(44, 130, 16) if y < 140 - (x - 60) * 0.1)}</g>
    <g font-family="DM Sans, sans-serif" font-size="12" font-weight="700" fill="#1E2A1F">
      <rect x="86" y="66" width="74" height="22" rx="11" fill="#fff"/><text x="123" y="81" text-anchor="middle">Olivar 1</text>
      <rect x="252" y="62" width="88" height="22" rx="11" fill="#fff"/><text x="296" y="77" text-anchor="middle">Viña Alta</text>
      <rect x="106" y="160" width="72" height="22" rx="11" fill="#fff"/><text x="142" y="175" text-anchor="middle">Huerta</text>
      <rect x="258" y="152" width="92" height="22" rx="11" fill="#fff"/><text x="304" y="167" text-anchor="middle">Zona parcial</text>
    </g>
  </svg>
  <div class="map-ficha"><b>Superficie total</b><span>12,48 ha · 4 recintos SIGPAC</span></div>
</div>'''


def maqueta_validacion():
    filas = [('ok', 'Producto autorizado (registro vigente)'), ('ok', 'Autorizado para el cultivo'),
             ('ok', 'Dosis ≥ mínima · Dosis ≤ máxima'), ('ok', 'Intervalo entre aplicaciones correcto'),
             ('aviso', 'Plazo de seguridad: cosecha a partir del 14 de junio')]
    items = ''.join('<li class="%s">%s<span>%s</span></li>' % (c, ico('check' if c == 'ok' else 'aviso'), t) for c, t in filas)
    return f'''<div class="mock-card" role="img" aria-label="Validaciones de un tratamiento antes de guardarlo">
  <div class="mc-cab"><span class="mc-ico">{ico('matraz')}</span><div><b>Nueva aplicación de tratamiento</b><small>Olivar 1 · Repilo · 2,5 L/ha</small></div></div>
  <ul class="mc-lista">{items}</ul>
  <div class="mc-pie"><span class="firma">{ico('firma')}Firma del aplicador</span><span class="mc-btn">Guardar</span></div>
</div>'''


def maqueta_asistente():
    return f'''<div class="mock-chat" role="img" aria-label="Asistente de IA de CuaderCampo: un tratamiento dictado por voz convertido en registro listo para guardar">
  <div class="ch-cab"><span class="ch-ico">{ico('chispa')}</span><div><b>Asistente CuaderCampo</b><small>Voz y chat · Finca Los Olivos</small></div></div>
  <div class="ch-msg yo"><span class="ch-voz">{ico('microfono')}<i></i><i></i><i></i><i></i><i></i><i></i></span>«He tratado el Olivar 1 con cobre, dos litros y medio por hectárea. Lo ha echado Juan.»</div>
  <div class="ch-msg ia">Te he preparado la aplicación. Revísala antes de guardarla:
    <dl class="ch-ficha"><dt>Plantación</dt><dd>Olivar 1 · 4,2 ha</dd><dt>Producto</dt><dd>Cobre (oxicloruro)</dd><dt>Dosis</dt><dd>2,5 L/ha · 10,5 L</dd><dt>Aplicador</dt><dd>J. Pérez · carnet vigente</dd></dl>
    <span class="ch-ok">{ico('check')}Validaciones correctas</span>
  </div>
  <div class="ch-msg yo">¿Cuándo puedo cosechar la Viña Alta?</div>
  <div class="ch-msg ia">A partir del <b>14 de junio</b>: el último tratamiento tiene 21 días de plazo de seguridad.</div>
  <div class="ch-entrada"><span>Escribe o pulsa el micrófono…</span><span class="ch-mic">{ico('microfono')}</span></div>
</div>'''


def bloque_asistente(clase=' class="alt"'):
    f = next(x for x in FUNCIONES if x[0] == 'asistente')
    lista = ''.join('<li>%s<span>%s</span></li>' % (ico('check'), d) for d in f[6])
    return f'''<section{clase}><div class="wrap"><div class="grid g2 destacado">
  <div>
    <span class="nuevo">{ico('chispa')}Nuevo · Asistente de IA</span>
    <h2>Díctalo en voz alta. <span class="acento">CuaderCampo lo anota</span></h2>
    <p class="entradilla">{f[5]}</p>
    <ul class="checks">{lista}</ul>
    <div class="btn-par">{btn_crear('Probarlo gratis')}{btn('funciones.html#asistente', 'Más sobre el asistente', 'btn-ghost', 'flecha')}</div>
  </div>
  <div class="vis-centro">{maqueta_asistente()}</div>
</div></div></section>'''


# ---------------------------------------------------------------- Páginas
def p_index():
    baldosas = ''.join(baldosa(f) for f in FUNCIONES[:8])
    sols = ''.join(tarjeta_solucion(s) for s in SOLUCIONES)
    cult = ''.join('<a class="chip-cultivo" href="cultivos.html#%s">%s<span>%s</span></a>' % (c[0], ico(c[1]), c[2]) for c in CULTIVOS)
    por_que = ''.join('<div class="card motivo"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in POR_QUE)
    cuerpo = f'''
<div class="hero"><div class="wrap hero-grid">
  <div class="hero-txt">
    <span class="eyebrow-dark">Cuaderno de campo digital · preparado para el SIEX</span>
    <h1>Tu cuaderno de campo, <span class="acento">siempre al día</span></h1>
    <p class="lead">Anota tratamientos, abonados, riegos y cosechas desde el móvil, a mano o por voz, en el mismo tajo. CuaderCampo comprueba dosis y plazos por ti, descuenta el inventario y genera el cuaderno oficial. Y si quieres, lo compartes con tu cooperativa.</p>
    <div class="actions">
      {btn_crear()}
      {btn('como-funciona.html', 'Ver cómo funciona', 'btn-ghost', 'flecha')}
    </div>
  </div>
  <div class="hero-vis">{maqueta_movil()}</div>
</div>
<div class="wrap"><div class="hero-stats">
  <div><b>13</b><span>módulos, con asistente de IA</span></div>
  <div><b>1 min</b><span>para anotar un tratamiento</span></div>
  <div><b>0</b><span>hojas que pasar a limpio</span></div>
  <div><b>100%</b><span>con códigos oficiales SIEX</span></div>
</div></div>{surcos(alto=True)}</div>

<section><div class="wrap">
  {cabeza('Por qué existe CuaderCampo', 'El cuaderno no sobra. Sobra el papeleo alrededor del cuaderno', 'Hacemos CuaderCampo porque el campo merece herramientas pensadas para el campo, no para la oficina.')}
  <div class="grid g3">{por_que}</div>
  <div class="pie-seccion">{btn('quienes-somos.html', 'Conoce quiénes somos', 'btn-ghost', 'personas')}</div>
</div></section>

<section class="alt"><div class="wrap">
  {cabeza('Qué hacemos', 'Todo tu cuaderno de campo, en un mismo lugar', 'Desde el contorno de la finca hasta el fichero oficial. Cada módulo habla con los demás: lo que aplicas sale del inventario y lo que cosechas respeta los plazos.')}
  <div class="grid baldosas">{baldosas}</div>
  <div class="pie-seccion">{btn('funciones.html', 'Ver todas las funciones', 'btn-ghost', 'flecha')}</div>
</div></section>

{bloque_asistente('')}

<section class="alt"><div class="wrap"><div class="grid g2 destacado invertido">
  <div>
    <span class="eyebrow-dark">Tratamientos fitosanitarios</span>
    <h2>Te avisa antes de equivocarte, no después</h2>
    <p class="entradilla">Al registrar una aplicación, CuaderCampo consulta el vademécum y comprueba el registro del producto, la autorización para tu cultivo, la dosis, el intervalo, el número máximo de aplicaciones y el plazo de seguridad. Si algo no cuadra, lo ves antes de guardar.</p>
    <ul class="checks">
      <li>{ico('check')}<span><b>Vademécum integrado</b>Usos autorizados, dosis, plazos y materias activas.</span></li>
      <li>{ico('check')}<span><b>Firma del aplicador</b>Con el dedo, en la pantalla, al terminar.</span></li>
      <li>{ico('check')}<span><b>Inventario automático</b>El producto se descuenta del lote al guardar.</span></li>
    </ul>
    <div class="btn-par">{btn('funciones.html#tratamientos', 'Más sobre tratamientos', 'btn-ghost', 'flecha')}</div>
  </div>
  <div class="vis-centro">{maqueta_validacion()}</div>
</div></div></section>

<section class="verde"><div class="wrap"><div class="grid g2 destacado">
  <div class="vis-centro">{maqueta_mapa()}</div>
  <div>
    <span class="eyebrow">Cuaderno digital oficial</span>
    <h2>Preparado para el SIEX, sin que tengas que aprender el SIEX</h2>
    <p class="entradilla">El cuaderno de explotación pasa a ser digital y a hablar el idioma de la Administración. CuaderCampo guarda cada registro con los códigos y catálogos oficiales —explotación REA, recintos SIGPAC, DGC, actividades y unidades— y genera el fichero validado por titular y por campaña.</p>
    <div class="btn-par">{btn('cuaderno-digital-siex.html', 'Qué es el cuaderno digital SIEX', 'btn-primary', 'sello')}</div>
  </div>
</div></div></section>

<section><div class="wrap">
  {cabeza('Para quién', 'Un mismo cuaderno, cuatro maneras de usarlo', 'El agricultor anota, la cooperativa gestiona, su técnico valida. Cada uno ve lo que le toca.')}
  <div class="grid g4 sols">{sols}</div>
</div></section>

<section class="alt"><div class="wrap">
  {cabeza('Cómo funciona', 'Del registro al cuaderno oficial, en seis pasos')}
  {pasos(PASOS)}
  <div class="pie-seccion">{btn('como-funciona.html', 'Ver en detalle', 'btn-ghost', 'flecha')}{btn_crear()}</div>
</div></section>

<section><div class="wrap">
  {cabeza('Por cultivo', 'Hecho para tu cultivo', 'Del olivar de secano al invernadero, pasando por la platanera en bancales.')}
  <div class="chips-cultivo">{cult}</div>
</div></section>

<section class="alt"><div class="wrap">
  {cabeza('Ejemplos de uso', 'Así se trabaja con CuaderCampo', 'Escenarios ilustrativos de fincas y cooperativas distintas.')}
  {ejemplos(EJEMPLOS[:3])}
  <div class="pie-seccion">{btn('ejemplos.html', 'Ver más ejemplos', 'btn-ghost', 'flecha')}</div>
</div></section>

<section><div class="wrap">
  {cabeza('Planes', 'Un plan para cada finca', 'Sin permanencia y con {d} días de prueba de CuaderFinca. Pregúntanos qué plan te encaja.'.format(d=PRUEBA_DIAS))}
  {tarjetas_planes(compacto=True)}
  <div class="pie-seccion"><p class="note-inline">¿Quieres comparar todo lo que incluye cada plan? <a href="planes.html">Ver planes en detalle</a></p></div>
</div></section>

<section class="alt"><div class="wrap">
  {cabeza('Preguntas frecuentes', 'Lo que más nos preguntan')}
  {faq(FAQ_GENERAL[:5])}
  <div class="pie-seccion">{btn('preguntas-frecuentes.html', 'Ver todas las preguntas', 'btn-ghost', 'pregunta')}</div>
</div></section>

{panel('Deja el cuaderno de papel esta campaña', 'Crea tu cuenta, da de alta tu finca y anota tu primer tratamiento hoy mismo.', btn_crear() + btn_entrar('Ya tengo cuenta', 'btn-line'))}
'''
    return pagina('index', 'CuaderCampo — Cuaderno de campo digital para agricultores y cooperativas (SIEX)',
                  'Tu cuaderno de campo, siempre al día. Recintos SIGPAC, tratamientos, fertilización, riego, cosechas e inventario desde el móvil, preparado para el SIEX.',
                  cuerpo, 'index', ld=[ld_app(), ld_faq(FAQ_GENERAL[:5])])


def p_funciones():
    chips = ''.join('<a href="#%s">%s%s</a>' % (f[0], ico(f[1]), f[3]) for f in FUNCIONES)
    bloques = []
    for i, (fid, icono, tono, nombre, resumen, texto, detalles) in enumerate(FUNCIONES):
        lista = ''.join('<li>%s<span>%s</span></li>' % (ico('check'), d) for d in detalles)
        vis = {'recintos': maqueta_mapa(), 'tratamientos': maqueta_validacion(), 'asistente': maqueta_asistente()}.get(fid)
        if not vis:
            vis = f'<div class="ficha-func" style="--tono:{TONOS[tono]}"><span class="ff-ico">{ico(icono)}</span><b>{nombre}</b><span>{resumen}</span></div>'
        alt = ' class="alt"' if i % 2 else ''
        if fid == 'asistente':
            nombre = nombre + ' <span class="nuevo nuevo-mini">Nuevo</span>'
        orden = ' invertido' if i % 2 else ''
        bloques.append(f'''<section{alt} id="{fid}"><div class="wrap"><div class="grid g2 destacado{orden}">
  <div>
    <div class="ind-head"><span class="ico-grande">{ico(icono)}</span><div><span class="eyebrow-dark">{'%02d' % (i + 1)} · Módulo</span><h2>{nombre}</h2></div></div>
    <p class="entradilla">{texto}</p>
    <ul class="checks">{lista}</ul>
  </div>
  <div class="vis-centro">{vis}</div>
</div></div></section>''')
    cuerpo = page_head('Todo lo que necesita tu cuaderno de campo',
                       'Trece módulos, con asistente de IA por voz y chat, que hablan entre sí: lo que aplicas sale del inventario, lo que cosechas respeta los plazos y todo acaba en el cuaderno oficial.',
                       [('', 'Funciones')], 'Funciones', btn_crear()) + f'''
<section class="tight"><div class="wrap"><nav class="chips-nav" aria-label="Módulos">{chips}</nav></div></section>
{''.join(bloques)}
{panel('Pruébalo con tu propia finca', 'Crea tu cuenta y prueba el plan CuaderFinca durante {d} días.'.format(d=PRUEBA_DIAS), btn_crear() + btn('planes.html', 'Ver planes', 'btn-line', 'etiqueta'))}
{relacionados(['cuaderno-digital-siex', 'como-funciona', 'planes'])}
'''
    return pagina('funciones', 'Funciones — Recintos SIGPAC, tratamientos, fertilización, riego e inventario | CuaderCampo',
                  'Recintos SIGPAC, plantaciones, tratamientos con validaciones, asistente de IA por voz y chat, fertilización N-P-K, riego, cosechas, inventario por lotes, aplicadores, cooperativas y su técnico y cuaderno oficial SIEX.',
                  cuerpo, 'funciones', ld=[ld_app()])


def p_para_quien():
    sols = ''.join(tarjeta_solucion(s) for s in SOLUCIONES)
    cuerpo = page_head('Un mismo cuaderno, cuatro maneras de usarlo',
                       'El agricultor anota, la cooperativa gestiona y su técnico valida. Cada uno ve lo que le toca, y nadie teclea dos veces lo mismo.',
                       [('', 'Para quién')], 'Para quién') + f'''
<section><div class="wrap">
  <div class="grid g2 sols">{sols}</div>
</div></section>
<section class="alt"><div class="wrap">
  {cabeza('Cómo encajan las piezas', 'La finca es del agricultor. El resto, se invita')}
  <div class="grid g3">
    <div class="card"><span class="ico">{ico('brote')}</span><h3>El agricultor es el dueño</h3><p>Crea su finca, anota sus labores y decide con quién comparte cada finca y con qué nivel de acceso.</p></div>
    <div class="card"><span class="ico">{ico('edificio')}</span><h3>Una cooperativa gestora por finca</h3><p>La cooperativa solicita la gestión; el agricultor la acepta o la rechaza, y puede cambiarla cuando quiera.</p></div>
    <div class="card"><span class="ico">{ico('insignia')}</span><h3>El técnico, sobre datos reales</h3><p>Ve las fincas que tiene asignadas, emite instrucciones y valida con su ROPO lo que se aplicó.</p></div>
  </div>
</div></section>
{panel('¿No sabes por dónde empezar?', 'Escríbenos y te contamos cómo encaja CuaderCampo en tu caso: una finca familiar, una explotación grande o una cooperativa con cientos de socios.', btn('#escribenos', 'Hablemos', 'btn-primary', 'mail') + btn_crear('Crear cuenta gratis', 'btn-line'))}
{relacionados(['funciones', 'cultivos', 'ejemplos'])}
'''
    return pagina('para-quien', 'Para quién es CuaderCampo — Agricultores, cooperativas, técnicos y explotaciones grandes',
                  'CuaderCampo para agricultores, cooperativas y SAT, sus técnicos con ROPO y explotaciones con muchas fincas. Un mismo cuaderno de campo, cada uno con lo que le toca.',
                  cuerpo, 'para-quien')


def p_solucion(s):
    cta = btn('#alta', 'Solicitar alta de cooperativa', 'btn-primary', 'edificio') if s['slug'] == 'para-cooperativas' else btn_crear()
    tit, items = s['para']
    cards = ''.join('<div class="card cob"><span class="ico">%s</span><h3>%s</h3><p>%s</p></div>' % (ico('check'), a, b) for a, b in items)
    ejs = [x for x in EJEMPLOS if x[0] == s['slug']] or EJEMPLOS[:2]
    otras = ''.join(tarjeta_solucion(o, mini=True) for o in SOLUCIONES if o is not s)
    vis = maqueta_validacion() if s['slug'] in ('para-asesores',) else maqueta_mapa() if s['slug'] == 'para-explotaciones' else maqueta_movil()
    form_kw = None
    if s['slug'] == 'para-cooperativas':
        form_kw = dict(titulo='Solicita el alta de tu cooperativa',
                       texto='Cuéntanos cuántos socios y técnicos tenéis y qué cultivos lleváis. Te preparamos una propuesta, una demostración con datos de ejemplo y un plan de alta para tus socios.',
                       asunto='Alta de cooperativa', boton='Enviar solicitud por WhatsApp', ancla='alta', campos='cooperativa')
    cuerpo = page_head(s['titulo'], s['resumen'], [('para-quien.html', 'Para quién'), ('', s['nombre'])],
                       s['antetitulo'], cta) + f'''
<section><div class="wrap"><div class="grid g2 destacado">
  <div>
    <span class="eyebrow-dark">El problema</span>
    <h2>Lo que queremos quitarte de encima</h2>
    <p class="entradilla">{s['problema']}</p>
    <div class="btn-par">{cta}{btn('como-funciona.html', 'Cómo funciona', 'btn-ghost')}</div>
  </div>
  <div class="vis-centro">{vis}</div>
</div></div></section>

<section class="alt"><div class="wrap">
  {cabeza('Cómo empezar', 'Tres pasos y listo')}
  {pasos(s['pasos'])}
</div></section>

<section><div class="wrap">
  {cabeza(s['nombre'], tit)}
  <div class="grid g3">{cards}</div>
</div></section>

<section class="alt"><div class="wrap">
  {cabeza('Ejemplos de uso', 'Así se usa en la práctica', 'Escenarios ilustrativos.')}
  {ejemplos(ejs)}
</div></section>

<section><div class="wrap">
  {cabeza('Preguntas frecuentes', 'Dudas habituales')}
  {faq(s['faq'])}
</div></section>

{panel(s['cta'], 'Sin permanencia. Cuéntanos tu caso y te preparamos el plan que mejor encaja.', cta + btn('planes.html', 'Ver planes', 'btn-line', 'etiqueta'))}

<section><div class="wrap">
  {cabeza('Para quién', 'Otros perfiles')}
  <div class="grid g3 sols mini">{otras}</div>
</div></section>
'''
    return pagina(s['slug'], 'CuaderCampo para %s — %s' % (s['nombre'].lower(), s['titulo']), s['resumen'], cuerpo,
                  'para-quien', ld=[ld_faq(s['faq'])], form_kw=form_kw)


def p_siex():
    faq_siex = [
        ('¿Me afecta ya la obligación del cuaderno digital?', 'Depende del tamaño y del tipo de tu explotación y del calendario vigente, que han ido ajustando el Ministerio de Agricultura y las comunidades autónomas. Consulta a tu cooperativa o a tu comunidad autónoma. En cualquier caso, si llevas tu cuaderno en CuaderCampo, el día que te afecte no tendrás que cambiar nada.'),
        ('¿Sigue siendo válido el cuaderno en papel?', 'Mientras no te alcance la obligación del formato digital, el cuaderno de explotación puede llevarse en papel. Pero tiene que estar al día, y pasarlo a digital después lleva mucho más trabajo que anotarlo bien desde el principio.'),
        ('¿CuaderCampo envía los datos a la Administración por mí?', 'CuaderCampo genera el fichero del cuaderno digital con el formato y los códigos oficiales, validado antes de descargarlo, para que lo presentes tú o tu entidad gestora por el canal que establezca tu comunidad autónoma.'),
        ('¿Qué pasa con los datos que ya tengo en papel?', 'Puedes empezar en cualquier momento de la campaña. Da de alta tu finca y tus plantaciones, y registra los tratamientos de la campaña en curso con su fecha real.'),
    ]
    datos = [('sello', 'Explotación REA', 'El código de tu explotación en el Registro de Explotaciones Agrícolas y el titular.'),
             ('mapa', 'Recintos y DGC', 'La declaración gráfica de cultivos: recintos SIGPAC, superficie, cultivo y sistema de cultivo.'),
             ('matraz', 'Tratamientos', 'Producto, nº de registro, dosis, plaga, justificación, estado fenológico, aplicador y equipo.'),
             ('gota-hoja', 'Fertilización', 'Material fertilizante, riqueza, método y aportes de N, P y K por hectárea.'),
             ('azada', 'Actividades', 'Siembras, labores, riegos, cosechas y tratamientos postcosecha.'),
             ('personas', 'Personas y equipos', 'Técnico con ROPO, aplicadores con carnet y maquinaria con inspección ITEAF.')]
    cards = ''.join('<div class="card"><span class="ico">%s</span><h3>%s</h3><p>%s</p></div>' % (ico(i), t, d) for i, t, d in datos)
    cuerpo = page_head('El cuaderno digital SIEX, explicado sin jerga',
                       'Qué es el SIEX, qué cambia en tu cuaderno de campo y cómo te deja preparado CuaderCampo, te afecte ya o no.',
                       [('', 'Cuaderno digital SIEX')], 'Cuaderno digital oficial', btn_crear()) + f'''
<section><div class="wrap"><div class="grid g2 destacado">
  <div class="texto-largo">
    <h2>Qué es el SIEX</h2>
    <p>El <b>Sistema de Información de Explotaciones Agrícolas (SIEX)</b> lo crea el Real Decreto 1054/2022. Reúne en un mismo sistema la información de las explotaciones: quién es el titular, qué recintos cultiva, qué tratamientos y abonados aplica y qué cosecha.</p>
    <p>Dentro del SIEX está el <b>cuaderno digital de explotación agrícola</b>: el mismo cuaderno de campo de siempre, pero en formato electrónico y con los códigos y catálogos oficiales del Ministerio. Su obligatoriedad se aplica de forma progresiva, según el calendario que marcan el Ministerio y las comunidades autónomas.</p>
    <h2>Qué cambia para ti</h2>
    <p>Lo que hay que anotar es prácticamente lo mismo que ya pedía el cuaderno en papel. Lo que cambia es el <b>cómo</b>: cada producto, cultivo, plaga o unidad tiene un código oficial, y el cuaderno se entrega como un fichero que se valida automáticamente.</p>
    <p>Por eso no basta con «pasar a ordenador» lo que tenías en la libreta: hay que traducirlo al idioma del SIEX. Eso es exactamente lo que hace CuaderCampo por debajo, mientras tú ves palabras normales.</p>
  </div>
  <div class="vis-centro">{maqueta_validacion()}</div>
</div></div></section>

<section class="alt"><div class="wrap">
  {cabeza('Qué datos lleva', 'Lo que guarda tu cuaderno digital', 'CuaderCampo los recoge mientras trabajas, con los catálogos oficiales en cada campo.')}
  <div class="grid g3">{cards}</div>
</div></section>

<section><div class="wrap"><div class="grid g2" style="gap:44px;align-items:start">
  <div>
    {cabeza('Cómo te prepara CuaderCampo', 'Cumplir sin tener que estudiarse la norma')}
    <ul class="checks">
      <li>{ico('check')}<span><b>Catálogos oficiales en cada registro</b>Productos, cultivos, plagas, estados fenológicos, unidades y materiales fertilizantes.</span></li>
      <li>{ico('check')}<span><b>Validaciones antes de guardar</b>Datos obligatorios, dosis, plazos y autorizaciones, en el momento.</span></li>
      <li>{ico('check')}<span><b>Un cuaderno por finca y campaña</b>Sin mezclar registros entre fincas ni entre campañas.</span></li>
      <li>{ico('check')}<span><b>Exportación validada</b>Fichero oficial del cuaderno digital, además de PDF y Excel.</span></li>
      <li>{ico('check')}<span><b>Borrados comunicables</b>Lo anulado conserva su identificador para comunicar la baja.</span></li>
    </ul>
  </div>
  <div class="note nota-grande">{ico('info')}<div><b>Normativa de referencia</b><p>Real Decreto 1054/2022 (SIEX y cuaderno digital), Real Decreto 1311/2012 (uso sostenible de productos fitosanitarios) y Real Decreto 1051/2022 (nutrición sostenible en los suelos agrarios). Este resumen es divulgativo: consulta siempre la normativa vigente y el calendario de tu comunidad autónoma.</p></div></div>
</div></div></section>

<section class="alt"><div class="wrap">
  {cabeza('Preguntas frecuentes', 'Dudas sobre el cuaderno digital')}
  {faq(faq_siex)}
</div></section>

{panel('Empieza tu cuaderno digital hoy', 'Cuanto antes empieces, menos tendrás que recuperar.', btn_crear() + btn('funciones.html#siex', 'Ver el módulo SIEX', 'btn-line', 'sello'))}
{relacionados(['funciones', 'como-funciona', 'preguntas-frecuentes'])}
'''
    return pagina('cuaderno-digital-siex', 'Cuaderno digital SIEX: qué es y cómo prepararte | CuaderCampo',
                  'Qué es el SIEX y el cuaderno digital de explotación agrícola, qué cambia en tu cuaderno de campo y cómo te deja preparado CuaderCampo.',
                  cuerpo, 'cuaderno-digital-siex', ld=[ld_faq(faq_siex)])


def p_cultivos():
    chips = ''.join('<a href="#%s">%s%s</a>' % (c[0], ico(c[1]), c[2]) for c in CULTIVOS)
    bloques = ''.join(f'''<article class="card cultivo" id="{cid}">
  <div class="ind-head"><span class="ico-grande">{ico(icono)}</span><h2>{nombre}</h2></div>
  <p>{texto}</p>
  <ul class="checks">{''.join('<li>%s<span>%s</span></li>' % (ico('check'), x) for x in items)}</ul>
</article>''' for cid, icono, nombre, texto, items in CULTIVOS)
    cuerpo = page_head('Hecho para tu cultivo',
                       'Cada cultivo tiene su calendario, sus plagas y su manera de trabajar. CuaderCampo se adapta a la tuya.',
                       [('', 'Por cultivo')], 'Por cultivo') + f'''
<section class="tight"><div class="wrap"><nav class="chips-nav" aria-label="Cultivos">{chips}</nav></div></section>
<section><div class="wrap"><div class="grid g2 cultivos">{bloques}</div></div></section>
{panel('¿Tu cultivo no está en la lista?', 'CuaderCampo trabaja con el catálogo oficial de cultivos del SIEX, así que sirve para cualquier cultivo. Escríbenos si quieres que te contemos cómo encaja el tuyo.', btn_crear() + btn('#escribenos', 'Pregúntanos', 'btn-line', 'mail'))}
{relacionados(['funciones', 'ejemplos', 'para-quien'])}
'''
    return pagina('cultivos', 'Cuaderno de campo para olivar, viñedo, cítricos, frutales y huerta | CuaderCampo',
                  'CuaderCampo para olivar, viñedo, cítricos, frutales, hortícolas e invernadero, cereal, almendro y subtropicales. Un cuaderno de campo adaptado a tu cultivo.',
                  cuerpo, 'funciones')


def p_ejemplos():
    cuerpo = page_head('Así se trabaja con CuaderCampo',
                       'Seis escenarios de fincas, explotaciones y cooperativas distintas para que veas cómo encaja en tu día a día.',
                       [('', 'Ejemplos de uso')], 'Ejemplos de uso') + f'''
<section><div class="wrap">
  <p class="note-inline" style="margin-bottom:22px">Escenarios ilustrativos, construidos a partir de situaciones habituales en el campo. No corresponden a clientes concretos.</p>
  {ejemplos(EJEMPLOS)}
</div></section>
{panel('Tu finca puede ser el siguiente ejemplo', 'Crea tu cuenta gratis y anota tu primer tratamiento en minutos.', btn_crear() + btn('planes.html', 'Ver planes', 'btn-line', 'etiqueta'))}
{relacionados(['para-quien', 'cultivos', 'funciones'])}
'''
    return pagina('ejemplos', 'Ejemplos de uso de CuaderCampo — Fincas, explotaciones y cooperativas',
                  'Escenarios de uso de CuaderCampo en olivar, viñedo, invernadero, platanera y cooperativas.',
                  cuerpo, 'funciones')


def p_como():
    faq_como = FAQ_GENERAL[3:4] + [
        ('¿En qué dispositivos funciona?', 'En cualquier móvil, tableta u ordenador con un navegador actualizado: Android, iPhone, Windows o Mac.'),
        ('¿Por qué me pedís el móvil?', 'Para verificar tu identidad con un código por SMS antes de crear tu primera finca. Así protegemos tu cuaderno y evitamos cuentas falsas.'),
        ('¿Puedo empezar con una finca de prueba?', 'Sí. Puedes crear una finca de demostración con datos de ejemplo para conocer la aplicación antes de dar de alta la tuya.'),
    ] + FAQ_GENERAL[9:10]
    cuerpo = page_head('De la cuenta al cuaderno oficial, en seis pasos',
                       'Sin instalar nada, sin cursos y sin papeles. Diez minutos para dar de alta tu finca y un minuto para cada anotación.',
                       [('', 'Cómo funciona')], 'Cómo funciona', btn_crear()) + f'''
<section><div class="wrap">
  <h2 class="sr-only">Los seis pasos</h2>
  {pasos(PASOS)}
</div></section>

<section class="alt"><div class="wrap"><div class="grid g2 destacado">
  <div class="vis-centro">{maqueta_movil()}</div>
  <div>
    <span class="eyebrow-dark">Instálala en tu móvil</span>
    <h2>Una app sin tiendas de aplicaciones</h2>
    <p class="entradilla">CuaderCampo es una aplicación web: entras en <a href="{APP['entrar']}" rel="noopener">app.cuadercampo.com</a> y, si quieres, la añades a la pantalla de inicio. Se abre como cualquier otra app, siempre actualizada y sin ocupar memoria.</p>
    <ul class="checks">
      <li>{ico('movil')}<span><b>En Android</b>Abre el menú del navegador y pulsa «Instalar aplicación» o «Añadir a pantalla de inicio».</span></li>
      <li>{ico('movil')}<span><b>En iPhone</b>En Safari, pulsa «Compartir» y después «Añadir a pantalla de inicio».</span></li>
      <li>{ico('descarga')}<span><b>En el ordenador</b>Úsala en el navegador para revisar, imprimir y descargar tus cuadernos.</span></li>
    </ul>
  </div>
</div></div></section>

{bloque_asistente('')}

<section class="alt"><div class="wrap">
  {cabeza('Ayuda dentro de la app', 'Nunca te quedas a medias')}
  <div class="grid g4">
    <div class="card"><span class="ico">{ico('pregunta')}</span><h3>Ayuda en cada apartado</h3><p>¿Qué es un recinto? ¿Y una huerta? Cada pantalla te lo explica la primera vez.</p></div>
    <div class="card"><span class="ico">{ico('engranaje')}</span><h3>Configuración en cuatro pasos</h3><p>Datos de la finca, labores que realizas y cómo quieres registrar los tratamientos.</p></div>
    <div class="card"><span class="ico">{ico('cuaderno')}</span><h3>Finca de demostración</h3><p>Prueba con datos de ejemplo antes de meter los tuyos.</p></div>
    <div class="card"><span class="ico">{ico('mail')}</span><h3>Personas que contestan</h3><p>Escríbenos y te ayudamos a dar de alta tu primera finca.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  {cabeza('Preguntas frecuentes', 'Dudas al empezar')}
  {faq(faq_como)}
</div></section>
{panel('¿Empezamos?', 'Crea tu cuenta y da de alta tu finca en unos minutos.', btn_crear() + btn_entrar('Ya tengo cuenta', 'btn-line'))}
'''
    return pagina('como-funciona', 'Cómo funciona CuaderCampo — Tu cuaderno de campo en seis pasos',
                  'Crea tu cuenta, da de alta tu finca, dibuja o importa tus recintos SIGPAC, registra plantaciones y anota desde el campo. Descarga tu cuaderno oficial en PDF, Excel o SIEX.',
                  cuerpo, 'como-funciona', ld=[ld_faq(faq_como)])


def p_planes():
    filas = [
        ('Fincas', '1', 'Hasta 3', 'Ilimitadas', 'Las de tus socios'),
        ('Superficie', 'Hasta 5 ha', 'Hasta 60 ha', 'Ilimitada', 'Ilimitada'),
        ('Recintos SIGPAC, mapa y plantaciones', '✓', '✓', '✓', '✓'),
        ('Tratamientos con vademécum y validaciones', '✓', '✓', '✓', '✓'),
        ('Labores, riegos y cosechas', '✓', '✓', '✓', '✓'),
        ('Asistente de IA (anotaciones por voz o chat)', '30 al mes', '150 al mes', '500 al mes', '40 por finca y mes, o sin límite con tu clave'),
        ('Fertilización con N, P y K', '—', '✓', '✓', '✓'),
        ('Inventario por lotes y facturas', '—', '✓', '✓', '✓'),
        ('Aplicadores, carnets y maquinaria ITEAF', '—', '✓', '✓', '✓'),
        ('Compartir con tu cooperativa gestora', '—', '✓', '✓', '✓'),
        ('Exportación SIEX, PDF y Excel', 'Solo PDF', '✓', '✓', '✓'),
        ('Biblioteca de documentos de la finca', '—', '—', '✓', '✓'),
        ('Instrucciones de tratamiento del técnico (ROPO)', '—', '—', '—', '✓'),
        ('Descuento del 15 % para socios', '—', '—', '—', '✓'),
        ('Panel de cooperativa y técnicos', '—', '—', '—', '✓'),
        ('Soporte', 'Correo', 'Correo', 'Prioritario', 'Dedicado'),
    ]
    cab = ''.join('<th scope="col">%s</th>' % p[1] for p in PLANES)
    cuerpo_t = ''.join('<tr><th scope="row">%s</th>%s</tr>' % (f[0], ''.join('<td data-col="%s">%s</td>' % (PLANES[i][1], v) for i, v in enumerate(f[1:]))) for f in filas)
    faq_planes = [
        ('¿Necesito tarjeta para empezar?', 'No. La prueba de %d días del plan CuaderFinca no pide tarjeta.' % PRUEBA_DIAS),
        ('¿Cuánto cuesta cada plan?', 'Depende de tus fincas, tus hectáreas o, si eres cooperativa, de las fincas que gestionas. Pulsa «Hacer consulta» y te enviamos el precio sin compromiso.'),
        ('¿El asistente de IA cuesta aparte?', 'No, va incluido en todos los planes con un número de anotaciones al mes: 30 en CuaderHuerta, 150 en CuaderFinca y 500 en CuaderExplotación. En CuaderCooperativa hay 40 por finca gestionada y mes, compartidas entre técnicos y socios, o sin límite si la cooperativa usa su propia clave de IA. Una anotación es un dictado o una conversación de chat que termina en un registro. Si las agotas, sigues anotando igual con los formularios y el contador se reinicia el día 1.'),
        ('¿Hay permanencia?', 'No. Puedes cambiar de plan o darte de baja cuando quieras.'),
        ('¿Qué pasa con mis datos si dejo de pagar?', 'Tu cuenta pasa al plan CuaderHuerta. No se borra nada: puedes seguir consultando tus registros y descargar tus cuadernos.'),
        ('¿Y si soy socio de una cooperativa con plan CuaderCooperativa?', 'Tu cooperativa puede incluir tus fincas en su plan, y entonces tienen las funciones de CuaderFinca sin coste para ti. Si prefieres tu propio plan, como socio tienes un 15 % de descuento en CuaderFinca y CuaderExplotación, y tu cooperativa deja de pagar por esas fincas.'),
        ('¿Cómo pago?', 'Con tarjeta o domiciliación bancaria desde tu cuenta. Las cooperativas pueden pagar por transferencia contra factura.'),
    ]
    cuerpo = page_head('Un plan para cada finca',
                       'Sin permanencia y con %d días de prueba del plan CuaderFinca. Elige según tus fincas y tus hectáreas; puedes cambiar cuando quieras.' % PRUEBA_DIAS,
                       [('', 'Planes')], 'Planes') + f'''
<section><div class="wrap">
  <h2 class="sr-only">Elige tu plan</h2>
  {tarjetas_planes()}
  <p class="note-inline" style="margin-top:8px">Si tu finca ya está en tu propio plan, tu cooperativa gestora no paga por ella.</p>
</div></section>

<section class="alt"><div class="wrap">
  {cabeza('Comparativa', 'Qué incluye cada plan')}
  <div class="tabla-scroll"><table class="datos comparativa"><thead><tr><th scope="col">Función</th>{cab}</tr></thead><tbody>{cuerpo_t}</tbody></table></div>
</div></section>

<section><div class="wrap">
  {cabeza('Preguntas frecuentes', 'Dudas sobre planes y pagos')}
  {faq(faq_planes)}
</div></section>
{panel('¿Eres una cooperativa o una SAT?', 'Te preparamos una propuesta a medida, con alta y formación para tus técnicos y tus socios.', btn('para-cooperativas.html#alta', 'Solicitar propuesta', 'btn-primary', 'edificio') + btn_crear('Crear cuenta gratis', 'btn-line'))}
'''
    return pagina('planes', 'Planes — Cuaderno de campo para cada finca y cooperativa | CuaderCampo',
                  'CuaderHuerta, CuaderFinca, CuaderExplotación y CuaderCooperativa: qué incluye cada plan. Sin permanencia. Haz tu consulta y te enviamos el precio.',
                  cuerpo, 'planes', ld=[ld_app(), ld_faq(faq_planes)])


def p_quienes():
    por_que = ''.join('<div class="card motivo"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in POR_QUE)
    que = ''.join('<li>%s<span><b>%s</b>%s</span></li>' % (ico('check'), t, d) for t, d in QUE_HACEMOS)
    historia = ''.join('<p>%s</p>' % p for p in HISTORIA)
    valores = ''.join('<div class="card valor"><span class="ico">%s</span><h3>%s</h3><p>%s</p></div>' % (ico(i), t, d) for _, i, t, d in VALORES)
    equipo = ''.join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in EQUIPO)
    cuerpo = page_head('Hacemos el cuaderno de campo que nos habría gustado encontrar',
                       'Por qué hacemos CuaderCampo, qué hacemos y quiénes estamos detrás.',
                       [('', 'Quiénes somos')], 'Quiénes somos') + f'''
<section><div class="wrap">
  {cabeza('Por qué', 'Por qué hacemos CuaderCampo')}
  <div class="grid g3">{por_que}</div>
</div></section>

<section class="alt"><div class="wrap"><div class="grid g2 destacado">
  <div>
    {cabeza('Qué hacemos', 'Un cuaderno de campo que se rellena en el campo')}
    <ul class="checks">{que}</ul>
  </div>
  <div class="vis-centro">{maqueta_movil()}</div>
</div></div></section>

<section><div class="wrap"><div class="grid g2" style="gap:44px;align-items:start">
  <div class="texto-largo">
    <span class="eyebrow-dark">Quiénes somos</span>
    <h2>Un estudio de diseño con <span class="acento">raíces en el campo</span></h2>
    {historia}
  </div>
  <div>
    <div class="cita"><p>«El cuaderno no les sobra. Les sobra el papeleo alrededor del cuaderno.»</p><span>Lo que más escuchamos al diseñar CuaderCampo</span></div>
    <div class="grid equipo">{equipo}</div>
  </div>
</div></div></section>

<section class="alt"><div class="wrap">
  {cabeza('Nuestros valores', 'Lo que no negociamos')}
  <div class="grid g4">{valores}</div>
</div></section>

{panel('¿Nos ayudas a mejorarlo?', 'Cada función de CuaderCampo nace de una conversación con alguien del campo. Cuéntanos qué te falta.', btn('#escribenos', 'Escríbenos', 'btn-primary', 'mail') + btn_crear('Crear cuenta gratis', 'btn-line'))}
'''
    return pagina('quienes-somos', 'Quiénes somos — Por qué hacemos CuaderCampo',
                  'CuaderCampo nace de un estudio de diseño y desarrollo con raíces en el campo para que el cuaderno de explotación se rellene en el campo, no en la oficina.',
                  cuerpo, 'quienes-somos')


def p_faq():
    grupos = [
        ('El producto', FAQ_GENERAL[0:1] + FAQ_GENERAL[3:4] + FAQ_GENERAL[7:12]),
        ('Normativa y SIEX', FAQ_GENERAL[1:3]),
        ('Planes y datos', FAQ_GENERAL[4:7]),
        ('Cooperativas y técnicos', SOLUCIONES[1]['faq'] + SOLUCIONES[2]['faq'][:2]),
    ]
    todo = [x for _, l in grupos for x in l]
    bloques = ''.join('<section%s><div class="wrap"><div class="section-head"><h2>%s</h2></div>%s</div></section>'
                      % (' class="alt"' if i % 2 else '', t, faq(l)) for i, (t, l) in enumerate(grupos))
    cuerpo = page_head('Preguntas frecuentes', 'Respuestas claras sobre CuaderCampo, el cuaderno digital SIEX, los planes y tus datos.',
                       [('', 'Preguntas frecuentes')]) + bloques + \
        panel('¿No encuentras tu respuesta?', 'Escríbenos por WhatsApp o por correo y te contestamos en menos de un día laborable.',
              btn('#escribenos', 'Escríbenos', 'btn-primary', 'mail') + btn_crear('Crear cuenta gratis', 'btn-line'))
    return pagina('preguntas-frecuentes', 'Preguntas frecuentes — CuaderCampo',
                  'Qué es CuaderCampo, si es obligatorio el cuaderno digital, qué es el SIEX, cuánto cuesta y de quién son tus datos.',
                  cuerpo, 'preguntas-frecuentes', ld=[ld_faq(todo)])


def p_contacto():
    cuerpo = page_head('Hablemos de tu finca', 'Agricultores, cooperativas, técnicos o explotaciones grandes: cuéntanos qué necesitas y te contestamos personas.',
                       [('', 'Contacto')]) + f'''
<section><div class="wrap"><div class="grid g3">
  <a class="card rel" href="{APP['entrar']}" rel="noopener"><span class="ico">{ico('llave')}</span><h3>Ya uso CuaderCampo</h3><p>Entra en tu cuaderno. Si necesitas ayuda, escríbenos desde el formulario.</p><span class="more">Entrar {ico('flecha')}</span></a>
  <a class="card rel" href="para-cooperativas.html#alta"><span class="ico">{ico('edificio')}</span><h3>Soy una cooperativa</h3><p>Solicita el alta y una propuesta para tus técnicos y socios.</p><span class="more">Solicitar alta {ico('flecha')}</span></a>
  <a class="card rel" href="{APP['crear']}" rel="noopener"><span class="ico">{ico('brote')}</span><h3>Quiero empezar</h3><p>Crea tu cuenta gratis y da de alta tu primera finca en minutos.</p><span class="more">Crear cuenta {ico('flecha')}</span></a>
</div></div></section>
'''
    return pagina('contacto', 'Contacto — CuaderCampo', 'Escríbenos para dudas sobre CuaderCampo, el cuaderno digital SIEX o planes para cooperativas.',
                  cuerpo, 'contacto', form_kw=dict(titulo='Escríbenos', ancla='escribenos'))


# ---------------------------------------------------------------- Legales
def legal(slug, titulo, intro, secciones):
    nav = ''.join('<li><a href="#s%d">%s<span>%s</span></a></li>' % (i, ico('flecha'), t) for i, (t, _) in enumerate(secciones, 1))
    body = ''.join('<div class="legal-sec" id="s%d"><h2>%s</h2>%s</div>' % (i, t, h) for i, (t, h) in enumerate(secciones, 1))
    cuerpo = page_head(titulo, intro, [('', titulo)]) + f'''
<section><div class="wrap"><div class="legal-layout">
  <aside class="legal-nav"><p class="legal-nav-t">En esta página</p><ul class="foot-links dark">{nav}</ul></aside>
  <div class="legal-body">{body}<p class="legal-version">Última actualización: noviembre de {ANIO}.</p></div>
</div></div></section>'''
    return pagina(slug, '%s — CuaderCampo' % titulo, intro, cuerpo, form=False)


def p_aviso():
    mail = '<a href="mailto:%s">%s</a>' % (EMPRESA['email'], EMPRESA['email'])
    s = [
        ('Titular del sitio', f'<p>Este sitio web (cuadercampo.com) y la aplicación CuaderCampo (app.cuadercampo.com) son titularidad de: {PENDIENTE} (nombre o razón social, NIF y domicilio). Contacto: {mail}.</p>'),
        ('Objeto', '<p>Este sitio informa sobre CuaderCampo, un cuaderno de campo digital para explotaciones agrícolas, y da acceso a la aplicación. El uso de la aplicación se rige además por sus propias condiciones de uso, que se aceptan al crear la cuenta.</p>'),
        ('Propiedad intelectual', '<p>La marca CuaderCampo, el logotipo, el diseño y los textos de este sitio están protegidos. No se permite su reproducción sin autorización expresa del titular.</p>'),
        ('Información normativa', '<p>Los contenidos sobre normativa (SIEX, cuaderno digital, fitosanitarios y fertilización) son divulgativos y pueden no reflejar el último cambio legal o el calendario de cada comunidad autónoma. Consulta siempre la normativa vigente. Las validaciones de la aplicación ayudan, pero no sustituyen la lectura de la etiqueta del producto ni el criterio del asesor.</p>'),
        ('Responsabilidad', '<p>El titular no se responsabiliza del mal uso de los contenidos ni de los daños derivados de interrupciones del servicio ajenas a su control.</p>'),
        ('Legislación aplicable', '<p>Este aviso se rige por la legislación española.</p>'),
    ]
    return legal('aviso-legal', 'Aviso legal', 'Datos del titular y condiciones de uso de este sitio web.', s)


def p_privacidad():
    mail = '<a href="mailto:%s">%s</a>' % (EMPRESA['email'], EMPRESA['email'])
    s = [
        ('Responsable', f'<p>CuaderCampo (titular y NIF: {PENDIENTE}). Contacto: {mail}.</p>'),
        ('Qué datos tratamos en este sitio', '<p>Los que nos facilitas al escribirnos o suscribirte a las novedades: nombre, apellidos, correo electrónico, teléfono (opcional), entidad y el contenido de tu mensaje. Este sitio no tiene formularios que envíen datos a un servidor: al enviar, se abre WhatsApp con el mensaje redactado para que lo mandes tú al número de CuaderCampo, y ese mensaje queda sujeto también a las condiciones de WhatsApp.</p>'),
        ('Finalidad y legitimación', '<p>Responder a tu consulta, preparar una propuesta si eres una cooperativa y, si te suscribes, enviarte novedades. La base legal es tu consentimiento, que puedes retirar en cualquier momento.</p>'),
        ('Datos de la aplicación', '<p>Los datos de tus fincas, recintos, cultivos y registros se tratan en la aplicación solo para prestarte el servicio. Tú decides qué cooperativa gestiona cada finca. No vendemos ni cedemos tus datos a terceros salvo obligación legal.</p>'),
        ('Conservación', '<p>Conservamos los datos mientras sean necesarios para la finalidad indicada y durante los plazos legales aplicables al cuaderno de explotación.</p>'),
        ('Tus derechos', f'<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {mail}. También puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>'),
    ]
    return legal('politica-de-privacidad', 'Política de privacidad', 'Cómo tratamos los datos personales que nos facilitas.', s)


def p_cookies():
    s = [
        ('Cookies de este sitio', '<p>Este sitio web no instala cookies propias de análisis ni de publicidad. Solo se guarda, si procede, la información técnica imprescindible para que las páginas funcionen.</p>'),
        ('Servicios de terceros', '<p>Para mostrar las tipografías, tu navegador descarga recursos de Google Fonts (fonts.googleapis.com, fonts.gstatic.com), que puede registrar tu dirección IP conforme a su propia política de privacidad.</p>'),
        ('La aplicación', '<p>La aplicación (app.cuadercampo.com) usa el almacenamiento técnico necesario para mantener tu sesión iniciada. Se explica en su propia política.</p>'),
        ('Cómo gestionarlas', '<p>Puedes bloquear o eliminar las cookies desde la configuración de tu navegador.</p>'),
    ]
    return legal('cookies', 'Política de cookies', 'Qué cookies y recursos de terceros utiliza este sitio.', s)


def lista_paginas():
    return [('index', 'Inicio'), ('funciones', 'Funciones'), ('cultivos', '— Por cultivo'), ('ejemplos', '— Ejemplos de uso'),
            ('para-quien', 'Para quién')] + [(s['slug'], '— ' + s['nombre']) for s in SOLUCIONES] + [
        ('cuaderno-digital-siex', 'Cuaderno digital SIEX'), ('como-funciona', 'Cómo funciona'), ('planes', 'Planes'),
        ('quienes-somos', 'Quiénes somos'), ('preguntas-frecuentes', 'Preguntas frecuentes'), ('contacto', 'Contacto'),
        ('aviso-legal', 'Aviso legal'), ('politica-de-privacidad', 'Política de privacidad'), ('cookies', 'Política de cookies'),
        ('mapa-web', 'Mapa web')]


def p_mapa():
    items = ''.join('<li><a href="%s.html">%s<span>%s</span></a></li>' % (s, ico('flecha'), t) for s, t in lista_paginas())
    cuerpo = page_head('Mapa web', 'Todas las páginas del sitio.', [('', 'Mapa web')]) + \
        '<section><div class="wrap"><ul class="foot-links dark mapa">%s</ul></div></section>' % items
    return pagina('mapa-web', 'Mapa web — CuaderCampo', 'Todas las páginas del sitio de CuaderCampo.', cuerpo)


def p_404():
    cuerpo = page_head('Esta página no está en el cuaderno', 'Puede que haya cambiado de dirección. Vuelve al inicio o elige una sección.',
                       [('', '404')]) + panel('¿Qué buscabas?', 'Estas son las páginas más visitadas.',
                                              btn('index.html', 'Inicio') + btn('funciones.html', 'Funciones', 'btn-line') +
                                              btn('planes.html', 'Planes', 'btn-line') + btn_entrar('Entrar en la app', 'btn-line'))
    return pagina('404', 'Página no encontrada — CuaderCampo', 'Página no encontrada.', cuerpo, form=False)


# ---------------------------------------------------------------- llms.txt
def llms_txt():
    u = lambda slug: '%s%s.html' % (BASE, slug)
    planes = '\n'.join('  - %s: %s Incluye: %s.' % (n, p, ', '.join(inc)) for _, n, p, _m, _a, inc in PLANES)
    pasos_t = '\n'.join('%d. %s: %s' % (i, t, d) for i, (t, d) in enumerate(PASOS, 1))
    funcs = '\n'.join('- **%s**: %s' % (f[3], f[4]) for f in FUNCIONES)
    sols = '\n'.join('- [%s](%s): %s' % (s['nombre'], u(s['slug']), s['resumen']) for s in SOLUCIONES)
    faq_t = '\n'.join('- **%s** %s' % (q, r) for q, r in FAQ_GENERAL)
    return f"""# CuaderCampo

> {EMPRESA['lema']}. Cuaderno de campo digital para agricultores y cooperativas en España, preparado para el SIEX (cuaderno digital de explotación agrícola, Real Decreto 1054/2022). Recintos SIGPAC, plantaciones, tratamientos fitosanitarios con validaciones, fertilización, riego, cosechas e inventario desde el móvil.

Web: {BASE} · Aplicación: {APP['entrar']} · Contacto: {EMPRESA['email']}

## Por qué existe

{chr(10).join('- **%s**: %s' % (t, d) for t, d in POR_QUE)}

## Funciones

{funcs}

## Para quién

{sols}

## Cómo funciona

{pasos_t}

## Planes (precio bajo consulta, sin permanencia, {PRUEBA_DIAS} días de prueba de CuaderFinca)

{planes}

## Preguntas frecuentes

{faq_t}

## Más información

- [Funciones]({u('funciones')})
- [Cuaderno digital SIEX]({u('cuaderno-digital-siex')})
- [Por cultivo]({u('cultivos')})
- [Ejemplos de uso]({u('ejemplos')}) (escenarios ilustrativos)
- [Planes]({u('planes')})
- [Quiénes somos]({u('quienes-somos')})
- [Preguntas frecuentes]({u('preguntas-frecuentes')})
- [Contacto]({u('contacto')})

## Optional

- [Aviso legal]({u('aviso-legal')})
- [Política de privacidad]({u('politica-de-privacidad')})
- [Política de cookies]({u('cookies')})
- [Sitemap]({BASE}sitemap.xml)
"""


# ---------------------------------------------------------------- Salida
def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(contenido)


def main():
    paginas = {
        'index': p_index(), 'funciones': p_funciones(), 'para-quien': p_para_quien(),
        'cuaderno-digital-siex': p_siex(), 'cultivos': p_cultivos(), 'ejemplos': p_ejemplos(),
        'como-funciona': p_como(), 'planes': p_planes(), 'quienes-somos': p_quienes(),
        'preguntas-frecuentes': p_faq(), 'contacto': p_contacto(), 'aviso-legal': p_aviso(),
        'politica-de-privacidad': p_privacidad(), 'cookies': p_cookies(), 'mapa-web': p_mapa(),
    }
    for s in SOLUCIONES:
        paginas[s['slug']] = p_solucion(s)
    for slug, html in paginas.items():
        escribir(os.path.join(RAIZ, slug + '.html'), html)
    # GitHub Pages sirve 404.html en cualquier ruta: <base> fija los enlaces relativos.
    escribir(os.path.join(RAIZ, '404.html'), p_404().replace('<head>\n', '<head>\n<base href="%s">\n' % BASE, 1))

    urls = ''.join('<url><loc>%s</loc></url>\n' % (BASE if s == 'index' else BASE + s + '.html') for s, _ in lista_paginas())
    escribir(os.path.join(RAIZ, 'sitemap.xml'),
             '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    escribir(os.path.join(RAIZ, 'robots.txt'), 'User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n' % BASE)
    escribir(os.path.join(RAIZ, 'llms.txt'), llms_txt())
    print('%d páginas generadas (+404, sitemap.xml, robots.txt, llms.txt)' % len(paginas))


if __name__ == '__main__':
    main()
