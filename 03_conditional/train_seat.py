from unittest import case


seat_type=input("Enter seat type (e.g., 'economy', 'business', 'first'): ").lower()

match seat_type:
    case 'economy':
        print("You have selected an economy seat.")
    case 'business':
        print("You have selected a business seat.") 
    case 'first':  
        print("You have selected a first-class seat.")
    case _:
        print("Invalid seat type selected. Please choose from economy, business, or first.")