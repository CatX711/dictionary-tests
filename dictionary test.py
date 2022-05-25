class_data = {
    "Sam": "Hey there, welcome to Python! I'm Sam.",
    "Jack": "Hello, I am jack!",
    "Emma": "Hello, I am Emma. I am on a machine learning course.",
    "Wattson": "Hello, I am Wattson."
}
print(class_data["Jack"])
print(class_data["Sam"])
print(class_data["Emma"])
print(class_data["Wattson"])


class_data2 = {
    "coins": int("2982"),
    "swords": int("2")
}
pickupitem = input()
if pickupitem == "pickup":
    print("You have ", class_data2["coins"] + 2, "coins.")
if pickupitem == "pickup2":
    print(" You have ", class_data2["swords"] + 1, "swords")

