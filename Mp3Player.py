#Written by 《ERFAN》
#t.me/ErfanMAfshar
import os

def main() :
    os.system('clear')
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("<                         >")
    print("<       Mp3 Player        >")
    print("<                         >")
    print("<   {00} Play Mp3         >")
    print("<   {99} Exit             >")
    print("<                         >")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    i = input("~~> ")

    from playsound import playsound
    def pyRed (skk) : print("\033[91m {}\033[00m".format(skk))
    def pyGreen(skk): print("\033[92m {}\033[00m".format(skk))
    if i == "00" :
        pyRed(" Note : Press Space After Paste URL")
        url = input("Enter URL of Music: ")
        pyGreen("Please Wait...")
        playsound(url)
        print("Done")
        qq = input("\nPress Enter...")
        if qq == "" :
            main()
    elif i == "99":
        print("...GoodBye...")
        exit()
    else :
        print("Please select the correct option!")
        s = input("\nPress Enter...")
        if s == "" :
            main()
main()
