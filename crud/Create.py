from core.security import hash_password
from models import (User,
                    Team,
                    Team_member,
                    Project,
                    Issue)

from schemas import user_requests, team_requests, project_requests,issue_requests
from models import db_depends



def create_new_user(db:db_depends, user:user_requests):
    user_model = User(
        user_name = user.user_name,
        email = user.email,
        hashed_password = hash_password(user.password),
        role = user.role,
        is_active = user.is_active
    )

    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model

def new_team(db:db_depends,
             team:team_requests,
             user_id:int):
    team_model = Team(**team.model_dump(),
                      owner_id=user_id)

    db.add(team_model)
    db.commit()
    db.refresh(team_model)
    return team_model

def add_member(db:db_depends,
               user_id:int,
               team_id:int):
    team_member = Team_member(user_id=user_id,
                              team_id=team_id)
    db.add(team_member)
    db.commit()
    db.refresh(team_member)
    return team_member

def add_project(db:db_depends,
                project:project_requests,
                team_id:int):
    project_model = Project(**project.model_dump(),
                            team_id=team_id)
    db.add(project_model)
    db.commit()
    db.refresh(project_model)

    return project_model

def add_issue(db:db_depends,
          issue:issue_requests,
          user_id:int,
          project_id:int):
    issue_model = Issue(**issue.model_dump(),
                        project_id=project_id,
                        assigned_to=user_id)

    db.add(issue_model)
    db.commit()
    db.refresh(issue_model)

    return issue_model