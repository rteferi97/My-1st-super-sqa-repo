# Mixed Product Data Structure
products = [
    {
        "id": 1,
        "name": "Laptop",
        "categories": ["Electronics", "Computers"],
        "price": 1000,
        "specs": {
            "RAM": "16GB",
            "Storage": "512GB SSD",
            # "Auto Shut-Off": "yes"
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
            "Auto Shut-Off": "Yes",
            # "Screen Size": "8.1 inches"
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
            "Battery Life": "24 hours",
            # "Auto Shut-Off": "Yes"
        },
        "in_stock": True
    }
]

# # Exercise 1: Print the names and categories of each product
# print("+++++++++++++++++++EXERCISE 1+++++++++++++++++++")
# for product in products:
#     print(f"Name: {product['name'].upper()}, Categories: {', '.join(product['categories'])}")
#     print(f"Product name: {product['name'].upper()} & Category:{product['categories']}")
#
# # Exercise 2: Calculate the average price of in-stock products
# print("+++++++++++++++++++EXERCISE 2+++++++++++++++++++")
#
# total_in_stock_products = 0
# total_in_stock_price = 0
#
# for product in products:
#     if product['in_stock'] == True:
#         total_in_stock_price = total_in_stock_price + product['price']
#         total_in_stock_products += 1
# in_stock_avg = total_in_stock_price/total_in_stock_products
# print(in_stock_avg)
#
# # Exercise 3: List products with more than one category
# print("+++++++++++++++++++EXERCISE 3+++++++++++++++++++")
#
# for product in products:
#     if len(product['categories']) > 1:
#         print(product['name'])
#
#
#
#
# # Exercise 4: Print the specs of each in-stock product
# print("+++++++++++++++++++EXERCISE 4+++++++++++++++++++")
#
# for product in products:
#     if product['in_stock'] :
#         print(f" Specs of our in-stock products! --> {product['name']} : {product['specs']}")
#
#
# # Exercise 5: Find the most expensive in-stock product
# # print("+++++++++++++++++++EXERCISE 5+++++++++++++++++++")
#
# most_expensive_item_in_stock = None
# max_price = 0
#
# for product in products:
#     if product["in_stock"] and product["price"] > max_price:
#         max_price = product["price"]
#         most_expensive_product = product
#
# print(f"Most expensive product: {most_expensive_product['name']} --  Price: ${most_expensive_product['price']}")
# # #print(most_expensive_product['name'], "$", most_expensive_product['price'])
#
#
# # Exercise 6: Count the number of in-stock products that have "Auto Shut-Off" feature
# print("+++++++++++++++++++EXERCISE 6+++++++++++++++++++")
# auto_shutoff_count = 0
#
# for product in products:
#     if product['in_stock']:
#         if product['specs'].get("Auto Shut-Off"):
#             if product['specs'].get("Auto Shut-Off").lower() == 'yes':
#                 auto_shutoff_count += 1
#
# print(auto_shutoff_count)
#
# auto_shutoff_count = 0
# keyword_find = ['Auto Shut-Off']
#
# for product in products:
#     if product['in_stock']:
#         for info in product['specs']:
#            # # print(info)
#             if info in keyword_find:
#                 auto_shutoff_count += 1
# print(auto_shutoff_count)
#
# # Exercise 7: Update the price of all in-stock products by 10%
# print("+++++++++++++++++++EXERCISE 7+++++++++++++++++++")
#
# for product in products:
#     if product['in_stock']:
#         product['price'] = product['price'] + (product['price'] * .10)
#
# print(products)
#
# # Exercise 8: Print the names of products costing more than $200
# print("+++++++++++++++++++EXERCISE 8+++++++++++++++++++")
# items_over_20 = {}
#
# for product in products:
#     if product['price'] > 200:
#         items_over_20.update({product['name']: product['price']})
# print(items_over_20)
#
#
# # Exercise 9: List products that belong to the 'Electronics' category
# print("+++++++++++++++++++EXERCISE 9+++++++++++++++++++")
#
# electronics_category = []
# electronics_category_dict = {}
#
# for product in products:
#     for category in product['categories']:
#         # print(category)
#         if category.lower() == "electronics":
#             electronics_category.append(product['name'])
#             electronics_category_dict.update({product['name']: product['price']})
#
# print(electronics_category_dict)
#
# # Exercise 10: Calculate the average screen size of in-stock smartphones
# print("+++++++++++++++++++EXERCISE 10+++++++++++++++++++")
#
# total_screen_size = 0
# in_stock_smartphones = 0
#
# for product in products:
#     # print(product['name'].lower())
#     # if product['name'].lower() == "smartphone":
#     if product['in_stock'] and product['specs'].get("Screen Size"):
#         in_stock_smartphones += 1
#         screen_size = product['specs'].get("Screen Size").strip(" inches")
#         total_screen_size = total_screen_size + float(screen_size)
#
# avg_smartphone_price = round((total_screen_size / in_stock_smartphones), 2)
#
# print(avg_smartphone_price)
#
# # # different way..
# total_screen_size = 0
# in_stock_smartphones = 0
# for product in products:
#     # print(product['name'].lower())
#     if product['in_stock']:
#         specs = product['specs']
#         if "Screen Size" in specs.keys():
#             in_stock_smartphones += 1
#             screen_size = product['specs'].get("Screen Size").strip(" inches")
#             total_screen_size = total_screen_size + float(screen_size)
#
#
# avg_smartphone_price = round((total_screen_size/in_stock_smartphones),2)
# print(avg_smartphone_price)
#