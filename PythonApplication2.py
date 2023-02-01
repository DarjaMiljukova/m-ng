#Игра "Камень Ножницы Бумага"

import random



while True:
    user_action = input("Tee oma valik – kivi, käärid või paber: ")
    possible_actions = ["kivi", "käärid", "paber"]
    computer_action = random.choice(possible_actions)
    print(f"\nSa tegid oma valiku {user_action}, teine mängija on oma valiku teinud {computer_action}.\n")
    if user_action == computer_action:
        print(f"Mõlemad mängijad valisid {user_action}. viik!")
    elif user_action == "kivi":
        if computer_action == "käärid":
            print("kivi lööb käärid. Sa võitsid")
        else:
            print("paber mähib kivi. Sa kaotasid")
    elif user_action == "paber":
        if computer_action == "kivi":
            print("paber mähib kivi. Sa võitsid")
        else:
            print("käärid lõigatud paber. Sa kaotasid")
    elif user_action == "käärid":
        if computer_action == "paber":
            print("käärid lõigatud paber. Sa võitsid")
        else:
            print("kivi lööb käärid. Sa kaotasid")
    play_again = "" 
    play_again = input("Kas soovite rohkem mängida? (jah/ei): ") 
    if play_again.lower() != "jah": 
        break 
