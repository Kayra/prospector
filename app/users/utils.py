from app.prospector.models import db


def delete_site(site_to_delete):

    for page_to_delete in site_to_delete.pages:
        db.session.delete(page_to_delete)
    db.session.commit()

    db.session.delete(site_to_delete)
    db.session.commit()


def delete_user_account(user_to_delete):

    sites_to_delete = DomainData.query.filter_by(owner=user_to_delete.id)

    for site_to_delete in site_to_delete:
        delete_site(site_to_delete)

    db.session.delete(user_to_delete)
    db.session.commit()

