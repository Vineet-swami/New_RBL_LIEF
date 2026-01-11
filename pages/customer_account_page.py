
from pages import life_assured_details_page


class CustomerAccountPage:
    def __init__(self, page):
        self.page = page
        self.cif_selector = page.locator("//input[@placeholder='Enter Customer ID']")
        self.get_details_button = page.locator("//button[contains(text(),'Get Details')]")
        self.customer_selector = page.locator("//div/child::div[   p[contains(text(),'Name')]   and   p[contains(text(),'Customer ID:')]   and   p[contains(text(),'Ankur Mishra')] ]")
        self.proceed_button = page.locator("//div/button[contains(text(), 'Proceed')]")

    async def enter_cif_and_get_details(self, cif_number: str):
        await self.cif_selector.fill(cif_number)
        await self.get_details_button.click()
        await self.customer_selector.wait_for(state="visible")
        await self.customer_selector.click()
        await self.proceed_button.wait_for(state="visible")
        await self.proceed_button.click()
        return life_assured_details_page.LifeAssuredDetailsPage(self.page)