import os
from pages.login_page import LoginPage
import pytest
from pages.suitability_matrix import SuitabilityMatrixPage

@pytest.mark.asyncio
async def test_click_proceed(page):
    login_page = LoginPage(page)
    product_selection = await login_page.login(
        os.getenv("EMPLOYEE_ID"),
        os.getenv("PASSWORD")
    )
    customer_account = await product_selection.select_product_by_name()
    relationship_with_proposer = await customer_account.enter_cif_and_get_details(
        os.getenv("CIF_NUMBER")
    )
    life_assured = await relationship_with_proposer.select_relationship_with_proposer(
        os.getenv("LIFE_ASSURED_NAME")
    )
    await page.wait_for_url("**/life/features", timeout=60_000)

    await life_assured.click_proceed()

    await life_assured.fill_suitability_matrix()

    assert "recommended-plans" in page.url