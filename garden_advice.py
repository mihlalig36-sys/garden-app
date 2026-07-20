# Gardening Advice App

"""
Gardening Advice App
====================

A simple interactive program that provides gardening tips based on season and plant type.

Features:
- User input for season and plant type
- Modular functions for better readability
- Support for flowers, vegetables, and herbs
"""

def get_season_advice(season):
    """Return advice based on the season."""
    if season.lower() == "summer":
        return "Water your plants regularly and provide some shade."
    elif season.lower() == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No specific advice for this season."


def get_plant_advice(plant_type):
    """Return advice based on the plant type."""
    if plant_type.lower() == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type.lower() == "vegetable":
        return "Keep an eye out for pests!"
    elif plant_type.lower() == "herb":
        return "Plant in well-drained soil and harvest regularly for best flavor."
    else:
        return "No specific advice for this type of plant."


def main():
    """Main function to run the gardening advice app."""
    print("Welcome to the Gardening Advice App! \n")
    
    # Get user input
    season = input("Enter the current season (summer/winter): ").strip().lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").strip().lower()

    # Input validation
    if season not in ["summer", "winter"]:
        season = "other"
    if plant_type not in ["flower", "vegetable", "herb"]:
        plant_type = "other"
    
    # Get advice
    season_advice = get_season_advice(season)
    plant_advice = get_plant_advice(plant_type)
    
    # Display advice
    print("\n" + "="*40)
    print("GARDENING ADVICE")
    print("="*40)
    print(f"Season: {season.capitalize()}")
    print(f"Plant Type: {plant_type.capitalize()}")
    print(f"Advice: {season_advice} {plant_advice}")
    print("="*40)


if __name__ == "__main__":
    main()