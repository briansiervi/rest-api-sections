lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5,9,12,3,1,21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")

# print(player_one == player_two)
# print(player_one.name)
# print(player_one.total())

# print(player_one.name)
# print(player_two.name)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # @classmethod
    # def go_to_school(cls):
    #     print("I'm going to school.")
    #     print("I'm a {}".format(cls))

    @staticmethod
    def go_to_school():
        print("I'm going to school.")

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")

anna.marks.append(56)
anna.marks.append(71)
# print(anna.average())

# anna.go_to_school()
Student.go_to_school()