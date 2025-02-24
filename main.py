import yaml
import random
from typing import List, Tuple
import os

class CLIQuiz:
    def __init__(self, questions_file: str = "questions.yaml"):
        self.questions_file = questions_file
        self.questions = self.load_questions()
        self.correct_answers = []
        self.wrong_answers = []

    def load_questions(self) -> List[Tuple[str, str]]:
        """Load and return questions from the YAML file."""
        if not os.path.exists(self.questions_file):
            print(f"Error: {self.questions_file} not found!")
            return []
        
        with open(self.questions_file, 'r') as file:
            data = yaml.safe_load(file)
        
        return [(q['action'], q['answer']) for q in data['questions']]

    def run_quiz(self):
        """Run the CLI command quiz."""
        if not self.questions:
            return

        # Shuffle questions
        random.shuffle(self.questions)
        
        print("Type your answer or 'skip' to move to the next question.")
        print("Press Ctrl+C to exit.")

        try:
            for action, correct_answer in self.questions:
                print(f"\nAction: {action}")
                answer = input("Your answer: ").strip()
                
                if answer.lower() == 'skip':
                    self.wrong_answers.append((action, correct_answer, "skipped"))
                    continue
                
                if answer == correct_answer:
                    print("✓ Correct!")
                    self.correct_answers.append((action, correct_answer))
                else:
                    print(f"✗ Incorrect. The correct answer is: {correct_answer}")
                    self.wrong_answers.append((action, correct_answer, answer))

        except KeyboardInterrupt:
            print("\n\nQuiz interrupted. Here's your summary:")

        self.show_summary()

    def show_summary(self):
        """Display the quiz results."""
        total = len(self.correct_answers) + len(self.wrong_answers)
        if total == 0:
            return

        print("\n=== Quiz Summary ===")
        print(f"Total questions attempted: {total}")
        print(f"Correct answers: {len(self.correct_answers)}")
        print(f"Wrong/skipped answers: {len(self.wrong_answers)}")
        print(f"Success rate: {(len(self.correct_answers) / total) * 100:.1f}%")

        if self.wrong_answers:
            print("\nQuestions to practice:")
            for action, correct, given in self.wrong_answers:
                print(f"\nAction: {action}")
                print(f"Correct answer: {correct}")
                if given != "skipped":
                    print(f"Your answer: {given}")

if __name__ == "__main__":
    quiz = CLIQuiz()
    quiz.run_quiz()
