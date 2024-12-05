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
    # query = '''
    #     SELECT 
    #         LogID,
    #         ActionType,
    #         AdminID,
    #         Details,
    #         Timestamp
    #     FROM Activity_Logs
    # '''
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