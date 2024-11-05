languages = ['English', 'German', 'Spanish']

for item in languages:
    with open(f"{item}.txt", "w") as file:
        file.write(item)