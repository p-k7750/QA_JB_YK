from pom_kawasaki_project.pages.fill_contact_info_page import MenuPage
from pom_kawasaki_project.pages.Select_checkbox_page import ReviewPage
from pom_kawasaki_project.pages.result_of_search_page import ResultPage
from pom_kawasaki_project.pages.view_detail_page import ViewDetailPage
from pom_kawasaki_project.globals import url, invalid_item, valid_item
from pom_kawasaki_project.utils import Global_Accept_Cookies
from pom_kawasaki_project.pages.buy_product import SalePage

class Test_of_Kawasaki_Site:

    def test_result_search_valid_item(self,setup_playwright_project):
        """
        Purpose of the test: Search for a valid product on the site.
        If the product is not found in the results, return the result in assert.
        Steps:
        1.Open the main page.
        2.Accept cookie.
        2.Search for a valid item.
        3.Verify the item appears in results.
        Expected Result:
        The searched product should be displayed in the results search.
        """
        page=setup_playwright_project
        page.goto(url)
        Global_Accept_Cookies.accept_cookies(page)
        result_page = ResultPage(page)
        text = result_page.get_exist_search_results(valid_item)
        assert valid_item  in text, "Entered not valid item — failing test"

    def test_result_search_invalid_item(self,setup_playwright_project):
        """
        Purpose of the test: Search for invalid product on the site.
        If 0 is found in the results of appear at the bottom of the page,
        return the result in assert.
        Steps:
        1.Open the main page.
        2.Accept cookie.
        3.Search for invalid item.
        4.Verify the item appears in at the bottom of the page.
        Expected Result:
        The searched product should be displayed in the results search.
        """
        page = setup_playwright_project
        page.goto(url)
        Global_Accept_Cookies.accept_cookies(page)
        result_page = ResultPage(page)
        text = result_page.get_not_exist_search_results(invalid_item)
        assert "0" not in text, "Not found product — failing test"

    def test_view_detail_of_product(self, setup_playwright_project):
        """
        Purpose of the test: view detail of product on the site.
        Steps:
        1.Open the main page.
        2.Accept cookie.
        3.Search for a valid item.
        4.Click on VIEW SPACE AND DETAIL.
        5.On the product page click on POWER.
        6.Print HORSE POWER.
        Expected Result:
        return the result in assert if not found Keyword of valid item in url.
        """
        page = setup_playwright_project
        page.goto(url)
        Global_Accept_Cookies.accept_cookies(page)
        view_detail_page=ViewDetailPage(page)
        view_detail_page.view_detail_item(valid_item)
        assert "klx" in page.url.lower(), f"Expected 'klx' in URL, got {page.url}"

    def test_of_fill_contact_info(self, setup_playwright_project):
        """
        Purpose of the test: fill contact information and check valid mail.
        Steps:
        1.Open the main page.
        2.Accept cookie.
        3.Select TEST RIDE from the top menu.
        4.Selects one of the options from SELECT A VEHICLE CATEGORY.
        5.Fills in all fields.
        Expected Result:
        return the result in assert if email is invalid.
        """
        page = setup_playwright_project
        page.goto(url)
        Global_Accept_Cookies.accept_cookies(page)
        menu_detail_page = MenuPage(page)
        menu_detail_page.top_menu_fill_detail()

    def test_Select_checkbox(self, setup_playwright_project):
        """
        Purpose of the test: Actions on checkboxes.
        Steps:
        1.Open the main page.
        2.Accept cookie.
        3.In NEWS at the end of the page, click on Awards & Reviews.
        4.Selects one of the options.
        5.Check all checkboxes.
        6.Uncheck all checkboxes
        """
        page = setup_playwright_project
        page.goto(url)
        review_page = ReviewPage(page)
        review_page.select_vehicle_category()

    def test_buy_product(self, setup_playwright_project):
        """
        Purpose of the test: String operations Loop operations Conditional operations and data retrieval.
        Steps:
        1.Open the main page.
        2.Accept cookie.
        3.Select ELECTRIFICATION from the top menu.
        4.Select ELECTRODE from the sub menu.
        5.Choose ELECTRODE16.
        6.Click on BUY NOW.
        7.Print all prices of products on the page.
        Expected Result:
        return the result in assert if found in the price range 1000-1500.
        """
        page = setup_playwright_project
        page.goto(url)
        sale_product_page = SalePage(page)
        valid_prices = sale_product_page.sale()
        assert   valid_prices, "No products found in the price range 1000-1500."




