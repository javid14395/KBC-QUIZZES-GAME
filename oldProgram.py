import time
hh = int(time.strftime("%H"))
hh = int(input())
if hh < 12:
    print("Good Mornig")
elif hh > 12:
    print("Good Afternon")
elif hh > 6:
    print("Good Evening")
else:
    print("Good Night")

for i in range(1,8,2):
    print(i)

j = int(input("Enter Between 100 : "))

match j:
    case 80:
        print("Yuo Are Good Person")
    case 50 :
        print("Yuo Are ok Person")
    case _:
        print("Yuo Are note god")

 it is program for KBC 
''' 
1 13 qusion for each contast 

'''