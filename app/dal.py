from typing import List, Dict, Any

def get_customers_by_credit_limit_range(conn):
    from db import get_db_connection
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT customerName, creditLimit
                    FROM customers
                    WHERE creditLimit < 10000 or creditLimit > 100000
                    ''')
        
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()

def get_orders_with_null_comments(conn):

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT orderNumber,comments 
                    FROM orders
                    WHERE comments is not null
                    ORDER BY orderDate
                    ''')
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()

def get_first_5_customers(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT customerName, contactFirstName, contactLastName
                    FROM customers
                    ORDER BY contactLastName
                    LIMIT 5
                    ''')
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()
        
def get_payments_total_and_average(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT sum(amount), avg(amount), max(amount), min(amount)
                    FROM payments
                    ''')
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()

def get_employees_with_office_phone(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT e.firstName,e.lastName, offi.phone
                    FROM employees as e
                    JOIN offices as offi
                    ON e.officeCode = offi.officeCode
                    ''')
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()

def get_customers_with_shipping_dates(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT c.customerName, o.requiredDate
                    FROM customers as c
                    JOIN orders as o
                    ON c.customerNumber = o.customerNumber
                    ''')
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()

def get_customer_quantity_per_order(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT c.customerName, max(od.orderLineNumber) as maxByOrder 
                    FROM customers as c
                    JOIN orders as o
                    ON c.customerNumber = o.customerNumber
                    JOIN orderdetails as od
                    ON o.orderNumber = od.orderNumber
                    GROUP BY od.orderNumber
                    ORDER BY customerName
                    ''')
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()

def get_customers_payments_by_lastname_pattern(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    SELECT c.customerName, concat(e.firstName, " ", e.lastName) as employeeName, sum(p.amount) as total
                    FROM customers as c
                    JOIN employees as e
                    ON c.salesRepEmployeeNumber = e.employeeNumber
                    JOIN payments as p
                    ON p.customerNumber = c.customerNumber
                    WHERE e.firstName LIKE '%ly%' or '%mu%'
                    GROUP BY p.customerNumber
                    ORDER BY total DESC
                    ''')
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()
