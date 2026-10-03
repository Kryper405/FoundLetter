found = 0
word = input("Введите слово: ")
letter = input("Введите букву которую хотите найти:")
for i in word:
    if i == letter:
        found += 1


print("Найдено букв:", found)

