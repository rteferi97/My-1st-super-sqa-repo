# Food data structure
food_menu = [
    {
        "category": "Appetizers",
        "items": [
            {"name": "Caesar Salad", "price": 8.99},
            {"name": "Garlic Bread", "price": 4.99},
            {"name": "Bruschetta", "price": 6.99}
        ]
    },
    {
        "category": "Main Course",
        "items": [
            {"name": "Steak", "price": 19.99},
            {"name": "Grilled Salmon", "price": 16.99},
            {"name": "Chicken Parmesan", "price": 14.99},
            {"name": "Vegetable Stir-Fry", "price": 12.99}
        ]
    },
    {
        "category": "Desserts",
        "items": [
            {"name": "Cheesecake", "price": 7.99},
            {"name": "Chocolate Brownie", "price": 5.99},
            {"name": "Ice Cream Sundae", "price": 6.99}
        ]
    }
]

# Exercise 1: Print the names of all food categories
# Easy one so start with this
print("+++++++++++++++++++EXERCISE 1+++++++++++++++++++")
for category in food_menu:
    print(category['category'])

# Exercise 2: Calculate the total price of all items in the menu
print("+++++++++++++++++++EXERCISE 2+++++++++++++++++++")

total_price = 0
for category in food_menu:
    for items in category["items"]:
        total_price = total_price + items["price"]

new_total = round(total_price,2)

print(f"Total price is: ${new_total}")


# Exercise 3: Find the most expensive item in each category --> keep it simple; start with what the question gives
print("+++++++++++++++++++EXERCISE 3+++++++++++++++++++")

# most_expensive_list = []

for category in food_menu:
    most_expensive_item = None
    for items in category["items"]:
        if most_expensive_item is None or items["price"] > most_expensive_item["price"]:#how is most_expensive_item["price"] existing?
            most_expensive_item = items
    print(f"Most expensive {category['category']} : {most_expensive_item['name']}")

# Exercise 4: Check if any category has items with a price greater than $20
print("+++++++++++++++++++EXERCISE 4+++++++++++++++++++")
has_expensive_items = False

for category in food_menu:
    for items in category['items']:
        if items["price"] > 10:
            has_expensive_items = True
            break
print(f" are there items above $20 ? {has_expensive_items}")

# Exercise 5: Print the names of the vegetarian items (category: Main Course, item: Vegetable Stir-Fry)
print("+++++++++++++++++++EXERCISE 5+++++++++++++++++++")

carnivorous_foods = ['salmon',"Salmon","Chicken", 'chicken', "Steak", 'steak']

vegetarian = []
for category in food_menu:
    for items in category['items']:
        if items['name'] not in carnivorous_foods:
            vegetarian.append(items['name'])
            # food_menu.remove(items['name'])

print(vegetarian)
# print(food_menu)

# print(f"Category: {category['category']}, item: {items['name']}")

# Exercise 6: Calculate the average price of items in the Desserts category
print("+++++++++++++++++++EXERCISE 6+++++++++++++++++++")

total_dessert_price = 0
dessert_items_count = 0
for category in food_menu:
    if category['category'] == "Desserts":
        for items in category['items']:
            total_dessert_price = total_dessert_price + items['price']
            dessert_items_count += 1
average_price = total_dessert_price/dessert_items_count

print(f"Average price of dessert: {round(average_price, 2)}")

# Exercise 7: Update the price of the Grilled Salmon item to $18.99
print("+++++++++++++++++++EXERCISE 7+++++++++++++++++++")

for category in food_menu:
    for items in category['items']:
        if items['name'] == "Grilled Salmon":
            items['price'] == 18.99



# Exercise 8: Print the names of the items with prices greater than $15
print("+++++++++++++++++++EXERCISE 8+++++++++++++++++++")

items_above_15 = []


for category in food_menu:
    for items in category['items']:
        if items["price"] > 15:
            items_above_15.append(items['name']) #OR
            print(items['name'])
print(" ")
print("or in a different format... ")
print(" ")
print(f"Items above $15: {items_above_15}")

# Exercise 9: Find the cheapest item in the menu
print("+++++++++++++++++++EXERCISE 9+++++++++++++++++++")
# import pdb; pdb.set_trace()

cheapest_item = None

for category in food_menu:
    for items in category['items']:
        if cheapest_item is None or items['price'] < cheapest_item['price']:
            cheapest_item = items

print(cheapest_item)




# Exercise 10: Count the total number of items in the menu
print("+++++++++++++++++++EXERCISE 10+++++++++++++++++++")

total_item_count = 0

for category in food_menu:
    for items in category['items']:
        total_item_count += 1

print(total_item_count)