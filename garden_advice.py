"""A simple gardening advice program with improvement tasks."""


def get_season_advice(season):
    """Return gardening advice based on the selected season."""
    if season == "summer":
        return "Water plants early in the morning to reduce evaporation."
    if season == "autumn":
        return "Collect fallen leaves and add them to compost."
    if season == "winter":
        return "Protect sensitive plants from frost."
    if season == "spring":
        return "Prepare beds and begin planting new seedlings."
    return "Please enter a valid season."


month = input("Enter the current month: ").strip().lower()
season = input("Enter the current season: ").strip().lower()

print(get_season_advice(season))

# TODO: Create a reusable function for monthly planting advice.
if month == "january":
    print("Plant heat-tolerant crops such as beans and tomatoes.")
elif month == "june":
    print("Plant winter crops such as spinach and peas.")
else:
    print("Check your local climate before planting this month.")