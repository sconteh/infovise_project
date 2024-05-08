
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

# def test_