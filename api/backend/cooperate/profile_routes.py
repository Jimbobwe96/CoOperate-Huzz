from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
import logging

logger = logging.getLogger(__name__)

#------------------------------------------------------------
# Create a new Blueprint for student profiles
profiles = Blueprint('profiles', __name__)

#------------------------------------------------------------
# Fetch all profiles
@profiles.route('/profiles', methods=['GET'])
def get_profiles():
    query = '''
        SELECT *
        FROM Students
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    profiles_data = cursor.fetchall()
    response = make_response(jsonify(profiles_data))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Fetch a specific profile by StudentID
@profiles.route('/profiles/<int:student_id>', methods=['GET'])
def get_profile(student_id):
    query = f'''
        SELECT *
        FROM Students
        WHERE StudentID = {student_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    profile_data = cursor.fetchone()
    
    if not profile_data:
        response = make_response(jsonify({"error": "Profile not found"}), 404)
        return response

    # Fetch skills and experiences
    skills_query = f'''
        SELECT Skill.SkillName, StudentSkills.Proficiency
        FROM StudentSkills
        JOIN Skill ON StudentSkills.SkillID = Skill.SkillID
        WHERE StudentSkills.StudentID = {student_id}
    '''
    experiences_query = f'''
        SELECT Title, Company, StartTime, EndTime
        FROM Experiences
        WHERE StudentID = {student_id}
    '''
    cursor.execute(skills_query)
    skills = cursor.fetchall()

    cursor.execute(experiences_query)
    experiences = cursor.fetchall()

    # Combine data
    profile_data['skills'] = skills
    profile_data['experiences'] = experiences

    response = make_response(jsonify(profile_data))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Add a new student profile
@profiles.route('/profiles', methods=['POST'])
def add_profile():
    data = request.json
    query = '''
        INSERT INTO Students (FirstName, LastName, GPA, Major, CurrentYear, HomeCollege, AdvisorID, Email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    values = (
        data['FirstName'], data['LastName'], data['GPA'], data['Major'],
        data['CurrentYear'], data['HomeCollege'], data.get('AdvisorID'), data['Email']
    )
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    response = make_response("Profile added successfully", 201)
    return response

#------------------------------------------------------------
# Update an existing student profile
@profiles.route('/profiles/<int:student_id>', methods=['PUT'])
def update_profile(student_id):
    data = request.json
    query = f'''
        UPDATE Students
        SET FirstName = %s, LastName = %s, GPA = %s, Major = %s, 
            CurrentYear = %s, HomeCollege = %s, AdvisorID = %s, Email = %s
        WHERE StudentID = {student_id}
    '''
    values = (
        data['FirstName'], data['LastName'], data['GPA'], data['Major'],
        data['CurrentYear'], data['HomeCollege'], data.get('AdvisorID'), data['Email']
    )
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    response = make_response("Profile updated successfully", 200)
    return response

#------------------------------------------------------------
# Delete a student profile
@profiles.route('/profiles/<int:student_id>', methods=['DELETE'])
def delete_profile(student_id):
    query = f'''
        DELETE FROM Students
        WHERE StudentID = {student_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    response = make_response("Profile deleted successfully", 200)
    return response
