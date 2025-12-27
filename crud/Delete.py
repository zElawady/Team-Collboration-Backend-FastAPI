from models import db_depends, Issue

def delete_issue(db:db_depends,
                 issue_id:int):
    issue = db.query(Issue).filter(Issue.id == issue_id).first()

    db.delete(issue)
    db.commit()

    return True
