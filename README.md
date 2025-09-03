# Система управления клиентами и заказами

Python-скрипт для управления данными клиентов, расчета скидок и генерации отчетов.

##  Оглавление

- [Возможности](#-возможности)
- [Установка](#-установка)
- [Использование](#-использование)

##  Возможности

-  Управление данными клиентов и заказов
-  Автоматический расчет скидок (10% при сумме > 1000)
-  Генерация детальных отчетов


##  Установка

1. Клонируйте репозиторий:
   git clone https://github.com/ktulhu2k/customer_system.git

2. Убедитесь, что у вас установлен Python 3.7+

##  Использование
```python
python
from customer_system import Customer, Order, print_customer_report

c1 = Customer(1,"SAP Customer")
o1 = Order(101,500)
o2 = Order(102,800)
c1.add_order(o1)
c1.add_order(o2)

print_customer_report(c1)

c2=Customer(2,"Empty Customer")
print_customer_report(c2)
```

