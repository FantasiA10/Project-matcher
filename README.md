
# swe_project
An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

## Tech Stack used for this project:

Testing: pytest

Server: Flask && flask-restx

Lint: flake8

Database: MongoDB

CI/CD: Github Action

Cloud deployment: Heroku


Backend deployed to Heroku at https://project-finder.herokuapp.com/


Frontend deployed to Heroku at https://project-matcher.herokuapp.com/


Backend Github Link: https://github.com/BowenGong2000/swe_project


Frontend Github Link: https://github.com/FantasiA10/Project-matcher

## Project Setup Update: 

1. install pymongo, 
    pip install pymongo
2. install pymongo[srv]
    pip install "pymongo[srv]"
3. install passlib for password encyption
    pip install passlib
4. run command
    sed -i -e 's/\r$//' server.sh
5. run command
    for Windows users: 
        ./server.sh

    for Mac users: 
        ./run.sh-e

Go to http://127.0.0.1:5000


## Requirements

### User endpoints:
- Signup
- Login
- Get a description of a user
- List all registered users
- Delete a user
- Reset user password

### Projects endpoints:
- List all available projects
- Get a description of a project
- Create a project
- Delete a project
- Approve a project (admin only)

### Application endpoints:
- List all applications of a user
- Get a description of a application
- Accept/reject an appliacations

### In-project actions:
- Allow user to view
- Allow user to manage projects (add, delete)
- Allow admin to approve a project

### In-application actions:
- Allow user to view
- Allow user to create a application for a specific project
- Allow user to cancel a applications
- Allow user to accept/reject applications of a project

### Flowchart:
![alt text](static/images/flowchart.png)


resources of code for UI:
head protray https://www.deviantart.com/karmaanddestiny/art/Default-user-icon-4-858661084
form comtribution: https://github.com/JeetSaru/Responsive-HTML-Table-With-Pure-CSS---Web-Design-UI-Design