from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, id, name, age, position):
        self.id = id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}"


class PositionModel(db.Model):
    __tablename__ = "positions"

    name = db.Column(db.String, primary_key=True)
    average_salary = db.Column(db.Integer())
    requirements = db.Column(db.String())

    def __init__(self, name, average_salary, requirements):
        self.name = name
        self.average_salary = average_salary
        self.requirements = requirements

    def __repr__(self):
        return f"{self.name}"


class CompanyModel(db.Model):
    __tablename__ = "companies"

    name = db.Column(db.String, primary_key=True)
    country_name = db.Column(db.String())
    emp_amount = db.Column(db.Integer())

    def __init__(self, name, country_name, emp_amount):
        self.name = name
        self.country_name = country_name
        self.emp_amount = emp_amount

    def __repr__(self):
        return f"{self.name}"


class CountryModel(db.Model):
    __tablename__ = "countries"

    name = db.Column(db.String, primary_key=True)
    population = db.Column(db.Integer())
    location = db.Column(db.String())

    def __init__(self, name, population, location):
        self.name = name
        self.population = population
        self.location = location

    def __repr__(self):
        return f"{self.name}"