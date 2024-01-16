function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};

  budget[`income-${getCurrentYear() - 3}`] = income;
  budget[`gdp-${getCurrentYear() - 3}`] = gdp;
  budget[`capita-${getCurrentYear() - 3}`] = capita;

  return budget;
}
