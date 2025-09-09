"""Модуль для управления данными клиентов и заказов.

Предоставляет функционал для расчета скидок и генерации отчетов.
"""

class Customer:
    """Класс для представления клиента и его заказов.
    
    Attributes:
        customer_id (int): Уникальный идентификатор клиента
        customer_name (str): Имя клиента
        orders (List[Order]): Список заказов клиента
    """
    
    def __init__(self, customer_id: int, customer_name: str) -> None:
        """Инициализирует объект клиента.
        
        Args:
            customer_id: Уникальный идентификатор клиента
            customer_name: Имя клиента
        """
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.orders = []

    def add_order(self, order: 'Order') -> None:
        """Добавляет заказ в список заказов клиента.
        
        Args:
            order: Объект заказа для добавления
        """
        self.orders.append(order)

    def get_total_amount(self) -> float:
        """Вычисляет общую сумму всех заказов клиента.
        
        Returns:
            float: Общая сумма заказов
        """
        return sum(order.amount for order in self.orders)


class Order:
    """Класс для представления заказа.
    
    Attributes:
        order_id (int): Уникальный идентификатор заказа
        amount (float): Сумма заказа
    """
    
    def __init__(self, order_id: int, amount: float) -> None:
        """Инициализирует объект заказа.
        
        Args:
            order_id: Уникальный идентификатор заказа
            amount: Сумма заказа
        """
        self.order_id = order_id
        self.amount = amount


def calculate_discount(customer: Customer) -> float:
    """Рассчитывает скидку для клиента на основе общей суммы заказов.
    
    Скидка в размере 10% предоставляется, если общая сумма заказов
    превышает 1000 единиц.
    
    Args:
        customer: Объект клиента для расчета скидки
        
    Returns:
        float: Размер скидки
    """
    total_amount = customer.get_total_amount()
    
    if total_amount > 1000:
        return total_amount * 0.1
    return 0.0


def print_customer_report(customer_obj) -> None:
    """Выводит детальный отчет по клиенту и его заказам.
    
    Отчет включает:
    - Имя клиента
    - Количество заказов
    - Общую сумму заказов
    - Размер скидки
    - Среднюю сумму заказа
    
    Args:
        customer: Объект клиента для генерации отчета
    """
    print('Customer Report for:', customer_obj.customer_name )
    print('Total Orders:', len(customer_obj.orders))
    total_amount = customer_obj.get_total_amount()
    print('Total Amount:', total_amount)
    print('Discount:', calculate_discount(customer_obj))
    print('Average Order:', total_amount / len(customer_obj.orders) if customer_obj.orders else '-')
