import json

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

    # print(pytania)
    points = 0

    for element in data:
        print(element["question"])
        opcje = "\n".join([f"{k}:{v}" for k,v in element["options"].items()])
        print(opcje)
        user_answer = input('Your answer: ')

        if user_answer == element["correct"]:
            print('Correct Answer!')
            points += 1
        else:
            print('Wrong Answer!')

    print(f'{first_name}, Your score is: {points}')

def main():
    received_first_name, received_age = welcome()
    quiz(received_first_name)

if __name__ == "__main__":
    main()