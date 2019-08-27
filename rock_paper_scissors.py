"""
A Game of Rock papar scissors
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
"""
def rps(event1,event2):
    """
    if event1 won trues FIRST, TIE, SECOND
    event 1 is R P S
    """
    #print(event1, event2)
    if event1 == event2:
        print("Its a tie.")
    else:
        if (event1=='R' and event2 == 'S') or (event1=='P' and event2 == 'R') or (event1=='S' and event2 == 'P'):
            print("The First person won.")
        else:
            print("The second person won.")
        


while True: 
    usr_command = input("Enter RPS of First: R P or S: ")
    second_command = input("Enter RPS of Second: R P or S: ")
    if usr_command == "quit":
        break
    else: 
        print("OK " + usr_command + " versus " + second_command)
        if (usr_command == "R") or (usr_command =='P') or (usr_command =='S'):
            print("First entry is good" )
        else:
            print("You didn't type R, P, or S")
            break
        
        if (second_command == "R") or (second_command =='P') or (second_command =='S'):
            print("Second entry is good" )
        else:
            print("You didn't type R, P, or S")
            break

        rps(usr_command,second_command)
