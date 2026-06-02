import json

class Question:
    def __init__(self, text, option, correct_answer):
        self.text = text
        self.option = option
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class QuizGame:
    def __init__(self, player_name, file_path):
        self.player_name = player_name
        self.file_path = file_path
        self.questions = []
        self.points = 0

        self.load_questions()

    def load_questions(self):
        with open(self.file_path) as file:
            data = json.load(file)
            
            for element in data:
                question_obj = Question(
                    element["question"],
                    element["options"],
                    element["correct"]
                )
                self.questions.append(question_obj)
        

    def start(self):
        for question in self.questions:
            print(question.text)
            options = "\n".join(f"{k}: {v}" for k,v in question.option.items())
            print(options)
            user_answer = input("Your answer: ")

            if question.check_answer(user_answer):
                print("Correct answer!")
                self.points += 1
            else:
                print("Wrong answer!")

        print(f"{self.player_name}, your score is {self.points}")
        

def welcome():
    first_name = input('What is your first name? ')
    print(f'Hello, {first_name}!')

    if first_name == 'Krzysztof':
        print('You have a nice name!')
    else:    
        print('Your name is not as nice as Krzysztof, but it is still nice!')
        
    while True:
        try:
            age = int(input('How old are you? '))
            break # Jeśli się udało, przerywamy pętlę
        except ValueError:
            print("Type a number not a string!")


    if age >= 18:
        print('You are an adult!')
    else:    
        print('You are a child!')

    return first_name, age


def main():
    received_first_name, received_age = welcome()
    game = QuizGame(received_first_name, file_path='questions.json')
    game.start()

if __name__ == "__main__":
    main()