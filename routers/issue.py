from fastapi.routing import APIRouter
from models.database import db_depends

from services.auth import user_depends
from fastapi import status, HTTPException

from crud import add_issue, update_issue, get_issue, delete_issue
from schemas import issue_requests, issue_respons


router = APIRouter(prefix='/issue', tags=['Issue'])

# End_points
## -> POST
@router.post('/add_issue/{project_id}',
             status_code=status.HTTP_201_CREATED,
             response_model=issue_respons)
async def create_issue(db:db_depends,
                       user:user_depends,
                       issue:issue_requests,
                       project_id:int):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='invalid user')

    new_issue = add_issue(db,issue,user.get('id'),project_id)
    return new_issue

## -> PUT
@router.put('/update_issue/{issue_id}',
            status_code=status.HTTP_200_OK,
            response_model=issue_respons)
async def inhanced_issue(db:db_depends,
                       user:user_depends,
                       issue_id:int,
                       issue:issue_requests):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='invalid user')

    issue_model = update_issue(db,user.get('id'),issue_id,issue)

    if issue_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    return issue_model

## -> GET
@router.get('/project_issue/{issue_id}',
            status_code=status.HTTP_200_OK,
            response_model=issue_respons)
async def project_issue(db:db_depends,
                        user:user_depends,
                        issue_id:int):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='invalid user')

    issue = get_issue(db, issue_id)
    return issue


## -> DELETE
@router.delete('/remove_issue/{issue_id}',
            status_code=status.HTTP_200_OK)
async def remove_issue(db:db_depends,
                       user:user_depends,
                       issue_id:int):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='invalid user')

    issue = delete_issue(db,issue_id)

    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not Found" )
    return "Done✅"