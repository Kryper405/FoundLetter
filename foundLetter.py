found = 0
word = input("Write a word: ")
letter = input("write letter:")
for i in word:
    if i == letter:
        found += 1


print("Found letters:", found)

