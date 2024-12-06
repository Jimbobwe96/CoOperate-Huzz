from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
coop_list = Blueprint('coop_list', __name__)

#------------------------------------------------------------

# returns all of the previous students and their stats that have had a given position 
@coop_list.route('/coop_list/<PositionID>', methods=['GET'])
def get_student_reviews(positionID):
    query = f'''
        SELECT *
        FROM coopList
        WHERE PositionID = {str(positionID)}
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

# returns all of the previous students and their stats that have had a given position 
@coop_list.route('/coop_list/student/<studentID>', methods=['GET'])
def get_student_list(studentID):
    query = f'''
        SELECT cr.Title, c.Name, cr.City
        FROM CoopList cl JOIN CoopRole cr ON cl.PositionID = cr.PositionID JOIN Company c on cl.CompanyID = c.CompanyID
        WHERE studentID = {str(studentID)}
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
# add a coop to a given students list of coops 
@coop_list.route('/coop_list/student/<student_id>', methods=['POST'])
def add_role_to_student_list(student_id):
    data = request.json

    company_id = data.get('company_id')
    position_id = data.get('position_id')

    query = f'''
        INSERT INTO CoopList (StudentID, CompanyID, PositionID)
        VALUES ('{student_id}', '{company_id}', '{position_id}')
    '''
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    cursor.execute(query)

    db.get_db().commit()
    
    response = make_response("Successfully added position to student's list")
    response.status_code = 200
    return response
