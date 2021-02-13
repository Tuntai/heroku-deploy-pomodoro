import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/activity')
def acti_page():
    return render_template('activities.html')


@app.route('/apps')
def apps_page():
    return render_template('apps.html')


@app.route('/timer')
def timer_page():
    return render_template('includes/timer.html')


@app.route('/relax')
def relax_page():
    return render_template('includes/relax.html')


@app.route('/task')
def task_page():
    return render_template('includes/task.html')


@app.route('/yoga')
def yoga_page():
    return render_template('includes/yoga.html')


@app.route('/resource')
def resource_page():
    return render_template('resource.html')




if __name__ == "__main__":
    app.run(debug=False)