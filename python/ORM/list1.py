import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://maddog:fhs7812@localhost:5432/maddog1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	flights = Flight.query.all()
	for flight in flights:
		print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")

if __name__ == "__main__":
	with app.app_context():
		main()		

# SQLALCHEMY examples

# Flight.query.filter_by(origin="Paris").first()
# Flight.query.filter_by(origin="Paris").count()
# Flight.qyery.filter_by(id=28).first() or Flight.query.get(28)

# UPDATE
# flight = Flight.query.get(6) 
# flight.duration = 280

# DELETE
# flight = Flight.query.get(28)
# db.session.delete(flight)

# SELECT * FROM flights ORDER BY origin;
# Flight.query.order_by(Flight.origin).all()

# SELECT * FROM flights ORDER BY origin DESC
# Flight.query.order_by(Flight.origin.desc()).all()

# SELECT * FROM flights WHERE origin != "Paris"
# Flight.query.filter(Flight.origin != "Paris").all()

# SELECT * FROM flights WHERE ORIGIN like "%a%"
# Flight.query.filter(Flight.origin.like("%a%")).all()

# SELECT * FROM flights WHERE origin IN ('Tokyo', 'Paris')
# Flight.query.filter(Flight.origin.in_(["Tokyo", 'Paris'])).all()

# SELECT * FROM flights WHERE origin = "Paris" AND duration > 500;
# Flight.query.filter(and_(Flight.origin == 'Paris', Flight.duration > 500)).all

# SELECT * FROM flights JOIN passengers ON flights.id = passemgers.flight_id;
# db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()