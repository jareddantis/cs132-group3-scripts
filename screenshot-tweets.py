from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    # Open list of URLs
    with open('urls.txt', 'r') as f:
        urls = f.readlines()
    
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Load each URL
    for url in urls:
        driver.get(url)

        # Get Tweet ID from URL
        tweet_id = int(url.split('/')[-1])
        
        # Wait for page to finish loading by checking for tweet content element
        content_el = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, '//article[@data-testid="tweet" and @tabindex="-1"]')
        )

        # If the tweet contains an image, wait for it to load
        if content_el.find_elements(By.XPATH, './/div[@data-testid="tweetPhoto"]'):
            WebDriverWait(driver, 10).until(
                lambda d: d.find_element(By.XPATH, '//article[@data-testid="tweet" and @tabindex="-1"]//img[@alt="Image"]')
            )

        # Hide persistent layers to avoid screenshotting them
        driver.execute_script('document.querySelector("div.css-1dbjc4n.r-aqfbo4.r-gtdqiz.r-1gn8etr.r-1g40b8q").style.display = "none"')                         # Top bar
        driver.execute_script('document.querySelector("div.css-1dbjc4n.r-aqfbo4.r-1p0dtai.r-1d2f490.r-12vffkv.r-1xcajam.r-zchlnj").style.display = "none"')     # Bottom bar
        
        # Hide notifications modal if present
        if driver.find_elements(By.XPATH, '//div[@role="modal"]'):
            driver.execute_script('document.querySelector("div[role=modal]").style.display = "none"')
        
        # Save screenshot
        content_el.screenshot(f'{tweet_id}.png')
    
    driver.quit()
