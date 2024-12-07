from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
students = Blueprint('students', __name__)

#------------------------------------------------------------
@students.route('/students', methods=['GET'])
def get_students():
    query = '''
        SELECT  StudentID, 
                FirstName, 
                LastName, 
                Major, 
                GPA,
                HomeCollege,
                Email 
        FROM Students
    '''
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response


#------------------------------------------------------------
@students.route('/students/advisor/<AdvisorID>', methods=['GET'])
def get_advisor_student(AdvisorID):
    query = f'''
        SELECT *
        FROM Students
        WHERE AdvisorID = {str(AdvisorID)}
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response

#------------------------------------------------------------
@students.route('/students/<StudentID>', methods=['GET'])
def get_student(StudentID):
    query = f'''
        SELECT *
        FROM Students
        WHERE StudentID = {str(StudentID)}
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response

#------------------------------------------------------------

# returns all the advisor infomration to the given students advisor
@students.route('/students/<studentID>/advisor', methods=['GET'])
def get_student_advisor_info(studentID):
    query = f'''
        SELECT a.FirstName, a.LastName, a.Email
        FROM Students s JOIN advisors a on s.advisorID = a.advisorID
        WHERE StudentID = {str(studentID)}
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response

#------------------------------------------------------------

# returns all the advisor infomration to the given students advisor
@students.route('/students/<studentID>/advisor/remove', methods=['PUT'])
def remove_student_advisor(studentID):
    query = f'''
        UPDATE Students
        SET AdvisorID = NULL
        WHERE StudentID = {studentID}
    '''
    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(query)

    db.get_db().commit()
    
    response = make_response("Successfully removed advisor")
    response.status_code = 200
    return response

#------------------------------------------------------------

# returns all the advisor infomration to the given students advisor
@students.route('/students/advisor/<advisor_id>/add', methods=['PUT'])
def add_student_advisor(advisor_id):
    data = request.json

    student_id = data.get('student_id')


    query = f'''
        UPDATE Students
        SET AdvisorID = {advisor_id}
        WHERE StudentID = {student_id}
    '''
    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(query)

    db.get_db().commit()
    
    response = make_response("Successfully added advisor")
    response.status_code = 200
    return response

#------------------------------------------------------------
 
# PUT route for updating a review
@students.route('/students/<StudentID>', methods=['PUT'])
def update_student(StudentID):
    # Get the JSON payload from the request
    data = request.json

    # Extract relevant fields
    major = data.get('major')
    current_year = data.get('cur_year')
    gpa = data.get('gpa')
    home_college = data.get('home_college')

    # SQL query
    query = f'''
        UPDATE Students
        SET Major = '{major}', 
            GPA = '{gpa}', CurrentYear = '{current_year}', HomeCollege = '{home_college}'
        WHERE StudentID = '{StudentID}'
    '''

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(query)

    db.get_db().commit()
    
    response = make_response("Successfully updated profile")
    response.status_code = 200
    return response
