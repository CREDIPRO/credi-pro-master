const periodInputElement = document.querySelector("input#period");
const amountInputElement = document.querySelector("input#amount");
const amountTextElement = document.querySelector("h3#amount-text");
const resultInputElement = document.querySelector("#results");
const formElement = document.querySelector("form#calculator-form");
const mexicanCurrency = { style: "currency", currency: "MXN" };

const calculateCreditAmount = () => {
  try {
    const amount = parseFloat(amountInputElement.value.replace(/,/g, ""));
    const time = parseInt(periodInputElement.value);
    const rate = 0.03;

    if (isNaN(amount) || isNaN(time)) throw new Error("Por favor, ingresa valores válidos.");

    const payment = (amount * rate) / (1 - Math.pow(1 + rate, -time));
    const textContext = getCurrencyFormat(payment.toFixed(2));
    const currency = getCurrencyFormat(amount);

    amountTextElement.textContent = currency ?? 0;
    resultInputElement.value = textContext ?? 0;
  } catch (error) {
    window.alert(error.message);
  }
};

const getCurrencyFormat = (value) => new Intl.NumberFormat("es-MX", mexicanCurrency).format(value);

periodInputElement.addEventListener("input", calculateCreditAmount);
amountInputElement.addEventListener("input", calculateCreditAmount);
formElement.addEventListener("submit", (e) => e.preventDefault());

calculateCreditAmount();
