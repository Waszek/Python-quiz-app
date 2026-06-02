import json

class Question:
    def __init__(self, text, option, correct_answer):
        self.text = text
        self.option = option
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


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



def quiz(first_name):
    with open('questions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    question_objects = []

    points = 0

    for element in data:
       question_obj = Question(
           element["question"],
           element["options"],
           element["correct"]
       )
       question_objects.append(question_obj)

    for question in question_objects:
        print(question.text)
        options = "\n".join(f"{k}: {v}" for k,v in question.option.items())
        print(options)
        answer = input('Your answer: ')

        if question.check_answer(answer):
                print('Correct answer!')
                points += 1
        else:
                print('Wrong answer!')
    

    print(f'{first_name}, Your score is: {points}')

def main():
    received_first_name, received_age = welcome()
    quiz(received_first_name)

if __name__ == "__main__":
    main()