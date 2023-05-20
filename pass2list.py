from itertools import permutations
import sys
#only for vscode debug activate this
#char=1
if __name__ == "__main__":
    def sets(char):
        with open(output, "w") as file:
            for num in range(int(min) , int(max)+1):
                for all in list(permutations(char,num)):
                    outcome = "".join(all)
                    file.write(str(outcome) + "\n")
                file.close()
    def show(char):
        for num in range(int(min) , int(max)+1):
            for all in list(permutations(char,num)):
                outcome = "".join(all)
                print(outcome)
    options = ['--help',"-cli","--show"]
    information = ["to show option","to enter the program simple cli to use costume charset","to print all the outcomes instead of withing them to the file"]
    if len(sys.argv) < 2:
        print("use --help to show options or use -cli for simple cli ")
        quit()
    elif sys.argv[1] == '--help':
        for opt, info in zip(options, information):
            print(str(opt)+'   '+str(info))
        print("you can also use python3 pass2list.py -o Outputfile min-len max-len charset")
        print("you can also use python3 pass2list.py --show min-len max-len charset")    
        print("Default charsets are ?l for lowecase ?u for uppercase and ?n for number and ?A for all")
        print("you can use Default charsets combine like ?ln for lowercase and number and ...!")
        quit()
    elif sys.argv[1] == "-cli":
        charinput = list(input('input the costum charset or ?Default-Char for default charsets!  '))
        for charsets in charinput:
            if charsets == "?l":
                char = list('abcdefghijklmnopqrstuvwxyz')
                break
            elif charsets == "?n":
                char = list("1234567890")
                break
            elif charsets == "?u":
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                break
            elif charsets == "?ln" or charsets == "?nl":
                char = list('abcdefghijklmnopqrstuvwxyz1234567890')
                break
            elif charsets == "?ul" or charsets == '?lu':
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
                break
            elif charsets == "?un" or charsets == "?nu":
                char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
                break
            elif charsets == "?A":
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
                break
            else:
                char = charinput
        min = input("input minimum-len : ")
        max = input("input the maximum-len : ")
        output = input('please input the output file path ! ')
        sets(char)
    elif sys.argv[1] == "-o":
        output = sys.argv[2]
        min = sys.argv[3]
        max = sys.argv[4]
        for charsets in sys.argv[5]:
            if charsets == "?l":
                char = list('abcdefghijklmnopqrstuvwxyz')
                break
            elif charsets == "?n":
                char = list("1234567890")
                break
            elif charsets == "?u":
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                break
            elif charsets == "?ln" or charsets == "?nl":
                char = list('abcdefghijklmnopqrstuvwxyz1234567890')
                break
            elif charsets == "?ul" or charsets == '?lu':
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
                break
            elif charsets == "?un" or charsets == "?nu":
                char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
                break
            elif charsets == "?A":
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
                break
            else:
                char = list(sys.argv[5])
        sets(char)
    elif sys.argv[1] == "--show":
        min = sys.argv[2]
        max = sys.argv[3]
        for charsets in sys.argv[4]:
            if charsets == "?l":
                char = list('abcdefghijklmnopqrstuvwxyz')
                break
            elif charsets == "?n":
                char = list("1234567890")
                break
            elif charsets == "?u":
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                break
            elif charsets == "?ln" or charsets == "?nl":
                char = list('abcdefghijklmnopqrstuvwxyz1234567890')
                break
            elif charsets == "?ul" or charsets == '?lu':
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
                break
            elif charsets == "?un" or charsets == "?nu":
                char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
                break
            elif charsets == "?A":
                char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
                break
            else:
                char = list(sys.argv[4])
        show(char)
    else:
        print("use --help to show options or use -cli for simple cli ")
        quit()
