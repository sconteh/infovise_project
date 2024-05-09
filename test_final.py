"INST326 - Final Project Test Cases - DeJon Young, Samuel Conteh"
import unittest
import pytest
from final import User


"""
Explain: create_account 
Test Case: add_courses, authenticate, access_user, change_password,  recommend_career_paths 
"""
# final.access_user 
# call objects User.add_courses
def test_authenticate(): 
    new_variable = User('sconteh', 'PythonIsCool123!', 'Samuel', 'Conteh')

    assert User.authenticate('PythonIsCool123!') == 'PythonIsCool123!' # testing the add_courses function 

# def test_access_user():

# def test_recommend_career_paths():
def test_recomend_career_paths():
    User.add_courses({'INST341': {'name': 'Introduction to Digital Curation', 'career_paths': ['Data Analyst', 'Digital Archivist'], 'credits': 'N/A'}})
    User.recommend_career_paths ({'INST341': {'name': 'Introduction to Digital Curation', 'career_paths': ['Data Analyst', 'Digital Archivist'], 'credits': 'N/A'}})

   
# def test_change_password
def test_change_password():
    # Change the password
    old_password = 'PythonIsCool123!'
    new_password = 'object_orient'
    User.change_password(old_password, new_password)
    
    # Verify that the password has been changed
    # Create a new user object with the updated password
    updated_user = User('sconteh', 'object_orient', 'Samuel', 'Conteh')
    
     # Verify authentication with the new password
    assert updated_user.authenticate(new_password)

if __name__ == '__main__':
    unittest.main()