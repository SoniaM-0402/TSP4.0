import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# 1. Load or Create Finance Data
try:
    df = pd.read_csv('finance_data.csv')
except FileNotFoundError:
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'Category': ['Income', 'Rent', 'Groceries', 'Entertainment', 'Transport', 'Utilities', 'Savings', 'Income', 'Shopping', 'Dining'],
        'Amount': [3000, -1200, -250, -150, -100, -200, -500, 3000, -300, -100]
    }
    df = pd.DataFrame(data)
    df.to_csv('finance_data.csv', index=False)

# 2. Data Preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# 3. Expense Categorization
expense_df = df[df['Amount'] < 0]
income_df = df[df['Amount'] > 0]

# 4. Budget Comparison (Sample Budget)
budget = {'Rent': -1200, 'Groceries': -400, 'Entertainment': -200, 'Transport': -150, 'Utilities': -250, 'Savings': -600, 'Shopping': -300, 'Dining': -200}
expense_summary = expense_df.groupby('Category')['Amount'].sum()
budget_df = pd.DataFrame({'Category': list(budget.keys()), 'Budget': list(budget.values())})
budget_df['Actual'] = budget_df['Category'].map(expense_summary)
budget_df.fillna(0, inplace=True)

# 5. Visualizations
plt.figure(figsize=(12, 6))
sns.barplot(x='Category', y='Actual', data=budget_df, color='red', label='Actual Spending')
sns.barplot(x='Category', y='Budget', data=budget_df, color='blue', alpha=0.5, label='Budget')
plt.title('Budget vs Actual Spending')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 6. Monthly Spending Trend
monthly_expense = expense_df.groupby('Month')['Amount'].sum()
plt.figure(figsize=(12, 6))
monthly_expense.plot(marker='o', linestyle='-', color='red')
plt.title('Monthly Expense Trend')
plt.xlabel('Month')
plt.ylabel('Total Expenses')
plt.grid(True)
plt.show()

# 7. Income vs Expenses Pie Chart
summary = {'Income': income_df['Amount'].sum(), 'Expenses': -expense_df['Amount'].sum()}
plt.figure(figsize=(6, 6))
plt.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Income vs Expenses Breakdown')
plt.show()

print("Analysis Summary:")
print("1. Budget comparison shows where overspending occurs.")
print("2. Monthly trend highlights spikes in expenses.")
print("3. Pie chart gives an overview of savings vs expenses.")
