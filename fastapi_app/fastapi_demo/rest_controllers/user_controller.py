from fastapi import APIRouter, HTTPException
from fastapi_demo.models.user_models import SignupDetails
from fastapi_demo.service.user_service import user_service
import logging
from typing import List

log = logging.getLogger(__name__)

#Define prefix of the controller and grouping all rest end points in user-actions
router = APIRouter(prefix="/user", tags=["user-actions"])

@router.post("/add-user")
async def addUser(signup_request: SignupDetails):
    log.info(f'Signing user {signup_request.first_name} with email {signup_request.email}.....')
    try:
        if isUserExists(signup_request):
            raise Exception("User already exists")
    except Exception as e:
        log.error(f"user already exists {signup_request.email}")
        raise HTTPException(status_code=409, detail=str(e))

    user_service.createUser(signup_request)

    log.info(f'User {signup_request.first_name} with email {signup_request.email} successfully registerd.')
    return {"user": f'{signup_request.first_name}',
            "status":"Registered"}


@router.get("/list")
async def getAllUsers():
    users = user_service.getAllUsers()
    log.info(f'Total numbers of users {len(users)}')
    return users


@router.get("/find/{email}")
async def findUserByEmail(email:str):
    log.info(f'Finding user by email {email}......')

    user = user_service.findUserByEmail(email)
    if user is not None:
        log.info(f'User details fetched for this email: {email}')
        return user
    else:
        log.error(f'No user details fetched for this email: {email}')
        raise HTTPException(status_code=404, detail=f'No user details found for this email {email}')
    
@router.delete("/delete/{email}")
async def deleteUserByEmail(email:str):
    log.info(f'Deleting user by email {email}......')

    is_user_deleted = user_service.deleteUserByEmail(email)
    
    if not is_user_deleted:
        raise HTTPException(status_code=404, detail=f"User with email {email} not found.")

    return {"user": f'User with email {email}',
            "status":"Deleted"}

def isUserExists(userDetails: SignupDetails):
    for user in users:
        if userDetails.email == user.email:
            return True