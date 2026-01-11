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
    relationship_with_proposer = await customer_account.enter_cif_and_get_details(
        os.getenv("CIF_NUMBER")
    )
    await relationship_with_proposer.select_relationship_with_proposer(
        os.getenv("LIFE_ASSURED_NAME")
    )
    popup = page.locator("text=The request for your consent has been sent")

    # popup may or may not appear (defensive)
    if await popup.count() > 0:
        await popup.wait_for(state="hidden", timeout=60_000)

    await page.wait_for_url("**/life/features", timeout=60_000)

    await page.mouse.click(10, 10)

    # assert True
    assert "life/features" in page.url