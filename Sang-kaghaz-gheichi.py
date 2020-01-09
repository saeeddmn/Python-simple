#By Saeed Damghanian
#simple project that has not graphics

import random
while(True):
    select = input('\nKhosh amadid. Entekhab ba shomast: Sang | Kaghaz | Gheichi :' )
    sel=random.randint(0,2)
    csel = "sang"
    if sel == 0:
        csel="sang"
    elif sel== 1:
        csel="kaghaz"
    elif sel== 2:
        csel="Gheichi"
    print(f"Enetekhabe computer: {csel}")

    if select==csel:
        print("Barande nadarim, Mosavi shodid!.........")
    elif select=="sang" and csel=="kaghaz":
        print("Computer Barande shod!.........")
    elif select=="sang" and  csel=="gheichi":
        print("Shoma barande shodid!")
        
    elif select=="kaghaz" and csel=="gheichi":
        print("Computer Barande shod!.........")
    elif select=="kaghaz" and csel=="sang":
        print("Shoma barande shodid!")
    elif select =="gheichi" and csel=="sang":
        print("Computer Barande shod!.........")
    elif select =="gheichi" and csel=="kaghaz":
        print("Shoma barande shodid!")
        
    c=input("Replay: R || Exit: E ")
    if c=='e' or c=='E':
        exit()
    
