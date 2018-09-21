my_variable = "hello"

# print(my_variable[0])

for a in my_variable:
    print(a)


my_list = [1,3,5,7,9]

for number in my_list:
    print(number ** 2)

user_wants_number = True
while user_wants_number:
    print(10)
      
    user_input = input("Sould we print again? (y/n): ")
    if user_input =='n':
        user_wants_number = False