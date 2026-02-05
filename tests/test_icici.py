import os
from pages.login_page import LoginPage
import pytest

@pytest.mark.asyncio
async def test_icici(page):
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

    recommended_plan = await life_assured.fill_suitability_matrix()

    await recommended_plan.select_icici_plan()

    assert "proposal" in page.url


