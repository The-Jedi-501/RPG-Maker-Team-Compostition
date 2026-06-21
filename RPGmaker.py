'''

=============================================================
RPG Maker - Destiny 2 (video game style) - Fireteam Compostion Checker
=============================================================

AUTHOR: Christopher DeMoura
Language: Python
Purpose: To create a project of which encompasses all of my knowledge so far of Python into a project to further my understanding of those various functions within the code itslef

Code walkthrough and Goals: 
-Main idea is to essenlly create a fireteam (essentallu varibles in a list acting as players all unique) of which we would select how many by picking either 3 or 6 adn to tell essnely view and give you a breakdown of if the team compostion of all the players  was good or not

-Please note there is alot of comments most are just notes I made along the way as you will see to either explain how a new piece of code worked or to show a new implemtentaion i had found that i found interesting and wanted to implement

Code topics used here and the purpose they served:
-Polymophism --- 
-Inheritance --- all about having the parent ex(titan,bubble) and getting its own unique aspect in the form of another object (ex tank)
-Header Files (Dont exist here but instead its called "Modules") --- meant to add but complelty forgot but definetly somethign that will be on next github project repo 
-Dict --- Hash map 
-Classes --- Used to essenlly store adn have all my info into one piece 
-Lists --- Think Vector (C++) or Arrays (C) just a way to store objects
-Functions --- used to keep code all nice and clean 
-Basic Code functions (Loops, condiotional, variables, etc.) --- Its used literally  everywhere 

Breakdown to how I organize this code:
- ALWAYS 3 ENTERS between a set of functions to be cleaner for myslef
- USE 2 when parts are still one coheisve unit but just to clean up and 1 for keeping ideas and implentation of next step  
- Attempt to keep varible names relevant to code and actions they will be doing 
-
'''
import random #need this to randomize think of imports as a C or C++ #include <...>

class RPG:
    def __init__(self, owner, Super):#owner=titan, Super = Void Super
        self.owner = owner
        self.Super = Super
        self.role = "Unknown"  # default, child classes override this

    
    def display(self):
        print(f"Class: {self.owner} | Super: {self.Super} | Role: {self.role}")
        
        

def View_Team(rpg):
    if isinstance(rpg, list): # doing an if check for if i am lookign at jsut myself vs lookign at teh whole team 
        for i, build in enumerate(rpg): #we use the f to say hey bout to use varibales get ready, {} is used to drop varibles inside strign 
            print(f"{i+1})", end=" ")
            build.display()
    else:
        rpg.display()



def pick_class(): 
    print("1) Titan")
    print("2) Hunter")
    print("3) Warlock")
    
    UserClassChoice = safety_net(1, 3)
        
    ClassDict = { #Dicts just a hash map goal here yo take input and then after this
        1 : "Titan",
        2 : "Hunter",
        3 : "Warlock"
    }
    print('\n')
    return ClassDict[UserClassChoice]  # sends the value back to whoever called it


    
def pick_super(chosen_class):
    print("Now I need you to select a super this is like what role you will fill for the sake of htis practice code:")
    if chosen_class == "Titan":
        options = {1: "Thundercrash", 2: "Bubble", 3: "Hammer"}
    elif chosen_class == "Hunter":
        options = {1: "Tether", 2: "Nighthawk", 3: "Blade Barrage"}
    elif chosen_class == "Warlock":
        options = {1: "Well", 2: "Nova Bomb", 3: "NeedleStorm"}

    for key, value in options.items():
        print(f"{key}) {value}")

    choice = safety_net(1, 3)
    return options[choice]

    

class Titan(RPG): #This is the INHERITACNE which is all about having the parent ex(titan,bubble) adn getting its own unique aspect in the form of another object (ex tank) 
    def __init__(self, Super):#setup -- getting the child ready 
        super().__init__("Titan", Super)# sends "Titan" and the super up to RPG
        self.role = "Tank"              # Titan's own unique thing - this is inheritnaly what they are identified as I have this idea that there indpenadant role increases there comp checker in a way
        
        
    def analyze(self):                    # behavior -- print out this stuff later 
        if self.Super == "Thundercrash":
            print("Titan — DPS burst")
        elif self.Super == "Bubble":
            print("Titan — team support")
        elif self.Super == "Hammer":
            print("Titan — sustained DPS")


class Hunter(RPG):
    def __init__(self, Super):
        super().__init__("Hunter", Super)
        self.role = "DPS"
        
    def analyze(self):                    # behavior -- print out this stuff later 
        if self.Super == "Blade Barrage":
            print("Hunter — DPS burst")
        elif self.Super == "Tether":
            print("Hunter — team support")
        elif self.Super == "Nighthawk":
            print("Hunter — sustained DPS")


class Warlock(RPG):
    def __init__(self, Super):
        super().__init__("Warlock", Super)
        self.role = "Support"
        
    def analyze(self):                    # behavior -- print out this stuff later 
        if self.Super == "Nova Bomb":
            print("Warlock — DPS burst")
        elif self.Super == "Well":
            print("Warlock — team support")
        elif self.Super == "NeedleStorm":
            print("Warlock — sustained DPS")    



def check_comp(fireteam): # Purpose is to essentailly check if the Team we have is good or not adn doing in a seperate function just to keep clean 
    dps = 0
    support = 0
    
    for guardian in fireteam:
        if guardian.Super in ["Thundercrash", "Nighthawk", "Nova Bomb", "Blade Barrage", "Hammer", "NeedleStorm"]:
            dps += 1
        elif guardian.Super in ["Well", "Bubble", "Tether"]:
            support += 1
    
    if dps == 0:
        print("⚠ No DPS — you're gonna struggle on boss") #Leant you can use special characters like the Hazard anch checkbox by essentlly finding/google and copying them in 
    if support == 0:
        print("⚠ No support — team will die")
    if dps >= 2 and support >= 1:
        print("✓ Good comp")
        
        

def build_random_guardian(): #RANDOMIZER LOGIC 
    classes = ["Titan", "Hunter", "Warlock"] #LIST
    supers = {#DICT
        "Titan": ["Thundercrash", "Bubble", "Hammer"],
        "Hunter": ["Tether", "Nighthawk", "Blade Barrage"],
        "Warlock": ["Well", "Nova Bomb", "NeedleStorm"]
    }
    rand_class = random.choice(classes)
    rand_super = random.choice(supers[rand_class])
    
    if rand_class == "Titan":
        return Titan(rand_super)
    elif rand_class == "Hunter":
        return Hunter(rand_super)
    elif rand_class == "Warlock":
        return Warlock(rand_super)
    
    
def safety_net(min_val, max_val): #Since ther is alot of saftey checks might as well get more practice in code here 
    choice = int(input("> "))
    while choice < min_val or choice > max_val:
        print(f"Must be between {min_val} and {max_val}")
        choice = int(input("> "))
    return choice
    
    

def gaurdian_builder(): #turned this into a function call becasue i had used twice and made the main code look ugly 
    print("Build your character:")
    chosen_class = pick_class()  # gets "Titan", "Hunter", or "Warlock" back
    chosen_super = pick_super(chosen_class)  # pass chosen_class in #pick said sub class this is the end of classes specifically for parents
    
    if chosen_class == "Titan":
        return  Titan(chosen_super)   # child class is now down and my character is put unto my_build
    elif chosen_class == "Hunter":
        return  Hunter(chosen_super)
    elif chosen_class == "Warlock":
        return  Warlock(chosen_super)


                          
def main():
    #Main idea rn is to go from how many players -> i make my guy -> then determine how we want the other players -> then we move unto showing the team compostion
    print("Select activity (1 or 2):")
    print("1) Dungeon (3 players)")
    print("2) Raid (6 players)")
    
    activity = safety_net(1, 2)   
    
    activities = {1: "Dungeon", 2: "Raid"}
    activity_name = activities[activity]
    team_size = 3 if activity == 1 else 6 #this is logic for when we randomize it help 
    
    print() #Leant i dont need to do a ('\n') just () very nice 
    
    my_build = gaurdian_builder() 
     
    fireteam = []               # stores everyone
    fireteam.append(my_build)   # add yourself to the list
    
    print()
    print("Would you like for the other players to be randomzied or woudld you like to select that:")
    #WAY 1 HASH OR PRINT EACH 2 PRINTS ONE FRO RAND OR PICKIN IF RAND WOUDL DO 
    options = {#COMPLETLY OVERKILL BUT WANTED TO PRACTICE JUST USINGIT 
    1: "Randomize",
    2: "Pick manually"
}

    for key, value in options.items():
        print(f"{key}) {value}")

    team_pick = safety_net(1, 2) 
    team_result = options[team_pick]
    
    if team_result == "Randomize":  
        for _ in range(team_size - 1):  # fill the rest randomly
            fireteam.append(build_random_guardian())
    
    else: 
        for i in range(team_size - 1):
            my_build = gaurdian_builder()
            fireteam.append(my_build)  # add yourself to the list


    print(f"\n--- {activity_name} Team ---")
    View_Team(fireteam)


    print("\n--- Analysis ---")
    for guardian in fireteam:
        guardian.analyze()  # this is the poly call --- were looking at the fireteam from above spcially the analyze fcuntion so (fireteam say first was a titan, and i chose bubble then analyze will print out support or whatever i wrote above in inheritacne)
                            # POLYMORPHISM — same .analyze() call, each guardian runs its own version
    
    check_comp(fireteam) #this it the logical print check stuff to see if were all nice compostion of people 
   
if __name__ == "__main__": #DONT FORGET IT 
    main()
    
    
    
'''
Next Project Repo want to get into 
Modules — split across files like headers
Excel export — openpyxl at the end --- never did but had done some light research into it and how to incorporate it 


ex output at end
Dungeon Team

1) Titan - Thundercrash
2) Hunter - Tether
3) Warlock - Well

Analysis: mayvbe these are if ie if hunter tether print debuff is applied very nice 
✓ DPS covered
✓ Debuff covered
✓ Healing covered

Team Rating: 9/10
-went thru alot of differnt ways to go about this and implementation im happy with what I have as of making code

'''
