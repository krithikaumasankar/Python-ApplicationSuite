#QUIZ
class InvalidOptionError(Exception):        # Custom Exception
    pass

class Quiz:
    def __init__(self):
        # Questions list
        self.questions = [
            "1. Largest planet?\nA. Earth\nB. Mars\nC. Jupiter",
            "2. 5 + 3 = ?\nA. 6\nB. 8\nC. 10",
            "3. Capital of India?\nA. Mumbai\nB. Delhi\nC. Chennai",
            "4. Water chemical formula?\nA. H2O\nB. CO2\nC. O2",
            "5. Sun rises in?\nA. West\nB. East\nC. North",
            "6. 10 * 2 = ?\nA. 20\nB. 15\nC. 25",
            "7. Fastest land animal?\nA. Lion\nB. Cheetah\nC. Tiger",
            "8. National animal of India?\nA. Lion\nB. Tiger\nC. Elephant"
        ]

        # Correct answers
        self.answers = ['C', 'B', 'B', 'A', 'B', 'A', 'B', 'B']

        # Score variable
        self.score = 0

    def start_quiz(self):
        for i in range(len(self.questions)):
            while True:  # Loop until valid input
                try:
                    print("\n" + self.questions[i])
                    user_ans = input("Enter option (A/B/C): ").upper()

                    if user_ans not in ['A', 'B', 'C']:
                        raise InvalidOptionError("Invalid option selected!")

                    # Check answer
                    if user_ans == self.answers[i]:
                        print("Correct!")
                        self.score += 1
                    else:
                        print("Wrong!")

                    break  # Exit loop after valid input

                except InvalidOptionError as e:
                    print(e)

    def display_score(self):
        print("\nQuiz Completed!")
        print(f"Your final score is: {self.score} / {len(self.questions)}")

# Create object and call methods
print("\n\tWELCOME TO QUIZ....")
q = Quiz()
q.start_quiz()
q.display_score()
