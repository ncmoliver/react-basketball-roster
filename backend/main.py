from flask import request, jsonify
from config import app, db
from models import Player

@app.route("/players", methods=["GET"])
def get_players():
    # Get all contacts in the database - Python Objects
    players = Player.query.all()
    # Convert Python objects to JSON
    json_players = list(map(lambda x: x.to_json(), players))
    return jsonify({"players": json_players})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True)
