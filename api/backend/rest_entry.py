from flask import Flask

from backend.db_connection import db
from backend.cooperate.review_routes import reviews
from backend.cooperate.student_routes import students
from backend.cooperate.skill_routes import skills
from backend.cooperate.experiences_routes import experiences
from backend.cooperate.admins_routes import admins
from backend.cooperate.coop_role_routes import coop_role
from backend.cooperate.company_routes import company
from backend.cooperate.coop_list_routes import coop_list
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables
    # This function reads all the values from inside
    # the .env file (in the parent folder) so they
    # are available in this file.  See the MySQL setup 
    # commands below to see how they're being used.
    load_dotenv()

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # # these are for the DB object to be able to connect to MySQL. 
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER').strip()
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD').strip()
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST').strip()
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT').strip())
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME').strip()  # Change this to your DB name

    # Initialize the database object with the settings above. 
    app.logger.info('current_app(): starting the database connection')
    db.init_app(app)


    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.logger.info('current_app(): registering blueprints with Flask app object.')   
    # app.register_blueprint(simple_routes)
    # app.register_blueprint(customers,   url_prefix='/c')
    # app.register_blueprint(products,    url_prefix='/p')
    app.register_blueprint(reviews,     url_prefix='/r')
    app.register_blueprint(students,    url_prefix='/s')
    app.register_blueprint(skills,      url_prefix='/sk')
    app.register_blueprint(experiences, url_prefix='/e')
    app.register_blueprint(admins,      url_prefix='/a')
    app.register_blueprint(coop_role,   url_prefix='/cr')
    app.register_blueprint(company,     url_prefix='/c')
    app.register_blueprint(coop_list,   url_prefix='/cl')

    # Don't forget to return the app object
    return app

