from app import app
from flask import jsonify
from app.service import userservice


@app.route('/users')
def get_users():
    return jsonify(userservice.get_users())
