"""Hugo test suite"""
# pylint: disable=no-member
import pytest
from selenium.webdriver.support.ui import WebDriverWait \
    # pylint: disable=import-error
from selenium.webdriver.common.by import By  # pylint: disable=import-error

DEFAULT_TIMEOUT = 15
SITENAME = "My New Hugo Site"


def get_default_url(url):
    """get the default URL for the site"""
    if url[-1] == "/":  # pylint: disable=no-else-return
        return url
    else:
        return url + "/"


def get_default_title():
    """Get the default title of the site"""
    return SITENAME


@pytest.mark.usefixtures("setup")
class TestHugo:
    """Class to analyse the web site"""

    def get_button_by_link_name(self, linktext):
        """get button from a specific link"""
        return self.driver.find_element(By.LINK_TEXT, linktext)

    def wait_for_page_to_load(self, url, title):
        """wait for a page to load"""
        self.driver.get(url)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            lambda driver: title in self.driver.title
        )

    def load_index_page(self, url):
        """Load the index page"""
        self.wait_for_page_to_load(url, get_default_title())

    def test_index_page(self, url):
        """check the index page is configured correctly"""
        page_url = get_default_url(url)
        page_title = "My Practice Area | " + get_default_title()

        self.load_index_page(url)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_index_page_00.png")

# RACI Post

    def test_first_post(self, url):
        """check the first post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/raci/"
        page_title = "Parts Unlimited | "+get_default_title()

        first_post = self.get_button_by_link_name("Parts Unlimited")
        first_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_first_post_00.png")

# postmortem test

    def test_postmortem(self, url):
        """check the postmortem post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/postmortem/"
        page_title = "Post Mortem | "+get_default_title()

        postmortem_post = self.get_button_by_link_name(
            "Post Mortem")  # new joiner post
        postmortem_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_Postmortem_00.png")

# pythoncircle

    def test_pythoncircle(self, url):
        """check the python post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/pythoncircle/"
        page_title = "Python Circle | "+get_default_title()

        pythoncircle_post = self.get_button_by_link_name(
            "Python Circle")
        pythoncircle_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_pythoncircle_00.png")

# Hailstone

    def test_hailstone(self, url):
        """check the hailstone post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/hailstone/"
        page_title = "Hailstone | "+get_default_title()

        hailstone_post = self.get_button_by_link_name(
            "Hailstone")
        hailstone_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_Hailstone_00.png")

# Kevin Bacon

    def test_kevinbacon(self, url):
        """check the kevin bacon post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/kevinbacon/"
        page_title = "Kevin Bacon | "+get_default_title()

        kevinbacon_post = self.get_button_by_link_name(
            "Kevin Bacon")
        kevinbacon_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_kevinbacon_00.png")

# CI and UX

    def test_ciux(self, url):
        """check the kevin bacon post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/ciux/"
        page_title = "CI and UX Tests | "+get_default_title()

        ciux_post = self.get_button_by_link_name(
            "CI and UX Tests")
        ciux_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_ciux_00.png")

# Logic Apps

    def test_logicapp(self, url):
        """check the logic app post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/logicapp/"
        page_title = "Logic Apps | "+get_default_title()

        logicapp_post = self.get_button_by_link_name(
            "Logic Apps")
        logicapp_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_logicapp_00.png")

# Terraform Planets

    def test_terraformplanets(self, url):
        """check the terraform planets post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/terraformplanets/"
        page_title = "Terraform Planets | "+get_default_title()

        terraformplanets_post = self.get_button_by_link_name(
            "Terraform Planets")
        terraformplanets_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_terraformplanets_00.png")

# Consultant Profile

    def test_consultantprofile(self, url):
        """check the consultant profile post is configured correctly"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"post/consultantprofile/"
        page_title = "Consultant Profile | "+get_default_title()

        consultantprofile_post = self.get_button_by_link_name(
            "Consultant Profile")
        consultantprofile_post.click()

        self.wait_for_page_to_load(page_url, page_title)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_consultantprofile_00.png")
