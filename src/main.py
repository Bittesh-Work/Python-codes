from Questions import Question
questions_prompt = [
    "Colour of apple? \n a. red \n b. green \n c. yellow\n\n",
    "Colour of guava? \n a. red \n b. green \n c. yellow\n\n",
    "Colour of banana? \n a. red \n b. green \n c. yellow\n\n"
]

questions =[
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "c")
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt + "\n" +"Your answer is kpratyush: ")
        if answer == question.answer:
            score+= 1
    print ("You got " + str(score) + "/" + str(len(questions)) + " correct")
    print("hallo")
    print("gadha")


run_test(questions) 