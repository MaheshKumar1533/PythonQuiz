import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
NEW_QUIZ_QUESTIONS = {
    'What is the largest mammal on Earth?': ['Blue Whale', 'Elephant', 'Giraffe', 'Lion'],
    'Which country is known as the Land of the Rising Sun?': ['Japan', 'China', 'India', 'Australia'],
    'What is the square root of 144?': ['12', '10', '14', '16'],
    'In which year did the Titanic sink?': ['1912', '1905', '1920', '1935'],
    'Who wrote the play "Romeo and Juliet"?': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Mark Twain'],
    'What is the smallest prime number?': ['2', '1', '3', '5'],
    'Which planet is known as the Red Planet?': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
    'What is the capital of Canada?': ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'],
    'Which programming language is used for building mobile applications in Android?': ['Java', 'Swift', 'Python', 'C#'],
    'What is the currency of Japan?': ['Yen', 'Won', 'Dollar', 'Euro'],
}

def initiate_quiz():
    questions = fetch_questions(NEW_QUIZ_QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)
    print(f"\nYou got {num_correct} correct out of {num} questions")

def fetch_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    shuffled_alternatives = random.sample(alternatives, k=len(alternatives))
    user_answer = get_user_choice(question, shuffled_alternatives)
    if user_answer == correct_answer:
        print(" Correct! ")
        return 1
    else:
        print(f"The correct answer is {correct_answer!r}, not {user_answer!r}")
        return 0

def get_user_choice(question, alternatives):
    print(f"{question}?")
    all_options = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in all_options.items():
        print(f"  {label}) {alternative}")
    while (answer_label := input("\nYour Choice? ")) not in all_options:
        print(f"Please choose one of {', '.join(all_options)}")
    return all_options[answer_label]


if __name__ == "__main__":
    initiate_quiz()
    print("Thank you for your participation!")
