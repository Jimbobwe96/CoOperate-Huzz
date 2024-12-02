from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from datetime import date


## dummy data
data_store = {
    1: {
        "StudentID": 101,
        "Title": "Software Engineer",
        "Industry": "Technology",
        "StartTime": date(2022, 6, 1),
        "EndTime": date(2023, 6, 1),
        "Company": "TechCorp",
        "ExperienceID": 1
    },
    2: {
        "StudentID": 102,
        "Title": "Data Analyst",
        "Industry": "Finance",
        "StartTime": date(2021, 1, 15),
        "EndTime": date(2022, 1, 15),
        "Company": "DataSolutions",
        "ExperienceID": 2
    }
}

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
Experiences = Blueprint('Experiences', __name__)

#------------------------------------------------------------

# gets all of the experiences of a given student
@Experiences.route('/Experiences/<StudentID>', methods=['GET'])
def get_student_experiences(studentID):
    query = f'''
        SELECT *
        FROM Experiences
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

# post a specific student's experiences
@Experiences.route('/Experiences/<StudentID>', methods=['POST'])
def post_student_experience(studentID):
    query = f'''
        INSERT INTO EXPERIENCES (StudentID, Title, Industry, StartTime, EndTime,
          Company, ExperienceID)
        VALUES ()
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

# delete a specific  experiences
@Experiences.route('/Experiences/<int:Experience_id>', methods=['DELETE'])
def delete_student_experiences(Experience_id):
    return 'Experience sucessfully deleted', 200

#------------------------------------------------------------

# edit a specific experience
@Experiences.route('/Experiences/<int:Experience_id>', methods=['PUT'])
def update_experience(Experience_id):
    # Check if the experience exists in the data store
    if Experience_id not in data_store:
        return jsonify({"error": "Experience not found"}), 404

    # Parse the incoming JSON request data
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    # Get the current experience and update it
    experience = data_store[Experience_id]
    experience.update(request_data)  # Merge existing experience with the provided data

    return jsonify({"message": "Experience updated successfully", "experience": experience}), 200
