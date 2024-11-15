message = "Hello"

def get_frequency(text, word):
    words = text.split(" ")
    count = text.count(word)
    frequency = count / len(words) * 100
    return frequency

frecuency = get_frequency("I love sun", "love")
if frecuency > 5:
    print("High frecuency")
else:
    print ("Low frecuency")

print(message)