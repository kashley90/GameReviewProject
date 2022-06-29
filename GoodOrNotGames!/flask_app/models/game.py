from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Games:
    db_name = 'mydb'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.images= db_data['images']
        self.game_title = db_data['game_title']
        self.description = db_data['description']
        self.total_score = db_data['total_score']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO games (images, game_title, description, total_score) VALUES ((%(images)s,%(game_title)s,%(description)s,%(total_score)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM games;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_games = []
        for row in results:
            all_games.append( cls(row) )
        return all_games
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM games WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE games SET total_score=%(total_score)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)



# All below for game_reviews
    