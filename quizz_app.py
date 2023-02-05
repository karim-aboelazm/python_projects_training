questions = [
    {
        "question":"What is the result of 2+5 ?",
        "choices" : [8 , 9 , 6 , 7],
        "answer"  : 7,
    },
    {
        "question":"What is the Templates files ?",
        "choices" : [".py",".txt",".html",".css"],
        "answer"  : ".html",
    },
    {
        "question":"What is the name of step after secondary ?",
        "choices" : ["primary","prep","Univeristy","deplom"],
        "answer"  : "Univeristy",
    },
    {
        "question":"What is the third color in Egypt Flag ?",
        "choices" : ["White","Red","Black","Yellow"],
        "answer"  : "Black",
    },   
]
score = 0
for q in questions:
    print("\n" + q["question"])
    for i, c in enumerate(q["choices"]):
        print(f"{str(i+1)}. {c}")
    user_answer = int(input("Enter Your Answer (1, 2, 3, or 4): "))
    if q["choices"][user_answer-1] == q["answer"]:
        print("Correct.. :) ")
        score += 1
    else:
        print("Incorrect.. :( ")
print(f"Your Score : {score} / {len(questions)}")
        