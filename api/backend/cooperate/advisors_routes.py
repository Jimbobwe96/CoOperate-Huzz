from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
advisors = Blueprint('advisors', __name__)

#------------------------------------------------------------

# returns all of the advisors and their information
@advisors.route('/advisors', methods=['GET'])
def get_reviews():
    query = '''
        SELECT  FirstName, 
                LastName, 
                College, 
                Email, 
                AdvisorID, 
        FROM Advisors
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
@advisors.route('/advisors/<advisor_id>', methods=['DELETE'])
def del_advisor(advisor_id):
    query = f'''
        DELETE FROM Advisors
        WHERE CompanyID = {advisor_id}
    '''

    # get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()  

    response = make_response("Successfully deleted advisor")
    response.status_code = 200
    return response

