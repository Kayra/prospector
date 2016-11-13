from config import DOMAIN_IMPORTANCE

from app.models import DomainScores, PageScores


class Ranker():

    def __init__(self):

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

    def calculate_domain_score(self, domain_data):

        fields_to_ignore = ['id', 'domain_url', 'site_name', 'ranking', 'level', 'pages']

        domain_scores = DomainScores.query.one()

        scores = 0
        for column in domain_scores.__table__.columns:
            if column.name not in fields_to_ignore:
                scores += 1

        total_domain_score = 0
        for column in domain_data.__table__.columns:

            column_data = getattr(domain_data, column.name)

            if column_data and column.name not in fields_to_ignore and column.name in domain_scores.__table__.columns:
                total_domain_score += getattr(domain_scores, column.name)

        return total_domain_score / scores

    def calculate_page_score(self, page_data):

        fields_to_ignore = ['id', 'site_id', 'page_url', 'number_of_internal_links', 'url_character_length']

        total_page_score = 0

        for field in self.page_scores.items():
            if field[0] not in fields_to_ignore and getattr(page_data, field[0]):
                total_page_score += self.page_scores[field[0]]

        total_page_score += self.calculate_number_based_score(self.page_scores['number_of_internal_links'], page_data.number_of_internal_links)
        total_page_score += self.calculate_number_based_score(self.page_scores['url_character_length'], page_data.number_of_internal_links)

        return total_page_score / len(self.page_scores)

    def calculate_number_based_score(self, score_field, page_data_field):

        field_score = list(score_field['low'].values())[0]

        for label, score in score_field.items():
            if page_data_field > list(score.keys())[0]:
                field_score = list(score.values())[0]

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

    def rank_site(self, domain_data):

        domain_score = self.calculate_domain_score(domain_data)

        average_page_score = sum([self.calculate_page_score(page) for page in domain_data.pages]) / domain_data.pages.count()

        return round((average_page_score + (domain_score * DOMAIN_IMPORTANCE)) / (1 + DOMAIN_IMPORTANCE))
