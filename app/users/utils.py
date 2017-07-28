from app.prospector.models import db



def delete_site(site_to_delete):

    for page_to_delete in site_to_delete.pages:
        db.session.delete(page_to_delete)
    db.session.commit()

    db.session.delete(site_to_delete)
    db.session.commit()



def delete_user_account(user_id):
    pass
