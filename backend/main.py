from flask import request, jsonify
from config import app, db
from models import Player

# Get All Players
@app.route("/players", methods=["GET"])
def get_players():
    # Get all contacts in the database - Python Objects
    players = Player.query.all()
    # Convert Python objects to JSON
    json_players = list(map(lambda x: x.to_json(), players))
    return jsonify({"players": json_players})


#Create A New Player
@app.route("/create_player", methods=["POST"])
def create_player():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name, and email"}), 
            400,
        )
    
    new_player = Player(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_player)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Player created"}), 201


# Update Player
@app.route("/update_player/<int:user_id>", methods=["PATCH"])
def update_player(user_id):
    player = Player.query.get(user_id)

    if not player:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    player.first_name = data.get("firstName", player.first_name)
    player.last_name = data.get("lastName", player.last_name)
    player.email = data.get("email", player.email)

    db.session.commit()

    return jsonify({"message": "User updated."}), 200

# Delete Player
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    player = Player.query.get(user_id)

    if not player:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(player)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True)
