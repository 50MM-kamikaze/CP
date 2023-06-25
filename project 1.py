print("QUIZZZ \n")
y_n  = input("do you wanna play ? give y or n : ")
y_n = y_n.capitalize()
if y_n != 'Y':
    quit()
print("the game starts")

print("Give the option number for the answers \n")
initial_score = 100
questions = [["whos the best actor" , "1. jake" , "2. ksi " , 2] , 
             ["whos the best actor" , "1. jake" , "2. ksi " , 2] ,
             ["whos best actor" , "1. jake" , "2. ksi " , 2] ,
             ["whos the best actor" , "1. jake" , "2. ksi " , 2] ,
             ["whos the best actor" , "1. jake" , "2. ksi " , 2] ,]

for i in range(0,len(questions)):
    question = questions[i]
    print(f"""{1} st question :- 
        {question[0]} \n options below:-
        {question[1]}      {question[2]} \n """)
    given_answer = int(input("Give the answer = "))
    if given_answer == int(question[-1]):
        print("correct answer.")
        print(f"your score is {initial_score} ")
        pass 
    else:
        initial_score -= 20
        print(initial_score)
        pass
final_score = initial_score
print(f"""Your final score is  {final_score}
 you are done with the quizz""")