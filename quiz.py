from random import shuffle

QUESTIONS = {
    "Question 1: What is the capital of France?": [
        "Paris", "Berlin", "Madrid", "London"
    ],
    "Question 2: Which planet is known as the Red Planet?": [
        "Earth", "Mars", "Venus", "Jupiter"
    ],
    "Question 3: What is the largest mammal in the world?": [
        "Elephant", "Blue whale", "Giraffe", "Lion"
    ],
}

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, alternatives):
        correct_answer = alternatives[0]
        shuffled_alternatives = alternatives.copy()
        shuffle(shuffled_alternatives)

        print(question)
        for label, alternative in enumerate(shuffled_alternatives):
            print(f"  {label}) {alternative}")

        answer_label = int(input("Your answer (enter the number): "))
        answer = shuffled_alternatives[answer_label] if 0 <= answer_label < len(shuffled_alternatives) else None

        if answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer!r}.\n")

    def run_quiz(self):
        for question, alternatives in self.questions.items():
            self.ask_question(question, alternatives)
        print(f"Quiz completed! Your final score is {self.score}/{len(self.questions)}.")

# Example usage:
quiz_instance = Quiz(QUESTIONS)
quiz_instance.run_quiz()