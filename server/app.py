# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.get(id)  

    if earthquake:
        response = {
            'id': earthquake.id,
            'magnitude': earthquake.magnitude,
            'location': earthquake.location,
            'year': earthquake.year
        }
        return make_response(response, 200)
    else:
        error_response = {
            'message': f'Earthquake {id} not found.'
        }
        return make_response(error_response, 404)
    

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    count = len(earthquakes)

    earthquake_data = []
    for earthquake in earthquakes:
        earthquake_dict = {
            'id': earthquake.id,
            'magnitude': earthquake.magnitude,
            'location': earthquake.location,
            'year': earthquake.year
        }
        earthquake_data.append(earthquake_dict)

    response = {
        'count': count,
        'quakes': earthquake_data
    }
    return jsonify(response), 200
        


if __name__ == '__main__':
    app.run(port=5555, debug=True)
