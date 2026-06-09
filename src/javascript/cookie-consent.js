(function () {
  var CONSENT_KEY = "credipro_cookie_consent";
  var CONSENT_DAYS = 365;

  function getJsBase() {
    var script = document.currentScript || document.querySelector('script[src*="cookie-consent.js"]');
    if (script && script.getAttribute("src")) {
      return script.getAttribute("src").replace(/cookie-consent\.js(\?.*)?$/, "");
    }
    var parts = window.location.pathname.replace(/\/$/, "").split("/").filter(Boolean);
    return (parts.length === 0 ? "./" : "../".repeat(parts.length)) + "src/javascript/";
  }

  function getStylesHref(jsBase) {
    return jsBase.replace("/javascript/", "/styles/") + "cookie-consent.css?v=1";
  }

  function getPrivacyHref() {
    var parts = window.location.pathname.replace(/\/$/, "").split("/").filter(Boolean);
    if (parts.length === 0) return "./privacidad/";
    return "../".repeat(parts.length) + "privacidad/";
  }

  function loadStylesheet(href) {
    if (document.querySelector('link[href*="cookie-consent.css"]')) return;
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = href;
    document.head.appendChild(link);
  }

  function loadPixel(jsBase) {
    if (document.querySelector('script[src*="meta-pixel.js"]')) return;
    var s = document.createElement("script");
    s.src = jsBase + "meta-pixel.js";
    s.async = true;
    document.head.appendChild(s);
  }

  function readConsent() {
    try {
      var raw = localStorage.getItem(CONSENT_KEY);
      if (!raw) return null;
      var data = JSON.parse(raw);
      var maxAge = CONSENT_DAYS * 24 * 60 * 60 * 1000;
      if (Date.now() - data.at > maxAge) {
        localStorage.removeItem(CONSENT_KEY);
        return null;
      }
      return data.value;
    } catch (e) {
      return null;
    }
  }

  function saveConsent(value) {
    localStorage.setItem(
      CONSENT_KEY,
      JSON.stringify({ value: value, at: Date.now() })
    );
  }

  function removeBanner() {
    var el = document.getElementById("credipro-cookie-banner");
    if (el) el.remove();
  }

  function showBanner(jsBase) {
    if (document.getElementById("credipro-cookie-banner")) return;

    var privacyHref = getPrivacyHref();
    var banner = document.createElement("div");
    banner.id = "credipro-cookie-banner";
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", "Aviso de cookies");
    banner.innerHTML =
      '<div class="cookie-banner__inner">' +
      '<p class="cookie-banner__text">Utilizamos cookies para mejorar tu experiencia en el sitio. Puedes aceptar o rechazar las opcionales. Más información en nuestra <a href="' +
      privacyHref +
      '">Política de privacidad</a>.</p>' +
      '<div class="cookie-banner__actions">' +
      '<button type="button" class="cookie-banner__btn cookie-banner__btn--reject" data-cookie-reject>Rechazar</button>' +
      '<button type="button" class="cookie-banner__btn cookie-banner__btn--accept" data-cookie-accept>Aceptar</button>' +
      "</div></div>";

    document.body.appendChild(banner);

    banner.querySelector("[data-cookie-accept]").addEventListener("click", function () {
      saveConsent("accepted");
      removeBanner();
      loadPixel(jsBase);
    });

    banner.querySelector("[data-cookie-reject]").addEventListener("click", function () {
      saveConsent("rejected");
      removeBanner();
    });
  }

  function init() {
    var jsBase = getJsBase();
    loadStylesheet(getStylesHref(jsBase));

    var consent = readConsent();
    if (consent === "accepted") {
      loadPixel(jsBase);
      return;
    }
    if (consent === "rejected") {
      return;
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", function () {
        showBanner(jsBase);
      });
    } else {
      showBanner(jsBase);
    }
  }

  init();
})();
