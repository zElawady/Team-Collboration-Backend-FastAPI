from models import db_depends, Issue
from schemas import issue_requests

def update_issue(db:db_depends,
                 user_id:int,
                 issue_id:int,
                 issue:issue_requests):
    issue_model = db.query(Issue).filter(Issue.id == issue_id,
                                         Issue.assigned_to == user_id).first()

    issue_model.title = issue.title
    issue_model.description = issue.description
    issue_model.status = issue.status
    issue_model.priority = issue.priority

    db.add(issue_model)
    db.commit()
    db.refresh(issue_model)

    return issue_model
