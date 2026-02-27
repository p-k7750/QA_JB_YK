from pom_kawasaki_project.utils import search_item

class SearchPage:
    def __init__(self,page):
        self.page=page

    def search_item(self,item:str):
        search_item(self.page,item)
        text = self.page.locator("[id='OrigSearchString']").get_attribute("value")
        return text







