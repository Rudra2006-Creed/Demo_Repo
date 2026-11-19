n = int(input())
inventory ={}

for i in range(n):
    name, quantity = input().split()
    inventory[name] = quantity

    # ADD
name, quantity = input().split()
inventory[name]=quantity

# remove

name = input()

inventory.pop(name)

# print(inventory)

for name, quantity in inventory.items():
    print(f"{name}: {quantity}")