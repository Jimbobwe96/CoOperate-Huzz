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
# TODO
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
# TODO
@students.route('/students/<AdvisorID>', methods=['GET'])
def get_advisor_student(AdvisorID):
    query = f'''
        SELECT *
        FROM Students
        WHERE StudentID = {str(AdvisorID)}
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
# TODO
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
 
# PUT route for updating a review
@students.route('/students/<StudentID>', methods=['PUT'])
def update_student(StudentID):
    try:
        # Get the JSON payload from the request
        data = request.json

        # Extract relevant fields
        first_name = data.get('FirstName')
        last_name = data.get('LastName')
        major = data.get('Major')
        current_year = data.get('CurrentYear')
        gpa = data.get('GPA')
        home_college = data.get('HomeCollege')

        # Validate input
        if not all([first_name, last_name, major, current_year, home_college]) or not isinstance(gpa, (int, float)):
            return make_response(jsonify({'error': 'Invalid input data'}), 400)

        # SQL query
        query = '''
            UPDATE Students
            SET FirstName = %s, LastName = %s, Major = %s, 
                GPA = %s, CurrentYear = %s, HomeCollege = %s
            WHERE StudentID = %s
        '''

        # Get a cursor object from the database
        cursor = db.get_db().cursor()

        # Log query and parameters
        current_app.logger.debug(f"Executing Query: {query}")
        current_app.logger.debug(f"With Parameters: {first_name}, {last_name}, {major}, {gpa}, {current_year}, {home_college}, {StudentID}")

        # Execute the query
        cursor.execute(query, (first_name, last_name, major, gpa, current_year, home_college, StudentID))
        db.get_db().commit()

        # Log row count
        current_app.logger.debug(f"Rows affected: {cursor.rowcount}")

        # If no rows were updated, return 404
        if cursor.rowcount == 0:
            return make_response(jsonify({'error': 'Student not found'}), 404)

        # Return success
        return make_response(jsonify({'message': 'Student updated successfully'}), 200)
    except Exception as e:
        # Log the error
        current_app.logger.error(f"Error: {e}")
        return make_response(jsonify({'error': str(e)}), 500)
