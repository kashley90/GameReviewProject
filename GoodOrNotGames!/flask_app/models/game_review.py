from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Reviews:
    db_name = 'mydb'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.user_id = db_data['user_id']
        self.game_id = db_data['game_id']
        self.review = db_data['review']
        self.score = db_data['score']
        self.reviewer = None
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_all_reviews(cls,data):
        query = "SELECT * FROM game_reviews WHERE game_id=%(game_id)s;"
        results =  connectToMySQL(cls.db_name).query_db(query,data)
        all_reviews = []
        for row in results:
            print(row['review'])
            all_reviews.append( cls(row) )
        return all_reviews


    @classmethod
    def get_all_reviews_with_users(cls,data):
        query ="""SELECT * FROM game_reviews 
        LEFT JOIN users ON game_reviews.user_id=users.id
        WHERE game_id=%(game_id)s;"""
        results =  connectToMySQL(cls.db_name).query_db(query,data)
        all_reviews = []
        for row in results:
            current_review=( cls(row) )
            user_data={
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            current_review.reviewer = user.User(user_data)
            all_reviews.append(current_review)
        return all_reviews

    @classmethod
    def get_one_review(cls,data):
        query = "SELECT * FROM game_reviews WHERE id=%(id)s;"
        results =  connectToMySQL(cls.db_name).query_db(query,data)
        # one_review = results[0]
        return cls(results[0])

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM game_reviews;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_reviews = []
        for row in results:
            print(row['review'])
            all_reviews.append( cls(row) )
        return all_reviews

    @classmethod
    def save(cls,data):
        query = "INSERT INTO game_reviews (user_id,game_id,review,score) VALUES (%(user_id)s,%(game_id)s,%(review)s,%(score)s);"
        return  connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE game_reviews SET review=%(review)s, score=%(score)s, updated_at=NOW() WHERE id = %(game_id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM game_reviews WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_review(review):
        is_valid = True
        if len(review['review']) < 10:
            is_valid = False
            flash("Description must be at least 10 characters","review")
        if len(review['score']) < 1  >= 10:
            is_valid = False
            flash("Number must be at least 1 and no more than 10","review")
        return is_valid
