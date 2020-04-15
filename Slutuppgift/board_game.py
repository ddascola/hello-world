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
        #self.game_dict = {}
        


    def add_game(self, title, players, duration, age):
        temp_game = Game(title, int(players), int(duration), int(age))
        #self.game_list.append(temp_game)
        self[title] = temp_game
        #cabinet.game_list.append(cabinet)
        
        #with open('boardgamee.json', 'a') as list_of_games:
            #json.dump(cabinet.game_dict, list_of_games)

    def remove_game(self, title):
        for i, game in enumerate(self.game_list):
            if game.title == title:
                del self.game_list[i]
                break
        
            

cabinet = Game_cabinet()
#def game_menu(games):
choice = 0
while choice != 6:
    choice = int(input("1.Add new game\n2.Show list of games\n3.Save your newly added games\n4.Show list of games from file\n5.Remove a game\nMake your choice: "))
    if choice == 1:
        print("Please enter title, recommended amount of players, duration in minutes and minimum age for the game")
        title = input("Title: ")
        #title = "monopol"
        players = int(input("Recommended amount of players: "))
        #players = int(4)
        duration = int(input("Duration of game in minutes: "))
        #duration = int(75)
        age = int(input("Minimum age for the game: "))
        #age = int(13)

        cabinet.add_game(title, players, duration, age)
        
        
    elif choice == 2:
        for game in cabinet.game_dict:
            print(f"Title: {game.title}, Players: {game.players}, Duration: {game.duration}, Age: {game.age}")

    elif choice == 3:
        with open('boardgamee.json', 'a') as list_of_games:
            #boardgame_dict = json.load(list_of_games)
            #boardgame_dict.append(cabinet)
            json.dump(cabinet, list_of_games)


    elif choice == 4:
        with open('boardgamee.json', 'r') as list_of_games:
            boardgame_dict = json.load(list_of_games)
            print(boardgame_dict)
        

    elif choice == 5:
        with open('boardgame.csv', newline= "") as list_of_games:
            complete_list = list(csv.reader(list_of_games))
            cabinet.game_list.extend(complete_list)
            title = str(input("Which game would you like to delete? "))
            title = title.title()
            remove_game(title)
        with open('boardgame.csv', 'w', newline = "") as list_of_games:
            wr = csv.writer(list_of_games, quoting = csv.QUOTE_NONE)
            wr.writerow(cabinet.game_list)
            


print(cabinet.game_dict)
print(cabinet.game_list)










    

