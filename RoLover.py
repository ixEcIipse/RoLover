import os

try:
    from admcheck.main import *
    from colorama import *
    import time
except:
    input("failed to import modules, press enter to install or ctrl + c to exit. ")
    os.system("pip install admcheck && pip install colorama")
    print("finished installing please restart terminal.")

os.system("cls")
close()

if is_Admin():
    pass
else:
    print(Fore.YELLOW + "[error 2] invalid permissions, please restart as administrator" + Fore.WHITE)
    exit()


def menu():
    print(Fore.LIGHTMAGENTA_EX + """
   __         __    ,d8b.d8b,    
  /__\ ___   / /  __888888888_ 
 / \/// _ \ / /  / _`Y88888Y' _|
/ _  \ (_) / /__| (_)`Y888Y'  __|
\/ \_/\___/\____/\___/ `Y' \___|
the tool for your deepest desires <3

[1] list nsfw roblox games
[2] open auto uploader
[3] open auto uploader v2
[4] check software version
[5] info
[6] exit

    """)
opt = input("enter option> ")
if opt == "1":
    print("""
    1. https://www.roblox.com/games/11765041959/This-project-has-been-retired
    2. https://www.roblox.com/games/205455582/Wonderland
    3. https://www.roblox.com/games/11872742462/dwasdw

    """)
    input("press enter to go back to menu")
    os.system("cls")
    menu()

elif opt == "2":
    os.system("start https://condogames.xyz/games/latest")
    os.system("cls")
    menu()

elif opt == "3":
    os.system("start https://susroblox.carrd.co/")
    os.system("cls")
    menu()

elif opt == "4":
    print("[ver 1.1.4]")
    input("press enter to go back to main menu")
    menu()

elif opt == "5":
    print("""
    RoLove ver 1.1.4

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.
    """)
    print("")
    input("press enter to return to the main menu.")
    menu()

elif opt == "6":
    print("thanks for using <3")
    os.system("exit")


else:
    print("not an option")
    time.sleep(3)
    menu()

menu()