import json
import pandas as pd
class Game(dict):
    def __init__ (self, title, min_players, max_players, min_duration, max_duration, age):
        self['title'] = title.title()
        self['min_players'] = min_players
        self['max_players'] = max_players
        self['min_duration'] = min_duration
        self['max_duration'] = max_duration
        self['age'] = age

class Game_cabinet(dict): #9
    
    def add_game(self, title, min_players, max_players, min_duration, max_duration, age):
        temp_game = Game(title, int(min_players), int(max_players),int(min_duration), int(max_duration), int(age))
        self[title] = temp_game

def user_input(message): #10, #11. Here I wanted to make a function to be sure that the value entered by the user is an integer.
    while True:
        try:
            global input_value
            input_value = int(input(message))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            break

def add_a_game():
    print('Please enter title, amount of players, duration in minutes and minimum age for the game')
    title = input('Title: ')
    user_input('Minimum amount of players: ')
    min_players = input_value
    
    user_input('Maximum amount of players: ')
    max_players = input_value

    user_input('Minimum duration of game in minutes: ')
    min_duration = input_value

    user_input('Maximum duration of game in minutes: ')
    max_duration = input_value
    
    user_input('Minimum age for the game: ')
    age = input_value

    cabinet.add_game(title, min_players, max_players, min_duration, max_duration, age)

def show_games(): #4, #12. This function is made to display all the saved games to the user in an easy to read dataframe.
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_dict = json.load(list_of_games)
        boardgame_df = pd.DataFrame(boardgame_dict)
        boardgame_df = boardgame_df.T # This is used to change the position of the keys from axis 0 to axis 1 in the dataframe.
        print(boardgame_df)

def change_game(): #1, #2
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_list = json.load(list_of_games)
        game_id = str(input('Which game woud you like to change? '))
        game_id = game_id.lower()
        attribute = str(input('Choose the attribute you want to update: title / min_players / max_players / min_duration / max_duration / age: '))
        attribute = attribute.lower()
        new_attribute = input('New attribute: ')
        new_attribute = new_attribute.title()
        boardgame_list[game_id][attribute] = new_attribute
    with open('boardgame.json', 'w') as list_of_games:
        json.dump(boardgame_list, list_of_games)

def remove_game(): #3.
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_dict = json.load(list_of_games)
        game_id = str(input('Which game do you want to remove? '))
        game_id = game_id.lower()
        try: # Here I wanted to make sure that the game a user tries to remove actually exists
            del boardgame_dict[game_id]
            with open('boardgame.json', 'w') as list_of_games:
                json.dump(boardgame_dict, list_of_games)
                print(game_id.title(), 'was successfully removed')
        except KeyError:
            print('The game does not exist')

def filter_game(): #5, #6, #7, #8
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_dict = json.load(list_of_games)
        boardgame_df = pd.DataFrame(boardgame_dict)
        boardgame_df = boardgame_df.T
        # To be able to compare the value entered by the user and the values in the dataframe, there is a need to convert the dataframe values to numeric values.
        boardgame_df[['min_players', 'max_players', 'min_duration', 'max_duration', 'age']] = boardgame_df[['min_players', 'max_players', 'min_duration', 'max_duration', 'age']].apply(pd.to_numeric)
        
        user_input('How many players are you? ')
        inp_players = input_value
        
        user_input('Estimate how much time you can spare, answer in minutes: ')
        inp_duration = input_value
        
        user_input('How old is the youngest player in your group? ')
        inp_age = input_value
        
        # Declaring the evaluation order of the statements for filtering the dataframe with '()', and combining the statements with '&'.
        matches_df = boardgame_df[(boardgame_df.min_players <= inp_players) & (boardgame_df.max_players >= inp_players) & (boardgame_df.min_duration <= inp_duration) & (boardgame_df.max_duration >= inp_duration) & (boardgame_df.age <= inp_age)]
        if matches_df.empty == True:
            print('No games matching the criteria')
        else:
            print(matches_df)

def save_game():
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_dict = json.load(list_of_games)
        boardgame_dict.update(cabinet)
    with open('boardgame.json', 'w') as list_of_games:
        json.dump(boardgame_dict, list_of_games)

cabinet = Game_cabinet()
choice = 0
while choice != None: # Making room for user mistakes while making their choice. If for example I were to have an 8 instead of None and the user entered an 8 by mistake, the program would stop.
    user_input('1.Add new game\n2.Save your newly added games\n3.Show list of games from file\n4.Make changes to a game\n5.Remove a game\n6.Search for a suitable game\n7.Exit program\nMake your choice: ')
    choice = input_value
    if choice == 1:
        add_a_game()
        
    elif choice == 2:
        save_game()
        print('Your games are now saved')
    
    elif choice == 3:
        show_games()
        

    elif choice == 4:
        change_game()

    elif choice == 5:
        remove_game()

    elif choice == 6:
        filter_game()

    elif choice == 7:
        save_game() # Safety feature if the user forgets to save their games and exits the program.
        exit()

    else:
        print('Choose an alternative between 1 and 7')

#Sources:
#1. https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
#2. https://www.geeksforgeeks.org/python-update-nested-dictionary/
#3. https://www.programiz.com/python-programming/nested-dictionary Example: 6
#4. https://www.youtube.com/watch?v=x3ueeuoU2x0
#5. https://www.youtube.com/watch?v=2AFGPdNn4FM
#6. https://stackoverflow.com/questions/15891038/change-data-type-of-columns-in-pandas
#7. https://www.youtube.com/watch?v=YPItfQ87qjM
#8. https://pythonexamples.org/pandas-check-if-dataframe-is-empty/
#9. https://www.quora.com/How-do-I-create-a-constructor-without-arguments-in-python
#10. https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
#11. https://stackoverflow.com/questions/50559252/python-while-true-try-except-returning-value
#12. https://stackoverflow.com/questions/31658183/how-to-switch-columns-rows-in-a-pandas-dataframe