# -*- coding: utf-8 -*-
"""Artículos del blog de CuaderCampo (campaña general dic. 2026).

Cada artículo: slug, fecha (AAAA-MM-DD, la de su post de feed), público, titular,
entradilla, cuerpo en HTML sencillo (<p>, <h2>, <ul>), CTA (texto, enlace) e imagen.
La imagen vive en assets/blog/<slug>.jpg.
"""

CTA_PRUEBA = ('Prueba CuaderCampo 30 días', 'https://app.cuadercampo.com/auth')
CTA_CONSULTA = ('Habla con nosotros', 'contacto.html')

ARTICULOS = [
    {
        'slug': 'tratamiento-en-dos-minutos',
        'fecha': '2026-11-30',
        'publico': 'Agricultor',
        'titulo': 'Un tratamiento apuntado en dos minutos, desde el móvil',
        'entradilla': 'Acabas de tratar y todavía tienes el olor del caldo encima. Es el mejor momento para apuntarlo: '
                      'en el mismo campo, con el móvil y sin volver a casa a rellenar papeles.',
        'cuerpo': '''
<p>El cuaderno de campo se suele dejar para el domingo por la tarde. Y ahí empiezan los problemas: ¿qué dosis puse en la parcela de abajo?, ¿fue el martes o el miércoles?, ¿qué lote de producto abrí? En CuaderCampo el tratamiento se apunta paso a paso, en el momento, con preguntas cortas y botones grandes pensados para usar con una mano.</p>
<h2>Los pasos, uno detrás de otro</h2>
<ul>
<li><strong>Fecha y hora</strong> de inicio y de fin.</li>
<li><strong>Recintos y superficie</strong>: eliges en qué recintos has tratado y la app suma las hectáreas.</li>
<li><strong>Cultivo y estado fenológico</strong>, con el catálogo oficial.</li>
<li><strong>Productos y dosis</strong>, buscando en el vademécum por nombre o número de registro.</li>
<li><strong>Plaga o motivo y justificación</strong> de la actuación.</li>
<li><strong>Aplicador y equipo</strong>, que ya tienes guardados en tu ficha.</li>
</ul>
<h2>Lo que la app hace por ti</h2>
<p>Al elegir el producto, CuaderCampo calcula el <strong>plazo de seguridad</strong> y te avisa si la dosis se sale de lo autorizado. Si llevas el inventario en la app, el producto se descuenta solo del lote que hayas usado. Y si te equivocas, puedes anular la aplicación y el stock vuelve a su sitio.</p>
<p>Todo queda guardado en tu cuaderno, listo para descargarlo en PDF o en el archivo oficial cuando te lo pidan.</p>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Agricultor de mediana edad con gorra en un campo de cultivo canario al atardecer, mirando su teléfono móvil con una mano, mochila pulverizadora a la espalda, fotografía realista, luz cálida, sin texto ni logotipos',
    },
    {
        'slug': 'cuaderno-digital-sin-jaleo',
        'fecha': '2026-12-03',
        'publico': 'Agricultor',
        'titulo': 'El cuaderno de explotación digital, explicado sin jaleo',
        'entradilla': 'SIEX, CUE, REA, formato legible por máquina… Te contamos en cristiano qué cambia, qué fechas '
                      'importan y cómo cumplir sin complicarte.',
        'cuerpo': '''
<p>El Real Decreto 1054/2022 creó tres piezas: el <strong>SIEX</strong> (el sistema de información de explotaciones), el <strong>REA</strong> (el registro autonómico de explotaciones agrícolas) y el <strong>CUE</strong> (el cuaderno digital de explotación agrícola). Desde 2025, usar el CUE digital es voluntario: puedes llevar el cuaderno en papel o en digital, y los dos valen.</p>
<h2>Las fechas que conviene tener a mano</h2>
<ul>
<li><strong>Desde el 1 de enero de 2026</strong>, cada aplicación de fertilizante o materia orgánica tiene que quedar registrada en el cuaderno (en papel o digital): fecha, parcela, tipo de fertilizante y dosis.</li>
<li><strong>El 1 de enero de 2027</strong> es la fecha prevista en España para que los usuarios profesionales lleven el registro de tratamientos fitosanitarios en formato electrónico legible por máquina.</li>
</ul>
<h2>Qué hay que anotar en cada tratamiento</h2>
<p>Como mínimo: el producto, la plaga, la fecha y la dosis. Además, la zona y el cultivo, el aplicador y, si lo hay, el asesor, el equipo de aplicación y una valoración del tratamiento.</p>
<h2>Cómo te ayuda CuaderCampo</h2>
<p>CuaderCampo sigue el diseño oficial del cuaderno digital (versión 3.11.4). Apuntas igual que siempre y, cuando lo necesites, descargas tu cuaderno en <strong>PDF</strong> para leerlo y en el <strong>archivo estructurado oficial</strong> para la Administración. Así llegas a 2027 con el trabajo hecho.</p>
<p><em>Este artículo resume la normativa estatal publicada a noviembre de 2026. Consulta siempre con tu cooperativa o tu técnico los requisitos de tu comunidad autónoma.</em></p>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Libreta de campo de papel gastada junto a un teléfono móvil sobre una caja de madera de fruta en una finca agrícola, luz de mañana, fotografía realista de detalle, sin texto legible ni logotipos',
    },
    {
        'slug': 'dicta-no-escribas',
        'fecha': '2026-12-08',
        'publico': 'Agricultor',
        'titulo': 'Dicta, no escribas: el asistente de voz de CuaderCampo',
        'entradilla': 'Con las manos sucias o los guantes puestos, escribir en el móvil es un suplicio. Ahora basta con '
                      'decirlo en voz alta.',
        'cuerpo': '''
<p>Pulsa el micrófono y cuéntalo como se lo contarías a un compañero: «Hoy he cosechado ciento veinte kilos de papa en la finca de arriba». CuaderCampo transcribe lo que dices y <strong>rellena el formulario por ti</strong>: fecha, recinto, cultivo, cantidad.</p>
<h2>Tú tienes siempre la última palabra</h2>
<p>El asistente prepara un borrador, pero <strong>nunca guarda nada solo</strong>. Revisas los campos, cambias lo que haga falta y pulsas Guardar, como en cualquier otro registro. Si algo no le queda claro, te lo pregunta.</p>
<h2>También en formato chat</h2>
<p>Si prefieres escribir, puedes hablar con el asistente por chat. Te hace las preguntas necesarias para dar de alta un tratamiento, un riego, una cosecha o una compra, y te abre el formulario ya relleno.</p>
<h2>¿Dónde funciona?</h2>
<p>En los apartados principales de la app: tratamientos, fertilización, riego, cosechas, labores, plantaciones, recintos, compras e inventario, aplicadores y equipos. El número de dictados al mes depende de tu plan.</p>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Manos de agricultor con guantes de trabajo sujetando un teléfono móvil cerca de la boca para dictar, fondo desenfocado de huerta verde, fotografía realista, sin texto ni logotipos',
    },
    {
        'slug': 'inventario-se-descuenta-solo',
        'fecha': '2026-12-12',
        'publico': 'Agricultor',
        'titulo': 'El inventario de fitosanitarios que se descuenta solo',
        'entradilla': 'Se acabó contar botes en el almacén. Cada tratamiento resta del stock el producto que has usado, '
                      'lote a lote.',
        'cuerpo': '''
<p>Saber qué te queda en el almacén no debería requerir una tarde con una libreta. En CuaderCampo el inventario se alimenta solo: entra con las compras y sale con los tratamientos.</p>
<h2>Así funciona</h2>
<ul>
<li><strong>Compras</strong>: registras la factura y los productos entran al inventario con su lote y su caducidad.</li>
<li><strong>Tratamientos</strong>: al apuntar una aplicación, eliges el lote y la cantidad usada se descuenta.</li>
<li><strong>Unidades</strong>: la app convierte entre litros y mililitros o kilos y gramos, para que no tengas que hacer cuentas.</li>
<li><strong>Errores</strong>: si anulas un tratamiento, el producto vuelve a su lote.</li>
</ul>
<h2>Trazabilidad de verdad</h2>
<p>Cada aplicación queda unida al lote que usaste. Si un día hay que saber dónde fue a parar un lote concreto, lo tienes en un momento.</p>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Estantería ordenada de almacén agrícola con envases genéricos de productos fitosanitarios sin etiquetas legibles, luz natural, fotografía realista, sin marcas ni logotipos ni texto',
    },
    {
        'slug': 'tu-finca-tus-datos',
        'fecha': '2026-12-16',
        'publico': 'Agricultor',
        'titulo': 'Tu finca, tus datos: tú decides quién los ve',
        'entradilla': 'Tu cuaderno es tuyo. En CuaderCampo eres tú quien da acceso a la cooperativa, finca a finca, '
                      'y quien lo retira cuando quiere.',
        'cuerpo': '''
<p>Muchos agricultores tienen fincas en distintas zonas y trabajan con más de una cooperativa. Por eso en CuaderCampo el acceso no es para todo o nada: se decide <strong>finca a finca</strong>.</p>
<h2>Una cooperativa gestora por finca</h2>
<p>Para cada finca eliges una sola <strong>cooperativa gestora</strong>. Esa cooperativa y sus técnicos pueden ver la finca y ayudarte con el cuaderno. Las demás no ven nada. La finca se tiñe con los colores y el logo de su cooperativa, así sabes de un vistazo quién lleva cada una.</p>
<h2>Siempre bajo tu control</h2>
<ul>
<li>Tú das el acceso y tú lo puedes retirar.</li>
<li>Cada finca tiene un único titular y cada cuaderno es de una sola persona.</li>
<li>Puedes descargar tus datos cuando quieras.</li>
</ul>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Vista aérea de parcelas agrícolas de distintos verdes separadas por muros de piedra en Canarias, fotografía realista de dron, luz suave, sin texto ni logotipos',
    },
    {
        'slug': 'cooperativa-todas-las-fincas',
        'fecha': '2026-12-20',
        'publico': 'Cooperativa',
        'titulo': 'Todas las fincas de tus socios, en un solo panel',
        'entradilla': 'Deja de perseguir libretas y fotos por WhatsApp. Con CuaderCampo, tu cooperativa ve al día las fincas '
                      'que sus socios le confían.',
        'cuerpo': '''
<p>Para una cooperativa, el cuaderno de campo de sus socios es un rompecabezas: cada uno lo lleva a su manera, en papel, en una hoja de cálculo o en ningún sitio. CuaderCampo pone orden sin cambiar quién manda: el agricultor apunta y la cooperativa acompaña.</p>
<h2>Qué tiene tu cooperativa</h2>
<ul>
<li><strong>Panel de cooperativa</strong> con las fincas que los socios han puesto bajo vuestra gestión.</li>
<li><strong>Técnicos con su papel</strong> (administración, técnico o solo lectura) y fincas asignadas a cada uno.</li>
<li><strong>Vuestra marca</strong>: logo, colores y contacto en las fincas que gestionáis.</li>
<li><strong>Instrucciones del técnico</strong> que el agricultor aplica con un botón.</li>
<li>Cuadernos en <strong>PDF y archivo oficial</strong>, listos para cualquier control.</li>
</ul>
<h2>Sin pagar dos veces</h2>
<p>Si un socio ya tiene su propio plan, su finca no cuenta en la factura de la cooperativa. Y los socios de una cooperativa con CuaderCampo tienen descuento en su plan.</p>
''',
        'cta': CTA_CONSULTA,
        'img_prompt': 'Técnica agrícola joven revisando una tableta junto a un agricultor mayor en una finca de cultivo, conversación tranquila, fotografía realista, luz natural, sin texto ni logotipos',
    },
    {
        'slug': 'del-contador-al-cuaderno',
        'fecha': '2026-12-22',
        'publico': 'Agricultor',
        'titulo': 'Del contador al cuaderno: los metros cúbicos de riego sin apuntar a mano',
        'entradilla': 'Haz una foto al contador, escribe la lectura y CuaderCampo se encarga del resto: consumo, reparto '
                      'por plantación y cuaderno oficial.',
        'cuerpo': '''
<p>El agua es cara y cada vez se controla más. Llevar bien el riego en el cuaderno ya no es un extra. Con los contadores de CuaderCampo, el consumo sale solo.</p>
<h2>Cómo funciona</h2>
<ul>
<li>Das de alta el contador con la <strong>procedencia del agua</strong> y tu <strong>comunidad de regantes</strong>, de los catálogos oficiales.</li>
<li>Apuntas la <strong>lectura</strong> en m³, con una foto si quieres.</li>
<li>La app calcula el <strong>consumo</strong> desde la lectura anterior. Si la cifra baja, te pregunta si cambiaste o reiniciaste el contador.</li>
<li>El consumo se <strong>reparte entre las plantaciones</strong> según su superficie, y puedes ajustarlo a mano.</li>
</ul>
<h2>Directo al cuaderno oficial</h2>
<p>Tus riegos toman el volumen y la procedencia del contador, que van al cuaderno oficial. Y al final de la campaña tienes el resumen: metros cúbicos por contador, por plantación y por hectárea.</p>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Contador de agua de riego en una tubería en una finca agrícola, gotas de agua, plantas jóvenes con riego por goteo al fondo, fotografía realista de detalle, sin texto legible ni logotipos',
    },
    {
        'slug': 'inspeccion-sin-sustos',
        'fecha': '2026-12-26',
        'publico': 'Agricultor',
        'titulo': 'Inspección sin sustos: tu cuaderno listo en un clic',
        'entradilla': 'Cuando llega el control, lo último que quieres es buscar papeles. Con CuaderCampo descargas todo '
                      'en un momento.',
        'cuerpo': '''
<p>Una inspección, una auditoría de calidad o simplemente una consulta de tu cooperativa: siempre que te piden el cuaderno, tiene que estar completo y legible. En CuaderCampo está todo en un mismo sitio.</p>
<h2>Qué puedes descargar</h2>
<ul>
<li><strong>PDF</strong> del cuaderno, ordenado y fácil de leer.</li>
<li><strong>Archivo estructurado oficial</strong> del cuaderno digital (formato de la Administración, versión 3.11.4).</li>
<li><strong>Un ZIP</strong> con todo junto, para enviarlo de una vez.</li>
</ul>
<h2>Con todo lo que piden</h2>
<p>Tratamientos con producto, número de registro, dosis, plaga y justificación; aplicador con su carné; equipos con su inspección; fertilizaciones, riegos y cosechas. Y un registro de actividad que deja rastro de quién hizo cada cambio y cuándo.</p>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Agricultor sonriente entregando una carpeta a un inspector en la entrada de una finca, ambiente cordial, fotografía realista, luz de mañana, sin texto ni logotipos',
    },
    {
        'slug': 'recintos-sigpac-en-el-mapa',
        'fecha': '2026-12-28',
        'publico': 'Agricultor',
        'titulo': 'Tus recintos SIGPAC, en el mapa',
        'entradilla': 'Tu finca como la ves desde arriba, con cada recinto y el cultivo de cada campaña.',
        'cuerpo': '''
<p>En el papel, un recinto es un número. En CuaderCampo es un trozo de tierra que reconoces en el mapa. Das de alta tu explotación con su titular y su código REA, y añades los recintos SIGPAC.</p>
<h2>Lo que ves</h2>
<ul>
<li><strong>Mapa de la finca</strong> con cada recinto dibujado.</li>
<li><strong>Cultivo de cada campaña</strong> en cada recinto, para no confundir años.</li>
<li><strong>Superficie</strong> de cada recinto, que luego se usa al apuntar tratamientos y riegos.</li>
</ul>
<h2>Menos errores al apuntar</h2>
<p>Cuando registras un tratamiento eliges los recintos en el mapa o en la lista, y la app suma la superficie. Así el cuaderno cuadra con lo que tienes declarado.</p>
''',
        'cta': CTA_PRUEBA,
        'img_prompt': 'Vista cenital de parcelas agrícolas de cultivos variados con caminos de tierra, estilo mapa aéreo, fotografía realista de dron, colores verdes y ocres, sin texto ni logotipos',
    },
    {
        'slug': 'consejo-del-tecnico-con-un-boton',
        'fecha': '2026-12-31',
        'publico': 'Cooperativa',
        'titulo': 'Del consejo del técnico a la aplicación, con un botón',
        'entradilla': 'El técnico de la cooperativa prescribe el tratamiento; el agricultor lo aplica y lo registra sin '
                      'volver a escribir nada.',
        'cuerpo': '''
<p>La recomendación del técnico suele llegar en un papel o en un mensaje, y luego hay que pasarla al cuaderno a mano. En CuaderCampo, la instrucción del técnico ya es el registro.</p>
<h2>Cómo funciona</h2>
<ul>
<li>El técnico de la cooperativa gestora crea la <strong>instrucción</strong>: plantaciones, productos con dosis, plaga, justificación, estado fenológico y su número ROPO.</li>
<li>El agricultor la ve en su finca y pulsa <strong>Aplicar</strong>.</li>
<li>Se abre el tratamiento ya relleno: solo confirma la fecha real, el aplicador, el equipo y los lotes.</li>
<li>El inventario se descuenta y el tratamiento queda enlazado a la instrucción.</li>
</ul>
<h2>Visitas firmadas</h2>
<p>Las visitas técnicas y auditorías también quedan en la app, con la firma del técnico y del titular en la pantalla y su PDF en la biblioteca de documentos.</p>
''',
        'cta': CTA_CONSULTA,
        'img_prompt': 'Técnico agrícola señalando las hojas de una planta en un cultivo mientras un agricultor observa, ambos con ropa de campo, fotografía realista, luz natural, sin texto ni logotipos',
    },
]
