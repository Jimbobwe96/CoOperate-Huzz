from flask import request, jsonify, make_response, Blueprint, current_app
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
        SELECT *, 
        c.Name 'Company',
        cr.Title 'Role'
        FROM Reviews `r` JOIN CoopRole `cr` ON r.PositionID = cr.PositionID
                       JOIN Company `c` ON cr.CompanyID = c.CompanyID
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
@reviews.route('/reviews/<reviewID>', methods=['GET'])
def get_student_reviews(reviewID):
    query = f'''
        SELECT *
        FROM Reviews
        WHERE reviewID = {str(reviewID)}
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)
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
@reviews.route('/reviews/<reviewID>', methods=['PUT'])
def update_review(reviewID):
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    culture = the_data['culture']
    satisfaction = the_data['satisfaction']
    compensation = the_data['compensation']
    learning_oppurtunity = the_data['learning_oppurtunity']
    work_life_balance = the_data['work_life_balance']
    summary = the_data['summary']
    
    query = f'''
        UPDATE Reviews 
        SET Culture = '{culture}',
            Satisfaction = '{satisfaction}',
            Compensation = '{compensation}',
            LearningOpportunity = '{learning_oppurtunity}',
            WorkLifeBalance = '{work_life_balance}',
            Summary = '{summary}'
        WHERE ReviewID = {reviewID}
    '''
 
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully edited review")
    response.status_code = 200
    return response
    
#------------------------------------------------------------
@reviews.route('/reviews/<review_id>', methods=['DELETE'])
def del_by_reviewid(review_id):
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
@reviews.route('/reviews/<positionID>', methods=['GET'])
def get_position_reviews(positionID):
    query = f'''
        SELECT *
        FROM Reviews
        WHERE positionID = {str(positionID)}
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
@reviews.route('/reviews/<review_id>/flag', methods=['PUT'])
def flag_by_reviewid(review_id):
    query = f'''
        UPDATE Reviews
        SET Flagged = 1
        WHERE ReviewID = {int(review_id)}
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully flagged review")
    response.status_code = 200
    return response

#------------------------------------------------------------
@reviews.route('/reviews/flagged', methods=['GET'])
def get_flagged_reviews():
    query = '''
        SELECT * 
        FROM Reviews
        WHERE Flagged = 1 AND ResolvedBy IS NULL
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
@reviews.route('/reviews/<review_id>/admin/<admin_id>/approve', methods=['PUT'])
def update_approved(review_id,admin_id):
    query = f'''
        UPDATE Reviews
        SET Flagged = 0, ResolvedBy = {int(admin_id)}
        WHERE ReviewID = {int(review_id)};
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully flagged review")
    response.status_code = 200
    log_update_approved(review_id, admin_id)
    return response

#------------------------------------------------------------
@reviews.route('/reviews/<review_id>/admin/<admin_id>/approve', methods=['POST'])
def log_update_approved(review_id,admin_id):
    query = f'''
        INSERT INTO Activity_Logs (AdminID, ActionType, Details)
        VALUES ({int(admin_id)}, CONCAT('Approved review #', {str(review_id)}), 'Incorrectly flagged review')
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully logged action")
    response.status_code = 200
    return response