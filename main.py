import random

print("Nu ska vi spela Sten, Sax eller Påse!")
print("Jag är Spel Mästaren")
username=input("Vad är ditt username?") 
mästarens_poäng=0
spelarens_poäng=0
antal_omgångar=int(input("ange antal omgångar vi ska spela ?"))
for i in range (antal_omgångar):
    print("Spelomgång",i+1)
    print("-"*10)
    while True:
        val = input("Välj Sten, Sax eller Påse: ").lower()
        if val in ["sten", "sax", "påse"]:
            break
    
    mästaren_val = random.choice(["sten", "sax", "påse"])
    print("mästaren spelar:", mästaren_val)
    print(username, "spelar:", val)
    if mästaren_val == val:
        print("Oavgjort!")
    elif mästaren_val == "sten" and val == "sax":
        print("Mästaren vinner!")
        mästarens_poäng += 1
    elif mästaren_val == "sten" and val == "påse":
        print(username," vinner!")
        spelarens_poäng += 1
    
    elif mästaren_val == "sax" and val == "påse":
        print("Mästaren vinner!")
        mästarens_poäng += 1
    elif mästaren_val == "sax" and val == "sten":
        print(username," vinner!")
        spelarens_poäng += 1
    
    elif mästaren_val == "påse" and val == "sten":
        print("Mästaren vinner!")
        mästarens_poäng += 1
    elif mästaren_val == "påse" and val == "sax":
        print(username," vinner!")
        spelarens_poäng += 1
    
print("SLUTRESULTAT")
print("-"*10)
print("-"*10)
print("Spel mästarens:", mästarens_poäng)
print(username,"poäng:", spelarens_poäng)

    
