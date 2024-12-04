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
    try:
        # Get the JSON payload from the request
        review_data = request.json

        # Extract relevant fields
        culture = review_data.get('culture')
        satisfaction = review_data.get('satisfaction')
        compensation = review_data.get('compensation')
        learning_opportunity = review_data.get('learning_opportunity')
        worklife_balance = review_data.get('worklife_balance')
        summary = review_data.get('summary')

        # Validate input (ensure all fields are provided and valid)
        if not all(isinstance(val, int) for val in [culture, satisfaction, compensation, learning_opportunity, worklife_balance]) or not isinstance(summary, str):
            return make_response(jsonify({'error': 'Invalid input data'}), 400)

        # SQL query for updating the review
        query = '''
            UPDATE Reviews
            SET culture = %s, satisfaction = %s, compensation = %s, 
                learning_opportunity = %s, worklife_balance = %s, summary = %s
            WHERE reviewID = %s
        '''
        # Get a cursor object from the database
        cursor = db.get_db().cursor()

        # Execute the query with parameters to avoid SQL injection
        cursor.execute(query, (culture, satisfaction, compensation, learning_opportunity, worklife_balance, summary, reviewID))
        db.get_db().commit()  # Commit the changes to the database

        # Check if any row was updated
        if cursor.rowcount == 0:
            return make_response(jsonify({'error': 'Review not found'}), 404)

        # Return a success response
        return make_response(jsonify({'message': 'Review updated successfully'}), 200)
    except Exception as e:
        # Handle unexpected errors
        return make_response(jsonify({'error': str(e)}), 500)
    
#------------------------------------------------------------
@reviews.route('/reviews/<reviewID>', methods=['DELETE'])
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