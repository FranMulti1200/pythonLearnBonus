from modules import functions

while True:
    list_balance = str(functions.get_balance())
    str_cu_balance = str(list_balance.split('$')[1])
    float_cu_balance = float(str_cu_balance)

    print("Welcome to the ATM!\n")
    print("Current Balance: $"+str_cu_balance+"\n")
    print("1. Check Balance\n")
    print("2. Deposit Money\n")
    print("3. Withdraw Money\n")
    print("4. Exit\n")

    option = input("Choose an option: ")
    match option:
        case "1":
            balance = functions.get_balance()
            print(f"Your current balance is: {balance} \n")
        case "2":
            #actual_balance = int(functions.get_balance())
            deposit = float(input("Enter amount to deposit: "))
            increase_balance =  float_cu_balance + deposit
            functions.write_balance("$"+str(increase_balance))
            newBalance = functions.get_balance()
            print("Deposit succesful! Your new balance is: "+newBalance+"\n")
        case "3":
            withdraw = float(input("Enter amount to withdraw: "))
            decrease_balance = float_cu_balance - withdraw
            functions.write_balance("$" + str(decrease_balance))
            newBalance = functions.get_balance()
            print("Witdrawal succesful! Your new balance is: " + newBalance + "\n")
        case "4":
            break
        case _:
            print("Wrong option, please choose one option between 1 and 4")







