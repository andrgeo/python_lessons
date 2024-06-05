numbers = int(input("введите 6 цифр 0-9"))
for number in range(numbers):
    ticket_num = []
    ticket_num.append(number)

first_trio = sum(ticket_num[0:3])
second_trio = sum(ticket_num[4:-1])

if first_trio == second_trio:
    print("Congratulations! it's happy Ticket")
else:
    print("Sorry! it's unhappy Ticket")