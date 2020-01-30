from flask import Flask,jsonify
import ipldb as idb
from mongoflask import MongoJSONEncoder
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.json_encoder = MongoJSONEncoder

@app.route('/')
def index():
    return jsonify({"message":"Hello We are learning Flask"})

@app.route('/ipl/labels')
def team_labels():
    labels = idb.get_team_labels()
    return jsonify({"labels":labels})

@app.route('/ipl/teams')
def team_details():
    team_details = idb.get_all_team_details()
    return jsonify({"teams":team_details})

@app.route('/ipl/players')
def players():
    players = idb.get_all_players()
    return jsonify({"players":players})

@app.route('/ipl/team/<teamname>')
def team_players(teamname):
    players = idb.get_team_players(teamname)
    return jsonify({"players":players})
@app.route("/ipl/team/rolestat/<teamname>")
def team_role_count(teamname):
    team_count = idb.get_players_role_count_by_team(teamname)
    return jsonify({"stat":team_count})

@app.route("/ipl/team/pricestat/<teamname>")
def team_income_stats(teamname):
    stat = idb.get_stat_team(teamname)
    return jsonify({"stat":stat})

@app.route("/ipl/team/<label>/<teamname>")
def get_player_by_role_by_team(label,teamname):
    players = idb.get_players_by_role_by_team(label,teamname)
    return jsonify({"players":players})

@app.route("/ipl/team/avgsalipl")
def all_team_stat():
    stat = ""
    return jsonify({"stat":stat})
    


if __name__ == "__main__":
    app.run()