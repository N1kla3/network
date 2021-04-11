from flask import Flask, render_template, request, redirect, abort
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'HELLO'


emp_url = 'http://localhost:5001/api/v1.0/emps'
company_url = 'http://localhost:5001/api/v1.0/companies'
country_url = 'http://localhost:5001/api/v1.0/countries'
position_url = 'http://localhost:5001/api/v1.0/positions'


@app.route('/emps/create', methods=['GET', 'POST'])
def create_emp():
    if request.method == 'GET':
        return render_template('createemp.html')

    if request.method == 'POST':
        emps = {
            'id': request.form['id'],
            'name': request.form['name'],
            'age': request.form['age'],
            'position': request.form['position']
        }
        r = requests.post(emp_url, json=emps)
        return redirect('/emps')


@app.route('/emps')
def RetrieveListEmp():
    r = requests.get(emp_url)
    responce = r.json()
    return render_template('datalistemp.html', employees=responce['Emps'])


@app.route('/emps/<string:id>')
def RetrieveEmployee(id):
    r = requests.get(emp_url + '/' + id)
    responce = r.json()
    return render_template('dataemp.html', employee=responce['Emp'])


@app.route('/emps/<string:id>/update', methods=['GET', 'POST'])
def update_emp(id):
    r = requests.get(emp_url + '/' + id)
    responce = r.json()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        put_data = {
            'id': responce["Emp"]['id'],
            'name': name,
            'age': age,
            'position': position
        }
        rr = requests.put(emp_url + '/' + id, json=put_data)
        return redirect(f'/emps/{name}')

    return render_template('updateemp.html', employee=responce['Emp'])


@app.route('/emps/<string:id>/delete', methods=['GET', 'POST'])
def delete_emp(id):
    if request.method == 'POST':
        requests.delete(emp_url + '/' + id)
        return redirect('/emps')

    return render_template('deleteemp.html')


@app.route('/positions/create', methods=['GET', 'POST'])
def create_pos():
    if request.method == 'GET':
        return render_template('positioncreate.html')

    if request.method == 'POST':
        name = request.form['name']
        average_salary = request.form['average_salary']
        requirements = request.form['requirements']
        data = {
            'name': name,
            'average_salary': average_salary,
            'requirements': requirements
        }
        r = requests.post(position_url, json=data)
        return redirect('/positions')


@app.route('/positions')
def RetrieveListPos():
    r = requests.get(position_url)
    resp = r.json()
    return render_template('positiondatalist.html', positions=resp['positions'])


@app.route('/positions/<string:name>')
def RetrievePos(name):
    r = requests.get(position_url + '/' + name)
    resp = r.json()
    if resp:
        return render_template('positiondata.html', position=resp['position'])
    return f"Position with name ={name} Doenst exist"


@app.route('/positions/<string:name>/update', methods=['GET', 'POST'])
def update_pos(name):
    r = requests.get(position_url + '/' + name)
    resp = r.json()
    if request.method == 'POST':
        if resp:
            newname = request.form['name']
            average_salary = request.form['average_salary']
            requirements = request.form['requirements']
            data = {
                'name': newname,
                'average_salary': average_salary,
                'requirements': requirements
            }
            requests.put(position_url + '/' + name, json=data)
            return redirect(f'/positions/{newname}')
        return f"Positions with name = {name} Does nit exist"

    return render_template('positionupdate.html', position=resp['position'])


@app.route('/positions/<string:name>/delete', methods=['GET', 'POST'])
def delete_pos(name):
    if request.method == 'POST':
        requests.delete(position_url + '/' + name)
        return redirect('/positions')

    return render_template('positiondelete.html')


@app.route('/companies/create', methods=['GET', 'POST'])
def create_company():
    if request.method == 'GET':
        return render_template('companycreate.html')

    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        emp_amount = request.form['emp_amount']
        data = {
            'name': name,
            'country_name': country,
            'emp_amount': emp_amount
        }
        requests.post(company_url, json=data)
        return redirect('/companies')


@app.route('/companies')
def RetrieveListCompany():
    r = requests.get(company_url)
    resp = r.json()
    return render_template('companydatalist.html', companies=resp['companies'])


@app.route('/companies/<string:name>')
def RetrieveCompany(name):
    r = requests.get(company_url + '/' + name)
    resp = r.json()
    if resp:
        return render_template('companydata.html', company=resp['company'])
    return f"Company with name ={name} Doenst exist"


@app.route('/companies/<string:name>/update', methods=['GET', 'POST'])
def update_company(name):
    r = requests.get(company_url + '/' + name)
    company = r.json()
    if request.method == 'POST':
        if company:
            newname = request.form['name']
            country = request.form['country']
            emp_amount = request.form['emp_amount']
            data = {
                'name': newname,
                'country_name': country,
                'emp_amount': emp_amount
            }
            requests.put(company_url + '/' + name, json=data)
            return redirect(f'/companies/{newname}')
        return f"Company with name = {name} Does nit exist"

    return render_template('companyupdate.html', company=company['company'])


@app.route('/companies/<string:name>/delete', methods=['GET', 'POST'])
def delete_company(name):
    if request.method == 'POST':
        requests.delete(company_url + '/' + name)
        return redirect('/companies')

    return render_template('companydelete.html')


@app.route('/countries/create', methods=['GET', 'POST'])
def create_country():
    if request.method == 'GET':
        return render_template('countrycreate.html')

    if request.method == 'POST':
        name = request.form['name']
        population = request.form['population']
        location = request.form['location']
        data = {
            'name': name,
            'population': population,
            'location': location
        }
        requests.post(country_url, json=data)
        return redirect('/countries')


@app.route('/countries')
def RetrieveListCountry():
    r = requests.get(country_url)
    resp = r.json()
    return render_template('countrydatalist.html', countries=resp['countries'])


@app.route('/countries/<string:name>')
def RetrieveCountry(name):
    r = requests.get(country_url + '/' + name)
    country = r.json()
    if country:
        return render_template('countrydata.html', country=country['country'])
    return f"Country with name ={name} Doenst exist"


@app.route('/countries/<string:name>/update', methods=['GET', 'POST'])
def update_country(name):
    r = requests.get(country_url + '/' + name)
    country = r.json()
    if request.method == 'POST':
        if country:
            newname = request.form['name']
            population = request.form['population']
            location = request.form['location']
            data = {
                'name': newname,
                'population': population,
                'location': location
            }
            requests.put(country_url + '/' + name, json=data)
            return redirect(f'/countries/{newname}')
        return f"Countries with name = {name} Does nit exist"

    return render_template('countryupdate.html', country=country['country'])


@app.route('/countries/<string:name>/delete', methods=['GET', 'POST'])
def delete_country(name):
    if request.method == 'POST':
        requests.delete(country_url + '/' + name)
        return redirect('/countries')

    return render_template('countrydelete.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
