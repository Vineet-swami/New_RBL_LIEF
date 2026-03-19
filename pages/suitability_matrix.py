from playwright.async_api import Page, expect
import pytest
import os
from pages import recommended_plan_page

class SuitabilityMatrixPage:
    def __init__(self, page):
        self.page = page

        # Life_Assured_Selectors
        # Needed to be fill for non self only
        self.first_name_input = page.locator("//input[@placeholder='Enter First Name']")
        self.last_name_input = page.locator("//input[@placeholder='Enter Last Name']")
        self.date_of_birth_input = page.locator("//input[contains(@name,'dob')]")
        self.mobile = page.locator("//input[contains(@name,'contact_number')]")
        self.email = page.locator("//input[contains(@name,'email')]")

        # Required for self also
        self.proceed_button = page.locator("//button/child::p[contains(text(),'Proceed')]")
        self.life_assured_section = page.get_by_text("Assist us in identifying the customer's needs and goals, to recommend suitable plans", exact=True)

        # Life_Assured_Requirements Selectors
        self.education_dropdown = page.locator("//p[contains(text(),'Education of the Life Assured')]/ancestor::label/following-sibling::div")
        self.policies_dropdown = page.locator("//p[contains(text(),'How many insurance policies does the Life Assured already have?')]/ancestor::label/following-sibling::div")
        self.occupation_dropdown = page.locator("//p[contains(text(),'Occupation of the Life Assured')]/ancestor::label/following-sibling::div")
        self.cover_dropdown = page.locator("//p[contains(text(),'cover')]/ancestor::label/following-sibling::div")
        self.risk_taking = page.locator("//p[contains(text(),'Risk-taking')]/ancestor::label/following-sibling::div")
        self.annual_income = page.locator("//p[contains(text(),'Annual income')]/ancestor::label/following-sibling::div")
        self.age_range = page.locator("//p[contains(text(),'Age range')]/ancestor::label/following-sibling::div")
        self.life_stage = page.locator("//p[contains(text(),'Current life stage')]/ancestor::label/following-sibling::div")
        self.time_horizon = page.locator("//p[contains(text(),'Time horizon')]/ancestor::label/following-sibling::input")
        # self.next_button = page.locator("//button/child::p[contains(text(),'Next')]/ancestor::div[1]/preceding-sibling::div/child::p[contains(text(),'recommend suitable plans')]")
        self.next_button = self.page.get_by_role("button", name="Next")

    @pytest.mark.asyncio
    async def click_proceed(self):
        relationship_with_proposer = os.getenv("LIFE_ASSURED_NAME")
        if relationship_with_proposer.lower() != "self":
            first_name = os.getenv("LIFE_ASSURED_FIRST_NAME", "Test")
            await self.first_name_input.fill(first_name)

            last_name = os.getenv("LIFE_ASSURED_LAST_NAME", "User")
            await self.last_name_input.fill(last_name)

            dob = os.getenv("LIFE_ASSURED_DOB", "1990-01-01")
            await self.date_of_birth_input.fill(dob)    

            mobile_number = os.getenv("LIFE_ASSURED_MOBILE", "9876543210")
            await self.mobile.fill(mobile_number)

            email = os.getenv("LIFE_ASSURED_EMAIL", "test.user@example.com")
            await self.email.fill(email)

        # 1️⃣ Ensure the button is present in the DOM
        await expect(self.proceed_button).to_have_count(1)

        # 2️⃣ Scroll into view (CRITICAL)
        await self.proceed_button.scroll_into_view_if_needed()

        # 3️⃣ Ensure it is visible & enabled
        await expect(self.proceed_button).to_be_visible()
        await expect(self.proceed_button).to_be_enabled()

        # 4️⃣ Click
        await self.proceed_button.click()

        # 5️⃣ OPTIONAL: Small wait for UI reaction
        await self.page.wait_for_load_state("networkidle")

        await expect(self.life_assured_section).to_be_visible(timeout=30_000)
        await self.life_assured_section.click()

        # await self.education_dropdown.get_by_role("option", name="Graduate", exact=True).click()

    async def fill_suitability_matrix(self):
        await expect(self.education_dropdown).to_be_visible(timeout=30_000)
        await self.education_dropdown.click()
        await self.page.get_by_role("option", name="Graduate", exact=True).click()

        await self.policies_dropdown.click()
        await self.page.get_by_role("option", name="1-2", exact=True).click()

        await self.occupation_dropdown.click()
        await self.page.get_by_role("option", name="Salaried", exact=True).click()

        await self.cover_dropdown.click()
        await self.page.get_by_role("option", name="Savings", exact=True).click()

        await self.risk_taking.click()
        await self.page.get_by_role("option", name="Balanced", exact=True).click()

        await self.annual_income.click()
        await self.page.get_by_role("option", name="Less than 10,00,000", exact=True).click()

        await self.time_horizon.fill("5")
        await self.page.mouse.click(10, 10)

        await self.next_button.scroll_into_view_if_needed()
        await expect(self.next_button).to_be_visible()
        await expect(self.next_button).to_be_enabled()
        await self.next_button.click()

        await self.page.wait_for_url("**/recommended-plans", timeout=20_000)

        return recommended_plan_page.SelectICICIPlan(self.page)

