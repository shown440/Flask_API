######### Dictionary vs Class_and_Object ###############
lotterty_player = {
    "name" : "Shown",
    "numbers" : (10, 20, 30, 40, 50)
}
#print(lotterty_player.total())

##################################
class LottertyPlayer:
    def __init__(self):
        self.name = "Shifullah"
        self.numbers = (100, 210, 30, 40, 50)

    def total(self):
        return sum(self.numbers)

# player_1 = LottertyPlayer()
# player_2 = LottertyPlayer()
# print(player_1.name)
# print(player_1.total())
# print(player_1 == player_2) ### False cz both are difference instance but same attributes

##############################################
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks)/len(self.marks)
shifullah = Student("Shifullah", "Satkhira Govt. School")
#shifullah.name = "Shifullah"
#shifullah.school = "Satkhira Govt. School"
shifullah.marks.append(80)
shifullah.marks.append(70)
print(shifullah.avg())
print(shifullah.name)
