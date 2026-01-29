from fastapi import FastAPI
from db_init import init_database
from dal import *
from db import get_db_connection
import json
app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    conn = get_db_connection()
    return get_customers_by_credit_limit_range(conn)

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    conn = get_db_connection()
    return get_orders_with_null_comments(conn)

@app.get("/q3/customers-first-5")
def customers_first_5():
    conn = get_db_connection()
    return get_first_5_customers(conn)

@app.get("/q4/payments-total-average")
def payments_total_average():
    conn = get_db_connection()
    return get_payments_total_and_average(conn)

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    conn = get_db_connection()
    return get_employees_with_office_phone(conn)

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    conn = get_db_connection()
    return get_customers_with_shipping_dates(conn)

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    conn = get_db_connection()
    return get_customer_quantity_per_order(conn)

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern():
    conn = get_db_connection()
    return get_customers_payments_by_lastname_pattern(conn)