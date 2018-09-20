my_variable = "hello"

grades = [77, 80, 90]
tuple_grades = (77, 80, 90) # imutable
set_grades = {77, 80, 90} # unique & unordered

#grades.append(100)
#print(grades)

# tuple_grades = tuple_grades + (100,)
# print(tuple_grades)

# grades[0] = 60
# print(grades)

# tuple_grades[0] = 60
# print(tuple_grades)

# set_grades[0] = 60
# set_grades.add(60)
# set_grades.add(60)
# print(set_grades)


#################################


your_lottery_numbers = {1,2,3,4,5}
winning_number = {1,3,5,7,8,11}
print(your_lottery_numbers)
print(winning_number)

print(your_lottery_numbers.intersection(winning_number))
print(winning_number.intersection(your_lottery_numbers))

print(winning_number.difference(your_lottery_numbers))

winning_number.intersection_update(your_lottery_numbers)
your_lottery_numbers.intersection_update(winning_number)

print(winning_number)
print(your_lottery_numbers)