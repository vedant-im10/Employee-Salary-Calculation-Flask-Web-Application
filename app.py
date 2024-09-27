from asyncio.windows_events import NULL
from flask import Flask, redirect, render_template, request, session, url_for
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "Shiddat"
app.permanent_session_lifetime = timedelta(hours=1)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=["POST"])
def calculate():

    session.permanent = True

    if request.form['id']:
        session["id"] = request.form['id']

    else:
        return redirect(url_for("index"))

    if not request.form['basic']:
        return redirect(url_for("index"))

    if int(request.form['basic']) == 0 or int(request.form['basic']) < 0 or int(request.form['basic']) > 100000:
        return "Please Enter The Basic Salary Between 1 to 100000"

    basicSalary = float(request.form['basic'])
    totalSalary = float(basicSalary)
    print(type(totalSalary))
    totalSalary = (totalSalary) + \
        float(basicSalary * 0.30) + float(basicSalary * 0.15) + \
        float(basicSalary * 0.10) + float(basicSalary * 0.05)
    session[request.form["id"]] = round(totalSalary, 2)
    return "Your Total Salary is : " + str(round(totalSalary, 2))


@app.route('/getSalary/<id>', methods=["GET"])
def getSalary(id):
    if id in session:
        return "Your Total Salary is : " + str(session[id])
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
