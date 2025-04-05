
budget = int(input("Введіть свій бюджет: "))


user_input = input("Введіть покупки (назва товару ціна): ")


purchases = user_input.split()


shopping_dict = {}


for i in range(0, len(purchases), 2):
    product_name = purchases[i]
    product_price = int(purchases[i + 1])
    shopping_dict[product_name] = product_price


total_cost = sum(shopping_dict.values())


if total_cost <= budget:
    print(f"Ви вміщаєтеся в бюджет! Залишок: {budget - total_cost} грн")
else:
    print(f"Не вистачає: {total_cost - budget} грн")

sorted_purchases = sorted(shopping_dict.items(), key=lambda x: x[1], reverse=True)


print("Список покупок у порядку спадання цін:")
for product, price in sorted_purchases:
    print(f"{product}: {price} грн")


