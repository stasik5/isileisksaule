// Įsileisk Saulę — menu, consent, click tracking
(function () {
  var btn = document.querySelector('.menu-btn'), nav = document.querySelector('.nav');
  if (btn && nav) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // --- Consent (Google Consent Mode v2) ---
  var KEY = 'is_consent';
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function apply(v) {
    if (typeof gtag !== 'function') return;
    var g = v === 'all' ? 'granted' : 'denied';
    gtag('consent', 'update', { analytics_storage: g, ad_storage: g, ad_user_data: g, ad_personalization: g });
  }
  var box = document.getElementById('consent');
  var saved = get();
  if (saved) apply(saved); else if (box) box.classList.add('show');
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-consent]');
    if (t) { var v = t.getAttribute('data-consent'); set(v); apply(v); if (box) box.classList.remove('show'); }
    var o = e.target.closest('[data-open-consent]');
    if (o && box) { e.preventDefault(); box.classList.add('show'); }
  });

  // --- Lead click tracking (GA4 events; mark as key events in GA4, import to Google Ads) ---
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!a || typeof gtag !== 'function') return;
    var h = a.getAttribute('href'), method = null;
    if (h.indexOf('tel:') === 0) method = 'phone';
    else if (h.indexOf('wa.me') > -1 || h.indexOf('whatsapp') > -1) method = 'whatsapp';
    else if (h.indexOf('viber:') === 0) method = 'viber';
    else if (h.indexOf('mailto:') === 0) method = 'email';
    if (!method) return;
    var ev = { phone: 'click_call', whatsapp: 'click_whatsapp', viber: 'click_viber', email: 'click_email' }[method];
    gtag('event', ev, { method: method, link_location: a.getAttribute('data-loc') || 'page', page_path: location.pathname });
    gtag('event', 'generate_lead', { method: method, page_path: location.pathname });
  });

  // --- Full-screen gallery viewer: tap a photo to enlarge; arrows / swipe to browse; Esc or × to close ---
  var items = [].slice.call(document.querySelectorAll('a[data-lb]'));
  if (items.length) {
    var lb = document.createElement('div'), cur = 0, opener = null, x0 = null;
    lb.className = 'lb';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Nuotrauka');
    lb.innerHTML = '<button type="button" class="lb-close" aria-label="Uždaryti">×</button>' +
      '<button type="button" class="lb-prev" aria-label="Ankstesnė nuotrauka">‹</button>' +
      '<img alt=""><p></p>' +
      '<button type="button" class="lb-next" aria-label="Kita nuotrauka">›</button>';
    document.body.appendChild(lb);
    var im = lb.querySelector('img'), cap = lb.querySelector('p');
    function show(i) {
      cur = (i + items.length) % items.length;
      var a = items[cur], alt = a.querySelector('img').getAttribute('alt') || '';
      im.src = a.getAttribute('href'); im.alt = alt; cap.textContent = alt;
    }
    function open(i) { opener = items[i]; show(i); lb.classList.add('open'); document.body.classList.add('lb-lock'); lb.querySelector('.lb-close').focus(); }
    function close() { lb.classList.remove('open'); document.body.classList.remove('lb-lock'); if (opener) opener.focus(); }
    items.forEach(function (a, i) {
      a.addEventListener('click', function (e) { e.preventDefault(); open(i); });
    });
    lb.addEventListener('click', function (e) {
      if (e.target.closest('.lb-prev')) show(cur - 1);
      else if (e.target.closest('.lb-next')) show(cur + 1);
      else if (e.target.closest('.lb-close') || e.target === lb) close();
    });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(cur - 1);
      else if (e.key === 'ArrowRight') show(cur + 1);
      else if (e.key === 'Tab') { // keep focus inside the viewer
        var b = [].slice.call(lb.querySelectorAll('button')), k = b.indexOf(document.activeElement);
        e.preventDefault(); b[(k + (e.shiftKey ? -1 : 1) + b.length) % b.length].focus();
      }
    });
    lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1));
    });
  }
})();
