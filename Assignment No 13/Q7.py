d = {"name": "Sayali", "age": 21, "city": "Pune"}

key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Updated Dictionary:", d)
else:
    print("Key not found")