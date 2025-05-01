a = int(input("Enter a Between 1 to 10 number"));
match a :
    case 1:
        print("You won a charger");
    case 3:
        print("You won $3");
    case 6:
        print("you won camera");
    case _:
        print("Better luck next time");

# a is matched and compared with all these cases