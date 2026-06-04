"""A simple gardening advice program with improvement tasks."""


month = input("Enter the current month: ").strip().lower()
season = input("Enter the current season: ").strip().lower()

# TODO: Refactor the repeated seasonal conditions into a reusable function.
if season == "summer":
    print("Water plants early in the morning to reduce evaporation.")
elif season == "autumn":
    print("Collect fallen leaves and add them to compost.")
elif season == "winter":
    print("Protect sensitive plants from frost.")
elif season == "spring":
    print("Prepare beds and begin planting new seedlings.")
else:
    print("Please enter a valid season.")

# TODO: Create a reusable function for monthly planting advice.
if month == "january":
    print("Plant heat-tolerant crops such as beans and tomatoes.")
elif month == "june":
    print("Plant winter crops such as spinach and peas.")
else:
    print("Check your local climate before planting this month.")