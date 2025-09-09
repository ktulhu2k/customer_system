"""Модуль для демонстрации работы с клиентами и заказами.

Создает клиентов и заказы, добавляет заказы клиентам и выводит отчет.
"""

from customer_system import Customer, Order, print_customer_report

c1 = Customer(1,"SAP Customer")
o1 = Order(101,500)
o2 = Order(102,800)
c1.add_order(o1)
c1.add_order(o2)
print_customer_report(c1)
c2 = Customer(2,"Empty Customer")
print_customer_report(c2) 
