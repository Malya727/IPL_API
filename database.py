import pymongo
myclient = pymongo.MongoClient("mongodb+srv://react:react@react-pmnjq.mongodb.net/test?retryWrites=true&w=majority")

db = myclient.IPL_2020


def get_team_names():
    collection = db.Team_Details
    teamLabels = []
    for x in collection.find({},{'_id':0,'label':1}):
        teamLabels.append(x['label'])
    return teamLabels

def get_team_details():
    collection = db.Team_Details
    teamList = []
    for x in collection.find({}):
        teamList.append(x)
    return teamList

def get_all_players():
    collection = db.Player_Details
    playersList = []
    for x in collection.find({}):
        playersList.append(x)
    return playersList

def get_team_players(teamName):
    collection = db.Player_Details 
    players = []
    for x in collection.find({"label":teamName}):
        players.append(x)
    return players

def get_count_role(teamName):
    collection = db.Player_Details
    count = []
    for x in collection.aggregate([{'$match':{"label":teamName}},{'$group':{'_id':{"role":"$role","team":"$label"},'count':{'$sum':1}}},{'$project':{"role":"$_id.role",'count':1,'_id':0}},{'$sort':{"team":1}}]):
        count.append(x)
    return count

def get_players_role_count_ipl():
    collection = db.Player_Details
    role_count = []
    for x in collection.aggregate([{"$group":{"_id":"$role","count":{"$sum":1}}},{"$project":{"role":"$_id","count":1,"_id":0}}]):
        role_count.append(x)
    return role_count
    

def get_stat_team(teamname):
    collection = db.Player_Details
    stat = []
    for x in collection.aggregate([{"$match":{"label":teamname}},{"$group":{"_id":"$role","Max":{"$max":"$price"},"Min":{"$min":"$price"},"Avg":{"$avg":"$price"},"Total":{"$sum":"$price"}}},{"$project":{"role":"$_id","_id":0,"Max":1,"Min":1,"Avg":1,"Total":1}}]):
        stat.append(x)
    return stat
    

def get_stat_ipl():
    collection = db.Player_Details
    stat = []
    for x in collection.aggregate([{"$group":{"_id":"$role","count":{"$sum":1},"Max":{"$max":"$price"},"Min":{"$min":"$price"},"Avg":{"$avg":"$price"},"Total":{"$sum":"$price"}}},{"$project":{"role":"$_id","_id":0,"Max":1,"Min":1,"Avg":1,"Total":1,"count":1}}]):
        stat.append(x)
    return stat