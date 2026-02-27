from playwright.sync_api import expect
from pom_kawasaki_project.globals import target_text,email,first_name,last_name,city,postal_code,phone
from pom_kawasaki_project.utils import fill_contact_fields


class MenuPage:
    def __init__(self,page):
        self.page=page

    def  top_menu_fill_detail(self):
        self.page.wait_for_timeout(10000)
        self.page.locator(".rightBar a").all()
        link = self.page.locator(".rightBar a", has_text="TEST RIDE")
        #expect(link).to_be_visible()
        link.click()
        select_element = self.page.locator("#favoriteProductCategory")
        expect (select_element).to_be_visible(timeout=10000)
        options = select_element.locator("option")
        for i in range(options.count()):
            option_text = options.nth(i).inner_text().strip()
            if option_text == target_text:
                value_to_select = options.nth(i).get_attribute("value")
                select_element.select_option(value=value_to_select)
        fill_contact_fields(page=self.page,first_name=first_name,last_name=last_name,email=email,city=city,postal_code=postal_code,phone=phone)