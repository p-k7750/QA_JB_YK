from pom_kawasaki_project.globals import url
from pom_kawasaki_project.pages.search_page import SearchPage

class ViewDetailPage(SearchPage):

    def __init__(self,page):
        super().__init__(page)

    def view_detail_item(self, item: str):
        self.page.wait_for_timeout(100)
        self.search_item(item)
        detail_button=self.page.locator("[class='blackBtn']").first
        detail_button.wait_for(state="visible", timeout=5000)
        link = detail_button.get_attribute("href")
        full_url = url + link
        self.page.goto(full_url)
        self.page.locator("button:has(span.headFive:text('POWER'))").first.click()
        power_td = self.page.locator("td.pTwo", has_text="hp").first
        power_text = power_td.text_content().strip()
        print("Power:", power_text)



