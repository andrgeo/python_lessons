
import random

numbers = []

for i in range(100):
    n = random.randint(1, 100)
    numbers.append(n)

print(numbers)

num_line = 33

new_dict = []

for number in range(100):
    if numbers[number] > num_line:
        new_dict.append("Hight")
    else:
        new_dict.append("Low")

print(new_dict)


#2
import names

names_list = []
for i in range(100):
    name = names.get_first_name()
    names_list.append(name)

a_m_names = []
other_names = []

for i in names_list:
    if i[0] == "A" or i[0] == "M":
        a_m_names.append(i)
    else:
        other_names.append(i)

print(names_list)
print(a_m_names)
print(other_names)

#3

words = []

while True:
    word = input("Введите слово: ")
    if len(word) == 0:
        break
    else:
        words.append(word)

first_letters = []
for letters in words:
    first_letter = letters[0]
    first_letters.append(first_letter)

final_word = ''.join(first_letters)
print('Получилось слово: ', final_word)