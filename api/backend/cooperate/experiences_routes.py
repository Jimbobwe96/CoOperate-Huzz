from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from datetime import date

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
experiences = Blueprint('experiences', __name__)

#------------------------------------------------------------

# gets all of the experiences of a given student
@experiences.route('/experiences/<student_id>', methods=['GET'])
def get_student_experiences(student_id):
    query = f'''
        SELECT *
        FROM Experiences
        WHERE StudentID = {str(student_id)}
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
@experiences.route('/experiences/<StudentID>', methods=['POST'])
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
@experiences.route('/experiences/<int:Experience_id>', methods=['DELETE'])
def delete_student_experiences(experienceId):
     query = f'''
        DELETE FROM Experiences
        WHERE ExperienceID = {experienceId}
    '''
     
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     response = make_response("Profile deleted successfully", 200)
     return response

#------------------------------------------------------------

# edit a specific experience
@experiences.route('/experiences/<int:Experience_id>', methods=['PUT'])
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
