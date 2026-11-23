# -*- coding: utf-8 -*-
"""Datos y textos del sitio de CuaderCampo (único punto de edición del contenido).

Todo el texto visible de las páginas sale de aquí o de generar.py.
Las marcas «pendiente» se completan antes de publicar datos legales definitivos.
"""

EMPRESA = {
    'nombre': 'CuaderCampo',
    'base_url': 'https://cuadercampo.com/',
    'email': 'hola@cuadercampo.com',
    'zona': 'España · servicio en todas las comunidades autónomas',
    'lema': 'Tu cuaderno de campo, siempre al día',
}

# Accesos a la aplicación (app.cuadercampo.com)
APP = {
    'entrar': 'https://app.cuadercampo.com/',
    'crear': 'https://app.cuadercampo.com/',
    'alta_coop': 'https://app.cuadercampo.com/',
}

PENDIENTE = 'pendiente de completar'

# ---------------------------------------------------------------- Planes
# Los precios NO se publican en la web (precio bajo consulta). Los campos mensual/anual se conservan sin usar.
# Asistente de IA: anotaciones al mes por plan (una anotación = un dictado o una conversación que acaba en registro).
# (clave, nombre, para quién,
#  mensual: (precio, sufijo, texto bajo el precio),
#  anual:   (precio, sufijo, texto bajo el precio),
#  incluye)
PLANES = [
    ('huerta', 'CuaderHuerta', 'Para empezar con una finca pequeña y dejar el papel.',
     ('0 €', '', 'Gratis para siempre'),
     ('0 €', '', 'Gratis para siempre'),
     ['1 finca y hasta 5 ha', 'Recintos SIGPAC y mapa', 'Plantaciones, labores, riegos y cosechas',
      'Tratamientos con vademécum y validaciones', 'Asistente de IA: 30 anotaciones al mes', 'Cuaderno en PDF',
      'App instalable en el móvil']),
    ('finca', 'CuaderFinca', 'Para el agricultor profesional que quiere cumplir sin perder tiempo.',
     ('12 €', '/mes', 'Facturado cada mes · impuestos incluidos'),
     ('10 €', '/mes', '120 € al año · ahorras 24 €'),
     ['Hasta 3 fincas y 60 ha', 'Todo lo de CuaderHuerta', 'Asistente de IA: 150 anotaciones al mes',
      'Fertilización con unidades N, P y K', 'Inventario por lotes y facturas de compra',
      'Aplicadores, carnets y maquinaria ITEAF', 'Compartir la finca con tu cooperativa gestora',
      'Exportación oficial SIEX, PDF y Excel']),
    ('explotacion', 'CuaderExplotación', 'Para el agricultor con muchas fincas o muchas hectáreas.',
     ('29 €', '/mes', 'Facturado cada mes · impuestos incluidos'),
     ('24 €', '/mes', '288 € al año · ahorras 60 €'),
     ['Fincas y hectáreas ilimitadas', 'Todo lo de CuaderFinca', 'Asistente de IA: 500 anotaciones al mes',
      'Biblioteca de documentos de la finca', 'Soporte prioritario por correo y teléfono']),
    ('cooperativa', 'CuaderCooperativa', 'Para cooperativas y SAT que gestionan las fincas de sus socios.',
     ('A medida', '', 'Desde 1,50 € por finca gestionada y mes'),
     ('A medida', '', 'Desde 1,25 € por finca y mes, facturado al año'),
     ['Panel de cooperativa con todas las fincas', 'Técnicos y asignación de fincas',
      'Asistente de IA: 40 anotaciones por finca y mes, compartidas', 'Solicitudes de gestión aceptadas por el agricultor',
      'Instrucciones de tratamiento del técnico (ROPO)', 'Etiqueta con el color de tu cooperativa',
      'Tu propia clave de IA (BYOK) sin límite de anotaciones',
      '15 % de descuento para tus socios en CuaderFinca y CuaderExplotación',
      'Alta y formación de tus socios']),
]
PLAN_DESTACADO = 'finca'
PRUEBA_DIAS = 30

# ---------------------------------------------------------------- Cómo funciona
PASOS = [
    ('Crea tu cuenta', 'Con tu correo y tu móvil. Te enviamos un código por SMS para proteger tu cuaderno.'),
    ('Da de alta tu finca', 'Nombre, titular y explotación REA. Configúrala en cuatro pasos y elige las labores que haces.'),
    ('Dibuja o importa tus recintos', 'Sobre el mapa o desde SIGPAC. Agrúpalos en huertas si los trabajas juntos.'),
    ('Registra tus plantaciones', 'Cultivo, variedad, marco y fecha de plantación sobre uno o varios recintos.'),
    ('Anota desde el campo', 'Tratamientos, abonados, riegos, labores y cosechas. A mano, por voz o escribiéndole al asistente de IA, en el tajo y en un minuto.'),
    ('Descarga y comparte', 'Tu cuaderno oficial en PDF, Excel o exportación SIEX. Compártelo con tu cooperativa si quieres.'),
]

# ---------------------------------------------------------------- Funciones de la app
# (id, icono, tono de baldosa, nombre, resumen, texto, detalles)
FUNCIONES = [
    ('recintos', 'mapa', 'brote', 'Recintos SIGPAC y mapa',
     'Dibuja el contorno de tu finca sobre el mapa o importa tus recintos SIGPAC.',
     'Un recinto es la unidad mínima del SIGPAC: una superficie continua con un mismo uso. En CuaderCampo los dibujas sobre la ortofoto o los importas, consultas su referencia y ves la superficie total de la finca de un vistazo.',
     ['Importación de recintos SIGPAC y dibujo sobre el mapa', 'Huertas o Unidades Homogéneas de Cultivo (UHC) que agrupan recintos',
      'Selección de plantaciones en el mapa: clic, rectángulo o polígono', 'Zonas parciales para tratar solo una parte de la parcela']),
    ('plantaciones', 'brote', 'salvia', 'Plantaciones',
     'Cultivos, variedades y marcos de plantación de cada finca.',
     'Una plantación es un cultivo concreto —especie y variedad— sobre uno o varios recintos, con su fecha, su marco y su sistema de cultivo. Es la pieza sobre la que cuelga todo lo demás: tratamientos, abonados, riegos y cosechas.',
     ['Especie, variedad, marco y densidad de plantación', 'Sistema de cultivo y de explotación (secano, regadío, invernadero…)',
      'Fecha de alta y baja de superficie', 'Agrupaciones de plantaciones por huerta']),
    ('tratamientos', 'matraz', 'salvia', 'Tratamientos fitosanitarios',
     'Registro fitosanitario conforme a la normativa, con validaciones antes de guardar.',
     'Un asistente te guía en cada aplicación: producto, dosis, plaga, plantaciones, aplicador y equipo. Antes de guardar, CuaderCampo comprueba el registro del producto, que esté autorizado para tu cultivo, la dosis mínima y máxima, el intervalo entre aplicaciones, el número máximo de aplicaciones y el plazo de seguridad.',
     ['Vademécum de fitosanitarios con usos autorizados, dosis y plazos', 'Avisos si el registro está caducado o el producto no está autorizado',
      'Estado fenológico, justificación y eficacia del tratamiento', 'Firma del aplicador con el dedo en la pantalla',
      'Copia una aplicación anterior en un toque', 'Anular sin borrar: el producto vuelve al inventario']),
    ('asistente', 'microfono', 'terracota', 'Asistente de IA por voz y chat',
     'Díctalo en voz alta o escríbelo: el asistente rellena el registro por ti.',
     'Con las manos ocupadas o los guantes puestos, pulsa el micrófono y di lo que has hecho. El asistente de IA entiende tus plantaciones, los productos del vademécum y las unidades, prepara el registro —producto, dosis, plantación, aplicador y fecha— y lo pasa por las mismas validaciones de siempre. Tú lo revisas y lo guardas. También puedes escribirle en el chat: te pregunta solo lo que falte.',
     ['«He tratado el Olivar 1 con cobre a 2,5 L/ha»: registro listo para revisar',
      '«Ayer regué el olivar y aboné el almendral»: dos registros de una vez',
      '«Riego de 40 m³ en los cítricos, agua del pozo»: anotado en segundos',
      'Si falta un dato, como el aplicador o el equipo, te lo pregunta',
      'Nada se guarda sin tu confirmación',
      'Incluido en todos los planes, con anotaciones al mes según el plan']),
    ('fertilizacion', 'gota-hoja', 'trigo', 'Fertilización N, P y K',
     'Abonados con sus unidades fertilizantes de N, P y K por hectárea.',
     'Registra cada abonado con su material fertilizante, su riqueza y el método de aplicación. CuaderCampo calcula los aportes de nitrógeno, fósforo y potasio por hectárea y descuenta el producto del inventario, como en los tratamientos.',
     ['Vademécum de fertilizantes con su riqueza en nutrientes', 'Necesidades de N, P₂O₅ y K₂O en unidades fertilizantes',
      'Fertirrigación, esparcido general o localizado, enterrado…', 'Preparado para el registro que pide la normativa de nutrición sostenible']),
    ('riego', 'agua', 'agua', 'Riego',
     'Riegos por plantación, con su volumen y la procedencia del agua.',
     'Anotar un riego lleva segundos: plantación, cantidad y origen del agua. Si riegas igual que la última vez, repites el último riego con un toque.',
     ['Volumen por plantación', 'Origen del agua (pozo, comunidad de regantes, red…)', 'Repetir el último riego', 'Histórico por campaña']),
    ('cosechas', 'cesta', 'trigo', 'Cosechas y trazabilidad',
     'La producción de cada plantación, con su destino y los plazos de seguridad.',
     'Registra lo recolectado en cada plantación, su cantidad y su destino. CuaderCampo te avisa si una cosecha cae dentro del plazo de seguridad de un tratamiento, para que la trazabilidad no dependa de la memoria.',
     ['Producción por plantación y campaña', 'Destino y comprador', 'Aviso de plazo de seguridad activo', 'Trazabilidad desde el tratamiento hasta la venta']),
    ('labores', 'azada', 'salvia', 'Labores culturales',
     'Poda, siembra, desbroce, recolección… sin horas ni costes.',
     'Cualquier labor realizada en la finca queda en tu cuaderno de campo. Sin rellenar horas ni costes que no te pide nadie: qué, dónde y cuándo.',
     ['Labores por plantación', 'Siembra y plantación', 'Buenas prácticas y medidas culturales', 'Actividades del cuaderno oficial (CUE)']),
    ('inventario', 'cajas', 'trigo', 'Inventario y facturas',
     'El stock se descuenta solo al aplicar.',
     'Sube tus facturas de compra: cada línea crea un lote en el inventario. Cada tratamiento o abonado descuenta automáticamente la cantidad usada, y si un producto se queda en negativo o un lote caduca, te enteras antes de que llegue la inspección.',
     ['Facturas de compra que justifican la procedencia', 'Stock por lotes calculado a partir de compras y aplicaciones',
      'Aviso de stock negativo y de lotes caducados', 'Fecha límite de venta y fin de uso de productos']),
    ('equipo', 'personas', 'salvia', 'Personas, aplicadores y maquinaria',
     'Los cargos del cuaderno, los carnets de los aplicadores y los equipos con los que aplicas.',
     'Indica los cargos que pide el cuaderno oficial: titular, responsable de fitosanitarios, de fertilización o de primeros auxilios. Registra a los aplicadores con su carnet fitosanitario y la maquinaria de aplicación con su inspección ITEAF. Las anotaciones las haces tú, el titular.',
     ['Cargos oficiales del cuaderno', 'Fichas de aplicadores y caducidad de carnets',
      'Aviso de carnets que caducan en los próximos 30 días', 'Maquinaria, ROMA e inspecciones ITEAF']),
    ('asesor', 'insignia', 'salvia', 'Asesoramiento técnico de tu cooperativa',
     'Visitas, instrucciones y validación del técnico de tu cooperativa con su ROPO.',
     'El técnico de tu cooperativa gestora deja sus visitas y recomendaciones en el propio cuaderno. Puede emitir una instrucción que tú conviertes en aplicación con un toque, y validar los tratamientos con su número ROPO.',
     ['Visitas de asistencia técnica', 'Instrucciones del técnico enlazadas a la aplicación',
      'Validación favorable o desfavorable con ROPO', 'Prescripciones y documentos privados de la finca']),
    ('cooperativa', 'edificio', 'salvia', 'Cooperativas',
     'Comparte cada finca con tu cooperativa, con el nivel de acceso que elijas.',
     'Cada finca tiene una única cooperativa gestora, y eres tú quien acepta su solicitud y elige su nivel de acceso. La cooperativa ve sus fincas en un panel, asigna técnicos y valida tratamientos sin pedirte papeles.',
     ['Gestora única por finca, elegida por el agricultor', 'Solicitudes de gestión y cambios de cooperativa',
      'Panel de cooperativa con agricultores, técnicos y asignaciones', 'Etiqueta con el color de la cooperativa en sus fincas']),
    ('siex', 'sello', 'bosque', 'Cuaderno digital oficial (SIEX)',
     'Preparado para el cuaderno digital obligatorio.',
     'CuaderCampo guarda tus datos con los códigos y catálogos oficiales del SIEX: explotación REA, declaración gráfica de cultivos (DGC), actividades y unidades oficiales. Genera un cuaderno por finca y por campaña, y lo exporta en el formato validado.',
     ['Explotación REA y declaración gráfica de cultivos (DGC)', 'Catálogos y códigos oficiales en cada registro',
      'Exportación JSON validada para el SIEX', 'Cuaderno por finca y campaña en PDF y Excel']),
]

TONOS = {
    # terracota suave: novedades
    'brote': '#E4EDD9', 'salvia': '#DCE5D0', 'trigo': '#F1E7CC', 'agua': '#DCE9E6',
    'bosque': '#234B2C', 'terracota': '#F4E1D4',
}

# ---------------------------------------------------------------- Para quién
SOLUCIONES = [
    {
        'slug': 'para-agricultores', 'ico': 'brote', 'nombre': 'Agricultores',
        'antetitulo': 'Para agricultores y agricultoras',
        'titulo': 'Tu cuaderno de campo en el bolsillo, no en el cajón',
        'resumen': 'Anota tratamientos, riegos y cosechas desde el móvil, en el mismo tajo. El cuaderno oficial se hace solo.',
        'problema': 'El cuaderno de papel se rellena el domingo, de memoria, con la etiqueta del producto en una mano y la factura en la otra. Y cuando llega una inspección o te lo pide la cooperativa, toca buscar la carpeta. Con CuaderCampo anotas en el momento, el móvil comprueba dosis y plazos por ti y el cuaderno siempre está listo.',
        'pasos': [
            ('Dibuja tu finca', 'Importa tus recintos SIGPAC o dibújalos sobre el mapa. Diez minutos, una sola vez.'),
            ('Anota en el campo', 'Elige plantación, producto y dosis. Si algo no cuadra con la etiqueta, te avisamos antes de guardar.'),
            ('Descarga tu cuaderno', 'En PDF para la inspección, en Excel para tu gestor y en formato SIEX para la Administración.'),
        ],
        'para': ('Lo que más se agradece', [
            ('Pensado para el móvil', 'Botones grandes, textos claros y se instala como una app, sin pasar por ninguna tienda.'),
            ('Te avisa antes, no después', 'Dosis fuera de rango, plazo de seguridad, carnet caducado o producto sin registro vigente.'),
            ('El inventario cuadra solo', 'Cada aplicación descuenta del stock. Las facturas justifican la procedencia de cada lote.'),
            ('Anota por voz', 'Pulsa el micrófono, di lo que has hecho y el asistente de IA rellena el registro. Tú solo lo revisas.'),
            ('Repite lo de siempre', 'Copia la aplicación anterior o repite el último riego con un toque.'),
            ('Tú decides quién lo ve', 'Comparte cada finca con tu cooperativa con el nivel de acceso que elijas, o con nadie.'),
            ('Empieza con tu finca', 'El plan CuaderHuerta está pensado para una finca de hasta 5 hectáreas. Pregúntanos por él.'),
        ]),
        'faq': [
            ('¿Necesito saber de informática?', 'No. Si usas WhatsApp, sabes usar CuaderCampo. Además, cada apartado tiene una ayuda corta que te explica qué es un recinto, una plantación o una aplicación.'),
            ('¿Funciona sin cobertura?', 'La app está pensada para el móvil y aguanta bien una cobertura floja. Si en tu finca no hay señal, puedes anotar al volver al coche o a casa: la fecha de la labor es la que tú indiques.'),
            ('¿Me sirve el cuaderno para la PAC y las inspecciones?', 'Sí. CuaderCampo genera el cuaderno de explotación con los datos que exige la normativa y en el formato del cuaderno digital (SIEX).'),
        ],
        'cta': 'Empieza hoy con tu primera finca',
    },
    {
        'slug': 'para-cooperativas', 'ico': 'edificio', 'nombre': 'Cooperativas',
        'antetitulo': 'Para cooperativas, SAT y entidades gestoras',
        'titulo': 'Todas las fincas de tus socios, sin pasar papeles a limpio',
        'resumen': 'Un panel con las fincas que tus socios comparten contigo, técnicos asignados y tratamientos validados con ROPO.',
        'problema': 'Cada campaña, los técnicos de la cooperativa recogen cuadernos de papel, los pasan a limpio y persiguen a los socios para que firmen. Con CuaderCampo cada socio anota en su móvil, comparte su finca contigo con un toque y tu equipo trabaja sobre datos que ya están en formato oficial.',
        'pasos': [
            ('Da de alta tu cooperativa', 'Envíanos la solicitud. La revisamos y te nombramos administrador.'),
            ('Invita a tus socios', 'Cada agricultor acepta la solicitud de gestión y elige qué nivel de acceso te da a cada finca.'),
            ('Trabaja desde el panel', 'Asigna técnicos, emite instrucciones, valida tratamientos y descarga los cuadernos.'),
        ],
        'para': ('Qué gana tu cooperativa', [
            ('Panel de cooperativa', 'Agricultores, fincas compartidas y solicitudes pendientes, agrupados y filtrables.'),
            ('Técnicos y asignaciones', 'Cada técnico ve solo las fincas que tiene asignadas y los tratamientos que le tocan.'),
            ('Instrucciones del técnico', 'El técnico emite la recomendación; el socio la convierte en aplicación sin volver a teclearla.'),
            ('Validación con ROPO', 'Validación favorable o desfavorable de cada tratamiento, registrada con el ROPO del técnico.'),
            ('Tu color, en su sitio', 'La etiqueta de tu cooperativa y el detalle de sus fincas llevan tu color corporativo.'),
            ('El socio manda', 'Cada finca tiene una única gestora y el agricultor puede cambiarla. La confianza se gana, no se impone.'),
        ]),
        'faq': [
            ('¿Cuánto cuesta para una cooperativa?', 'El plan CuaderCooperativa es a medida y se calcula por finca gestionada. Incluye el alta, la formación de los técnicos, una sesión para socios, anotaciones de IA para todas las fincas y un 15 % de descuento para tus socios que quieran su propio plan. No pagas por las fincas de socios que ya tienen un plan de pago. Pídenos tu propuesta.'),
            ('¿Puede la cooperativa ver todas las fincas de un socio?', 'Solo las que el socio comparte, y con el nivel de acceso que él elige. Una finca tiene una única cooperativa gestora.'),
            ('¿Mis técnicos necesitan otra herramienta?', 'No. El panel de cooperativa, las asignaciones, las instrucciones y las validaciones están dentro de CuaderCampo.'),
        ],
        'cta': 'Hablemos de tu cooperativa',
    },
    {
        'slug': 'para-asesores', 'ico': 'insignia', 'nombre': 'Técnicos de cooperativa',
        'antetitulo': 'Para técnicos de cooperativas y SAT con ROPO',
        'titulo': 'Tus recomendaciones, directas al cuaderno del agricultor',
        'resumen': 'Visitas, instrucciones y validaciones con tu ROPO, sobre datos de campo reales y en formato oficial.',
        'problema': 'Recomiendas un tratamiento por teléfono, el agricultor lo apunta en un papel y semanas después intentas adivinar qué aplicó, cuándo y a qué dosis. En CuaderCampo tu instrucción llega al cuaderno, el agricultor la aplica con un toque y tú la validas con tu ROPO.',
        'pasos': [
            ('Recibe tus fincas', 'Tu cooperativa te asigna las fincas de los socios que han aceptado su gestión.'),
            ('Emite instrucciones', 'Producto, dosis, plaga y plantaciones, con los usos autorizados del vademécum a mano.'),
            ('Valida con tu ROPO', 'Revisa lo aplicado y deja tu validación favorable o desfavorable registrada.'),
        ],
        'para': ('Herramientas para el técnico', [
            ('Vademécum integrado', 'Usos autorizados, dosis, plazos de seguridad y materias activas al recomendar.'),
            ('Validaciones automáticas', 'Dosis, intervalos, número de aplicaciones y autorización por cultivo, antes de firmar.'),
            ('Visitas registradas', 'Cada visita de asistencia queda en el cuaderno, con sus observaciones.'),
            ('Tus fincas asignadas', 'Una vista con los tratamientos pendientes de validar en tus fincas.'),
            ('Datos oficiales completos', 'Técnico, ROPO, justificación, fenología y unidades oficiales, como pide el SIEX.'),
            ('Menos llamadas', 'El historial de la finca está ahí: ya no hace falta preguntar qué se echó la última vez.'),
        ]),
        'faq': [
            ('¿Tengo que pagar como técnico?', 'No. Trabajas dentro del plan CuaderCooperativa de tu cooperativa o SAT, con las fincas que te asigna.'),
            ('¿Dónde queda mi ROPO?', 'Lo guardas una vez en tu perfil y se usa en cada validación que confirmas.'),
            ('¿Puedo validar desde el móvil?', 'Sí. Toda la aplicación funciona igual en el móvil, la tableta y el ordenador.'),
        ],
        'cta': 'Lleva tus fincas a CuaderCampo',
    },
    {
        'slug': 'para-explotaciones', 'ico': 'tractor', 'nombre': 'Explotaciones grandes',
        'antetitulo': 'Para agricultores con muchas fincas o muchas hectáreas',
        'titulo': 'Muchas fincas, un solo cuaderno siempre cuadrado',
        'resumen': 'Fincas y hectáreas ilimitadas, aplicadores con carnet, maquinaria con ITEAF e inventario por lotes, desde un solo panel.',
        'problema': 'Cuando llevas muchas fincas, el cuaderno se fragmenta: cada una en una libreta, los carnets de los aplicadores caducan sin que te enteres y el almacén no cuadra con lo aplicado. CuaderCampo pone orden sin añadir trabajo: tú anotas y el resto cuadra solo.',
        'pasos': [
            ('Da de alta todas tus fincas', 'Importa los recintos SIGPAC de cada finca, sin límite de fincas ni de hectáreas.'),
            ('Registra aplicadores y equipos', 'Carnets fitosanitarios, maquinaria de aplicación e inspecciones ITEAF.'),
            ('Controla el almacén', 'Facturas, lotes y descuento automático. Un cuaderno por finca y campaña.'),
        ],
        'para': ('Control sin papeleo', [
            ('Cargos oficiales', 'Titular, responsable de fitosanitarios, de fertilización y de primeros auxilios e higiene.'),
            ('Carnets al día', 'Te avisamos de los carnets que caducan en los próximos 30 días.'),
            ('Maquinaria e ITEAF', 'Equipos de aplicación, ROMA y próxima inspección, como exige el SIEX.'),
            ('Firma del aplicador', 'Cada aplicación se firma en la pantalla, con el dedo, por quien la hizo.'),
            ('Todas tus fincas', 'Cada finca con su cuaderno por campaña, sin mezclar registros, desde un solo panel.'),
            ('Inventario por lotes', 'Compras, aplicaciones y stock disponible por lote, con aviso de caducidad.'),
        ]),
        'faq': [
            ('¿Los aplicadores necesitan cuenta?', 'No necesariamente. Puedes tener fichas de aplicadores sin cuenta, con su carnet y su caducidad, y elegirlos al registrar la aplicación.'),
            ('¿Quién anota en el cuaderno?', 'Tú, como titular. Los aplicadores son fichas con su carnet que eliges al registrar cada aplicación; no necesitan cuenta.'),
            ('¿Cuántas hectáreas admite?', 'En el plan CuaderExplotación, fincas y hectáreas ilimitadas.'),
        ],
        'cta': 'Pon orden en tu explotación',
    },
]

# ---------------------------------------------------------------- Cultivos
# (id, icono, nombre, texto, qué se registra)
CULTIVOS = [
    ('olivar', 'oliva', 'Olivar', 'Desde el olivar familiar de secano hasta el superintensivo en seto. Tratamientos contra repilo y mosca, abonados foliares y una cosecha que hay que trazar hasta la almazara.',
     ['Tratamientos contra repilo, mosca y prays', 'Abonado foliar y de suelo', 'Cosecha por plantación con destino a almazara']),
    ('vinedo', 'uva', 'Viñedo', 'Mildiu, oídio y botritis marcan la campaña. Con CuaderCampo controlas intervalos y número máximo de aplicaciones de cada materia activa, y llegas a vendimia con los plazos de seguridad cumplidos.',
     ['Control de intervalos y aplicaciones máximas', 'Estado fenológico oficial en cada tratamiento', 'Vendimia con aviso de plazo de seguridad']),
    ('citricos', 'citrico', 'Cítricos', 'Muchas variedades, muchos tratamientos y mucho riego. Organiza tus parcelas en huertas, anota la fertirrigación y deja que el inventario se descuente solo.',
     ['Fertirrigación con unidades N-P-K', 'Huertas (UHC) para agrupar recintos', 'Tratamientos postcosecha']),
    ('frutales', 'manzana', 'Frutales de hueso y pepita', 'Melocotón, nectarina, cereza, manzana o pera: campañas cortas e intensas en las que un plazo de seguridad mal calculado cuesta una partida.',
     ['Plazos de seguridad y fechas de recolección', 'Tratamientos por zona parcial de la parcela', 'Trazabilidad por partida']),
    ('horticolas', 'hoja', 'Hortícolas e invernadero', 'Ciclos cortos, varias plantaciones al año sobre el mismo recinto y un ritmo de tratamientos que no perdona. El cuaderno tiene que ir tan rápido como tú.',
     ['Varias plantaciones por recinto y campaña', 'Repetir aplicaciones y riegos frecuentes', 'Siembras y trasplantes']),
    ('extensivos', 'espiga', 'Cereal y extensivos', 'Grandes superficies, pocas pasadas y mucha maquinaria. Importa tus recintos SIGPAC, registra herbicidas y abonados de fondo y controla la ITEAF de tus equipos.',
     ['Importación masiva de recintos SIGPAC', 'Herbicidas y abonado de fondo y cobertera', 'Maquinaria con inspección ITEAF']),
    ('frutos-secos', 'almendra', 'Almendro y frutos secos', 'Nuevas plantaciones en regadío y almendro tradicional de secano. Registra marcos, densidades y la evolución de cada plantación desde su primera hoja.',
     ['Marco y densidad de plantación', 'Abonado de plantaciones jóvenes con N, P y K', 'Riego deficitario controlado']),
    ('subtropicales', 'palmera', 'Subtropicales y platanera', 'Aguacate, mango y platanera, en la Península y en Canarias. Riego exigente, fincas en bancales y recintos pequeños que se dibujan mejor que se importan.',
     ['Dibujo de recintos pequeños en bancales', 'Riego por procedencia del agua', 'Cosechas continuas a lo largo del año']),
]

# ---------------------------------------------------------------- Escenarios
# Ejemplos ilustrativos de uso (no son testimonios de clientes).
EJEMPLOS = [
    ('para-agricultores', 'oliva', 'Olivar familiar · 4 ha', 'El cuaderno sale del cajón',
     'Un olivarero de secano con cuatro hectáreas repartidas en seis recintos los importa desde SIGPAC una tarde. Desde entonces anota cada tratamiento al terminar, desde el tractor. Al llegar la inspección, descarga el PDF desde el móvil en el mismo campo.'),
    ('para-cooperativas', 'edificio', 'Cooperativa de cítricos · 180 socios', 'De pasar a limpio a validar',
     'Los tres técnicos de una cooperativa dejan de recoger cuadernos en papel. Los socios comparten sus fincas, cada técnico ve las que tiene asignadas y valida los tratamientos con su ROPO. La campaña se cierra sin una sola hoja que teclear.'),
    ('para-explotaciones', 'uva', 'Bodega con viñedo propio · 60 ha', 'Carnets y equipos al día',
     'Una bodega con cinco aplicadores registra sus carnets y sus atomizadores. CuaderCampo avisa de un carnet que caduca en tres semanas y de una inspección ITEAF que vence antes del primer tratamiento contra el mildiu.'),
    ('para-agricultores', 'hoja', 'Invernadero · 2 ha', 'El almacén por fin cuadra',
     'Un horticultor sube las facturas de compra de la campaña. Cada aplicación descuenta del lote correspondiente y la app le avisa de un producto que ha superado su fecha límite de venta antes de usarlo.'),
    ('para-asesores', 'insignia', 'Técnico de SAT · 40 fincas', 'Una instrucción, cero llamadas',
     'El técnico de una SAT, con su ROPO, emite la instrucción para un tratamiento de cobre en todas sus fincas de viñedo. Cada agricultor la aplica con un toque y el técnico valida desde el móvil, con el historial de cada finca delante.'),
    ('para-explotaciones', 'palmera', 'Platanera en bancales · Canarias', 'Recintos pequeños, cuaderno grande',
     'Una explotación familiar con platanera en bancales dibuja sus recintos uno a uno sobre la ortofoto, registra los riegos por procedencia del agua y anota las cosechas semanales con su destino.'),
]

# ---------------------------------------------------------------- Preguntas frecuentes
FAQ_GENERAL = [
    ('¿Qué es CuaderCampo?', 'Es un cuaderno de campo digital para agricultores y cooperativas. Registras recintos, plantaciones, tratamientos, abonados, riegos, labores y cosechas desde el móvil, y CuaderCampo genera el cuaderno de explotación oficial, preparado para el SIEX.'),
    ('¿Es obligatorio el cuaderno de campo digital?', 'El cuaderno de explotación es obligatorio desde hace años para quien usa productos fitosanitarios. El Real Decreto 1054/2022 crea el Sistema de Información de Explotaciones Agrícolas (SIEX) y el cuaderno digital, cuya obligatoriedad se aplica de forma progresiva según el calendario que marcan el Ministerio y las comunidades autónomas. CuaderCampo te deja preparado tanto si ya te afecta como si no.'),
    ('¿Qué es el SIEX?', 'Es el sistema oficial en el que se integra la información de las explotaciones agrícolas: la declaración de cultivos, el cuaderno digital y los registros de tratamientos y fertilización. CuaderCampo guarda tus datos con los códigos y catálogos oficiales y exporta el cuaderno en el formato validado.'),
    ('¿Necesito instalar algo?', 'No. CuaderCampo funciona desde el navegador del móvil, la tableta o el ordenador. Si quieres, la añades a la pantalla de inicio y se abre como una app, sin pasar por ninguna tienda.'),
    ('¿Cuánto cuesta?', 'Tenemos planes para una finca pequeña, para el agricultor profesional, para explotaciones con muchas fincas y para cooperativas. El precio depende de tu caso: escríbenos y te lo enviamos sin compromiso. Puedes probar el plan CuaderFinca durante 30 días.'),
    ('¿Puedo cambiar de plan o darme de baja?', 'Sí, cuando quieras y desde tu cuenta. Si bajas al plan CuaderHuerta, no pierdes tus registros: sigues pudiendo consultarlos y descargar tus cuadernos.'),
    ('¿De quién son mis datos?', 'Tuyos. Tú decides qué cooperativa gestiona cada finca y con qué nivel de acceso, y puedes retirarlo. No vendemos ni cedemos tus datos a terceros.'),
    ('¿Puedo importar mis recintos SIGPAC?', 'Sí. Puedes importar tus recintos o dibujarlos sobre el mapa. Después los agrupas en huertas (UHC) si los trabajas de forma conjunta.'),
    ('¿Cómo sé qué productos puedo usar?', 'El vademécum de fitosanitarios incluye los usos autorizados, las dosis y los plazos de seguridad. Al registrar una aplicación, CuaderCampo te avisa si el producto no está autorizado para tu cultivo, si su registro ha caducado o si la dosis está fuera de rango.'),
    ('¿Qué pasa si me equivoco al registrar un tratamiento?', 'Puedes editarlo o anularlo. Una aplicación anulada no se borra: queda registrada como anulada, con su motivo, y el producto vuelve al inventario.'),
    ('¿Funciona en toda España?', 'Sí. CuaderCampo trabaja con SIGPAC y con los catálogos oficiales del Ministerio, válidos en todas las comunidades autónomas, también en Canarias.'),
    ('¿Puedo anotar por voz?', 'Sí. Pulsa el micrófono y di lo que has hecho, por ejemplo «He tratado el Olivar 1 con cobre a 2,5 litros por hectárea». El asistente de IA prepara el registro con la plantación, el producto, la dosis y la fecha, y te lo enseña para que lo revises antes de guardarlo. Si lo prefieres, escríbeselo en el chat.'),
    ('¿El asistente de IA es un extra de pago?', 'No. Viene incluido en todos los planes con un número de anotaciones al mes: 30 en CuaderHuerta, 150 en CuaderFinca y 500 en CuaderExplotación. En CuaderCooperativa hay 40 por finca gestionada y mes, o sin límite si la cooperativa usa su propia clave de IA. Si las agotas, sigues anotando igual con los formularios.'),
    ('¿Puede el asistente guardar algo sin que yo lo vea?', 'No. El asistente solo propone: cada registro pasa por las validaciones de dosis, plazos y autorizaciones y no se guarda hasta que tú lo confirmas.'),
    ('¿Puedo descargar mi cuaderno?', 'Sí, en PDF para imprimir o enseñar en una inspección, en Excel para tu gestor y en el fichero oficial del cuaderno digital.'),
]

# ---------------------------------------------------------------- Quiénes somos
POR_QUE = [
    ('Porque el papel se queda corto', 'El cuaderno de explotación lleva años siendo obligatorio, pero en la mayoría de las fincas sigue siendo una libreta con manchas de caldo que se rellena de memoria. Cuando llega una inspección, el problema no es haberlo hecho mal: es no poder demostrar que se hizo bien.'),
    ('Porque llega el cuaderno digital', 'Con el SIEX, el cuaderno pasa a ser digital y a hablar el idioma de la Administración: códigos oficiales, catálogos y ficheros validados. Las herramientas que había estaban pensadas para la oficina, no para quien está en el tajo.'),
    ('Porque las cooperativas no dan abasto', 'Los técnicos dedican semanas a pasar a limpio lo que otros apuntaron en papel. Ese tiempo debería estar en el campo, asesorando.'),
]

QUE_HACEMOS = [
    ('Un cuaderno de campo para el móvil', 'Anotar un tratamiento o un riego tiene que llevar menos tiempo que buscar la libreta.'),
    ('Rigor normativo sin jerga', 'Detrás de cada botón están los catálogos oficiales; delante, palabras que se entienden.'),
    ('Avisos antes de equivocarte', 'Dosis, plazos, carnets, registros e inventario se comprueban antes de guardar, no después.'),
    ('Un puente con la cooperativa', 'El agricultor comparte cada finca con quien quiere, y el técnico trabaja sobre datos reales.'),
]

VALORES = [
    ('sencillez', 'brote', 'Sencillez', 'Si una pantalla necesita un manual, está mal hecha. Textos grandes, pocos pasos y ayuda en cada apartado.'),
    ('rigor', 'sello', 'Rigor', 'Seguimos la normativa al pie de la letra para que tú no tengas que leértela.'),
    ('datos', 'escudo', 'Tus datos son tuyos', 'Tú decides quién ve cada finca. No vendemos datos ni los cedemos a terceros.'),
    ('campo', 'azada', 'Hecho con el campo', 'Cada función nace de una conversación con agricultores y técnicos de cooperativa.'),
]

HISTORIA = [
    'CuaderCampo nace en un estudio de diseño y desarrollo, Retuerto Graphic Design, con raíces familiares en el campo. Lo que empezó como una ayuda para pasar a limpio el cuaderno de una finca familiar se convirtió en una pregunta: ¿por qué anotar un tratamiento sigue siendo más difícil que pedir una cita médica desde el móvil?',
    'Hablamos con agricultores de olivar, viñedo, cítricos y huerta, y con técnicos de cooperativa que cada campaña tecleaban cientos de hojas manuscritas. Todos nos dijeron lo mismo: el cuaderno no les sobra, les sobra el papeleo alrededor del cuaderno.',
    'Así que lo diseñamos al revés: primero el agricultor en el campo, con el móvil y las manos ocupadas; después la cooperativa y su técnico; y por debajo, sin que se note, todo lo que pide el SIEX. Con una identidad que huele a huerta y no a oficina, porque el cuaderno es tuyo y tiene que parecerse a tu finca.',
]

EQUIPO = [
    ('Producto y diseño', 'Diseñamos cada pantalla para usarse de pie, al sol y con guantes.'),
    ('Desarrollo', 'Una aplicación web rápida, segura y que se instala en el móvil como una app.'),
    ('Revisión en el campo', 'Técnicos agrícolas y agricultores revisan la aplicación y nos dicen qué mejorar.'),
    ('Atención', 'Te contestamos personas, por correo, y te ayudamos a dar de alta tu primera finca.'),
]
