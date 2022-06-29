from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.game_review import Reviews
from flask_app.models.game import Games
from flask_app.models.user import User


@app.route('/new/review/<int:id>')
def new_review(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id,
    }
    user_data={
        "id":session["user_id"]
    }
    return render_template('new_review.html',user=User.get_by_id(user_data),game=Games.get_one(data))


@app.route('/create/review',methods=['POST'])
def create_review():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Reviews.validate_review(request.form):
        return redirect('/new/Review')
    data = {
        "review": request.form["review"],
        "score": int(request.form["score"]),
        "user_id": session["user_id"],
        "game_id": request.form["game_id"]
    }
    Reviews.save(data)
    return redirect('/dashboard')

@app.route('/edit/review/<int:id>')
def edit_review(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_review.html",review=Reviews.get_one_review(data),user=User.get_by_id(user_data))

@app.route('/update/review',methods=['POST'])
def update_review():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Reviews.validate_review(request.form):
        return redirect('/new/review')
    data = {
        "review": request.form["review"],
        "score": int(request.form["score"]),
        "user_id": session["user_id"],
        "game_id": request.form["game_id"],
        # "id": request.form["game_id"]
    }
    id=Reviews.update(data)
    return redirect('/dashboard')

@app.route('/review/<int:id>')
def show_review(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "game_id":id
    }
    user_data = {
        "id":session['user_id']
    }
    Reviews.get_all_reviews
    return render_template("show_reviews.html",reviews=Reviews.get_all_reviews_with_users(data),user=User.get_by_id(user_data))

@app.route('/destroy/review/<int:id>')
def destroy_review(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Reviews.destroy(data)
    return redirect('/dashboard')