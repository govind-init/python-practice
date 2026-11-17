sum = 0

while(True):
    userInput = input("Enter the price: ")

    if (userInput != "q"):
        sum = sum + int(userInput)
        print(f"order total so far: {sum}")

    else:
        print(f"your bill total is: {sum}.\nthanks for shpping with us")
        break
