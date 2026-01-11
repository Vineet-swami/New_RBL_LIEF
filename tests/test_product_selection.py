import os
from pages.login_page import LoginPage
from pages.product_selection_page import ProductSelectionPage
import pytest

@pytest.mark.asyncio
async def test_product_selection(page):
    login_page = LoginPage(page)
    product_selection = await login_page.login(
        os.getenv("EMPLOYEE_ID"),
        os.getenv("PASSWORD")
    )
    await product_selection.select_product_by_name()
    assert "customer-account" in page.url

