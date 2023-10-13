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






for category in food_menu:
    for item in category["items"]:
        if item["name"] == "Grilled Salmon":
            item["price"] = 18.99

print(food_menu)