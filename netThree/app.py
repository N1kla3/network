from flask import Flask, render_template, request, redirect, abort, url_for, jsonify
from Model import db, EmployeeModel, PositionModel, CompanyModel, CountryModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///identifier.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/api/v1.0/companies', methods=['GET'])
def get_companies():
    companies = CompanyModel.query.all()
    compan = []
    for row in companies:
        company = {
            'name': row.name,
            'country_name': row.country_name,
            'emp_amount': row.emp_amount
        }
        compan.append(company)

    return jsonify({'companies': compan})


@app.route('/api/v1.0/companies/<string:company_id>', methods=['GET'])
def get_company(company_id):
    company = CompanyModel.query.filter_by(name=company_id)
    if company == 0:
        abort(404)
    compan = []
    for c in company:
        compan = {
            'name': c.name,
            'country_name': c.country_name,
            'emp_amount': c.emp_amount
        }
    return jsonify({'company': compan})


@app.route('/api/v1.0/companies', methods=['POST'])
def create_company():
    if not request.json or not 'name' in request.json \
            or not 'country_name' in request.json \
            or not 'emp_amount' in request.json:
        abort(400)
    company = {
        'name': request.json['name'],
        'country_name': request.json['country_name'],
        'emp_amount': request.json['emp_amount'],
    }
    companyDB = CompanyModel(name=request.json['name'],
                             country_name=request.json['country_name'],
                             emp_amount=request.json['emp_amount'])
    db.session.add(companyDB)
    db.session.commit()
    return jsonify({'company': company}), 201


@app.route('/api/v1.0/companies/<string:company_id>', methods=['PUT'])
def update_company(company_id):
    company = CompanyModel.query.filter_by(name=company_id)
    if company == 0:
        abort(404)
    if not request.json:
        abort(400)
    for c in company:
        c.name = request.json.get('name', c.name)
        c.country_name = request.json.get('country_name', c.country_name)
        c.emp_amount = request.json.get('emp_amount', c.emp_amount)
    db.session.commit()
    return jsonify({'result': 'done'})


@app.route('/api/v1.0/companies/<string:company_id>', methods=['DELETE'])
def delete_company(company_id):
    company = CompanyModel.query.filter_by(name=company_id)
    if company == 0:
        abort(404)
    for c in company:
        db.session.delete(c)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/api/v1.0/countries', methods=['GET'])
def get_countries():
    countries = CountryModel.query.all()
    count = []
    for row in countries:
        country = {
            'name': row.name,
            'population': row.population,
            'location': row.location
        }
        count.append(country)

    return jsonify({'countries': count})


@app.route('/api/v1.0/countries/<string:country_id>', methods=['GET'])
def get_country(country_id):
    country = CountryModel.query.filter_by(name=country_id)
    if country == 0:
        abort(404)
    count = []
    for c in country:
        count = {
            'name': c.name,
            'population': c.population,
            'location': c.location
        }
    return jsonify({'country': count})


@app.route('/api/v1.0/countries', methods=['POST'])
def create_country():
    if not request.json or not 'name' in request.json \
            or not 'population' in request.json \
            or not 'location' in request.json:
        abort(400)
    country = {
        'name': request.json['name'],
        'population': request.json['population'],
        'location': request.json['location'],
    }
    countryDB = CountryModel(name=request.json['name'],
                             population=request.json['population'],
                             location=request.json['location'])
    db.session.add(countryDB)
    db.session.commit()
    return jsonify({'country': country}), 201


@app.route('/api/v1.0/countries/<string:country_id>', methods=['PUT'])
def update_country(country_id):
    country = CountryModel.query.filter_by(name=country_id)
    if country == 0:
        abort(404)
    if not request.json:
        abort(400)
    for c in country:
        c.name = request.json.get('name', c.name)
        c.population = request.json.get('population', c.population)
        c.location = request.json.get('location', c.location)
    db.session.commit()
    return jsonify({'result': 'done'})


@app.route('/api/v1.0/countries/<string:country_id>', methods=['DELETE'])
def delete_country(country_id):
    country = CountryModel.query.filter_by(name=country_id)
    if country == 0:
        abort(404)
    for c in country:
        db.session.delete(c)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/api/v1.0/emps', methods=['GET'])
def get_emps():
    emps = EmployeeModel.query.all()
    count = []
    for row in emps:
        emp = {
            'id': row.id,
            'name': row.name,
            'age': row.age,
            'position': row.position
        }
        count.append(emp)

    return jsonify({'Emps': count})


@app.route('/api/v1.0/emps/<string:emp_id>', methods=['GET'])
def get_emp(emp_id):
    emp = EmployeeModel.query.filter_by(name=emp_id)
    if emp == 0:
        abort(404)
    count = []
    for c in emp:
        count = {
            'id': c.id,
            'name': c.name,
            'age': c.age,
            'position': c.position
        }
    return jsonify({'Emp': count})


@app.route('/api/v1.0/emps', methods=['POST'])
def create_emps():
    if not request.json or not 'name' in request.json \
            or not 'age' in request.json \
            or not 'position' in request.json\
            or not 'id' in request.json:
        abort(400)
    emp = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age'],
        'position': request.json['position'],
    }
    empDB = EmployeeModel(id=request.json['id'], name=request.json['name'],
                             age=request.json['age'],
                             position=request.json['position'])
    db.session.add(empDB)
    db.session.commit()
    return jsonify({'Emp': emp}), 201


@app.route('/api/v1.0/emps/<string:emp_id>', methods=['PUT'])
def update_emps(emp_id):
    emp = EmployeeModel.query.filter_by(name=emp_id)
    if emp == 0:
        abort(404)
    if not request.json:
        abort(400)
    for c in emp:
        c.id = request.json.get('id', c.id)
        c.name = request.json.get('name', c.name)
        c.age = request.json.get('age', c.age)
        c.position = request.json.get('position', c.position)
    db.session.commit()
    return jsonify({'result': 'done'})


@app.route('/api/v1.0/emps/<string:emp_id>', methods=['DELETE'])
def delete_emps(emp_id):
    emp = EmployeeModel.query.filter_by(name=emp_id)
    if emp == 0:
        abort(404)
    for c in emp:
        db.session.delete(c)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/api/v1.0/positions', methods=['GET'])
def get_positions():
    positions = PositionModel.query.all()
    count = []
    for row in positions:
        pos = {
            'name': row.name,
            'average_salary': row.average_salary,
            'requirements': row.requirements
        }
        count.append(pos)

    return jsonify({'positions': count})


@app.route('/api/v1.0/positions/<string:position_id>', methods=['GET'])
def get_position(position_id):
    position = PositionModel.query.filter_by(name=position_id)
    if position == 0:
        abort(404)
    count = []
    for c in position:
        count = {
            'name': c.name,
            'average_salary': c.average_salary,
            'requirements': c.requirements
        }
    return jsonify({'position': count})


@app.route('/api/v1.0/positions', methods=['POST'])
def create_positions():
    if not request.json or not 'name' in request.json \
            or not 'average_salary' in request.json \
            or not 'requirements' in request.json:
        abort(400)
    position = {
        'name': request.json['name'],
        'average_salary': request.json['average_salary'],
        'requirements': request.json['requirements'],
    }
    positionDB = PositionModel(name=request.json['name'],
                          average_salary=request.json['average_salary'],
                          requirements=request.json['requirements'])
    db.session.add(positionDB)
    db.session.commit()
    return jsonify({'position': position}), 201


@app.route('/api/v1.0/positions/<string:position_id>', methods=['PUT'])
def update_positions(position_id):
    positions = PositionModel.query.filter_by(name=position_id)
    if positions == 0:
        abort(404)
    if not request.json:
        abort(400)
    for c in positions:
        c.name = request.json.get('name', c.name)
        c.average_salary = request.json.get('average_salary', c.average_salary)
        c.requirements = request.json.get('requirements', c.requirements)
    db.session.commit()
    return jsonify({'result': 'done'})


@app.route('/api/v1.0/positions/<string:position_id>', methods=['DELETE'])
def delete_positions(position_id):
    position = PositionModel.query.filter_by(name=position_id)
    if position == 0:
        abort(404)
    for c in position:
        db.session.delete(c)
    db.session.commit()
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
