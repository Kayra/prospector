from app.models import DomainData, db
from config import DOMAIN_IMPORTANCE


class Ranker():

    def __init__(self, site_id):

        self.domain_scores = {
            "google_analytics": 9,
            "bing_analytics": 8,
            "robots": 9,
            "sitemap": 9
        }

        self.page_scores = {
            "h1s": 9,
            "h2s": 8,
            "h3s": 7,
            "alt_tags": 6,
            "meta_desc": 7,
            "title": 8,
            "view_state": 2,
            "pagination": 8,
            "iframe": 4,
            "flash": 3,
            "no_index_no_follow": 6,
            "schema_tag": 7,
            "blog_location": 8,
            "number_of_internal_links": {
                "high": {
                    19: 9
                },
                "medium": {
                    9: 7
                },
                "low": {
                    8: 5
                }
            },
            "url_character_length": {
                "high": {
                    150: 2
                },
                "medium": {
                    100: 4
                },
                "low": {
                    50: 7
                }
            }
        }
        self.rank_site(site_id)

    def calculate_domain_score(self, domain_data):

        fields_to_ignore = ['id', 'domain_url', 'site_name', 'ranking', 'level', 'pages']

        total_score = 0
        for field in self.domain_scores.items():
            if field[0] not in fields_to_ignore and getattr(domain_data, field[0]):
                total_score += self.domain_scores[field[0]]

        return total_score / len(self.domain_scores)

    def calculate_page_score(self, page_data):

        fields_to_ignore = ['id', 'site_id', 'page_url', 'number_of_internal_links', 'url_character_length']

        page_score = 0

        for field in self.page_scores.items():
            if field[0] not in fields_to_ignore and getattr(page_data, field[0]):
                page_score += self.page_scores[field[0]]

        page_score += self.calculate_number_based_score(self.page_scores['number_of_internal_links'], page_data.number_of_internal_links)
        page_score += self.calculate_number_based_score(self.page_scores['url_character_length'], page_data.number_of_internal_links)

        return page_score / len(self.page_scores)

    def calculate_number_based_score(self, score_field, data_field):
        field_score = score_field['low']
        for amount, score in score_field.items():
            if data_field > amount:
                field_score = score
        return field_score

    def domain_level_calculator(self, domain_rank):
        if (domain_rank / 25) < 1:
            return 'low'
        elif (domain_rank / 25) < 2:
            return 'midlow'
        elif (domain_rank / 25) < 3:
            return 'midhigh'
        elif (domain_rank / 25) < 4:
            return 'high'

    def rank_site(self, site_id):

        site = DomainData.query.get(site_id)

        domain_score = self.calculate_domain_score(site)

        average_page_score = sum(self.calculate_page_score(page) for page in site.pages) / len(site.pages)

        site.ranking = round((average_page_score + (domain_score * DOMAIN_IMPORTANCE)) / (1 + DOMAIN_IMPORTANCE))

        db.session.add(site)
        db.session.commit()
