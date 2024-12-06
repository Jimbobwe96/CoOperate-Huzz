from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
coop_role = Blueprint('coop_role', __name__)

#------------------------------------------------------------

# gets all of the listed roles 
@coop_role.route('/coop_role', methods=['GET'])
def get_coop_role():
    query = '''
        SELECT
            c.Name 'Company',
            c.CompanyID 'CompanyID',
            cr.Title 'Role',
            CONCAT(cr.City, ', ', cr.Country) 'Location',
            cr.Pay 'Pay',
            cr.RequiredGPA 'Required GPA',
            cr.PositionID 'PositionID'
        FROM Company `c`
        JOIN CoopRole `cr` ON c.CompanyID = cr.CompanyID
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

# gets all of the listed roles for a specific company
@coop_role.route('/coop_role/company/<CompanyID>', methods=['GET'])
def get_company_roles(CompanyID):
    query = f'''
        SELECT
            c.Name 'Company',
            cr.Title 'Role',
            CONCAT(cr.City, ', ', cr.Country) 'Location',
            cr.Pay 'Pay',
            cr.RequiredGPA 'Required GPA',
            cr.PositionID 'PositionID'
        FROM Company `c`
        JOIN CoopRole `cr` ON c.CompanyID = cr.CompanyID
        WHERE c.CompanyID = {str(CompanyID)}
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
# gets the information for a specific co-op role and its associated reviews
@coop_role.route('/coop_role/<position_id>', methods=['GET'])
def get_coop_role_info_reviews(position_id):
    query = f'''
        SELECT
            c.Name 'Company',
            cr.Title 'Role',
            CONCAT(cr.City, ', ', cr.Country) 'Location',
            cr.Pay 'Pay',
            cr.RequiredGPA 'Required GPA',
            ROUND(AVG(r.Culture),2) 'Culture',
            ROUND(AVG(r.Satisfaction),2) 'Satisfaction',
            ROUND(AVG(r.Compensation),2) 'Compensation',
            ROUND(AVG(r.LearningOpportunity),2) 'Learning',
            ROUND(AVG(r.WorkLifeBalance),2) 'Work Life Balance'
        FROM CoopRole `cr`
        JOIN Company `c` ON c.CompanyID = cr.CompanyID
        JOIN Reviews `r` ON r.PositionID = cr.PositionID
        WHERE cr.PositionID = {position_id}
        GROUP BY c.Name, cr.Title, CONCAT(cr.City, ', ', cr.Country), cr.Pay, cr.RequiredGPA
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
@coop_role.route('/coop_role/company/<CompanyID>', methods=['POST'])
def log_update_approved(CompanyID):
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json

    #extracting the variable
    title = the_data['title']
    city = the_data['city']
    country = the_data['country']
    pay = the_data['pay']
    required_gpa = the_data['required_gpa']

    query = f'''
        INSERT INTO CoopRole (CompanyID, Title, City, Country, Pay, RequiredGPA)
        VALUES ({int(CompanyID)}, '{title}', '{city}', '{country}', '{pay}', '{required_gpa}')
    '''
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully logged action")
    response.status_code = 200
    return response