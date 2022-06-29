from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.game import Games

# @app.route('/review/<int:id>')
# def show_games(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":id
#     }
#     user_data = {
#         "id":session['user_id']
#     }
#     return render_template("dashboard.html",games=Games.get_all(data),user=User.get_by_id(user_data))