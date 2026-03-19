# import pytest_asyncio
# import os
# from playwright.async_api import async_playwright
# from dotenv import load_dotenv

# load_dotenv()

# @pytest_asyncio.fixture
# async def page():
#     async with async_playwright() as p:
#         is_ci = os.getenv("CI") == "true"
#         headless = os.getenv("HEADLESS", "true").lower() == "true" if not is_ci else True
#         browser = await p.chromium.launch(headless=False, args=["--no-sandbox"])
#         context = await browser.new_context()
#         page = await context.new_page()
#         yield page
#         if not is_ci:
#             input("Press ENTER to close the browser...")
#         else:
#             await context.close()
#             await browser.close()

import pytest_asyncio
import os
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()


@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:

        # Detect Docker/CI environment
        is_ci = os.getenv("CI", "false").lower() == "true"

        # Headless configurable (default True in Docker/CI)
        headless = os.getenv("HEADLESS", "true").lower() == "true"

        browser = await p.chromium.launch(
            headless=headless,
            args=["--no-sandbox"]
        )

        context = await browser.new_context()
        page = await context.new_page()

        yield page

        if not is_ci:
            input("Press ENTER to close the browser...")
        else:
            await context.close()
            await browser.close()
