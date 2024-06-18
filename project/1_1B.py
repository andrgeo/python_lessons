
fio = input("Введите имя и фамилию:")
fio1,fio2 = fio.title().split()

nickname = fio2[0:4] + fio1[0]

print(fio2, fio1, ":", nickname)