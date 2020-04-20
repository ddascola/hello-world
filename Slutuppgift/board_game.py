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

class Game_cabinet(dict):
    def __init__(self):
        self.game_list = []
        self.game_dict = {}
        
    def add_game(self, title, min_players, max_players, min_duration, max_duration, age):
        temp_game = Game(title, int(min_players), int(max_players),int(min_duration), int(max_duration), int(age))
        self[title] = temp_game

def add_a_game():
    print('Please enter title, amount of players, duration in minutes and minimum age for the game')
    title = input('Title: ')
    min_players = int(input('Minimum amount of players: '))
    max_players = int(input('Maximum amount of players: '))
    min_duration = int(input('Minimum duration of game in minutes: '))
    max_duration = int(input('Maximum duration of game in minutes: '))
    age = int(input('Minimum age for the game: '))

    cabinet.add_game(title, min_players, max_players, min_duration, max_duration, age)

def show_games():
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_dict = json.load(list_of_games)
        boardgame_df = pd.DataFrame(boardgame_dict)
        boardgame_df = boardgame_df.T
        print(boardgame_df)

def change_game():
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

def remove_game():
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_dict = json.load(list_of_games)
        game_id = str(input('Which game do you want to remove? '))
        del boardgame_dict[game_id]
    with open('boardgame.json', 'w') as list_of_games:
        json.dump(boardgame_dict, list_of_games)
        print(game_id.title(), 'was successfully removed')

def filter_game():
    with open('boardgame.json', 'r') as list_of_games:
        boardgame_dict = json.load(list_of_games)
        boardgame_df = pd.DataFrame(boardgame_dict)
        boardgame_df = boardgame_df.T
        boardgame_df[['min_players', 'max_players', 'min_duration', 'max_duration', 'age']] = boardgame_df[['min_players', 'max_players', 'min_duration', 'max_duration', 'age']].apply(pd.to_numeric)
        inp_players = int(input('How many players are you? '))
        inp_duration = int(input('Estimate how much time you can spare, answer in minutes: '))
        inp_age = int(input('How old is the youngest player in your group? '))
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
while choice != 8:
    choice = int(input('1.Add new game\n2.Save your newly added games\n3.Show list of games from file\n4.Make changes to a game\n5.Remove a game\n6.Search for a suitable game\n7.Exit program\nMake your choice: '))
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
        save_game()
        exit()

    else:
        print('Choose an alternative between 1 and 7')