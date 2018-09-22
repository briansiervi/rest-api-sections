# should_continue = True
# if should_continue:
#     print("Hello")

# known_people = ["Jhon", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def even_numbers():
#     evens = []
#     for number in numbers:
#         if number%2 == 0:
#             evens.append(number)
#     return evens


# teste = even_numbers()
# for a in teste:
#     print(a)

def who_do_you_know():
    persons = input("Enter the names of people you know, separated by commas: ")
    known_people = [person.strip().lower() for person in persons.split(",")]
    return known_people

def ask_user():
    person = input("Enter the person name: ")    

    if person.lower() in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("You don't know {}!".format(person))


ask_user()