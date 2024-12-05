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
admins = Blueprint('admins', __name__)

#------------------------------------------------------------
# TODO
@admins.route('/admins/logs', methods=['GET'])
def get_activity_logs():
    query = '''
        SELECT 
            al.LogID,
            al.ActionType AS `Action Type`, 
            al.AdminID AS `Admin ID`,
            CONCAT(a.FirstName, ' ', a.LastName) AS 'Admin Name',
            Details,
            Timestamp
        FROM Activity_Logs AS al
        JOIN Admin AS a 
        ON al.AdminID = a.AdminID
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
@admins.route('/admins/<admin_id>/reviews/<review_id>/reject', methods=['PUT'])
def reject_review(admin_id, review_id):
    update_query = f'''
        UPDATE Reviews
        SET ResolvedBy = {int(admin_id)}
        WHERE ReviewID = {int(review_id)}
    '''
    cursor = db.get_db().cursor() 
    cursor.execute(update_query)

    db.get_db().commit()
    
    response = make_response("Successfully rejected review")
    response.status_code = 200
    return response
    
#------------------------------------------------------------
# TODO
@admins.route('/admins/<admin_id>/reviews/<review_id>/reject', methods=['POST'])
def log_review_reject(admin_id, review_id):
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    details = the_data['details']

    insert_query = f'''
        INSERT INTO Activity_Logs (AdminID, ActionType, Details)
        VALUES ({int(admin_id)}, CONCAT('Rejcted Review ', {str(review_id)}), '{str(details)}')
    '''

    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(insert_query)

    db.get_db().commit()
        
    response = make_response("Successfully logged action")
    response.status_code = 200
    return response

#------------------------------------------------------------
# TODO
@admins.route('/admins/reviews', methods=['GET'])
def get_all_reviews_to_check():
    query = f'''
        SELECT * 
        FROM Reviews
        WHERE ResolvedBy IS NULL
    '''

    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response