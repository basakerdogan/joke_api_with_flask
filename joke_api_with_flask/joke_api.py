from flask import Flask, jsonify, request
import random

app = Flask(__name__)

master_key = "ztOIwf0SQcZz3UhImRqN00zoqGgM1QpJ"

jokes = [
    {"id": 1, "joke": "Why don't scientists trust atoms? Because they make up everything!", "joketype": "science"},
    {"id": 2, "joke": "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!", "joketype": "math"},
    {"id": 3, "joke": "Parallel lines have so much in common. It’s a shame they’ll never meet.", "joketype": "math"},
    {"id": 4, "joke": "Why don't skeletons fight each other? They don't have the guts.", "joketype": "punny"},
    {"id": 5, "joke": "I'm reading a book on anti-gravity. It's impossible to put down!", "joketype": "punny"},
    {"id": 6, "joke": "I told my wife she was drawing her eyebrows too high. She looked surprised.", "joketype": "punny"},
    {"id": 7, "joke": "What did the grape say when it got stepped on? Nothing, it just let out a little wine!", "joketype": "punny"},
    {"id": 8, "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!", "joketype": "punny"},
    {"id": 9, "joke": "I'm on a whiskey diet. I've lost three days already!", "joketype": "punny"},
    {"id": 10, "joke": "Why did the tomato turn red? Because it saw the salad dressing!", "joketype": "punny"}
]

@app.route('/random', methods=['GET'])
def get_random_joke():
    random_joke = random.choice(jokes)
    return jsonify(random_joke["joke"])

@app.route('/jokes/<int:joke_id>', methods=['GET'])
def get_joke_by_id(joke_id):
    selected_joke = next((joke for joke in jokes if joke['id'] == joke_id), None)
    if selected_joke:
        return jsonify(selected_joke["joke"])
    else:
        return jsonify({"error": "Joke not found"}), 404

@app.route('/filter', methods=['GET'])
def filter_jokes_by_type():
    joke_type = request.args.get('type')
    filtered_jokes = [joke for joke in jokes if joke['joketype'] == joke_type]
    return jsonify(filtered_jokes)

@app.route('/jokes', methods=['POST'])
def add_joke():
    data = request.json
    new_joke = {
        "id": len(jokes) + 1,
        "joke": data["joke"],
        "joketype": data["joketype"]
    }
    jokes.append(new_joke)
    return jsonify(new_joke), 201

@app.route('/jokes/<int:joke_id>', methods=['PUT'])
def modify_joke(joke_id):
    data = request.json
    for joke in jokes:
        if joke["id"] == joke_id:
            joke["joke"] = data.get("joke", joke["joke"])
            joke["joketype"] = data.get("joketype", joke["joketype"])
            return jsonify(joke), 200
    return jsonify({"error": "Joke not found"}), 404

@app.route('/jokes/<int:joke_id>', methods=['PATCH'])
def modify_joke(joke_id):
    data = request.json
    for joke in jokes:
        if joke["id"] == joke_id:
            if "joke" in data:
                joke["joke"] = data["joke"]
            if "joketype" in data:
                joke["joketype"] = data["joketype"]
            return jsonify(joke), 200
    return jsonify({"error": "Joke not found"}), 404

@app.route('/jokes/<int:joke_id>', methods=['DELETE'])
def delete_joke(joke_id):
    global jokes
    initial_length = len(jokes)
    jokes = [joke for joke in jokes if joke['id'] != joke_id]
    if len(jokes) < initial_length:
        return jsonify({"message": "Joke deleted successfully"}), 200
    else:
        return jsonify({"error": "Joke not found"}), 404

@app.route('/jokes', methods=['DELETE'])
def delete_all_jokes():
    if request.args.get('masterkey') == master_key:
        global jokes
        jokes = []
        return jsonify({"message": "All jokes deleted successfully"}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run(debug=True)
