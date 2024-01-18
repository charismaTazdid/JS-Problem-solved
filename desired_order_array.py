import operator

arr3 = [
    {"name": "International", "id": 30},
    {"name": "National", "id": 34},
    {"name": "Sports", "id": 3},
    {"name": "Entertainment", "id": 55},
    {"name": "Politics", "id": 38},
    {"name": "Education", "id": 67},
    {"name": "Technology", "id": 10},
]

desired_order = [67, 3, 55, 30, 34, 10, 38]

# Sort the array using a custom key function
arr3.sort(key=operator.itemgetter('id'))

# Rearrange the elements based on the desired order list
arr3 = sorted(arr3, key=lambda x: desired_order.index(x['id']))

print(arr3)
