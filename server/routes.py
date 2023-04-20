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
    project_lst = module.homepage_form()
    project_statistic = module.homepage_statistic()
    return render_template('homepage.html',
                           project_lst=project_lst,
                           project_statistic=project_statistic)


@app.route('/loginpage')
def loginpage():
    """
    Return login page
    """
    return render_template('user_login.html')


@app.route('/homepage_local', methods=['GET', 'POST'])
@module.login_required
def homepage_local():
    """
    return homepage base on account passed in through url
    """
    if session["user"]['email'].split('_')[0] == "Manager":
        return redirect('/manager_homepage')

    project_lst = module.homepage_form()
    project_statistic = module.homepage_statistic()
    return render_template('homepage_local.html',
                           project_lst=project_lst,
                           project_statistic=project_statistic)


@app.route('/add_project', methods=['GET', 'POST'])
@module.login_required
def add_project():
    """
    Return GET and POST reques from add project page
    """

    department_options = sc.get_departments()

    if request.method == 'GET':
        return render_template('add_project.html', department_options = department_options)
    project_details = {
      'name': request.form['name'],
      'account': session['user'],
      'num_members': request.form['member number'],
      'department_name': request.form['department'],
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


@app.route('/delete_pj/<pj_name>', methods=['POST'])
def delete_pj(pj_name):
    sc.delete_project(pj_name)

    user_email = session['user']['email']
    project_lst = sc.get_user_project(user_email)[user_email]
    return render_template('my_project.html', project_lst=project_lst)


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
            flash("You have not applied for any project yet.")
    
        return render_template('my_application.html', application_lst=application_lst)


@app.route('/apply', methods=['GET', 'POST'])
@module.login_required
def apply():
    """
    Return GET and POST request from apply page
    """
    project_options = sc.get_projects_names()

    if request.method == 'GET':
        return render_template('apply.html', project_options=project_options)
    else:
        string = str(request.form['applied project']) + "_" + str(session['user']["email"])
        apl_name = "".join(string.split())

        apl_details = {
            'application_name': apl_name,
            'applicant_name': request.form['full name'],
            'applicant_email': session['user']["email"],
            'applied_project': request.form['applied project'],
            'application_date': datetime.datetime.today().strftime("%m-%d-%Y"),
            'transcript': "string",
            'resume': "string",
            'application_status': "Pending",
        }
        
        if (sc.application_exist(apl_name)):
            flash("Error: You have already applied for this project.", "danger")
            return render_template('apply.html', project_options=project_options)
        else:
            sc.add_application(apl_details)
            flash("You successfully applied to " + "'" + request.form['applied project'] + "'.", "success")
            return render_template('apply.html', project_options=project_options)


@app.route('/delete_apl/<apl_name>', methods=['POST'])
def delete_apl(apl_name):
    sc.delete_application(apl_name)

    user_email = session['user']['email']
    application_lst = sc.get_user_application(user_email)[user_email]
    return render_template('my_application.html', application_lst=application_lst)



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
    load account page
    """
    pic_type, pic_data = sc.get_profile_pic(session['user']['email'])
    if pic_type:
        return render_template('accountpage.html', title='Account',
                               image_file=pic_data,
                               image_type=pic_type)
    else:
        image_file = url_for('static', filename='images/' + 'steven.jpg')
        return render_template('accountpage.html', title='Account',
                               image_file=image_file,
                               image_type=None)


@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_email = session['user']['email']
    sc.delete_user(user_email)
 
    project_lst = module.homepage_form()
    project_statistic = module.homepage_statistic()
    return render_template('homepage.html',
                           project_lst=project_lst,
                           project_statistic=project_statistic)


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


@app.route('/profile_pic_upload', methods=['GET', 'POST'])
def upload_image():
    """
    upload a person profile picture to server
    """
    file = request.files.get('file')
    if file:
        file_contents = file.read()
        profile_detail = {
            'user_email':  session['user']['email'],
            'filename': file.filename,
            'filedata': file_contents,
        }
        sc.update_profile_pic(profile_detail)
    return redirect('/account')

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from the request
        file = request.files['file']

        # Save the file to the upload folder
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Render the upload.html template with the filename
        return render_template('account.html', filename=filename)

    # Render the upload.html template if the request method is GET
    return render_template('account.html')


if __name__ == '__main__':
    app.run(debug=True)
