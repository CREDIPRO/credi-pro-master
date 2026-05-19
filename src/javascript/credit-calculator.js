/**
 * Simulador de crédito de nómina (pago quincenal estimado).
 */
(function () {
  const WA_NUMBER = "525568701352";
  const MONTHLY_RATE = 0.03;
  const mexicanCurrency = { style: "currency", currency: "MXN" };

  const formatMoney = (value) =>
    new Intl.NumberFormat("es-MX", mexicanCurrency).format(Number(value));

  function initCreditCalculator() {
    const periodInput = document.querySelector("input#period");
    const amountInput = document.querySelector("input#amount");
    const amountText = document.querySelector("#amount-text");
    const resultsEl = document.querySelector("#results");
    const periodLabel = document.querySelector("#period-label");
    const totalEl = document.querySelector("#total-payment");
    const form = document.querySelector("form#calculator-form");
    const waLink = document.querySelector("[data-sim-whatsapp]");

    if (!periodInput || !amountInput || !amountText || !resultsEl) return;

    const calculate = () => {
      const amount = parseFloat(amountInput.value);
      const periods = parseInt(periodInput.value, 10);

      if (Number.isNaN(amount) || Number.isNaN(periods)) return;

      const payment =
        (amount * MONTHLY_RATE) / (1 - Math.pow(1 + MONTHLY_RATE, -periods));
      const total = payment * periods;

      amountText.textContent = formatMoney(amount);
      resultsEl.textContent = formatMoney(payment.toFixed(2));

      if (periodLabel) {
        periodLabel.textContent = `${periods} quincenas`;
      }
      if (totalEl) {
        totalEl.textContent = `Total estimado a pagar: ${formatMoney(total.toFixed(2))}`;
      }
      if (waLink) {
        const msg = `Hola Credipro, quiero solicitar un crédito de nómina.\n\nMonto: ${formatMoney(amount)}\nPlazo: ${periods} quincenas\nPago quincenal estimado: ${formatMoney(payment.toFixed(2))}`;
        waLink.href = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`;
      }
    };

    periodInput.addEventListener("input", calculate);
    amountInput.addEventListener("input", calculate);
    if (form) {
      form.addEventListener("submit", (e) => e.preventDefault());
    }

    calculate();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCreditCalculator);
  } else {
    initCreditCalculator();
  }
})();
