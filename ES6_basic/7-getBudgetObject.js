export default function getBudgetObject(income=income, gdp=gdp, capita=capita) {
	const budget = {
		income,
		gdp,
		capita
	};

	return budget;
  }
