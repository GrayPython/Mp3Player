#Written by 《ERFAN》
#t.me/ErfanMAfshar
import os
os.system('pip install playsound')
import playsound
def main() :
    os.system('clear')
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("<                         >")
    print("<       Mp3 main        >")
    print("<                         >")
    print("<   {00} Play Mp3         >")
    print("<   {99} Exit             >")
    print("<                         >")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    i = input("~~> ")
    def pyRed (skk) : print("\033[91m {}\033[00m".format(skk))
    def pyGreen(skk): print("\033[92m {}\033[00m".format(skk))
    if i == "00" :
        pyRed(" Note : Press Space After Paste URL")
        url = input("Enter URL of Music: ")
        pyGreen("Please Wait...")
        playsound.playsound(url)
        print("Done")
    elif i == "99":
        print("...GoodBye...")
        exit()
    else :
        print("Please select the correct option!")
        s = input("\nPress Enter...")
        if s == "" :
            main()
if __name__ == '__main__' :
    main()
