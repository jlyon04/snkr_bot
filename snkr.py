import requests
from bs4 import BeautifulSoup

# URL = "https://www.nike.com/launch/t/snkrs-classics-1"
URL = "https://www.nike.com/launch/t/air-jordan-6-neutral-grey"


class snkr_bot:
    def __init__(self):
        self.page = None
        self.soup = None
        self.section = None
        self.container = None
        self.size_chart = None

    def load_page(self) -> bool:
        self.page = requests.get(URL)
        if self.page is None:
            return
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def get_section(self):
        self.section = self.soup.find(
            "section",
            class_="card-product-component ncss-row bg-white mt0-sm mb2-sm mt7-lg mb7-md show-product",
        )

    def get_product_container(self):
        self.container = self.section.find(
            "aside",
            class_="product-info-container ncss-row ta-sm-c pt6-sm prl7-md pb6-sm pt0-lg pb0-lg",
        )

    def is_buyable(self) -> bool:
        self.size_chart = self.container.find(
            "div", class_="product-info ncss-col-sm-12 full ta-sm-c"
        )
        if self.size_chart is None:
            return False
        return True

    def setup(self):
        # LOAD PAGE
        self.load_page()
        if self.soup is None:
            print("Load Page Erorr")
            return False
        # LOAD SECTION
        self.get_section()
        if self.section is None:
            print("Get Section Error")
            return False
        # LOAD TABLE
        self.get_product_container()
        if self.container is None:
            print("Size Table Error")
            return False
        return True


def main():
    bot = snkr_bot()
    if bot.setup() is False:
        return

    if bot.is_buyable():
        print("buyable")
    else:
        print("WAIT WAIT")


if __name__ == "__main__":
    main()