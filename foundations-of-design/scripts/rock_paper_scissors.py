import random

OPTIONS = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(OPTIONS)

def get_human_choice():
    choice_number = int(input('Enter the number of you choice: '))
    return OPTIONS[choice_number - 1]

def print_options():
    print('\n'.join(f'{ {(i)} {option.title()}' for i, option in enumerate(OPTIONS)))
    
def print_choices(human_choice, computer_choice):
    print(f'You chose {human_choice}')
    print(f'The computer chose {computer_choice}')

def print_win_lose(human_choice, computer_choice, human_beats, human_loses_to):
    if computer_choice == human_loses_to:
        print(f'Sorry, {computer_choice} beats {human_choice}')
    elif computer_choice == human_beats:
        print(f'Yes, {human_choice} beats {computer_choice}!')
        