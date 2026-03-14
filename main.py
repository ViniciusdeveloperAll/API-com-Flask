from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json["task"]
    tasks.append(task)
    return jsonify({"message": "task added"})

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    tasks.pop(index)
    return jsonify({"message": "task deleted"})

app.run()
