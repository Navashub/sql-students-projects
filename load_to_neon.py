import psycopg
from pathlib import Path

conn_str = 'postgresql://neondb_owner:npg_ioJQew4rnMC9@ep-square-credit-anpj5kzh-pooler.c-6.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require'

csv_path = Path('retail_sales_dataset.csv')

with psycopg.connect(conn_str) as conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS retail_sales (
                transaction_id INTEGER PRIMARY KEY,
                date DATE,
                customer_id TEXT,
                gender TEXT,
                age INTEGER,
                product_category TEXT,
                quantity INTEGER,
                price_per_unit NUMERIC,
                total_amount NUMERIC
            )
        ''')
        with csv_path.open('r', encoding='utf-8') as f:
            with cur.copy(
                "COPY retail_sales (transaction_id, date, customer_id, gender, age, product_category, quantity, price_per_unit, total_amount) FROM STDIN WITH CSV HEADER"
            ) as copy:
                copy.write(f.read())
    with conn.cursor() as cur:
        cur.execute('SELECT COUNT(*) FROM retail_sales')
        print('row_count', cur.fetchone()[0])
