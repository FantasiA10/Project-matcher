import os
from flask import Flask, url_for, render_template, session, request, redirect, send_file, make_response, flash
from flask_restx import Resource
import datetime
from server.user_login import User
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


@app.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Return homepage with list of projects
    """
    # if session["user"]['email'].split('_')[0] == "Manager":
    #     return redirect('/manager_homepage')

    project_lst = module.homepage_form()
    return render_template('homepage.html', project_lst=project_lst)


@app.route('/loginpage')
def loginpage():
    """
    Return login page
    """
    return render_template('user_login.html')


@app.route('/homepage_local', methods=['GET', 'POST'])
def homepage_local():
    """
    todo return homepage base on account passed in through url
    """
    project_lst = module.homepage_form()
    return render_template('homepage.html', project_lst=project_lst)


@app.route('/add_project', methods=['GET', 'POST'])
@module.login_required
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
      "if_approve": True,
    }
    file = request.files.get('file')
    if sc.project_exist(request.form['name']):
        flash("Error: Project name already existed.", "danger")
        return render_template('add_project.html')
    else:
        sc.add_project(project_details)
        if file:
            file_contents = file.read()
            file_detail = {
                'name': request.form['name'],
                'filename': file.filename,
                'filedata': file_contents,
            }
            sc.add_file(file_detail)
        flash("Thank you for sharing your project with us.", "success")
        return render_template('add_project.html')


@app.route('/single_post/<project>', methods=['GET', 'POST'])
def single_post(project):
    """
    Display more details about a single project
    """
    project_detail = sc.get_project_details(project)
    filename = sc.get_file_name(project)
    return render_template('post.html', project=project_detail,
                           filename=filename)


@app.route('/download/<project>', methods=['GET', 'POST'])
def download(project):
    """
    Download description file
    """
    return sc.get_file(project)


@app.route('/my_project', methods=['GET', 'POST'])
@module.login_required
def my_project():
    """
    Return my project page
    """
    if session['logged_in'] == True:
        user_email = session['user']['email']
        project_lst = sc.get_user_project(user_email)[user_email]
    
        return render_template('my_project.html', project_lst=project_lst)


@app.route('/my_application', methods=['GET', 'POST'])
@module.login_required
def my_application():
    """
    Return my application page
    """
    if session['logged_in'] == True:
        user_email = session['user']['email']
        application_lst = sc.get_user_application(user_email)[user_email]
        
        if application_lst == []:
            flash("You have not created any application yet.")
    
        return render_template('my_application.html', application_lst=application_lst)


@app.route('/apply', methods=['GET', 'POST'])
@module.login_required
def apply():
    """
    Return GET and POST reques from apply page
    """
    project_options = sc.get_projects_names()

    if request.method == 'GET':
        return render_template('apply.html', project_options=project_options)
    else:
        apl_details = {
        'application_name': str(request.form['applied project']) + "/" + str(session['user']["email"]),
        'applicant_name': request.form['full name'],
        'applicant_email': session['user']["email"],
        'applied_project': request.form['applied project'],
        'application_date': datetime.datetime.today().strftime("%m-%d-%Y"),
        'transcript': "string",
        'resume': "string",
        'application_status': "Pending",
        }
        file = request.files.get('file')

        sc.add_application(apl_details)

        flash("Your application is submited.", "success")
        return render_template('apply.html')


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
@module.login_required
def account():
    """
    todo
    """
    image_file = url_for('static', filename='images/' + 'steven.jpg')
    return render_template('account.html', title='Account', image_file=image_file)


@app.route("/manager_homepage", methods=['GET', 'POST'])
# @module.login_required
def manager_homepage():
    """
    todo
    """
    wait_approve_project_lst = module.homepage_form(approve=False)
    approve_project_lst = module.homepage_form()
    return render_template('manager_homepage.html',
                           wait_project_lst=wait_approve_project_lst,
                           project_lst=approve_project_lst)


@app.route("/approve_project/<project>", methods=['GET', 'POST'])
def approve_project(project):
    """
    approve a project and reload manager_home
    """
    sc.change_project_single_field(project, sc.APPROVE, True)
    return redirect("/manager_homepage")


@app.route("/disapprove_project/<project>", methods=['GET', 'POST'])
def disapprove_project(project):
    """
    approve a project and reload manager_home
    """
    sc.change_project_single_field(project, sc.APPROVE, False)
    return redirect("/manager_homepage")


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


@app.route('/service', methods=['GET'])
def service():
    """
    Todo
    """
    return render_template("service.html")


@app.route('/team', methods=['GET'])
def team():
    """
    Todo
    """
    return render_template("team.html")


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
