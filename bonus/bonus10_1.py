try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    if total_value == 0:
        exit("Your total value cannot be zero.")

    print(f"That is {(value / total_value) * 100}%")
except ValueError:
    print("You need to enter a number. Run the program again.")