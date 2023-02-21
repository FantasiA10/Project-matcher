import os
from flask import Flask, url_for, render_template, session, request, redirect, send_file, make_response, flash
from flask_restx import Resource
import datetime
from user_login import User
import db.projects as pj
import server.server_connect as sc
import server.module as module


app = Flask(__name__, template_folder="../templates")
app.secret_key = 'hskfakgkajgalg' #random key


@app.route('/user/signup', methods=['POST'])
def signup():
    """
    User create account
    """
    user = User()
    return user.signup()


@app.route('/user/signout')
def signout():
    """
    User sign out page
    """
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    """
    User login page
    """
    return User().login()


@app.route('/')
def home():
    """
    Return login page
    """
    return render_template('user_login.html')


@app.route('/homepage', methods=['GET', 'POST'])
@module.login_required
def homepage():
    """
    Return homepage with list of projects
    """
    if session["user"]['email'].split('_')[0] == "Manager":
        return render_template('manager_homepage.html')
    project_lst = module.homepage_form()
    return render_template('homepage.html', project_lst=project_lst)


@app.route('/homepage_local', methods=['GET', 'POST'])
def homepage_local():
    """
    todo return homepage base on account passed in through url
    """
    project_lst = module.homepage_form()
    return render_template('homepage.html', project_lst=project_lst)


@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    """
    Return GET and POST reques from add project page
    """
    if request.method == 'GET':
        return render_template('add_project.html')
    project_details = {
      'name': request.form['name'],
      'account': session['user'],
      'num_members': request.form['member number'],
      'department_name': request.form['depart'],
      'major_requirements': request.form['major'],
      'school_year': request.form['school year'],
      'GPA': request.form['gpa'],
      'project_duration': request.form['length'],
      'skill requirements': request.form['skill'],
      'post_date': datetime.datetime.today().strftime("%m-%d-%Y"),
      "description": request.form["description"],
      "if_approve": True
      #todo need request("FS")
    }
    if pj.check_if_exist(request.form['name']):
        flash("Error: Project name already existed.")
        return render_template('add_project.html')
    else:
        sc.add_project(project_details)
        flash("Thank you for sharing your project with us.")
        return render_template('my_project.html')


@app.route('/single_post/<project>', methods=['GET', 'POST'])
def single_post(project):
    """
    todo
    """
    project = sc.get_project_details(project)
    return render_template('post.html', project=project)


@app.route('/my_project')
def my_project():
    """
    Return my project page
    """
    return render_template('my_project.html')

@app.route('/my_application')
def my_application():
    """
    Return my application page
    """
    return render_template('my_application.html')


@app.route('/homepage_search', methods=['GET', 'POST'])
def homepage_search():
    """
    todo
    """
    key_word = request.form['key_word']
    project_lst = module.homepage_form(key_word)
    return render_template('homepage.html', project_lst=project_lst)


@app.route('/static/images/<file_name>', methods=['GET'])
def get_file(file_name):
    """
    todo
    """
    file_name = os.path.join("../static/images", file_name)
    return send_file(file_name)


@app.route('/static/<css_file>', methods=['GET'])
def get_css_file(css_file):
    """
    todo
    """
    file_name = os.path.join("../static", css_file)
    return send_file(file_name)


@app.route("/account", methods=['GET', 'POST'])
def account():
    """
    todo
    """
    image_file = url_for('../static/images/' + 'steven.jpg')
    return render_template('account.html', title='Account',
                           image_file=image_file)


@app.route("/manager_homepage", methods=['GET', 'POST'])
def manager_homepage():
    """
    todo
    """
    return render_template("manager_homepage.html")


@app.route('/about_us', methods=['GET'])
def about_us():
    """
    Todo
    """
    return render_template("about_us.html")


@app.route('/contact_us', methods=['GET'])
def contact_us():
    """
    Todo
    """
    return render_template("contact.html")


@app.route('/upload')
def upload_image():
    """
    Todo
    """
    return render_template('upload.html')

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_image():
  #  if request.method == 'POST':
  #     f = request.files['file']
  #     f.save(secure_filename(f.filename))
  #     return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
