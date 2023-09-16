# importing librarys and files
import ascii
from colorama import Style, Fore
import re
# showing the asscy art
ascii.show()

# main function
def main():
    text = str(input(Fore.RED+"Please Enter Your Text(The Text Should Seprated By '_' or '-' or 'space'): "+Style.RESET_ALL))
    text_arry = re.split(r'[_ -]', text)
    for i in range(len(text_arry)):
        text_arry[i] = text_arry[i].capitalize()
    text_arry[0] = text_arry[0][:1].lower() + text_arry[0][1:]
    final_text = "".join(text_arry)

    print ("\n"+Fore.GREEN + "The CamelCased Text is: " + Style.RESET_ALL + final_text + "\n")

# caling the main function
main()
while True:
    continuing = input("Do You Want To Continue ((Y)es or (N)o)? ")
    if continuing == "" or continuing == "Y" or continuing == "y" or  continuing == "Yes" or continuing == "yes":
        main()
    else:
        break;