from lib import DMY, MDY, YDM, YMD


def dob():


    try:

        yearStart = int(input("Enter Year Starting from?\n"))

        yearEnd = int(input("Enter Year Ending?\n"))

        if len(str(yearStart)) != 4 or len(str(yearEnd)) != 4 :

            print("<>Error, please enter year with four digits \n")

            dob()

        else:

            pattern = input("choose pattern for DOB-wordlist \n"
                            "here is the list of available patters :"
                            " \n \t 1 : ymd \n \t 2 : ydm \n \t 3 : mdy \n \t 4 : dmy \n"
                            "choose : ")

            if pattern == str(1):
                YMD.ymd(yearStart, yearEnd)

            elif pattern == str(2):
                YDM.ydm(yearStart, yearEnd)

            elif pattern == str(3):
                MDY.mdy(yearStart, yearEnd)

            elif pattern == str(4):
                DMY.dmy(yearStart, yearEnd)

            else:

                print("<>Error, you can choose only available patterns")


    except ValueError:

        print("<>Error, please enter only year \n")

        dob()


dob()




