from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory todo list
todos = [{"id":1,
          "title":"Reading",
          "done":False
          }]

# CREATE a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = {
        "id": len(todos),
        "title": data.get("title"),
        "done": False
    }
    todos.append(todo)
    return jsonify(todo), 201

# READ all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# READ a specific todo
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    if todo_id < len(todos):
        return jsonify(todos[todo_id])
    return jsonify({"error": "Todo not found"}), 404

# UPDATE a todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id >= len(todos):
        return jsonify({"error": "Todo not found"}), 404
    data = request.get_json()
    todos[todo_id]["title"] = data.get("title", todos[todo_id]["title"])
    todos[todo_id]["done"] = data.get("done", todos[todo_id]["done"])
    return jsonify(todos[todo_id])

# DELETE a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id >= len(todos):
        return jsonify({"error": "Todo not found"}), 404
    deleted = todos.pop(todo_id)
    return jsonify(deleted), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
