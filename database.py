import pymongo

myclient = pymongo.MongoClient("mongodb+srv://react:react@react-pmnjq.mongodb.net/test?retryWrites=true&w=majority")

db = myclient.IPL_2020

#Returns all the lables of teams
def get_team_labels():
    collection = db.Team_Details
    label = [x["label"] for x in collection.find({},{"_id":0,"label" : 1})]
    return label

#Returns all the team details
def get_all_team_details():
    collection = db.Team_Details
    teams = [x for x in collection.find({},)]
    return teams

#Returns all players
def get_all_players():
    collection = db.Player_Details
    players = [i for i in collection.find({})]
    return players

#Returns all the players who has label teamName
def get_team_players(teamName):
    collection = db.Player_Details
    players = [i for i in collection.find({"label": teamName})]
    return players

def get_players_nums(teamname):
    collection = db.Player_Details
    res = collection.aggregate([
        {"$match" : {"label" : teamname}},
        {"$group" : {"_id":"$role","total" : {"$sum" : 1}} },
        #{"$project" : {"Role" : "$_id", "total" : 1}}
    ])
    return [x for x in res]

def get_all_player_nums():
    collection = db.Player_Details
    res = collection.aggregate([
        {"$group" : {"_id":{"role" : "$role","team": "$label"},"total" : {"$sum" : 1}} },
        {"$project" : {"Role" : "$_id.role","Team":"$_id.team", "total" : 1,"_id":0}}
    ])
    return [x for x in res]
#teams stats max,min,avg,total salary

def get_stats():
    collection = db.Player_Details
    res = collection.aggregate([
        {"$group" : {"_id":"","max" : {"$max" : "$price"},"min" : {"$min" : "$price"},"avg" : {"$avg" : "$price"},"total" : {"$sum" : "$price"}} },
        {"$project" : {"max":1,"min":1,"avg":1,"total" : 1,"_id":0}}
    ])
    return [x for x in res]

def get_stats_by_team(teamname):
    collection = db.Player_Details
    res = collection.aggregate([
        {"$match" : {"label" : teamname}},
        {"$group" : {"_id":"$label","max" : {"$max" : "$price"},"min" : {"$min" : "$price"},"avg" : {"$avg" : "$price"},"total" : {"$sum" : "$price"}} },
        {"$project" : {"team":"$_id","max":1,"min":1,"avg":1,"total" : 1,"_id":0}}
    ])
    return [x for x in res]

