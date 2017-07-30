from app.prospector.models import DomainData, DomainScores, PageScores, db


def delete_domain(domain_to_delete):

    for page_to_delete in domain_to_delete.pages:
        db.session.delete(page_to_delete)
    db.session.commit()

    db.session.delete(domain_to_delete)
    db.session.commit()


def delete_user_account(user_to_delete):

    sites_to_delete = DomainData.query.filter_by(owner=user_to_delete.id)

    for site_to_delete in sites_to_delete:
        delete_domain(site_to_delete)

    domain_scores_to_delete = DomainScores.query.filter_by(owner=user_to_delete.id).first()
    page_scores_to_delete = PageScores.query.filter_by(owner=user_to_delete.id).first()

    db.session.delete(domain_scores_to_delete)
    db.session.delete(page_scores_to_delete)
    db.session.commit()

    db.session.delete(user_to_delete)
    db.session.commit()
