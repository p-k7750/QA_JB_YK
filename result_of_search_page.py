from pom_kawasaki_project.utils import search_item

class ResultPage:

    def __init__(self,page):
        self.page = page

    def get_not_exist_search_results(self, invalid_item: str):
        self.page.wait_for_timeout(10000)
        search_item(self.page,invalid_item)
        result = self.page.locator("[class='pTwo text-center']")
        result.wait_for(state="visible",timeout=1500)
        text = result.text_content()
        return text

    def get_exist_search_results(self,valid_item:str):
        search_item(self.page,valid_item)
        text = self.page.locator("[id='OrigSearchString']").get_attribute("value")
        return text



