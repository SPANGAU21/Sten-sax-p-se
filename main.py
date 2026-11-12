import random

print("Nu ska vi spela Sten, Sax eller Påse!")
print("Jag är Spel Mästaren")
username=input("Vad är ditt username?") 

antal_omgångar=int(input("ange antal omgångar vi ska spela ?"))
for i in range (antal_omgångar):
    print("Spelomgång",i+1)
    print("-"*10)
    val = input("Välj Sten, Sax eller Påse:")
    mästaren_val = random.choice(["sten", "sax", "påse"])
    print("mästaren spelar:", mästaren_val)
    print(username, "spelar:", val)
    if mästaren_val == val:
        print("Oavgjort!")
    elif mästaren_val == "sten" and val == "sax":
        print("Mästaren vinner!")

    
