import pandas as pd
from sqlalchemy import create_engine, text 
from pathlib import Path

CSV = Path(r'C:\Documents\Data analytics\projects\my-data-project\E-COMMERCE PROJECT\data\raw\Amazon Sale Report.csv')
DB_USER = 'postgres'        
DB_PASS = '27082002'
DB_HOST = 'localhost'
DB_PORT = 5433
DB_NAME = 'akshat_da'        
TABLE = 'public.ecommerce_amazon'

# read csv
df = pd.read_csv(CSV, low_memory=False)


#clean (column names -> snake_case, strip .0 from postal code, parse date)
df.columns = [c.strip().lower().replace(' ', '_').replace('-', '_') for c in df.columns]
if 'date' in df.columns:
    df['order_date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=False)
if 'ship_postal_code' in df.columns:
    df['ship_postal_code'] = df['ship_postal_code'].astype(str).str.replace(r'\.0$', '', regex=True).replace({'nan': None})

#  create engine and push
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


# df.to_sql will try to map dtypes automatically. Use if_exists='replace' or 'append'
df.to_sql(name=TABLE.split('.')[-1], schema='public', con=engine, if_exists='replace', index=False, method='multi', chunksize=5000)

# verification
with engine.connect() as conn:
    res = conn.execute(text("SELECT COUNT(*) FROM public.ecommerce_amazon"))
    print("rows in table:", res.scalar())

