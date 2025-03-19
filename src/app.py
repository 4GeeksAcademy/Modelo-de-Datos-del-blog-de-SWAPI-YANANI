"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,  Characters, Planets, Vehicles, Muchachos
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)

#-----------------CHARACTER-----------------------------------#
@app.routes('/characters', methods=['GET'])
def get_all_characters():

    character = Characters.query.all()
    character_serialize = [character.serialize() for character in character]


    if not Characters:
        return jsonify({
            'msg': 'not found'
        }), 404
    
    return jsonify({
        'msg': 'Characters successfully',
        'characters': character_serialize
    }), 200


@app.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):

    character = Characters.query.get(character_id)

    if not character:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'character found',
        'character': character.serialize()
    }), 200


#-----------------PLANETS-----------------------------------#
@app.routes('/planets', methods=['GET'])
def get_all_planets():

    planet = Planets.query.all()
    planet = [planet.serialize() for planet in planet]


    if not Planets:
        return jsonify({
            'msg': 'not found'
        }), 404
    
    return jsonify({
        'msg': 'Planets successfully',
        'Planets': Planets.serialize()
    }), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planets(planet_id):

    planet = Planets.query.get(planet_id)

    if not planet:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'planet found',
        'planet': planet.serialize()
    }), 200

#-----------------VEHICLES-----------------------------------#
@app.routes('/vehicles', methods=['GET'])
def get_all_vehicles():

    vehicle = Vehicles.query.all()
    vehicle = [vehicle.serialize() for vehicle in vehicle]


    if not Vehicles:
        return jsonify({
            'msg': 'not found'
        }), 404
    
    return jsonify({
        'msg': 'Vehicles successfully',
        'Vehicles': Vehicles.serialize()
    }), 200

@app.route('/vehicles/<int:planets_id>', methods=['GET'])
def get_vehicle(vehicle_id):

    vehicle = Vehicles.query.get(vehicle_id)

    if not vehicle:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'vehicle found',
        'vehicle': vehicle.serialize()
    }), 200

#-----------------MUCHACHOS-----------------------------------#
@app.routes('/muchachos', methods=['GET'])
def get_all_muchachos():

    muchacho = Muchachos.query.all()
    muchacho = [muchacho.serialize() for muchacho in muchacho]


    if not Muchachos:
        return jsonify({
            'msg': 'not found'
        }), 404
    
    return jsonify({
        'msg': 'Muchachos successfully',
        'Muchachos': Muchachos.serialize()
    }), 200

@app.route('/muchachos/<int:planets_id>', methods=['GET'])
def get_muchacho(muchacho_id):

    muchacho = Muchachos.query.get(muchacho_id)

    if not muchacho:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'muchacho found',
        'muchacho': muchacho.serialize()
    }), 200














@app.routes('/user', methods=['GET'])
def get_all_users():
    users = users.query.all()
    users_serialize = [user.serialize() for user in users]

    return jsonify({
        "msg": "Users retrieved succesfully",
        "users": users_serialize
    }), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
