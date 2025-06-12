# SaaS-Scenario-Model# SaaS Scenario Modeling App

👉 [Live App on Streamlit](https://saas-scenario-model-app-bqh8w6p52shrs9urxlaje7.streamlit.app)  
📁 [Code on GitHub](https://github.com/TimothyTPham/SaaS-Scenario-Model-Streamlit)

---

This interactive tool models how different business scenarios impact SaaS financial outcomes. Users can toggle between Base, Best Case, and Worst Case assumptions — with the ability to edit each input — to see how core metrics respond in real time.

## Initial Scenario Assumptions

| Metric                   | Base      | Best Case | Worst Case |
|--------------------------|-----------|-----------|------------|
| ARPU                     | $200      | $250      | $150       |
| Gross Margin %           | 80%       | 85%       | 70%        |
| Customer Lifetime (mo)   | 24        | 30        | 18         |
| CAC                      | $200      | $180      | $250       |
| New Customers / Month    | 250       | 300       | 150        |
| Fixed Costs / Month      | $40,000   | $35,000   | $45,000    |

All inputs are editable in the sidebar, so users can adjust assumptions as needed.

## Key Metrics

- Monthly Revenue
- Gross Profit
- CAC Spend
- Monthly Burn
- Net Cash Flow
- Customer Lifetime Value (LTV)
- LTV:CAC Ratio
- Payback Period

## Purpose

To demonstrate how financial levers like ARPU, CAC, and Gross Margin affect SaaS profitability and cash flow across different planning scenarios. Useful for FP&A, operators, and founders.

## Built With

- Streamlit
- Python (Pandas, Matplotlib)

## Functionality

- Toggle between Base, Best Case, and Worst Case scenarios
- Adjust all assumptions via sidebar inputs
- View key unit metrics in a live-updating table
- Visualize CAC, Gross Profit, Fixed Costs, and Net Cash Flow in a chart
- Includes dynamic ratio analysis (LTV:CAC, Payback)

## Author

Tim Pham  
[LinkedIn →](https://www.linkedin.com/in/timphamtx)
