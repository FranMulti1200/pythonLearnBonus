date = input("Enter today's date: ")
mood = input("How do rate your mood today from 1 to 10? ")
thoughts = input("Let your thought flow:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)