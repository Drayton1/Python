direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
        
    case "west":
        print("Left")
        
    case "south":
        print("Down")
        
    case "east":
        print("Right")
    case _:
        print("Not a valid direction.")
