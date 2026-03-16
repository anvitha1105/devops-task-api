from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "DevOps Task Manager API Running"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "task": data["task"],
        "status": "pending"
    }
    tasks.append(task)
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "task deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)