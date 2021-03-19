from flask import Flask, render_template, request, redirect, abort
from models import db, EmployeeModel, PositionModel, CompanyModel, CountryModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///identifier.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def hello():
    app.logger.info("Go to main page")
    return 'HELLO'


@app.route('/emps/create', methods=['GET', 'POST'])
def create_emp():
    if request.method == 'GET':
        return render_template('createemp.html')

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(id=id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
        app.logger.info("Employee created")
        return redirect('/emps')


@app.route('/emps')
def RetrieveListEmp():
    employees = EmployeeModel.query.all()
    return render_template('datalistemp.html', employees=employees)


@app.route('/emps/<int:id>')
def RetrieveEmployee(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee:
        app.logger.info("showing Employee")
        return render_template('dataemp.html', employee=employee)
    return f"Employee with id ={id} Doenst exist"


@app.route('/emps/<int:id>/update', methods=['GET', 'POST'])
def update_emp(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(name=name, age=age, position=position)
            db.session.add(employee)
            db.session.commit()
            app.logger.info("Updating employee")
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"

    return render_template('updateemp.html', employee=employee)


@app.route('/emps/<int:id>/delete', methods=['GET', 'POST'])
def delete_emp(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            app.logger.info("Deleting Employee")
            return redirect('/emps')
        abort(404)

    return render_template('deleteemp.html')


@app.route('/positions/create', methods=['GET', 'POST'])
def create_pos():
    if request.method == 'GET':
        return render_template('positioncreate.html')

    if request.method == 'POST':
        name = request.form['name']
        average_salary = request.form['average_salary']
        requirements = request.form['requirements']
        position = PositionModel(name=name, average_salary=average_salary, requirements=requirements)
        db.session.add(position)
        db.session.commit()
        app.logger.info("Creating Position")
        return redirect('/positions')


@app.route('/positions')
def RetrieveListPos():
    positions = PositionModel.query.all()
    return render_template('positiondatalist.html', positions=positions)


@app.route('/positions/<string:name>')
def RetrievePos(name):
    position = PositionModel.query.filter_by(name=name).first()
    if position:
        app.logger.info("Showing position")
        return render_template('positiondata.html', position=position)
    return f"Position with name ={name} Doenst exist"


@app.route('/positions/<string:name>/update', methods=['GET', 'POST'])
def update_pos(name):
    position = PositionModel.query.filter_by(name=name).first()
    if request.method == 'POST':
        if position:
            db.session.delete(position)
            db.session.commit()
            name = request.form['name']
            average_salary = request.form['average_salary']
            requirements = request.form['requirements']
            position = PositionModel(name=name, average_salary=average_salary, requirements=requirements)
            db.session.add(position)
            db.session.commit()
            app.logger.info("Updating position")
            return redirect(f'/positions/{name}')
        return f"Positions with name = {name} Does nit exist"

    return render_template('positionupdate.html', position=position)


@app.route('/positions/<string:name>/delete', methods=['GET', 'POST'])
def delete_pos(name):
    position = PositionModel.query.filter_by(name=name).first()
    if request.method == 'POST':
        if position:
            db.session.delete(position)
            db.session.commit()
            app.logger.info("Deleting position")
            return redirect('/positions')
        abort(404)

    return render_template('positiondelete.html')


@app.route('/companies/create', methods=['GET', 'POST'])
def create_company():
    if request.method == 'GET':
        return render_template('companycreate.html')

    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        emp_amount = request.form['emp_amount']
        company = CompanyModel(name=name, country_name=country, emp_amount=emp_amount)
        db.session.add(company)
        db.session.commit()
        app.logger.info("Creating company")
        return redirect('/companies')


@app.route('/companies')
def RetrieveListCompany():
    companies = CompanyModel.query.all()
    return render_template('companydatalist.html', companies=companies)


@app.route('/companies/<string:name>')
def RetrieveCompany(name):
    company = CompanyModel.query.filter_by(name=name).first()
    if company:
        app.logger.info("Show company")
        return render_template('companydata.html', company=company)
    return f"Company with name ={name} Doenst exist"


@app.route('/companies/<string:name>/update', methods=['GET', 'POST'])
def update_company(name):
    company = CompanyModel.query.filter_by(name=name).first()
    if request.method == 'POST':
        if company:
            db.session.delete(company)
            db.session.commit()
            name = request.form['name']
            country = request.form['country']
            emp_amount = request.form['emp_amount']
            company = CompanyModel(name=name, country_name=country, emp_amount=emp_amount)
            db.session.add(company)
            db.session.commit()
            app.logger.info("Updating company")
            return redirect(f'/companies/{name}')
        return f"Company with name = {name} Does nit exist"

    return render_template('companyupdate.html', company=company)


@app.route('/companies/<string:name>/delete', methods=['GET', 'POST'])
def delete_company(name):
    company = CompanyModel.query.filter_by(name=name).first()
    if request.method == 'POST':
        if company:
            db.session.delete(company)
            db.session.commit()
            app.logger.info("Deleting company")
            return redirect('/companies')
        abort(404)

    return render_template('companydelete.html')


@app.route('/countries/create', methods=['GET', 'POST'])
def create_country():
    if request.method == 'GET':
        return render_template('countrycreate.html')

    if request.method == 'POST':
        name = request.form['name']
        population = request.form['population']
        location = request.form['location']
        country = CountryModel(name=name, population=population, location=location)
        db.session.add(country)
        db.session.commit()
        app.logger.info("Creating country")
        return redirect('/countries')


@app.route('/countries')
def RetrieveListCountry():
    countries = CountryModel.query.all()
    return render_template('countrydatalist.html', countries=countries)


@app.route('/countries/<string:name>')
def RetrieveCountry(name):
    country = CountryModel.query.filter_by(name=name).first()
    if country:
        app.logger.info("Show country")
        return render_template('countrydata.html', country=country)
    return f"Country with name ={name} Doenst exist"


@app.route('/countries/<string:name>/update', methods=['GET', 'POST'])
def update_country(name):
    country = CountryModel.query.filter_by(name=name).first()
    if request.method == 'POST':
        if country:
            db.session.delete(country)
            db.session.commit()
            name = request.form['name']
            population = request.form['population']
            location = request.form['location']
            country = CountryModel(name=name, population=population, location=location)
            db.session.add(country)
            db.session.commit()
            app.logger.info("Updating country")
            return redirect(f'/countries/{name}')
        return f"Countries with name = {name} Does nit exist"

    return render_template('countryupdate.html', country=country)


@app.route('/countries/<string:name>/delete', methods=['GET', 'POST'])
def delete_country(name):
    country = CountryModel.query.filter_by(name=name).first()
    if request.method == 'POST':
        if country:
            db.session.delete(country)
            db.session.commit()
            app.logger.info("Deleting country")
            return redirect('/countries')
        abort(404)

    return render_template('countrydelete.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
