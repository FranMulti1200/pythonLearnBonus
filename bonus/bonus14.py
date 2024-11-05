from bonus.comvertes14 import convert
from bonus.parses14 import parse

feet_inches = input("Enter feet and inches: ")

#print(convert(feet_inches))
parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too smll.")
else:
    print("Kid can use the slide.")