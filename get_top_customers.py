orders = [
    {
        "id": 1,
        "customer": "Иван",
        "items": [
            {"name": "Ноутбук", "price": 50000},
            {"name": "Мышь", "price": 1500}
        ]
    },
    {
        "id": 2,
        "customer": "Мария",
        "items": [
            {"name": "Телефон", "price": 30000},
            {"name": "Чехол", "price": 1000},
            {"name": "Зарядка", "price": 2000}
        ]
    },
    {
        "id": 3,
        "customer": "Иван",
        "items": [
            {"name": "Клавиатура", "price": 3000}
        ]
    }
]
# - > [("Иван", 54500), ("Мария", 33000)]
# - 1)
r_data = []
for i_orders in orders:
    customer = i_orders.get('customer')
    sum_items = sum(i['price'] for i in i_orders.get('items'))
    r_data.append((customer, sum_items))
result = {}
for name, value in r_data:
    if name in result:
        result[name] += value
    else:
        result[name] = value
result_list = sorted(list(result.items()), key=lambda x: x[1], reverse=True)
print(result_list)
# - 2)
def get_top_customers(orders, n):
    totals = {}
    for order in orders:
        customer = order["customer"]
        order_sum = sum(item["price"] for item in order["items"])
        totals[customer] = totals.get(customer, 0) + order_sum
    
    result_list = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return result_list[:n]
print(get_top_customers(orders, 2))
# - 3)
from collections import Counter

def get_top_customers(orders, n):
    counter = Counter()
    for order in orders:
        counter[order["customer"]] += sum(item["price"] for item in order["items"])
    return counter.most_common(n)
print(get_top_customers(orders, 2))
