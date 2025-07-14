import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the financial data for the 20-year loan repayment period
years = list(range(0, 21))

# Initial investment at year 0
initial_investment = -129840000  # THB

# Annual revenue and costs
annual_revenue = 34000000  # THB
annual_operating_cost = 0.6 * annual_revenue  # 60% of revenue

# Calculate annual net cash flow after operating costs
annual_net_cash_flow = annual_revenue - annual_operating_cost

# Prepare cash flow list
cash_flows = [initial_investment] + [annual_net_cash_flow] * 20

# Calculate accumulated cash flow
accumulated_cash_flow = []
accum = 0
for cf in cash_flows:
    accum += cf
    accumulated_cash_flow.append(accum)

# Create DataFrame
df = pd.DataFrame({
    'Year': years,
    'Cash Flow (THB)': cash_flows,
    'Accumulated Cash Flow (THB)': accumulated_cash_flow
})

# Save to CSV
csv_filename = 'ton_mai_spa_phuket_financial_projection.csv' # edit name for new file
df.to_csv(csv_filename, index=False)

# --- Visualization ---
# Set the style to dark for the plot
plt.style.use('dark_background')
plt.rcParams.update({
    "figure.facecolor":  (0.12, 0.12, 0.12, 1),
    "axes.facecolor":    (0.12, 0.12, 0.12, 1),
    "axes.edgecolor":    "white",
    "axes.labelcolor":   "white",
    "xtick.color":       "white",
    "ytick.color":       "white",
    "text.color":        "white",
    "axes.titlecolor":   "white"
})


# Reshape the DataFrame for comparative plotting
df_melted = df.melt(id_vars=['Year'], value_vars=['Cash Flow (THB)', 'Accumulated Cash Flow (THB)'],
                    var_name='Flow Type', value_name='Amount (THB)')

# Create a figure and a set of subplots
plt.figure(figsize=(18, 8))

# Create the comparative bar chart
sns.barplot(x='Year', y='Amount (THB)', hue='Flow Type', data=df_melted, palette='magma')

plt.title('Comparative Cash Flow Analysis', fontsize=18)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Amount (THB)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
plt.savefig('cash_flow_comparative_visualization_dar.png')

# Show the plot
plt.show()

print("Comparative visualization has been generated and saved as 'cash_flow_comparative_visualization_dar.png'")
