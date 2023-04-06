import os

name = input("\nEnter Candidate Name : ")
while True:
    gender = input("\nEnter your Gender F/M: ")
    new = gender.lower()
    list1 = ("m","male",)
    list2 = ("f","female")
    if(new in list1 ):
        os.system("cls")
        print("\nWelcom Mr.", name, "in KON BANEGA CORORPATI")
        break
    elif(new in list2 ):
        os.system("cls")
        print("\nWelcom Mis.", name, "in KON BANEGA CORORPATI")
        break
os.system("timeout /t 3")
os.system("cls")
price = (1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 500000, 10000000)
Answer = ["b","d","b","d","b","d","d","b","c","d","a","a","c","d","c","b"]
j = 0
qst0 = "1. What is the output of the below program in python: print(0.2+0.4==0.6)\n \nA.True \nB.False \nC.Error \nD.Depends on machine"
qst1 = "2. Which is not a feature of Python language?\nA.Interpreted language\nB.Portable\nC.High level language\nD.Case Insensitive"
qst2 = "3. Python is a ___.object-oriented programming language.\nA.Special purpose\nB.General purpose\nC.Medium level programming language\nD.All of the mentioned above"
qst3 = "4. Developer of Python programming?\nA.Denis Ritchie\nB.Y.C. Khenderakar\nC.Tim Berner Lee\nD.Guido van Rossum"
qst4 = "5. What is the output in python language?Round (.4)-Round (-.5)\nA.0\nB.1\nC.2\nD..9"
qst5 = "6. Which are the application areas of Python programming?\nA.Web Development\nB.Game Development\nC.Artificial Intelligence and Machine Learning\nD.All of the above"
qst6 = "7. What is Numeric Types of Data Types?\nA.int\nB.float\nC.complex\nD.All of the  above"
qst7 = "8. What is output for below code?\na=2\nb=3\nprint(a,b)\na,b=b,a\nprint(a,b)\n\nA.23 23\nB.23 32\nC.32 32\nD.None of Above"
qst8 = "9. list, tuple dictionary are which types of Data Types.\nA.Binary Types\nB.Boolean Types\nC.Sequence Types\nD.None of the above"
qst9 = "10. Which types of logical operators in Python?\nA.AND\nB.OR\nC.NOT\nD.All of the above"
qst10 = "11. What is the name of the operator ** in Python?\nA.Exponentiation\nB.Modulus\nC.Floor division\nD.None of the these"
qst11 = "12. What is the output of following code?\nx='Ram, Shya'\nprint(x[::5]\nA.RS\nB.RAMSH\nC.RAM\nD.SHYAM"
qst12 = "13. What is the extension of Python Program?\nA..execute python\nB..python\nC..py\nD..run python"
qst13 = "14. Which keyword used in python language?\nA.finally\nB.lambda\nC.while\nD.All of Above"
qst14 = "15. Which return the % operator?\nA.Quotient\nB.Divisor\nC.Remainder\nD.Multiplication"
qst15 = "what is python \n A.snake \n B.Prograing Language \nC.Oprating System \nD.Aplication "
#qst = ["qst0","qst1","qst2","qst3","qst4","qst5","qst6","qst7","qst8","qst9","qst10","qst11","qst12","qst13","qst14","qst15"]
qst = [qst0,qst1,qst2,qst3,qst4,qst5,qst6,qst7,qst8,qst9,qst10,qst11,qst12,qst13,qst14,qst15]
while True:
    for i in range(15):
        print(qst[i])
        c = input("\nPlease Type Your Answer: ")
        n = c.lower()
        os.system("cls")
        print("\nPlease Wait We are Chacking Your Answer")
        os.system("timeout /t 3")
        os.system("cls")
        if n == Answer[i]:
            os.system("cls")
            print("\nCongratulation You are right")
            os.system("timeout /t 2")
            os.system("cls")
            j = j +1
            print("\nAgla Sawal",price[j],"Rs k liye")
            os.system("timeout /t 5")
            os.system("cls")
        else:
            print("\nAap Ne Galat Jawab Diya")
            break
    break
os.system("cls")
print("\n\nPlease Wait For your result")
os.system("timeout /t 5")
os.system("cls")
print("Congratulation You won \n\n",price[j],"\n\nin \' KBC \' Please Comback Again")