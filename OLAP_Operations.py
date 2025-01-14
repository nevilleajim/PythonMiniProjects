import pandas as pd
import de

# Sample data: sales transactions
data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'North', 'East', 'South', 'North'],
    'Sales': [100, 150, 200, 300, 250, 150, 400, 500, 300, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# OLAP operation: Summarize total sales by Product and Region
olap_result = df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum', fill_value=0)

print(olap_result)
