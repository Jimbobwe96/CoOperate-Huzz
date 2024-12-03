from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
StudentSkills = Blueprint('StudentSkills', __name__)

#------------------------------------------------------------

# Define the Blueprint for StudentSkills routes
StudentSkills = Blueprint('StudentSkills', __name__)

# 1. GET all skills for a student
@StudentSkills.route('/StudentSkills/<int:StudentID>', methods=['GET'])
def get_student_skills(StudentID):
    """
    Retrieve all skills and their proficiency levels for a specific student.
    """
    query = '''
        SELECT Skill.SkillName, StudentSkills.Proficiency
        FROM StudentSkills
        JOIN Skill ON StudentSkills.SkillID = Skill.SkillID
        WHERE StudentSkills.StudentID = :student_id
    '''
    # Execute the query and fetch all results
    result = db.session.execute(query, {"student_id": StudentID}).fetchall()

    # Convert the result into a list of dictionaries
    skills = [{"SkillName": row[0], "Proficiency": row[1]} for row in result]

    # Return the data as JSON
    return jsonify(skills)


#------------------------------------------------------------

# 2. POST add a skill for a student
@StudentSkills.route('/StudentSkills', methods=['POST'])
def add_student_skill():
    """
    Add a new skill and its proficiency level for a specific student.
    """
    # Get data from the JSON body of the request
    data = request.get_json()
    StudentID = data.get('StudentID')
    SkillID = data.get('SkillID')
    Proficiency = data.get('Proficiency')

    # SQL query to insert a new record into the StudentSkills table
    query = '''
        INSERT INTO StudentSkills (StudentID, SkillID, Proficiency)
        VALUES (:student_id, :skill_id, :proficiency)
    '''
    # Execute the query with the provided data
    db.session.execute(query, {
        "student_id": StudentID,
        "skill_id": SkillID,
        "proficiency": Proficiency
    })
    # Commit the transaction
    db.session.commit()

    # Return a success message
    return jsonify({"message": "Skill added successfully"}), 201

#------------------------------------------------------------

# 3. PUT update a student's skill proficiency
@StudentSkills.route('/StudentSkills/<int:StudentID>/<int:SkillID>', methods=['PUT'])
def update_student_skill(StudentID, SkillID):
    """
    Update the proficiency level of a specific skill for a student.
    """
    # Get data from the JSON body of the request
    data = request.get_json()
    Proficiency = data.get('Proficiency')

    # SQL query to update the proficiency level
    query = '''
        UPDATE StudentSkills
        SET Proficiency = :proficiency
        WHERE StudentID = :student_id AND SkillID = :skill_id
    '''
    # Execute the query with the provided data
    db.session.execute(query, {
        "proficiency": Proficiency,
        "student_id": StudentID,
        "skill_id": SkillID
    })
    # Commit the transaction
    db.session.commit()

    # Return a success message
    return jsonify({"message": "Skill proficiency updated successfully"}), 200

#------------------------------------------------------------

# 4. DELETE a skill for a student
@StudentSkills.route('/StudentSkills/<int:StudentID>/<int:SkillID>', methods=['DELETE'])
def delete_student_skill(StudentID, SkillID):
    """
    Remove a specific skill for a student.
    """
    # SQL query to delete a record from the StudentSkills table
    query = '''
        DELETE FROM StudentSkills
        WHERE StudentID = :student_id AND SkillID = :skill_id
    '''
    # Execute the query with the provided data
    db.session.execute(query, {
        "student_id": StudentID,
        "skill_id": SkillID
    })
    # Commit the transaction
    db.session.commit()

    # Return a success message
    return jsonify({"message": "Skill deleted successfully"}), 200
