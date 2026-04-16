from fastapi_demo.models.user_models import SignupDetails
import logging

# Simple in-memory storage for this example
mock_db = [
   {"first_name":"Imran", "last_name": "Khan", "email":"imran@gmail.com", "password":"Imran@123", "mobile": 8767876574, "age":41},
   {"first_name":"Vinay", "email":"vinay@gmail.com", "password":"India123", "mobile": 8000987098, "age":35}
]

log = logging.getLogger(__name__)

class ItemService:
    def createUser(self, signupDetails: SignupDetails):
        log.info(f'Adding user with email {signupDetails.email}')
        mock_db.append(signup_request)
        log.info(f'Added user with email {signupDetails.email}')

    def getAllUsers(self):
        log.info(f'Total numbers of users {len(mock_db)}')
        return mock_db

    def findUserByEmail(self, email:str):
        log.info(f'Finding user by email {email}......')

        for user in mock_db:
            if email.strip().upper() == user["email"].strip().upper():
                log.info(f'User details fetched : {user}')
                return user

        log.error(f'No user details fetched for this email: {email}')
        return None

    def deleteUserByEmail(self, email:str):
        log.info(f'Deleting user by email {email}......')
        log.info(f'Total users before deletion {len(mock_db)}.')

        # Find index of user
        user_found = False
        for index, user in enumerate(mock_db):
            if user["email"] == email:
                mock_db.pop(index)
                user_found = True
                break
    
        if not user_found:
            return False

        log.info(f'Total users after deletion {len(mock_db)}.')
        return True

# Instantiate a singleton
user_service = ItemService()

        

