import yaml
import random
from typing import List, Tuple
import os
import msvcrt
import sys

class CLIQuiz:
    def __init__(self, questions_file: str = "questions.yaml"):
        self.questions_file = questions_file
        self.questions = self.load_questions()
        self.correct_answers = []
        self.wrong_answers = []

    def clear_previous_lines(self, lines: int):
        """Clear the specified number of previous lines in the console."""
        for _ in range(lines):
            sys.stdout.write('\033[F')  # Move cursor up one line
            sys.stdout.write('\033[K')  # Clear line

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
        print("\n" + "="*50)

        try:
            for action, correct_answer in self.questions:
                tries = 3
                while tries > 0:
                    # Make the action box more compact and centered
                    print("\nAction:")
                    print("╔" + "═" * 60 + "╗")
                    print("║ " + action.center(58) + " ║")
                    print("╚" + "═" * 60 + "╝\n")
                    
                    answer = input("Your answer: ").strip()
                    
                    if answer.lower() == 'skip':
                        self.wrong_answers.append((action, correct_answer, "skipped"))
                        print("\n" + "─" * 50)
                        break
                    
                    if answer == correct_answer:
                        print("\n✓ Correct!\n")
                        self.correct_answers.append((action, correct_answer))
                        break
                    else:
                        tries -= 1
                        if tries > 0:
                            print("\n✗ Incorrect!")
                            print(f"The correct answer is: {correct_answer}")
                            print(f"Attempts remaining: {tries}")
                            print("\nPress 'r' to try again")
                            print("Press any other key to continue\n")
                            
                            key = msvcrt.getch().decode().lower()
                            if key != 'r':
                                self.wrong_answers.append((action, correct_answer, answer))
                                break
                            
                            # Clear all previous output if retrying
                            self.clear_previous_lines(9)  # Adjusted for new format
                        else:
                            print("\n✗ Incorrect!")
                            print(f"The correct answer is: {correct_answer}")
                            print("No attempts remaining\n")
                            self.wrong_answers.append((action, correct_answer, answer))
                print("═" * 50)

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
