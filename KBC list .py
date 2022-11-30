question_list=[
    " In India How  many state are there ?",
    "what is the capital of india?",
    "ng me konse cource pdye jate h?",
    "How many days in the leap year?"]

option_list=[
    ["22","25","28","29"],
    ["bhopal","delhi","chandigad","banglore"],
    ["python","java","agriculture","c++"],
    ["365","366","300","360"]]

solution_list=[4,2,1,2]

lifeline=[
    ["(3)29","(1)25"],
    ["(2)delhi","(1)bhopal"],
    ["(2)java","(1)python"],
    ["(1)365","(2)366"]]

print("welcome to KBC")
print("your game start now")

i=0
money=1000
c=1
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(option_list[i]):
        k=option_list[i][j]
        print(k)
        j=j+1
    if c<4:
        user_input=input("do you want  lifeline?")
        if user_input=="yes":
            c=c+1
            print("5050",lifeline[i])
    else:
        print("you can not use lifeline,because you already use two lifeline")
    b=int(input("choose correct answer:"))
    if b==solution_list[i]:
        money=money+10000
        print("your ans is correct")
        print("you win Rs./-",money)
    else:
        print("your ans is wrong")
        break
    i=i+1
