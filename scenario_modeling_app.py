import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page config ---
st.set_page_config(page_title="SaaS Scenario Modeling", layout="centered")
st.title("📊 SaaS Scenario Modeling")

# --- Scenario selector ---
scenario = st.radio("Choose a Scenario", ["Base", "Best Case", "Worst Case"], horizontal=True)

# --- Scenario presets ---
scenario_inputs = {
    "Base": {
        "ARPU": 200,
        "Gross Margin %": 0.80,
        "Lifetime": 24,
        "CAC": 200,
        "New Customers": 250,
        "Fixed Costs": 40000
    },
    "Best Case": {
        "ARPU": 250,
        "Gross Margin %": 0.85,
        "Lifetime": 30,
        "CAC": 180,
        "New Customers": 300,
        "Fixed Costs": 35000
    },
    "Worst Case": {
        "ARPU": 150,
        "Gross Margin %": 0.70,
        "Lifetime": 18,
        "CAC": 250,
        "New Customers": 150,
        "Fixed Costs": 45000
    }
}

# --- Sidebar editable inputs ---
st.sidebar.header("✏️ Editable Inputs")
defaults = scenario_inputs[scenario]

ARPU = st.sidebar.number_input("ARPU (Monthly Revenue)", min_value=0.0, value=float(defaults["ARPU"]))
gross_margin = st.sidebar.slider("Gross Margin %", 0, 100, int(defaults["Gross Margin %"] * 100)) / 100
lifetime = st.sidebar.number_input("Customer Lifetime (Months)", min_value=1, value=int(defaults["Lifetime"]))
CAC = st.sidebar.number_input("CAC (Customer Acquisition Cost)", min_value=0.0, value=float(defaults["CAC"]))
new_customers = st.sidebar.number_input("New Customers per Month", min_value=1, value=int(defaults["New Customers"]))
fixed_costs = st.sidebar.number_input("Fixed Costs (Monthly)", min_value=0.0, value=float(defaults["Fixed Costs"]))

# --- Calculations ---
monthly_revenue = ARPU * new_customers
monthly_gross_profit = monthly_revenue * gross_margin
monthly_CAC_spend = CAC * new_customers
monthly_burn = fixed_costs + monthly_CAC_spend
net_cash_flow = monthly_gross_profit - monthly_burn
LTV = ARPU * gross_margin * lifetime
LTV_CAC_ratio = LTV / CAC if CAC else 0
payback_period = CAC / (ARPU * gross_margin) if ARPU * gross_margin else 0

# --- Results table ---
metrics_df = pd.DataFrame({
    "Metric": [
        "Monthly Revenue",
        "Monthly Gross Profit",
        "CAC Spend",
        "Fixed Costs",
        "Monthly Burn",
        "Net Cash Flow",
        "Customer Lifetime Value (LTV)",
        "LTV:CAC Ratio",
        "Payback Period (Months)"
    ],
    "Value": [
        f"${monthly_revenue:,.0f}",
        f"${monthly_gross_profit:,.0f}",
        f"${monthly_CAC_spend:,.0f}",
        f"${fixed_costs:,.0f}",
        f"${monthly_burn:,.0f}",
        f"${net_cash_flow:,.0f}",
        f"${LTV:,.0f}",
        f"{LTV_CAC_ratio:.2f}x",
        f"{payback_period:.2f}"
    ]
})

st.subheader("📉 Scenario Metrics")
st.table(metrics_df)

# --- Chart ---
st.subheader("📊 Cash Flow Breakdown")

chart_df = pd.DataFrame({
    "Metric": ["Gross Profit", "CAC Spend", "Fixed Costs", "Net Cash Flow"],
    "Value": [monthly_gross_profit, monthly_CAC_spend, fixed_costs, net_cash_flow]
})

fig, ax = plt.subplots()
ax.bar(chart_df["Metric"], chart_df["Value"])
ax.set_ylabel("Monthly $ Amount")
ax.set_title("Cash Flow by Component")
st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 0.9em; color: gray;'>"
    "Built by <a href='https://www.linkedin.com/in/timphamtx' target='_blank'>Tim Pham</a>"
    "</div>",
    unsafe_allow_html=True
)
