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
RequiredSkills = Blueprint('RequiredSkills', __name__)

#------------------------------------------------------------

# gets all of the required skills of a given role
@RequiredSkills.route('/RequiredSkills/<PositionID>', methods=['GET'])
def get_role_requiredskills(PositionID):
    query = '''
        SELECT CoopRole.Title,
               Skill.SkillName
        FROM CoopRole
        JOIN RequiredSkills ON CoopRole.PositionID = RequiredSkills.PositionID
        JOIN Skill ON RequiredSkills.SkillID = Skill.SkillID
        WHERE CoopRole.PositionID = :position_id
    '''
    # Execute the query and fetch results
    result = db.session.execute(query, {"position_id": PositionID}).fetchall()

    # Transform the result into a JSON-serializable format
    skills = [{"Title": row[0], "SkillName": row[1]} for row in result]
    return jsonify(skills)

#------------------------------------------------------------

