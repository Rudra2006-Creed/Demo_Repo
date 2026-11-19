def analyze_products(products):
    total = 0
    highest_revenue = 0
    highest_product = ""

    for product,quantity,price in products:
        revenue=quantity*price
        print(f"{product}: {revenue}")
        total+=revenue

        if revenue > highest_revenue:
            highest_revenue=revenue
            highest_product=product
    average = total / len(products)

    print(f"Total Revenue: {total}")
    print(f"Highest Revenue Product: {highest_product}")
    print(f"Average Revenue: {above_average}")

    above_average = []

    for product,quantity,price in products:
            revenue=quantity*price
            if revenue>average:
                above_average.append(product)

    print("Above Average:", ",".join(above_average))

n=int(input())
products = []

for i in range(n):
    name,quantity,price = input().split()
    products.append((name,int(quantity),int(price)))

analyze_products(products)