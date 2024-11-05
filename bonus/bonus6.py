contents = ["contenido1", "contenido2", "contenido3"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)

a =("I am a string "
    "on my own")