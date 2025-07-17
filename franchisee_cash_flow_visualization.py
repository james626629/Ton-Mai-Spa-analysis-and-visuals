import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Financial Data Definition ---
# This script visualizes the cash flow for a franchisee over a 10-year period.
# The calculations are based on the cost analysis provided in 'Cost Analysis - Cost analysis test.csv'.

years = list(range(0, 11))  # Year 0 for initial investment, then 10 years of operation

# --- Initial Investment Calculation ---
# This is the sum of all one-time costs required to start the franchise.
# 1. Construction (Renovation): 5,000,000
# 2. Interior Decoration & Equipment: 2,000,000
# 3. Franchisee Fee: 6,000,000
# 4. Staffing & Training (Pre-opening): 250,000
# 5. Working Capital Reserve: 1,000,000
# 6. Marketing, Branding, Grand Opening (One-time): 70,000
# Total = 14,320,000 THB
initial_investment = -14320000  # THB

# --- Annual Net Profit Calculation ---
# This is the calculated profit after all annual costs and taxes.
# The provided data states a target profit margin of 35% on 36M THB annual sales.
# This implies total annual costs of 23.4M THB (36M * (1 - 0.35)).
# The itemized recurring costs (rent, licenses, royalties, etc.) from the source file sum to a much lower figure.
# Therefore, this calculation proceeds based on the stated 35% profit margin,
# assuming it correctly accounts for all costs (including large non-itemized costs like salaries).

# 1. Projected Annual Sales: 36,000,000 THB
# 2. Projected Profit Margin (Pre-tax): 35%
# 3. Annual Profit (Pre-tax): 36,000,000 * 0.35 = 12,600,000 THB
# 4. Corporate Income Tax (CIT) is 20% on net profit.
# 5. Tax Amount: 12,600,000 * 0.20 = 2,520,000 THB
# 6. Annual Profit (After Tax): 12,600,000 - 2,520,000 = 10,080,000 THB
# 7. Annual Net Profit: 10,080,000 THB- 2,210,000 THB = 7,870,000 THB 
annual_net_profit = 7870000  # THB 

# Prepare cash flow list: Year 0 is the initial investment, followed by 10 years of profit
cash_flows = [initial_investment] + [annual_net_profit] * 10

# Calculate the accumulated cash flow over the years
accumulated_cash_flow = []
current_accumulation = 0
for cf in cash_flows:
    current_accumulation += cf
    accumulated_cash_flow.append(current_accumulation)

# Create a pandas DataFrame to hold the financial data
df = pd.DataFrame({
    'Year': years,
    'Cash Flow (THB)': cash_flows,
    'Accumulated Cash Flow (THB)': accumulated_cash_flow
})

# Save the DataFrame to a CSV file for record-keeping
csv_filename = 'franchisee_financial_projection.csv'
df.to_csv(csv_filename, index=False)

# --- Visualization ---
# Set a dark theme for the plot for better visual appeal
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

# Reshape the DataFrame to make it suitable for plotting with seaborn's hue parameter
df_melted = df.melt(id_vars=['Year'], value_vars=['Cash Flow (THB)', 'Accumulated Cash Flow (THB)'],
                    var_name='Flow Type', value_name='Amount (THB)')

# Create a figure and axes for the plot
plt.figure(figsize=(18, 8))

# Generate the comparative bar chart using seaborn
sns.barplot(x='Year', y='Amount (THB)', hue='Flow Type', data=df_melted, palette='magma')

# Set plot titles and labels
plt.title('Franchisee Cash Flow Analysis (10 Years)', fontsize=18)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Amount (THB)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the generated plot to a file
output_image_filename = 'franchisee_cash_flow_comparative_visualization.png'
plt.savefig(output_image_filename)

# Display the plot
plt.show()

print(f"Comparative visualization has been generated and saved as '{output_image_filename}'")
print(f"Financial projection data saved to '{csv_filename}'")
