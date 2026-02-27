import re


class Global_Is_Valid_Mail:
    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None


class Global_Accept_Cookies:
    @staticmethod
    def accept_cookies(page):

        try:
            #page.wait_for_selector("#onetrust-accept-btn-handler", timeout=100)
            page.locator("#onetrust-accept-btn-handler").click()
            print("Cookies popup closed")
        except:
            print("Cookies popup not found")



def fill_contact_fields(page, first_name, last_name, email, city, postal_code, phone):
    page.locator("#FirstName").fill(first_name)
    page.locator("#LastName").fill(last_name)
    assert Global_Is_Valid_Mail.is_valid_email(email), f"Invalid email: {email}"
    page.locator("#Email").fill(email)
    page.locator("#City").fill(city)
    page.locator("#PostalCode").fill(postal_code)
    page.locator("#KmcPhone").fill(phone)



def search_item(page,valid_item:str):
    page.wait_for_timeout(10000)
    Search=page.locator("[id='searchEntry']")
    Search.click()
    Search.fill(valid_item)
    Search.press("Enter")