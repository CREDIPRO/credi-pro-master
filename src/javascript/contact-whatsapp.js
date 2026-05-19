/**
 * Envía el formulario de contacto a WhatsApp con los datos capturados.
 */
(function () {
  const WA_NUMBER = "525568701352";

  function initContactWhatsApp() {
    const form = document.querySelector("#contact-form");
    if (!form) return;

    const openWhatsApp = (event) => {
      event.preventDefault();

      const name = form.querySelector("#fullname")?.value.trim() || "";
      const email = form.querySelector("#email")?.value.trim() || "";
      const phone = form.querySelector("#phone")?.value.trim() || "";
      const message = form.querySelector("#message")?.value.trim() || "";

      let text = "Hola Credipro, me gustaría recibir información.";
      if (name) text += `\n\n*Nombre:* ${name}`;
      if (email) text += `\n*Correo:* ${email}`;
      if (phone) text += `\n*Teléfono:* ${phone}`;
      if (message) text += `\n\n*Mensaje:*\n${message}`;

      window.open(
        `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`,
        "_blank",
        "noopener,noreferrer"
      );
    };

    form.addEventListener("submit", openWhatsApp);
    form.querySelector("[data-whatsapp-submit]")?.addEventListener("click", openWhatsApp);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initContactWhatsApp);
  } else {
    initContactWhatsApp();
  }
})();
