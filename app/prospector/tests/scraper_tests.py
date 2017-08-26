import unittest

from bs4 import BeautifulSoup

from app.prospector.scrapers import DomainScraper, PageScraper
from app.prospector.tests import scraper_test_html

no_valid_string = ""
invalid_string = "1234567890¡€#¢¢∞§¶•ªº"

class TestGoogleAnalytics(unittest.TestCase):

    def test_google_analytics_no_valid_string(self):
        valid_html = scraper_test_html.google_analytics_valid_html
        test_soup = BeautifulSoup(valid_html, "html.parser")
        scraped_value = DomainScraper.scrape_google_analytics(test_soup)
        self.assertNotEquals(scraped_value, None)

    def test_google_analytics_invalid_strings(self):
        test_soup = BeautifulSoup(no_valid_string, "html.parser")
        scraped_value = DomainScraper.scrape_google_analytics(test_soup)
        self.assertEquals(scraped_value, None)

    def test_google_analytics_valid_strings(self):
        test_soup = BeautifulSoup(invalid_string, "html.parser")
        scraped_value = DomainScraper.scrape_google_analytics(test_soup)
        self.assertEquals(scraped_value, None)


class TestBingAnalytics(unittest.TestCase):

    def test_bing_analytics_no_valid_string(self):
        self.assertEquals(True, False)

    def test_bing_analytics_invalid_strings(self):
        self.assertEquals(True, False)

    def test_bing_analytics_valid_strings(self):
        self.assertEquals(True, False)


class TestHeaderTagScraper(unittest.TestCase):

    def test_header_tag_no_valid_string(self):
        self.assertEquals(True, False)

    def test_header_tag_invalid_strings(self):
        self.assertEquals(True, False)

    def test_header_tag_valid_strings(self):
        self.assertEquals(True, False)


class TestAltTagScraper(unittest.TestCase):

    def test_alt_tag_no_valid_string(self):
        self.assertEquals(True, False)

    def test_alt_tag_invalid_strings(self):
        self.assertEquals(True, False)

    def test_alt_tag_valid_strings(self):
        self.assertEquals(True, False)


class TestMetaDescriptionScraper(unittest.TestCase):

    def test_meta_description_no_valid_string(self):
        self.assertEquals(True, False)

    def test_meta_description_invalid_strings(self):
        self.assertEquals(True, False)

    def test_meta_description_valid_strings(self):
        self.assertEquals(True, False)


class TestTitleTextScraper(unittest.TestCase):

    def test_title_text_no_valid_string(self):
        self.assertEquals(True, False)

    def test_title_text_invalid_strings(self):
        self.assertEquals(True, False)

    def test_title_text_valid_strings(self):
        self.assertEquals(True, False)


class TestViewStateScraper(unittest.TestCase):

    def test_view_state_no_valid_string(self):
        self.assertEquals(True, False)

    def test_view_state_invalid_strings(self):
        self.assertEquals(True, False)

    def test_view_state_valid_strings(self):
        self.assertEquals(True, False)


class TestPaginationScraper(unittest.TestCase):

    def test_pagination_no_valid_string(self):
        self.assertEquals(True, False)

    def test_pagination_invalid_strings(self):
        self.assertEquals(True, False)

    def test_pagination_valid_strings(self):
        self.assertEquals(True, False)


class TestIframeContentScraper(unittest.TestCase):

    def test_iframe_content_no_valid_string(self):
        self.assertEquals(True, False)

    def test_iframe_content_invalid_strings(self):
        self.assertEquals(True, False)

    def test_iframe_content_valid_strings(self):
        self.assertEquals(True, False)


class TestFlashAttributeScraper(unittest.TestCase):

    def test_flash_attribute_no_valid_string(self):
        self.assertEquals(True, False)

    def test_flash_attribute_invalid_strings(self):
        self.assertEquals(True, False)

    def test_flash_attribute_valid_strings(self):
        self.assertEquals(True, False)


class TestNoIndexNoFollowAttributeScraper(unittest.TestCase):

    def test_no_index_no_follow_attribute_no_valid_string(self):
        self.assertEquals(True, False)

    def test_no_index_no_follow_attribute_invalid_strings(self):
        self.assertEquals(True, False)

    def test_no_index_no_follow_attribute_valid_strings(self):
        self.assertEquals(True, False)


class TestSchemaTagsScraper(unittest.TestCase):

    def test_schema_tags_no_valid_string(self):
        self.assertEquals(True, False)

    def test_schema_tags_invalid_strings(self):
        self.assertEquals(True, False)

    def test_schema_tags_valid_strings(self):
        self.assertEquals(True, False)


class TestBlogLocationsScraper(unittest.TestCase):

    def test_blog_locations_no_valid_string(self):
        self.assertEquals(True, False)

    def test_blog_locations_invalid_strings(self):
        self.assertEquals(True, False)

    def test_blog_locations_valid_strings(self):
        self.assertEquals(True, False)


class TestNumberOfInternalLinksScraper(unittest.TestCase):

    def test_number_of_internal_links_no_valid_string(self):
        self.assertEquals(True, False)

    def test_number_of_internal_links__invalid_strings(self):
        self.assertEquals(True, False)

    def test_number_of_internal_links_valid_strings(self):
        self.assertEquals(True, False)
