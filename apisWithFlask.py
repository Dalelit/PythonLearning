from flask import Flask
from flask import request
from json import dumps

active_games = dict()

app = Flask(__name__)

class battle_ship_board_specs:
    def __init__(self):
        self.rows = 10
        self.columns = 10
        self.boats = [5,4,3,3,2]

    def json_str(self):
        return dumps(self.__dict__)

specs = battle_ship_board_specs()


class battle_ship_board_game:

    def place_boats(self, boat_specs):
        x = y = 0
        for boat in boat_specs:
            self.boats.append(((x,y), (x,y+boat-1), False))
            x+=1

    def __init__(self, specs, id):
        self.id = id
        self.boats = list()
        self.place_boats(specs.boats)
        self.player1 = ''
        self.player2 = ''

        active_games[self.id.lower()] = self

    def status_info(self):
        d = dict()
        d['id'] = self.id
        d['player1'] = self.player1
        d['player2'] = self.player2
        return d

    def json_str(self):
        return dumps(self.__dict__)

@app.route('/')
def hello_world():
    return 'Hello battle ships'

@app.route('/specs')
def game_specs():
    return dumps(specs.json_str())

def generate_game_name():
    return f"Game{active_games.__len__()+1}"

@app.route('/newgame')
def new_game():
    game = battle_ship_board_game(specs, generate_game_name())
    return game.json_str()

@app.route('/availablegames')
def available_games():
    games = [v.status_info() for k,v in active_games.items() if v.player1 == '' or v.player2 == '']
    return dumps(games)

@app.route('/allgames')
def all_games():
    games = [v.status_info() for k,v in active_games.items()]
    return dumps(games)

@app.route('/games/<gameid>')
def access_game(gameid):
    gid = gameid.lower()

    if not active_games.__contains__(gid):
        print('Error - game not found')
        return 'No game exists'

    return dumps(active_games[gid].status_info())

@app.route('/games/<gameid>/join')
def join_game(gameid):
    print(f'Joining game {gameid}')
    gid = gameid.lower()

    if not active_games.__contains__(gid):
        print('Error - game not found')
        return 'No game exists'

    game = active_games[gid]

    player = request.args['player']
    if player:
        print(f'Player {player} joining')
        if not game.player1:
            game.player1 = player
        elif not game.player2:
            game.player2 = player
        else:
            print('Error - no free player spot')
            return 'No free player spot'
    else:
        print('Could not find player name')
        return 'No player arg'

    return dumps(game.status_info())

if __name__ == '__main__':

    # print(specs.json_str())
    
    new_game()
    g = battle_ship_board_game(specs, generate_game_name())
    battle_ship_board_game(specs, generate_game_name())

    g.player1 = "Joe"
    g.player2 = "Bob"

    print("Available games...")
    print(available_games())

    print("All games...")
    print(all_games())

    print("One game")
    print(access_game('Game2'))


