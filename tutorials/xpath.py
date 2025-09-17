from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #xpath by attribute
    #tagname[@attribute='value']
    username=page.wait_for_selector("//input[@name='username']")
    username.fill("Admin")
    password=page.wait_for_selector("//input[@placeholder='Password']")
    password.fill("admin123")
    login=page.wait_for_selector("//button[@type='submit']")
    login.click()
    page.wait_for_timeout(5000)
    browser.close()
    #text - //tagname[text()="text"]
    # page.wait_for_selector("//p[text()='Forgot your password?']").click()
    # page.wait_for_timeout(5000)
    
    #contains 
    #attributes - //tagname[contains(@attribute,'value')]
    #text - //tagname[contains(text(),'text')]
    
    
    
    
    
    
