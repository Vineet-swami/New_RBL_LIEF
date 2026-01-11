import os

import pytest
from pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_login(page):
    print(">>> TEST STARTED")
    login_page = LoginPage(page)
    await login_page.login(
        os.getenv("EMPLOYEE_ID"),
        os.getenv("PASSWORD")
    )
    print(">>> TEST FINISHED")
    assert "product-selection" in page.url
