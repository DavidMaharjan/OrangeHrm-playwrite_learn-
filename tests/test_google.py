import re 
from playwright.sync_api import  expect
def test_google(page):
    page.goto("https://www.google.com/ncr")
    try : 
        page.get_by_role("button",name="Accept all").click()
    except:
        print("no Popup")
    page.get_by_role("combobox",name="Search").fill("Playwright Python")
    page.expect(page.get_by_role("combobox",name="Search")).to_have_value("Playwright Python")
    page.keyboard.press("Enter")
   # expect(page).to_have_title(re.compile("Playwright Python",re.IGNORECASE))
    
    
