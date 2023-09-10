from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

@app.route('/get_data', methods=['GET'])
def get_data():
    results = UserData.query.all()
    return jsonify([{"id": result.id, "name": result.name, "age": result.age} for result in results])

if __name__ == "__main__":
    app.run(debug=True)
