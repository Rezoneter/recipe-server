from flask_restful import Resource
from mysql_connection import get_connection
from mysql.connector import Error
from flask import request

class UserRegisterResource(Resource):
    
    def post(self):
        return


