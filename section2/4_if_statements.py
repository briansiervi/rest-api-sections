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
    known_people = []
    persons = input("Enter the names of people you know, separated by commas: ")
    person_list = persons.split(",")

    for person in person_list:
        known_people.append(person.strip().lower())

    return known_people


def who_do_you_know2():
    anyone = "y"
    known_people = []

    while anyone == "y":
        person = input("Enter the person you know: ")
        anyone = input("Do you know anyone else? (y/n) ")

        known_people.append(person.lower())

    return known_people


def ask_user(commas):
    person = input("Enter the person name: ")
    you_know = False

    if commas == True:
        if person.lower() in who_do_you_know():
            you_know = True        
    else:
        if person.lower() in who_do_you_know2():
            you_know = True
    
    if you_know:
        print("You know {}!".format(person))
    else:
        print("You don't know {}!".format(person))


ask_user(True)
# ask_user(False)