import pages.customer_account_page as customer_account_page
from config.settings import BASE_URL
import pytest


class ProductSelectionPage:
    def __init__(self, page):
        self.page = page
        # self.product_selection_url = BASE_URL + "product-selection"
        self.product_card_selector = page.locator("//p[text()='Life']/parent::div")
        self.next_button_selector = page.locator("//button/child::p[contains(text(),'Next')]")

    @pytest.mark.asyncio
    async def select_product_by_name(self):
        await self.page.mouse.click(10, 10)
        await self.product_card_selector.wait_for(state="visible")
        await self.product_card_selector.click()
        await self.next_button_selector.wait_for(state="visible")
        await self.next_button_selector.click()

        return customer_account_page.CustomerAccountPage(self.page)

        