from flask import Flask,jsonify
import database as idb
from mongoflask import MongoJSONEncoder

app = Flask(__name__)
app.json_encoder = MongoJSONEncoder

@app.route("/")
def hello():
    return "Hello world"

@app.route("/IPL/Label")
def get_team_label():
    labels  = idb.get_team_labels()
    return jsonify({"labels" : labels})

@app.route("/IPL/Teams")
def get_teams():
    teams = idb.get_all_team_details()
    return jsonify({"teams": teams})

@app.route("/IPL/Teams/<teamname>")
def get_team_by_id(teamname):
    teamMembers = idb.get_team_players(teamname)
    return jsonify({"players" : teamMembers})

@app.route("/IPL/Players/<teamname>")
def get_players_num(teamname):
    player_info = idb.get_players_nums(teamname)
    return jsonify({"info" : player_info})

@app.route("/IPL/ALL")
def get_all_nums():
    nums = idb.get_all_player_nums()
    return jsonify(nums)

@app.route("/IPL/AllStats")
def get_all_stats():
    nums = idb.get_stats()
    return jsonify({"Stats" : nums})

@app.route("/IPL/AllStats/<teamname>")
def get_all_stats_by_team(teamname):
    nums = idb.get_stats_by_team(teamname)
    return jsonify({"Stats" : nums})

if __name__ == "__main__":
    app.run(debug=True)