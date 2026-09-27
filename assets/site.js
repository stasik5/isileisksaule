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
})();
