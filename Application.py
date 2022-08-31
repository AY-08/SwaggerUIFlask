from crypt import methods
from unittest import result
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime
import Models
# import serialization

# instantiate flask object
app = Flask(__name__)

# set app configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# flask swagger configs
SWAGGER_URL = ''
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Store API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# create db instance
db = SQLAlchemy(app)

# instanctiate ma
ma = Marshmallow(app)


class RoleSchema(ma.Schema):
    class Meta:
        fields = ('role_id', 'role_name')

role_schema = RoleSchema(many=True)




@app.route('/api/role', methods = ['GET'])
def getrole():
    roleid =[]

    query = db.session.query(Models.Role)
    result_set = role_schema.dump(query)
    return jsonify(result_set)

@app.route('/api/role/<int:id>')
def getroleid(id):
    roledeatils = []
    query = db.session.query(Models.Role).filter(Models.Role.role_id == id)
    print(query)
    result_set = role_schema.dump(query)
    return jsonify(result_set)


if __name__=='__main__':

    app.run(port=5000,debug=True) 

# Now point your browser to localhost:5000/api/docs/

