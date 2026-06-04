"""Provide simple gardening advice based on season and month."""


SEASON_ADVICE = {
    "summer": "Water plants early in the morning to reduce evaporation.",
    "autumn": "Collect fallen leaves and add them to compost.",
    "winter": "Protect sensitive plants from frost.",
    "spring": "Prepare beds and begin planting new seedlings.",
}

MONTH_ADVICE = {
    "january": "Plant heat-tolerant crops such as beans and tomatoes.",
    "february": "Maintain watering schedules during hot weather.",
    "march": "Prepare compost and begin planning autumn planting.",
    "april": "Plant leafy vegetables suited to cooler weather.",
    "may": "Protect young plants as temperatures begin to fall.",
    "june": "Plant winter crops such as spinach and peas.",
    "july": "Monitor plants for frost damage.",
    "august": "Prepare seed trays for spring planting.",
    "september": "Plant new seedlings as the weather warms.",
    "october": "Add mulch to keep soil moist.",
    "november": "Check plants regularly for pests.",
    "december": "Water plants consistently during summer heat.",
}


def get_season_advice(season):
    """Return gardening advice for the selected season."""
    return SEASON_ADVICE.get(
        season,
        "Please enter a valid season: summer, autumn, winter or spring.",
    )


def get_month_advice(month):
    """Return gardening advice for the selected month."""
    return MONTH_ADVICE.get(
        month,
        "Please enter a valid month, for example january or june.",
    )


def main():
    """Collect user input and display suitable gardening advice."""
    month = input("Enter the current month: ").strip().lower()
    season = input("Enter the current season: ").strip().lower()

    print("\nGardening advice:")
    print(get_season_advice(season))
    print(get_month_advice(month))


if __name__ == "__main__":
    main()