gang_members = []
def add_member (name, age, gang):
    member_history = {
        "name" : name ,
        "age" : age ,
        "gang" : gang
    }
    gang_members.append(member_history)

# name = input("Enter your name")
# age = int(input("Enter your age"))
# gang = input("Enter your gang")

while True :
    press = input("1 for add member | 2 for show member | [Any key] Quit: ")
    if press == "1" :
        name = input("Enter your name : ")
        age = int(input("Enter your age : "))
        gang = input("Enter your gang : ")
        add_member (name, age, gang)

    elif press == "2" :
        print(gang_members)
        
    else :
        print ("Quitting . . .")
        break
    


