#BATTLE SYSTEM#Python Based RPG Battle System, created by Chinmay Tiwari
import random
import time
playerhp = 10 
Attack1 = "COOL"
Attack2 = "DAMAGE"
Attack3 = "bOOM"
dam1 = 2
dam2 = 8
dam3 = 6
dam = 0
attack = 0
xp = 0
totxp = 0

def battle(HP,level,Monnam,playerhp,xp):
    #Start
    print("A WILD ", Monnam, " APPERED!")
    #GAME LOOP
    
    dam = 5
    re = 0
    loopran = 0
    

    gamerun = 'true'
    while gamerun == 'true':
        print("ATTACKS AVALIBLE. PRESS NUMBER OF ATTACK:")
        print("1.", Attack1,dam1)
        print("2.", Attack2,dam2)
        print("3.", Attack3,dam3)
        print("Cannot use:", re, "Because not charged")
        attack = int(input("?"))
        
        if attack == 1 and re != "1":
            dam = dam1
            re = "1"
        elif attack != 1 and re == "1":
            print("Attack is not READY!, SHOT AUTOMATICLY MISSED!")
            dam = 0
        if attack == 2 and re != "2":
            dam = dam2
            re = "2"
            print("FORDEBUG1: ", dam)
        elif attack != 2 and re == "2":
            print("Attack is not READY!, SHOT AUTOMATICLY MISSED!")
            dam = 0
        if attack == 3 and re != "3":
            dam = dam3
            re = "3"
        elif attack != 3 and re == "3":
            print("Attack is not READY!, SHOT AUTOMATICLY MISSED!")
            dam = 0
        
        
        
       #print("FORDEBUG2: ", dam)
        
        

        rand = random.randint(-3, 1)
        if rand != 1 and dam != 0:
            HP = (HP-(dam-rand))+(1.3*level)
            print(Monnam," Has ",HP)  
        else:
            print("MISS!")
            
       
        kill = random.randint(-3, 1)
        if kill != 1:
            playerhp = playerhp+kill
            print("BAM! YOU WERE HIT!!!!")
            print("YOU HAVE:" ,playerhp)  
        else:
            print(Monnam," MISSED!")
        if HP<1:
            print(Monnam, " DIED")
            print("You Win!")
            totxp = (random.randint(100, 500))-loopran
            while xp != totxp:
                print("TOTAL XP:", xp,end='\r')
                xp = xp+1
                time.sleep(0.02)
            
            gamerun = "FALSE"
        if playerhp<1:
            print("   YOU DIED!")
            print("   [Respawn]")
            print("  [Main Menu]")
            gamerun = 'FALSE'
        loopran = loopran+1




