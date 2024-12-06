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
company = Blueprint('company', __name__)

#------------------------------------------------------------

# returns all of the companies and their information
@company.route('/company', methods=['GET'])
def get_companies():
    query = '''
        SELECT  Name, 
                Industry, 
                Headquarters, 
                Size, 
                CompanyID, 
        FROM Company
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
# returns all the information for a given company
@company.route('/company/<companyID>', methods=['GET'])
def get_company(companyID):
    query = f'''
        SELECT *
        FROM Company
        WHERE CompanyID = {str(companyID)}
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

#------------------------------------------------------------
# returns the aggregated average scores for each company with each of their positions
@company.route('/company/positions/agg_data', methods=['GET'])
def get_all_company_agg_data():
    query = '''
        SELECT 
            c.Name AS Company,
            cr.Title AS PosTitle,
            (
                AVG(r.Culture) + 
                AVG(r.Satisfaction) + 
                AVG(r.Satisfaction) +
                AVG(r.LearningOpportunity) + 
                AVG(r.WorkLifeBalance)
            ) / 5 AS avg_overall_score
        FROM Company c
        JOIN CoopRole cr ON c.CompanyID = cr.CompanyID
        JOIN Reviews r ON cr.PositionID = r.PositionID
        GROUP BY c.CompanyID, c.Name, cr.Title
        ORDER BY c.Name, cr.Title;
    '''
    # query = '''
    #     SELECT 
    #         c.CompanyID 'CompanyID',
    #         c.Name 'Company',
    #         cr.PositionID 'PositionID',
    #         cr.Title 'PosTitle',
    #         AVG(r.Culture) 'avg_culture',
    #         AVG(r.Satisfaction) 'avg_satisfaction',
    #         AVG(r.LearningOpportunity) 'avg_learning',
    #         AVG(r.WorkLifeBalance) 'avg_balance'
    #     FROM Company `c`
    #     JOIN CoopRole `cr` ON c.CompanyID = cr.CompanyID
    #     JOIN Reviews `r` ON cr.PositionID = r.PositionID
    #     GROUP BY c.CompanyID, c.Name, cr.PositionID, cr.Title
    # '''
    logger.info(query)
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