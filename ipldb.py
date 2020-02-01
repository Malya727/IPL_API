from pymongo import MongoClient

uri = "mongodb+srv://db_user:db_user@cluster0-bmww9.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client.ipl2020

def get_team_labels():
    collection = db.iplteam
    labelList = []
    for x in collection.find({},{"_id":0,"label":1}):
        labelList.append(x["label"])
    return labelList

def get_all_team_details():
    collection = db.iplteam
    teamList = []
    for x in collection.find({}):
        teamList.append(x)
    return teamList

def get_all_players():
    collection = db.player
    players = []
    for x in collection.find({}):
        players.append(x)
    return players

def get_team_players(teamName):
    collection = db.player
    players = []
    for x in collection.find({"label":teamName}):
        players.append(x)
    return players

def get_players_role_count_by_team(teamName):
    collection = db.player
    x = collection.aggregate([
        {"$match":{"label":teamName}},
        {"$group":{"_id":"$role","count":{"$sum":1}}},
        {"$project":{"role":"$_id","count":1,"_id":0}}
    ])
    return [i for i in x]   
def get_players_role_count_ipl():
    pass
# min, max, avg, total salary of the team
def get_stat_team(teamname):
    collection = db.player
    res = collection.aggregate([
        {"$match":{"label":teamname}},
        {"$group":
            {
                "_id":"$label",
                "total":{"$sum":"$price"},
                "max":{"$max":"$price"},
                "min":{"$min":"$price"},
                "avg":{"$avg":"$price"}
            }
        },
    ])
    return [i for i in res]
# min, max, avg, total salary of the ipl2020
def get_stat_ipl():
    collection = db.player
    res = collection.aggregate([
        {"$group":{"_id":"$label","total":{"$sum":"$price"},"max":{"$max":"$price"},"min":{"$min":"$price"},"avg":{"$avg":"$price"}}},
    ])
    return [i for i in res]


def get_players_by_role_by_team(role,teamName):
    collection = db.player
    res = collection.find({"role":role,"label":teamName})
    return [ x for x in res]

def ipl_team_stat():
    collection=db.player
    res = collection.aggregate([
        {"$group":{"_id":"$label","amount":{"$sum":"$price"}}},
        {"$project":{"team":"$_id","amount":1,"_id":0}}
    ])
    return [r for r in res]

def stat_role_price_by_team(teamname):
    collection=db.player
    res = collection.aggregate([
        {"$match":{"label":teamname}},
        {"$group":{"_id":"$role","amount":{"$sum":"$price"}}},
        {"$project":{"role":"$_id","amount":1,"_id":0}}
    ])
    return [r for r in res]

def sort_player_by_price():
    collection=db.player
    res = collection.find().sort("price",-1)
    return [r for r in res]


