from flask import Flask,jsonify
import database as db
from mongoflask import MongoJSONEncoder
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.json_encoder = MongoJSONEncoder
@app.route('/')
def welcome():
    return jsonify({"message":"Hello World"})

@app.route('/ipl/teamLables')
def team_names():
    lables = db.get_team_names()
    return jsonify({"label":lables})

@app.route('/ipl/teamDetails')
def team_details():
    teams = db.get_team_details()
    return jsonify({"team":teams})

@app.route('/ipl/players')
def players():
    players = db.get_all_players()
    return jsonify({"Player":players})

# ---------------------

@app.route('/ipl/team/<teamname>')
def team_players(teamname):
    players = db.get_team_players(teamname)
    return jsonify({"players":players})

@app.route('/ipl/count/<teamname>')
def players_count(teamname):
    count = db.get_count_role(teamname)
    return jsonify({"count":count})

@app.route('/ipl/rolecount')
def role_count():
    count = db.get_players_role_count_ipl()
    return jsonify({"count":count})

@app.route('/ipl/stat/<teamname>')
def stat(teamname):
    stat = db.get_stat_team(teamname)
    return jsonify({"stat":stat})

@app.route('/ipl/stat_ipl')
def stat_ipl():
    stat = db.get_stat_ipl()
    return jsonify({"stat":stat})

    
if __name__ == '__main__':
    app.run()