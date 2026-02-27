class SalePage:
    def __init__(self, page):
        self.page = page

    def sale(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator("#cat-21").click()
        self.page.locator("#nav-tab-1003").click()
        self.page.locator('img[alt="ELEKTRODE® 16 3/4 product view"]').click()
        self.page.locator('a[aria-label="click here to Buy the ELEKTRODE Buy Now"]').click()
        self.page.wait_for_selector('div.accessoryCategory[data-cat="1092"] span.price-msrp')
        prices_text = self.page.locator('div.accessoryCategory[data-cat="1092"] span.price-msrp').all_text_contents()
        prices = []
        for p in prices_text:
            num = float(p.replace("$", "").replace(",", "").strip())
            prices.append(num)
        valid_prices = [price
                        for price in prices
                        if 1000 <= price <= 1500
                        ]
        for price in prices:
            if price > 1000:
                print(price)
            elif price < 2500:
                 print("No product above 2500")
        return valid_prices

