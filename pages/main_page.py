from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        #self.driver.get("https://www.amazon.com/")
        self.open_url()
        #sleep(10)

    def open_sub(self):
        self.open_url(end_url='/gp/product/B074TBCSC8')