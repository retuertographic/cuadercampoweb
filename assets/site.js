// CuaderCampo — interacción del sitio (sin dependencias).
var T = {
  abrir: 'Abrir menú', cerrar: 'Cerrar menú'
};

// Menú responsive
(function () {
  var btn = document.getElementById('navToggle');
  var nav = document.getElementById('mainNav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? T.cerrar : T.abrir);
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') nav.classList.remove('open');
  });
})();

// Menú principal con desbordamiento: los elementos que no caben se recogen
// en «Más», y vuelven al menú al ensanchar la ventana.
(function () {
  var nav = document.getElementById('mainNav');
  if (!nav) return;
  var lista = nav.querySelector('ul');
  var mas = lista.querySelector('.nav-mas');
  var drop = mas && mas.querySelector('.nav-drop');
  var cta = lista.querySelector('.cta');
  var wrap = document.querySelector('.site-header .wrap');
  if (!mas || !drop || !wrap) return;
  var movil = window.matchMedia('(max-width:1080px)');

  function restaurar() {
    while (drop.firstElementChild) lista.insertBefore(drop.firstElementChild, mas);
    mas.hidden = true;
    cerrar();
  }
  function cerrar() {
    mas.classList.remove('abierto');
    mas.querySelector('button').setAttribute('aria-expanded', 'false');
  }
  function ajustar() {
    restaurar();
    if (movil.matches) return;
    var items = Array.prototype.filter.call(
      lista.children, function (li) { return li !== mas && li !== cta; }
    );
    // Se recogen desde el final; «Inicio» no se mueve nunca.
    // «Contacto» se mantiene visible: se recogen antes los demás elementos.
    var fijo = items.filter(function (li) { var a = li.querySelector('a'); return a && a.getAttribute('href') === 'contacto.html'; })[0];
    var mover = items.filter(function (li) { return li !== fijo; });
    var i = mover.length - 1;
    while (wrap.scrollWidth > wrap.clientWidth + 1 && i >= 1) {
      mas.hidden = false;
      drop.insertBefore(mover[i], drop.firstChild);
      i--;
    }
    if (!drop.children.length) { mas.hidden = true; return; }
    // Si la página actual ha quedado recogida, se marca «Más».
    mas.classList.toggle('tiene-activo', !!drop.querySelector('a.active'));
  }

  mas.querySelector('button').addEventListener('click', function (e) {
    e.stopPropagation();
    var abierto = mas.classList.toggle('abierto');
    this.setAttribute('aria-expanded', String(abierto));
  });
  document.addEventListener('click', function (e) {
    if (!mas.contains(e.target)) cerrar();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') cerrar();
  });

  var pendiente;
  window.addEventListener('resize', function () {
    clearTimeout(pendiente);
    pendiente = setTimeout(ajustar, 120);
  });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(ajustar);
  ajustar();
})();

// Botón de volver arriba.
(function () {
  var boton = document.getElementById('irArriba');
  if (!boton) return;
  var visible = false;
  function revisar() {
    var debe = window.scrollY > 600;
    if (debe !== visible) { visible = debe; boton.hidden = !debe; }
  }
  boton.addEventListener('click', function () {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
  });
  window.addEventListener('scroll', revisar, { passive: true });
  revisar();
})();

// Formularios y alta en novedades: el sitio es estático, así que componen un mensaje
// con cada campo rellenado (etiqueta: valor) y lo abren en WhatsApp (data-wa = número).
function abrirWhatsApp(numero, texto) {
  var url = 'https://wa.me/' + numero + '?text=' + encodeURIComponent(texto);
  var ventana = window.open(url, '_blank', 'noopener');
  if (!ventana) window.location.href = url;
}

(function () {
  document.querySelectorAll('form.js-whatsapp').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var lineas = ['*' + form.dataset.asunto + '* — web cuadercampo.com', ''];
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.type === 'checkbox' || el.type === 'submit') return;
        var valor = el.value.trim();
        if (!valor) return;
        var etiqueta = form.querySelector('label[for="' + el.id + '"]');
        lineas.push((etiqueta ? etiqueta.textContent.trim() : el.name) + ': ' + valor);
      });
      var msg = form.querySelector('.form-msg');
      if (msg) msg.classList.add('show');
      abrirWhatsApp(form.dataset.wa, lineas.join('\n'));
    });
  });
})();

(function () {
  var form = document.getElementById('newsForm');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var correo = form.elements.email.value.trim();
    var texto = 'Hola, quiero suscribirme a la newsletter de CuaderCampo para recibir las novedades del SIEX, ' +
      'los cambios normativos y las nuevas funciones. Mi correo es: ' + correo;
    var ok = form.querySelector('.news-ok');
    if (!ok) {
      ok = document.createElement('p');
      ok.className = 'news-ok';
      ok.setAttribute('role', 'status');
      form.appendChild(ok);
    }
    ok.textContent = 'Se abrirá WhatsApp con tu solicitud de alta: solo tienes que pulsar enviar.';
    ok.classList.add('show');
    abrirWhatsApp(form.dataset.wa, texto);
  });
})();

// Planes: interruptor mensual/anual. Cambia los textos marcados con data-mensual / data-anual.
(function () {
  var selectores = document.querySelectorAll('.periodo');
  if (!selectores.length) return;
  var guardado = null;
  try { guardado = localStorage.getItem('cc-periodo'); } catch (e) {}
  function aplicar(periodo) {
    selectores.forEach(function (sel) {
      sel.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.dataset.periodo === periodo));
      });
    });
    document.querySelectorAll('[data-mensual]').forEach(function (el) {
      var nuevo = el.dataset[periodo];
      if (el.textContent === nuevo) return;
      el.classList.add('cambiando');
      setTimeout(function () { el.textContent = nuevo; el.classList.remove('cambiando'); }, 120);
    });
    try { localStorage.setItem('cc-periodo', periodo); } catch (e) {}
  }
  selectores.forEach(function (sel) {
    sel.hidden = false;
    sel.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-periodo]');
      if (b) aplicar(b.dataset.periodo);
    });
  });
  if (guardado === 'anual') aplicar('anual');
})();
