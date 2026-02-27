from urllib.parse import urljoin
from pom_kawasaki_project.globals import url

class ReviewPage:
    def __init__(self,page):
        self.page=page

    def select_vehicle_category(self):

        award_and_review_button = self.page.locator('a.pTwo[href="/en-us/research-tools/awards"]')
        award_link = award_and_review_button.get_attribute("href")
        full_url = urljoin(url, award_link)
        self.page.goto(full_url)
        element = self.page.locator('a[href="/en-us/research-tools/awards/side-x-side"]')
        element.wait_for(state="visible")
        side_x_side_link = element.get_attribute("href")
        full_url_side_x_side = urljoin(url, side_x_side_link)
        self.page.goto(full_url_side_x_side)
        checkboxes = self.page.locator("div.typeFilters input.filter-checkbox")
        count = checkboxes.count()

        for i in range(count):
             checkboxes.nth(i)
        print(f"Found {count} All marked\n")

        for i in range(count):
            checkbox = checkboxes.nth(i)

            if not checkbox.is_checked():
                checkbox.check()
                print(f"checkbox {i + 1} marked ")
        for i in range(count):
            checkbox = checkboxes.nth(i)

            if checkbox.is_checked():
                checkbox.uncheck()
                print(f"checkbox {i + 1} Removed ")





