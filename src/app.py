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
from models import db, User,  Characters, Planets, Vehicles, Muchachos, Favorite
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

#-----------------CHARACTERS------------------------------------------------------------------------#
@app.route('/characters', methods=['GET'])
def get_all_characters():

    characters = Characters.query.all()  
    characters_serialize = [character.serialize() for character in characters]

    if not characters:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'Characters successfully retrieved',
        'characters': characters_serialize
    }), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):

    character = Characters.query.get(character_id)

    if not character:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'Character found',
        'character': character.serialize()
    }), 200


#-----------------PLANETS--------------------------------------------------------------------------#
@app.route('/planets', methods=['GET'])
def get_all_planets():

    planets = Planets.query.all()
    planets_serialize = [planet.serialize() for planet in planets]

    if not planets:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'Planets successfully retrieved',
        'planets': planets_serialize
    }), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    planet = Planets.query.get(planet_id)

    if not planet:
        return jsonify({
            'msg': 'Not found'
        }), 404

    return jsonify({
        'msg': 'Planet found',
        'planet': planet.serialize()
    }), 200


#-----------------USERS Y FAVORITES------------------------------------------------------------------#
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_serialize = [user.serialize() for user in users]

    return jsonify({
        "msg": "Users retrieved successfully",
        "users": users_serialize
    }), 200


@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user_id = request.args.get('user_id') 

    if not user_id:
        return jsonify({
            'msg': 'User ID is required'
        }), 400

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            'msg': 'User not found'
        }), 404

    favorites = Favorite.query.filter_by(user_id=user.id).all()
    favorites_serialize = [favorite.serialize() for favorite in favorites]

    return jsonify({
        'msg': 'Favorites successfully retrieved',
        'favorites': favorites_serialize
    }), 200


@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = request.args.get('user_id')  
    if not user_id:
        return jsonify({
            'msg': 'User ID is required'
        }), 400

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            'msg': 'User not found'
        }), 404

    planet = Planets.query.get(planet_id)

    if not planet:
        return jsonify({
            'msg': 'Planet not found'
        }), 404

    # ------------Verificar si el planeta ya es un favorito del usuario (ESTO LO PROPUSO GPT Y NO LE VOY A DECIR QUE NO)------------
    existing_favorite = Favorite.query.filter_by(user_id=user.id, planet_id=planet.id).first()

    if existing_favorite:
        return jsonify({
            'msg': 'Planet already in favorites'
        }), 400

   
    new_favorite = Favorite(user_id=user.id, planet_id=planet.id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({
        'msg': 'Planet added to favorites successfully'
    }), 200


@app.route('/favorite/character/<int:character_id>', methods=['POST'])
def add_favorite_character(character_id):
    user_id = request.args.get('user_id')  

    if not user_id:
        return jsonify({
            'msg': 'User ID is required'
        }), 400

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            'msg': 'User not found'
        }), 404

    character = Characters.query.get(character_id)

    if not character:
        return jsonify({
            'msg': 'Character not found'
        }), 404

    
    existing_favorite = Favorite.query.filter_by(user_id=user.id, characters_id=character.id).first()

    if existing_favorite:
        return jsonify({
            'msg': 'Character already in favorites'
        }), 400

    
    new_favorite = Favorite(user_id=user.id, characters_id=character.id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({
        'msg': 'Character added to favorites successfully'
    }), 200


@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def remove_favorite_planet(planet_id):
    user_id = request.args.get('user_id')  
    if not user_id:
        return jsonify({
            'msg': 'User ID is required'
        }), 400

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            'msg': 'User not found'
        }), 404

    favorite = Favorite.query.filter_by(user_id=user.id, planet_id=planet_id).first()

    if not favorite:
        return jsonify({
            'msg': 'Favorite planet not found'
        }), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({
        'msg': 'Planet removed from favorites successfully'
    }), 200


@app.route('/favorite/character/<int:character_id>', methods=['DELETE'])
def remove_favorite_character(character_id):
    user_id = request.args.get('user_id')  

    if not user_id:
        return jsonify({
            'msg': 'User ID is required'
        }), 400

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            'msg': 'User not found'
        }), 404

    favorite = Favorite.query.filter_by(user_id=user.id, characters_id=character_id).first()

    if not favorite:
        return jsonify({
            'msg': 'Favorite character not found'
        }), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({
        'msg': 'Character removed from favorites successfully'
    }), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
