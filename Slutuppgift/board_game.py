import json
import pandas as pd
class Game(dict):
    def __init__ (self, title, players, duration, age):
        self['title'] = title.title()
        self['players'] = players
        self['duration'] = duration
        self['age'] = age
        #self.__dict__ = game_dict

class Game_cabinet(dict):
    def __init__(self):
        self.game_list = []
        self.game_dict = {}
        
    def add_game(self, title, players, duration, age):
        temp_game = Game(title, int(players), int(duration), int(age))
        self[title] = temp_game
        
cabinet = Game_cabinet()
choice = 0
while choice != 8:
    choice = int(input("1.Add new game\n2.Save your newly added games\n3.Show list of games from file\n4.Make changes to a game\n5.Remove a game\n6.Search for a suitable game\n7.Exit program\nMake your choice: "))
    if choice == 1:
        print("Please enter title, recommended amount of players, duration in minutes and minimum age for the game")
        title = input("Title: ")
        players = int(input("Recommended amount of players: "))
        duration = int(input("Duration of game in minutes: "))
        age = int(input("Minimum age for the game: "))

        cabinet.add_game(title, players, duration, age)
        
    elif choice == 2:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            boardgame_dict.update(cabinet)
        with open('boardgamee.json', 'w') as list_of_games:
            json.dump(boardgame_dict, list_of_games)

    elif choice == 3:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            print (json.dumps(boardgame_dict, indent=2))
        

    elif choice == 4:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_list = json.load(list_of_games)
            game_id = str(input('If you are unsure what to type to access the correct game, restart the program and choose option 4 (Type exit to close program and then start it again).\nWhen asked which game you would like to change, simply enter the word that is present above the title segment of the specific game.\nWhich game woud you like to change? '))
            game_id = game_id.lower()
            if game_id == 'exit':
                exit()
            attribute = str(input('Choose the attribute you want to update: players/duration/age: '))
            attribute = attribute.lower()
            new_value = input('New value: ')
            new_value = new_value.title()
            boardgame_list[game_id][attribute] = new_value
            #print(boardgame_list)
        with open('boardgamee.json', 'w') as list_of_games:
            json.dump(boardgame_list, list_of_games)

    elif choice == 5:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            game_id = str(input("Which game do you want to remove? "))
            del boardgame_dict[game_id]
        with open('boardgamee.json', 'w') as list_of_games:
            json.dump(boardgame_dict, list_of_games)
            print(game_id.title(), "was successfully removed")

    elif choice == 6:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            boardgame_df = pd.DataFrame(boardgame_dict)
            boardgame_df = boardgame_df.T
            boardgame_df[['players', 'duration', 'age']] = boardgame_df[['players', 'duration', 'age']].apply(pd.to_numeric)
            inp_players = int(input('How many players are you? '))
            inp_duration = int(input('For how long do you want to play? Answer in minutes: '))
            inp_age = int(input("How old is the youngest player in your group? "))
            #print(boardgame_df)
            print(boardgame_df[boardgame_df.age >= inp_age])#[boardgame_df.duration >= 8][boardgame_df.players ])

    elif choice == 7:
        exit()

    else:
        print('Choose an alternative between 1 and 7')