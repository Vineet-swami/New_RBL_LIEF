from multiprocessing import context
import os
from conftest import page
from pages import suitability_matrix

class LifeAssuredDetailsPage:
    def __init__(self, page):
        self.page = page
        self.life_assured_name_input = page.locator("//div/child::div[contains(text(),'Select Relationship')]")
        self.rbl_customer = page.locator("//span[contains(text(),'Life Assured is not a RBL Bank customer')]/preceding-sibling::span")
        self.next_button = page.locator("//button/child::p[contains(text(),'NEXT')]")

    async def select_relationship_with_proposer(self, life_assured_name: str):
        await self.life_assured_name_input.click()
        await self.page.wait_for_timeout(1000)  # Wait for options to load
 
        await self.page.get_by_role("option", name=life_assured_name).click()
        await self.page.wait_for_timeout(1000)
        if life_assured_name.lower() != "self":
            await self.rbl_customer.wait_for(state="visible")
            await self.rbl_customer.click(force=True)

        await self.next_button.click()
        return suitability_matrix.SuitabilityMatrixPage(self.page)



