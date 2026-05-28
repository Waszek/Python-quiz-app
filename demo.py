def powitanie():
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
    pytania = [
        ('What is the capital of Poland?',
        {
            'a': 'Warsaw',
            'b': 'Krakow',
            'c': 'Gdansk',
            'd': 'Wroclaw'
        },
        'a'),
        ('What is the capital of France?',
        {
            'a': 'Madrid',
            'b': 'Rome',
            'c': 'Paris',
            'd': 'Berlin'
        },
        'c'),
        ('What is the capital of Germany?',
        {
            'a': 'Vienna',
            'b': 'Berlin',
            'c': 'Hamburg',
            'd': 'Munich'
        },
        'b')
    ]

    # print(pytania)
    punkty = 0

    for pytanie, mozliwe_odpowiedzi, poprawna_odpowiedz in pytania:
        print(pytanie)
        opcje = "\n".join([f"{k}:{v}" for k,v in mozliwe_odpowiedzi.items()])
        print(opcje)
        odpowiedz_uzytkownika = input('Your answer: ')

        if odpowiedz_uzytkownika == poprawna_odpowiedz:
            print('Correct Answer!')
            punkty += 1
        else:
            print('Wrong Answer!')

    print(f'{first_name}, Your score is: {punkty}')

def main():
    received_first_name, received_age = powitanie()
    quiz(received_first_name)

if __name__ == "__main__":
    main()