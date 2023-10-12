# Mixed Product Data Structure
products = [
    {
        "id": 1,
        "name": "Laptop",
        "categories": ["Electronics", "Computers"],
        "price": 1000,
        "specs": {
            "RAM": "16GB",
            "Storage": "512GB SSD"
        },
        "in_stock": True
    },
    {
        "id": 2,
        "name": "Coffee Maker",
        "categories": ["Home Appliances"],
        "price": 100,
        "specs": {
            "Capacity": "12 Cups",
            "Auto Shut-Off": "Yes"
        },
        "in_stock": False
    },
    {
        "id": 3,
        "name": "Smartphone",
        "categories": ["Electronics", "Mobiles"],
        "price": 700,
        "specs": {
            "Screen Size": "6.1 inches",
            "Battery Life": "24 hours"
        },
        "in_stock": True
    }
]

# Exercise 1: Print the names and categories of each product
print("+++++++++++++++++++EXERCISE 1+++++++++++++++++++")
for product in products:
    print(f"Product name: {product['name'].upper()} & Category:{product['categories']}")

# # Exercise 2: Calculate the average price of in-stock products
print("+++++++++++++++++++EXERCISE 2+++++++++++++++++++")


# # Exercise 3: List products with more than one category
# print("+++++++++++++++++++EXERCISE 3+++++++++++++++++++")
# # Exercise 4: Print the specs of each in-stock product
# print("+++++++++++++++++++EXERCISE 4+++++++++++++++++++")
# # Exercise 5: Find the most expensive in-stock product
# print("+++++++++++++++++++EXERCISE 5+++++++++++++++++++")
# # Exercise 6: Count the number of in-stock products that have "Auto Shut-Off" feature
# print("+++++++++++++++++++EXERCISE 6+++++++++++++++++++")
# # Exercise 7: Update the price of all in-stock products by 10%
# print("+++++++++++++++++++EXERCISE 7+++++++++++++++++++")
# # Exercise 8: Print the names of products costing more than $200
# print("+++++++++++++++++++EXERCISE 8+++++++++++++++++++")
# # Exercise 9: List products that belong to the 'Electronics' category
# print("+++++++++++++++++++EXERCISE 9+++++++++++++++++++")
# # Exercise 10: Calculate the average screen size of in-stock smartphones
# print("+++++++++++++++++++EXERCISE 10+++++++++++++++++++")
