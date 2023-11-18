# table data
basket = [
    {"Product": "Leather wallet", "Unit Price": 1100, "GST": 18, "Quantity": 1},
    {"Product": "Umbrella", "Unit Price": 900, "GST": 12, "Quantity": 4},
    {"Product": "Cigarette", "Unit Price": 200, "GST": 28, "Quantity": 3},
    {"Product": "Honey", "Unit Price": 0, "GST": 0, "Quantity": 2}
]
max_gst_product = max(basket, key=lambda x: x["Unit Price"] * x["GST"] * x["Quantity"])
max_gst_product_name = max_gst_product["Product"]
print(max_gst_product)
print(max_gst_product_name )

total_amount = sum([(item["Unit Price"] * item["Quantity"] * (1 + item["GST"] / 100)) * (0.95 if item["Unit Price"] >= 500 else 1) for item in basket])
print(total_amount+200) 