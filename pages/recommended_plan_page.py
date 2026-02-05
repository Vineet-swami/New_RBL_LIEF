import pytest
from playwright.async_api import Page, expect


class SelectICICIPlan:
    def __init__(self, page):
        self.page = page
        self.icici_buy_button = page.locator("//p[text()='ICICI Pru Guaranteed Income For Tomorrow Pro']/../../../div//p[text()='Buy Now']")

    @pytest.mark.asyncio
    async def select_icici_plan(self):
        # 2️⃣ Scroll into view (CRITICAL)
        await self.icici_buy_button.scroll_into_view_if_needed()

        # 3️⃣ Ensure it is visible & enabled
        await expect(self.icici_buy_button).to_be_visible()
        await expect(self.icici_buy_button).to_be_enabled()

        await self.icici_buy_button.click()

        return self.page