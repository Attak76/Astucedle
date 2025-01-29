from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
color = ["#008F5C", "#E62B27", "#F4C500"]  # vert, rouge, violet

with open('bdd.json', 'r') as file:
    database = json.load(file)
    keys = database.keys()

@app.route('/route', methods=['GET'])
def get_route():
    global keys, database
    try:
        guess = request.args.get('guess')
        solution = database["T1"]

        if not guess:
            return jsonify({"error": "No input"}), 400

        if guess not in keys:
            return jsonify({"error": "Input not valid"}), 400

        template = database[guess]

        # Déterminer les couleurs pour chaque champ
        if guess == solution:
            g1 = guess
            c1 = color[0]
        else:
            g1 = guess
            c1 = color[1]

        if template["Terminus 1"] == solution["Terminus 1"]:
            g2 = template["Terminus 1"]
            c2 = color[0]
        else:
            g2 = template["Terminus 1"]
            c2 = color[1]

        if template["Terminus 2"] == solution["Terminus 2"]:
            g3 = template["Terminus 2"]
            c3 = color[0]
        else:
            g3 = template["Terminus 2"]
            c3 = color[1]

        c = 0
        for i in range(len(template["Communes"])):  
            if template["Communes"][i] == solution["Communes"][i]:
                c += 1
        if c / len(template["Communes"]) == 1:
            g4 = template["Communes"]
            c4 = color[0]
        elif c / len(template["Communes"]) == 0:
            g4 = template["Communes"]
            c4 = color[1]
        else:
            g4 = template["Communes"]
            c4 = color[2]

        if template["Nombre d'arrets"] > solution["Nombre d'arrets"]:
            g5 = template["Nombre d'arrets"]
            c5 = color[2]
            e5 = "sup"
        elif template["Nombre d'arrets"] < solution["Nombre d'arrets"]:
            g5 = template["Nombre d'arrets"]
            c5 = color[2]
            e5 = "inf"
        else:
            g5 = template["Nombre d'arrets"]
            c5 = color[0]
            e5 = "eq"

        if template["Interval"] == solution["Interval"]:
            g6 = template["Interval"]
            c6 = color[0]
        else:
            g6 = template["Interval"]
            c6 = color[1]

        # Construire la réponse avec les couleurs
        return jsonify({
            "Name":{"value": g1, "couleur": c1},
            "Terminus 1": {"value": g2, "couleur": c2},
            "Terminus 2": {"value": g3, "couleur": c3},
            "Communes": {"value": g4, "couleur": c4},
            "Nombre d'arrets": {"value": g5, "couleur": c5},
            "Interval": {"value": g6, "couleur": c6}
        })

    except Exception as e:
        return jsonify({"error": f"Une erreur est survenue: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(port = 5000, debug=True)
