from flask import Flask,jsonify
import database as idb
from mongoflask import MongoJSONEncoder

app = Flask(__name__)
app.json_encoder = MongoJSONEncoder

@app.route("/")
def hello():
    return "Hello world"

@app.route("/labels")
def get_team_label():
    labels  = idb.get_team_labels()
    return jsonify({"labels" : labels})

@app.route("/teams")
def get_teams():
    teams = idb.get_all_team_details()
    return jsonify({"teams": teams})

@app.route("/teams/<teamname>")
def get_team_by_id(teamname):
    teamMembers = idb.get_team_players(teamname)
    return jsonify({"players" : teamMembers})

@app.route("/players/<teamname>")
def get_players_num(teamname):
    player_info = idb.get_players_nums(teamname)
    return jsonify({"info" : player_info})

@app.route("/allcount")
def get_all_nums():
    nums = idb.get_all_player_nums()
    return jsonify(nums)

@app.route("/allstats")
def get_all_stats():
    nums = idb.get_stats()
    return jsonify({"Stats" : nums})

@app.route("/stats/<teamname>")
def get_all_stats_by_team(teamname):
    nums = idb.get_stats_by_team(teamname)
    return jsonify({"Stats" : nums})

if __name__ == "__main__":
    app.run(debug=True)