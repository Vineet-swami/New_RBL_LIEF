from config.settings import BASE_URL
from playwright.async_api import Page
import pytest
from pages import product_selection_page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_url = BASE_URL + "backdoor-login"
        self.employee_id_input = page.locator("//input[contains(@placeholder,'Enter Employee ID.')]")
        self.password_input = page.locator("//input[contains(@placeholder,'Enter Password.')]")
        self.login_button = page.locator("//button[contains(text(),'LOGIN')]")


    @pytest.mark.asyncio
    async def login(self, employee_id: str, password: str) -> product_selection_page.ProductSelectionPage:
        await self.page.goto(self.login_url)
        await self.employee_id_input.fill(employee_id)
        await self.password_input.fill(password)
        await self.login_button.click()

        await self.page.wait_for_url("**/product-selection")
        return product_selection_page.ProductSelectionPage(self.page)