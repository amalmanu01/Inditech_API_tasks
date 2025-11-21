
import requests
import sqlite3

API_URL = "http://api.petpooja.com/V1/orders/get_sales_data/?app_key=srd2neaq1xg7bzc6uyk5jmwv98o4tpfh&app_secret=fd08934c5224af4c975015e599d60a74bf857b4a&access_token=0442e1ee9899bc3806f1a40be490af4ec5c6602a&restID=51wok2zxnsad&from_date=2025-01-20%2000:00:00&to_date=2025-01-20%2023:59:59"

DB = "sales_data.db"

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        receipt_number TEXT,
        sale_date TEXT,
        transaction_time TEXT,
        sale_amount REAL,
        tax_amount REAL,
        discount_amount REAL,
        round_off REAL,
        net_sale REAL,
        payment_mode TEXT,
        order_type TEXT,
        transaction_status TEXT
    );
    """)
    conn.commit()
    conn.close()
    print("DBok")

def fetch_sales_data():
    resp = requests.get(API_URL)
    data = resp.json()
    if data.get("success") != "1":
        return None

    if "Records" not in data:
        return None
    return data["Records"]
def insert_sales_data(records):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    for r in records:
        cursor.execute("""
            INSERT INTO sales_data (
                receipt_number,
                sale_date,
                transaction_time,
                sale_amount,
                tax_amount,
                discount_amount,
                round_off,
                net_sale,
                payment_mode,
                order_type,
                transaction_status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            r.get("Receipt number"),
            r.get("Receipt Date"),
            r.get("Transaction Time"),
            float(r.get("Invoice amount", 0)),
            float(r.get("Tax amount", 0)),
            float(r.get("Discount amount", 0)),
            float(r.get("Round Off", 0)),
            float(r.get("Net sale", 0)),
            r.get("Payment Mode"),
            r.get("Order Type"),
            r.get("Transaction status")
        ))

    conn.commit()
    conn.close()

def main():
    init_db()
    records = fetch_sales_data()
    
    if records:
        insert_sales_data(records)
    else:
        print("err")


if __name__ == "__main__":
    main()
