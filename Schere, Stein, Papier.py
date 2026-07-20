import random

print("Willkommen zum Schere, Stein, Papier Spiel gegen den Computer!")

while True:


    auswahlMenue = inputInt("Was möchtest du machen? \n 1 = Spielen \n 2 = Beenden ")

    if auswahlMenue == 1:
        auswahl = ["schere", "stein", "papier"]
        runde = 0
        spielerPunkte = 0
        computerPunkte = 0
        print("Spiel startet!")


        while spielerPunkte < 3 and computerPunkte < 3:
        
            runde += 1
            print("Runde", runde)
        
            spieler = input("Was wählst du? Schere, Stein oder Papier?: ").lower()
        
            while spieler != "schere" and spieler != "stein" and spieler != "papier":
                spieler = input("Bitte wähle Schere, Stein oder Papier: ").lower()
        
            computer = random.choice(auswahl)
        
            print("Du hast", spieler.capitalize(), "gewählt")
            print("Der Computer hat", computer.capitalize(), "gewählt")   
            
            if spieler == computer:
                print("Unentschieden!")
            
            elif (spieler == "schere" and computer == "papier") or \
                 (spieler == "stein" and computer == "schere") or \
                 (spieler == "papier" and computer == "stein"):
                print("Du hast gewonnen! 🎉")
                spielerPunkte += 1
            
            else:
                print("Der Computer gewinnt!")
                computerPunkte += 1
        
            print("Punktestand:")
            print("Du:", spielerPunkte)
            print("Computer:", computerPunkte)
            print("----------------")
        
        print("Spiel beendet!")
        print("Deine Punkte:", spielerPunkte)
        print("Computer Punkte:", computerPunkte)
        
        if spielerPunkte > computerPunkte:
            print("Du hast das Spiel gewonnen! 🏆")
            
        elif computerPunkte > spielerPunkte:
            print("Der Computer hat gewonnen! 🤖")
            
        else:
            print("Unentschieden!")
    
    elif auswahlMenue == 2:
        print("Danke fürs Spielen! 👋")
        break
    
    else:
        print("Ungültige Auswahl!")
    