from models import db_depends
from models import Team, Project, Issue


def get_all_teams(db:db_depends,
                  user_id:int):
    teams = db.query(Team).filter(Team.owner_id == user_id).all()
    return teams

def get_all_projects(db:db_depends,
                     team_id:int):
    project_model = db.query(Project).filter(Project.team_id == team_id).all()
    return project_model

def get_issue(db:db_depends,
              issue_id:int):
    issue = db.query(Issue).filter(Issue.id == issue_id).first()

    return issue