from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/employees_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    location = db.Column(db.String())
    zipcode = db.Column(db.Integer())

    def __init__(self, name, location, zipcode):
        self.name = name
        self.location = location
        self.zipcode = zipcode

    def __repr__(self):
        return f"<Employee {self.name}>"


@app.route('/')
def hello():
	return {"hello": "world"}


@app.route('/employees', methods=['POST', 'GET'])
def handle_employees():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = Employee(name=data['name'], location=data['location'], zipcode=data['zipcode'])

            db.session.add(new_employee)
            db.session.commit()

            return {"message": f"car {new_employee.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cars = CarsModel.query.all()
        results = [
            {
            "name": employee.name,
            "location": employee.location,
            "zipcode": employee.zipcode
            } for employee in employees]

        return {"count": len(results), "employees": results, "message": "success"}


@app.route('/employees/<employee_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)

    if request.method == 'GET':
        response = {
            "name": employee.name,
            "location": employee.location,
            "zipcode": employee.zipcode
        }
        return {"message": "success", "employee": response}

    elif request.method == 'PUT':
        data = request.get_json()
        employee.name = data['name']
        employee.location = data['location']
        employee.zipcode = data['zipcode']

        db.session.add(employee)
        db.session.commit()
        
        return {"message": f"employee {employee.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(employee)
        db.session.commit()
        
        return {"message": f"employee {employee.name} successfully deleted."}


if __name__ == '__main__':
    app.run(debug=True)
