def draw_restaurant(floors = 0):
    """Adds restaurant to city

    Args:
    floors -- (integer) number of floors in restaurant (default 0)
    """
    
    # Restaurant name
    print("--------------------------")
    print("|      BU Bistro          |")
    for _ in range(floors):
        print("|                         |")
    # Door of fixed height: 3
    print("|         _______         |")
    for _ in range(3):
        print("|        |       |        |")
    print("--------------------------")

    return
