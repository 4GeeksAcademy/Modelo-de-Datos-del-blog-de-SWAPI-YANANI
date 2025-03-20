from app import app, db
from models import User, Characters, Planets, Vehicles, Muchachos, Favorite

with app.app_context():
    # Datos para la tabla User
    users = [
        User(username="skywalker", password="force123",
             email="luke@jedi.com", firstname="Luke", lastname="Skywalker"),
        User(username="vader", password="darkside",
             email="vader@sith.com", firstname="Darth", lastname="Vader"),
        User(username="yoda", password="wisdom", email="yoda@jedi.com",
             firstname="Master", lastname="Yoda"),
        User(username="solo", password="falcon",
             email="han@smuggler.com", firstname="Han", lastname="Solo"),
        User(username="leia", password="rebel", email="leia@republic.com",
             firstname="Leia", lastname="Organa")
    ]

    # Datos para la tabla Characters
    characters_1 = [
        Characters(name="Luke Skywalker", birth_year="19BBY", eye_color="Blue", gender="Male",
                   hair_color="Blond", height="172", url="https://swapi.dev/api/people/1/"),
        Characters(name="Darth Vader", birth_year="41.9BBY", eye_color="Yellow", gender="Male",
                   hair_color="None", height="202", url="https://swapi.dev/api/people/4/"),
        Characters(name="Leia Organa", birth_year="19BBY", eye_color="Brown", gender="Female",
                   hair_color="Brown", height="150", url="https://swapi.dev/api/people/5/"),
        Characters(name="Yoda", birth_year="896BBY", eye_color="Green", gender="Male",
                   hair_color="White", height="66", url="https://swapi.dev/api/people/20/"),
        Characters(name="Obi-Wan Kenobi", birth_year="57BBY", eye_color="Blue", gender="Male",
                   hair_color="Auburn", height="182", url="https://swapi.dev/api/people/10/")
    ]

    # Datos para la tabla Planets
    planets = [
        Planets(name="Tatooine", climate="Arid", rotation_time="23",
                diameter="10465", gravity="1 standard"),
        Planets(name="Hoth", climate="Frozen", rotation_time="24",
                diameter="7200", gravity="1.1 standard"),
        Planets(name="Dagobah", climate="Swamp",
                rotation_time="23", diameter="8900", gravity="N/A"),
        Planets(name="Endor", climate="Temperate", rotation_time="18",
                diameter="4900", gravity="0.85 standard"),
        Planets(name="Naboo", climate="Temperate", rotation_time="26",
                diameter="12120", gravity="1 standard")
    ]

    # Datos para la tabla Vehicles
    vehicles = [
        Vehicles(name="X-Wing", model="T-65B", vehicle_type="Starfighter", length="12.5",
                 value="150000", fuel_capacity="500", url="https://swapi.dev/api/vehicles/14/"),
        Vehicles(name="TIE Fighter", model="Twin Ion Engine", vehicle_type="Starfighter",
                 length="8.99", value="75000", fuel_capacity="300", url="https://swapi.dev/api/vehicles/21/"),
        Vehicles(name="Millennium Falcon", model="YT-1300", vehicle_type="Freighter", length="34.75",
                 value="200000", fuel_capacity="1000", url="https://swapi.dev/api/vehicles/10/"),
        Vehicles(name="AT-AT", model="All Terrain Armored Transport", vehicle_type="Walker",
                 length="20", value="500000", fuel_capacity="2000", url="https://swapi.dev/api/vehicles/18/"),
        Vehicles(name="Speeder Bike", model="74-Z", vehicle_type="Speeder", length="3",
                 value="8000", fuel_capacity="30", url="https://swapi.dev/api/vehicles/30/")
    ]

    # Datos para la tabla Muchachos
    muchachos = [
        Muchachos(name="Rebel Squad", group_name="Rebels",
                  activity_type="Battle", length="5", url="https://rebels.com/squad1"),
        Muchachos(name="Sith Lords", group_name="Sith",
                  activity_type="Dark Side Training", length="10", url="https://sith.com/lords"),
        Muchachos(name="Jedi Council", group_name="Jedi",
                  activity_type="Training", length="7", url="https://jedi.com/council"),
        Muchachos(name="Stormtroopers", group_name="Empire",
                  activity_type="Combat", length="3", url="https://empire.com/troopers"),
        Muchachos(name="Bounty Hunters", group_name="Freelancers",
                  activity_type="Hunting", length="6", url="https://hunters.com/bounty")
    ]

    # Datos para la tabla Favorite (asignando favoritos de forma aleatoria)
    favorites = [
        Favorite(user_id=1, characters_id=1, planet_id=1,
                 vehicle_id=1, Muchachos_id=1),
        Favorite(user_id=2, characters_id=2, planet_id=2,
                 vehicle_id=2, Muchachos_id=2),
        Favorite(user_id=3, characters_id=3, planet_id=3,
                 vehicle_id=3, Muchachos_id=3),
        Favorite(user_id=4, characters_id=4, planet_id=4,
                 vehicle_id=4, Muchachos_id=4),
        Favorite(user_id=5, characters_id=5, planet_id=5,
                 vehicle_id=5, Muchachos_id=5)
    ]

    # Agregar los datos a la sesión y guardarlos en la base de datos
    db.session.add_all(users + characters_1 + planets + vehicles + muchachos + favorites)
    db.session.commit()

    print("Datos insertados correctamente en la base de datos.")
