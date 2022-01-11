question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
option_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1] 
fifty=[["nine","seven"],["bhopal","delhi"],["Software Engineering", "Counseling"]]
fifty_solution=[2,2,1] 
print("namskar deviyo or sajno aap sabko namskar,sastryekal,adab")
print("chaliye aaj ka saval shuru karte hain")
print("pehla saval apki screen")
i=0
c=0
while i<len(question_list):
    print(i+1,question_list[i])
    a=0
    while a<=len(option_list):        
        print(a+1,option_list[i][a])
        a=a+1
    j=int(input('enter a answer :'))
    if j==solution_list[i]:
        print('congratulation')
    elif j==5050:
        if c==0:
            k=0
            while k<len(fifty[i]):
                print(k+1,fifty[i][k])
                k=k+1
            c=c+1
            lifeline=int(input("enter a your 5050 lifeline :"))
            if lifeline==fifty_solution[i]:
                print("correct")
            else:
                print("your answer is wrong")
                break
        else:
            print("you already use your lifeline ")
    else:
        print("wrong")
        break
    i=i+1


   # kbc game