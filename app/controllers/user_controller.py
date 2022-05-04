from enum import auto
from http import HTTPStatus
from lib2to3.pgen2 import token

import secrets
from flask import jsonify, request
from app.configs.auth import auth
from app.models.user_model import UserModel
from app.configs.database import db
from sqlalchemy.orm import Query, Session
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)


def create_user():
    data = request.get_json()

    data["api_key"] =secrets.token_urlsafe(128)
    
    user:UserModel = UserModel(**data)

    db.session.add(user)
    db.session.commit()

    return jsonify(user), HTTPStatus.OK

def login_user():
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data['email']).first()
    
    if not user or not user.check_password(data['password']):
        return{'MsgError':'Email ou senha errada'}, 401

    response = create_access_token(user)

    return jsonify({"token":response}), 200

#@auth.login_required
@jwt_required()
def list_user():

    users : UserModel = UserModel.query.all()

    return jsonify(users)

#@auth.login_required
@jwt_required()
def update_user():
    session:Session = db.session

    #data = request.get_json()
    #apy_key = request.headers['AUTHORIZATION']
    #apy_key = apy_key.replace("Bearer ", "", 1)
  
    user : Query = (
        session.query(UserModel)
        .filter(UserModel.api_key == apy_key
        )).update({
            UserModel.email: data["email"],
            UserModel.name: data["name"],
            UserModel.last_name: data["last_name"],
        })

    session.commit()
    print(user)

    return jsonify(user), 200

#@auth.login_required
@jwt_required()
def delete_user():
    session:Session = db.session

    #data = request.get_json()
    #apy_key = request.headers['AUTHORIZATION']
    #apy_key = apy_key.replace("Bearer ", "", 1)
  
    user : Query = (
        session.query(UserModel)
        .filter(UserModel.api_key == apy_key).first()
        )

    session.delete(user)
    session.commit()

    return '', 200