import random

questions = [
    {"question": "Which country is Delhi located in?", "options": ["a. India", "b. America", "c. Pakistan", "d. Nepal"], "correct_answer": "a"},
    {"question": "What is the capital of India?", "options": ["a. Bihar", "b. Punjab", "c. Delhi", "d. Uttar Pradesh"], "correct_answer": "c"},
    # Add more questions and answers here
]

prize_money = 0

def play_kbc():
    global prize_money
    correct_answers = 0
    for question in questions:
        print(question["question"])
        random.shuffle(question["options"])  # Shuffle options for each question
        for option in question["options"]:
            print(option)

        answer = input("Enter your answer (a, b, c, or d): ").lower()

        if answer == question["correct_answer"]:
            print("Congratulations! That's the correct answer.")
            correct_answers += 1
            prize_money += 10000  # Increase prize money for each correct answer
        else:
            print("Sorry, that's the wrong answer.")
            print(f"You answered {correct_answers} questions correctly and won ₹{prize_money}.")
            return

    print("Congratulations! You answered all the questions correctly and won ₹100000!")  # Adjust winning amount if needed

play_kbc()
