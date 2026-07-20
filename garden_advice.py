# Gardening Advice App

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
    else:
        return "No specific advice for this type of plant."


def main():
    """Main function to run the gardening advice app."""
    print("🌱 Welcome to the Gardening Advice App! 🌱\n")
    
    # Get user input
    season = input("Enter the current season (summer/winter): ").strip()
    plant_type = input("Enter the plant type (flower/vegetable): ").strip()
    
    # Get advice
    season_advice = get_season_advice(season)
    plant_advice = get_plant_advice(plant_type)
    
    # Display advice
    print("\n" + "="*40)
    print("🌿 GARDENING ADVICE")
    print("="*40)
    print(f"Season: {season.capitalize()}")
    print(f"Plant Type: {plant_type.capitalize()}")
    print(f"Advice: {season_advice} {plant_advice}")
    print("="*40)


if __name__ == "__main__":
    main()