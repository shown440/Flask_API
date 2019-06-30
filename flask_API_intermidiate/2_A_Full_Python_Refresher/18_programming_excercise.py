
def who_do_you_know():
    people = input("Enter the names of peoples you know: ")
    people_list = people.split(",")
    return people_list

def ask_user():
    person = input("Enter a name: ")
    if person in who_do_you_know():
        print("You know the {}".format(person))

ask_user()
