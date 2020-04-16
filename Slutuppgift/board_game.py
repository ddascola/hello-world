import pickle
import json
import numpy as np
import pandas as pd
import csv
class Game(dict):
    def __init__ (self, title, players, duration, age):
        self['title'] = title.title()
        self['players'] = players
        self['duration'] = duration
        self['age'] = age
        #self.__dict__ = game_dict
    
    def set_title(self, title):
        self.title = title.title()
    
    def set_players(self, players):
        self.players = players
    
    def set_duration(self, duration):
        self.duration = duration
    
    def set_age(self, age):
        self.age = age

    def __repr__(self):
        return "Game title:% s players:% s duration:% s age:% s" % (self.title, self.players, self.duration, self.age)


class Game_cabinet(dict):
    def __init__(self):
        self.game_list = []
        self.game_dict = {}
        


    def add_game(self, title, players, duration, age):
        temp_game = Game(title, int(players), int(duration), int(age))
        #self.game_list.append(temp_game)
        self[title] = temp_game

    def remove_game(self, title):
        for i, game in enumerate(self.game_list):
            if game.title == title:
                del self.game_list[i]
                break
        
            

cabinet = Game_cabinet()
choice = 0
while choice != 8:
    choice = int(input("1.Add new game\n2.Show list of games\n3.Save your newly added games\n4.Show list of games from file\n5.Make changes to a game\n6.Remove a game\nMake your choice: "))
    if choice == 1:
        print("Please enter title, recommended amount of players, duration in minutes and minimum age for the game")
        title = input("Title: ")
        players = int(input("Recommended amount of players: "))
        duration = int(input("Duration of game in minutes: "))
        age = int(input("Minimum age for the game: "))

        cabinet.add_game(title, players, duration, age)
        
        
    elif choice == 2:
        for game in cabinet.game_dict:
            print(f"Title: {game.title}, Players: {game.players}, Duration: {game.duration}, Age: {game.age}")
        

    elif choice == 3:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            boardgame_dict.update(cabinet)
        with open('boardgamee.json', 'w') as list_of_games:
            json.dump(boardgame_dict, list_of_games)


    elif choice == 4:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            print (json.dumps(boardgame_dict, indent=2))
        

    elif choice == 5:
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

    elif choice == 6:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            game_id = str(input("Which game do you want to remove? "))
            del boardgame_dict[game_id]
        with open('boardgamee.json', 'w') as list_of_games:
            json.dump(boardgame_dict, list_of_games)
            print(game_id.title(), "was successfully removed")

    elif choice == 7:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            boardgame_df = pd.DataFrame(boardgame_dict)
            boardgame_df = boardgame_df.T
            boardgame_df[['players', 'duration', 'age']] = boardgame_df[['players', 'duration', 'age']].apply(pd.to_numeric)
            #print(boardgame_df)
            print(boardgame_df[boardgame_df.age >= 7])









    

