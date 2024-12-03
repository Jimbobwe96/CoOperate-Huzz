from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
import logging
logger = logging.getLogger(__name__)

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
reviews = Blueprint('reviews', __name__)

#------------------------------------------------------------
# TODO
@reviews.route('/reviews', methods=['GET'])
def get_reviews():
    query = '''
        SELECT *
        FROM Reviews
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
@reviews.route('/reviews', methods=['POST'])
def add_new_review():

    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    student_id = the_data['student_id']
    culture = the_data['culture']
    satisfaction = the_data['satisfaction']
    compensation = the_data['compensation']
    learning_oppurtunity = the_data['learning_oppurtunity']
    work_life_balance = the_data['work_life_balance']
    summary = the_data['summary']
    position_id = the_data['position_id']
    
    query = f'''
        INSERT INTO Reviews (StudentID,
                            Culture,
                            Satisfaction,
                            Compensation,
                            LearningOpportunity,
                            WorkLifeBalance,
                            Summary,
                            PositionID)
        VALUES ('{student_id}', '{culture}', '{satisfaction}', '{compensation}', '{learning_oppurtunity}', '{work_life_balance}', '{summary}', '{position_id}')
    '''
 
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added review")
    response.status_code = 200
    return response
    
    

#------------------------------------------------------------
# TODO
@reviews.route('/reviews/<studentID>', methods=['GET'])
def get_student_reviews(studentID):
    query = f'''
        SELECT *
        FROM Reviews
        WHERE StudentID = {str(studentID)}
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response

#------------------------------------------------------------
# TODO
@reviews.route('/reviews/<review_id>', methods=['DELETE'])
def del_student_reviews(review_id):
    query = f'''
        DELETE FROM Reviews
        WHERE ReviewID = {int(review_id)}
    '''
    logger.info(query)
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully deleted review")
    response.status_code = 200
    return response

#------------------------------------------------------------
# TODO
@reviews.route('/reviews/<studentID>/<positionID>', methods=['GET'])
def get_spec_student_reviews(studentID, positionID):
    query = f'''
        SELECT *
        FROM Reviews
        WHERE StudentID = {str(studentID)}
        AND PositionID = {str(positionID)}
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
@reviews.route('/reviews/<studentID>/<positionID>', methods=['POST'])
def add_student_reviews_new(studentID, positionID):
    query = f'''
        INSERT INTO Reviews (StudentID, Date, Culture, Satisfaction, Compensation,
          LearningOpportunity, WorkLifeBalance, Summary, PositionID)
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
# TODO
@reviews.route('/reviews/<student_id>/<position_id>', methods=['DELETE'])
def del_student_reviews(student_id, position_id):
    query = f'''
        DELETE FROM Reviews
        WHERE StudentID = {int(student_id)} 
        AND PositionID = {int(position_id)}
    '''
    logger.info(query)
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully deleted review")
    response.status_code = 200
    return response