feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = feet * 0.3048 + inches *0.0254
    #return f"{feet} feet and {inches} inches is equal to {meters} meters."
    return meters


#print(convert(feet_inches))
parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too smll.")
else:
    print("Kid can use the slide.")