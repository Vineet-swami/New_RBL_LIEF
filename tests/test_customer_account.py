import os
from pages.login_page import LoginPage
import pytest   

@pytest.mark.asyncio
async def test_customer_account(page):
    login_page = LoginPage(page)
    product_selection = await login_page.login(
        os.getenv("EMPLOYEE_ID"),
        os.getenv("PASSWORD")
    )
    customer_account = await product_selection.select_product_by_name()
    await customer_account.enter_cif_and_get_details(
        os.getenv("CIF_NUMBER")
    )
    
    assert "life-assured" in page.url