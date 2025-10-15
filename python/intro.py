import pandas as pd
import os

#paths
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, '..', 'data', 'raw', 'Amazon Sale Report.csv')
df = pd.read_csv(path, low_memory=False, parse_dates=['Date'], dayfirst=False)

# Basic overview
print('>> shape:', df.shape)
print('>> columns:', df.columns.tolist())
print('\n>> dtypes:\n', df.dtypes)

# Nulls & uniqueness
print('\n>> nulls per column:\n', df.isnull().sum())
print('\n>> unique counts (first 20 columns):\n', df.nunique().head(20))

# head and sample problematic checks
print('\n>> first row (transposed):\n', df.head(1).T)
print('\n>> numeric summary:\n', df.select_dtypes(include='number').describe().T)

# Date range check for order/date columns that look like dates
if 'Date' in df.columns:
    print('\n>> Date range:', df['Date'].min(), 'to', df['Date'].max())

# checks for negatives/zeros in common fields
for col in ['Quantity', 'Price', 'Sales', 'Profit', 'Unit Price']:
    if col in df.columns:
        print(f"\n>> {col} min, max:", df[col].min(), df[col].max(), "zeros:", (df[col]==0).sum())

# Saving audit to file
output_path = os.path.join(script_dir, '..', 'docs', 'schema_audit.txt')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('shape: ' + str(df.shape) + '\n')
    f.write('columns: ' + ','.join(df.columns.tolist()) + '\n\n')
    f.write('nulls per column:\n' + df.isnull().sum().to_string() + '\n\n')
    f.write('numeric summary:\n' + df.select_dtypes(include='number').describe().T.to_string() + '\n')
print(f'\nSaved {output_path}')
