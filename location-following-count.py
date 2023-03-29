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

    # Load each Tweet URL
    user_locations = {}
    follow_counts = {}
    for url in urls:
        # Get username from URL
        username = url.split('/')[-3]
        if username in follow_counts:
            continue

        # Load profile page
        driver.get(f'https://twitter.com/{username}/following')

        # Get follow count element
        follow_count_el = WebDriverWait(driver, 2).until(
            lambda d: d.find_element(By.XPATH, f'//a[@href="/{username}/following"]')
        )
        
        # Get first <span> grandchild of follow count element
        follow_count = follow_count_el.find_element(By.XPATH, './/span').text
        print(f'@{username} is following {follow_count} accounts', end=' ')

        # Remove commas from follow count
        follow_count = follow_count.replace(',', '')
        follow_counts[username] = int(follow_count)

        # Get location element if present
        try:
            location_el = WebDriverWait(driver, 2).until(
                lambda d: d.find_element(By.XPATH, f'//span[@data-testid="UserLocation"]')
            )
        except:
            location = ''
            print(f'but did not specify a location in their profile.')
        else:
            # Get first <span> grandchild of element
            location = location_el.find_element(By.XPATH, './/span').text
            print(f'and is located in "{location}".')
        finally:
            user_locations[username] = location
    
    driver.quit()

    # Save follow counts to CSV file
    with open('following-count.csv', 'w') as f:
        for username, follow_count in follow_counts.items():
            f.write(f'{username},{follow_count}\n')

    # Save locations to TSV file
    with open('locations.tsv', 'w') as f:
        for username, location in user_locations.items():
            f.write(f'{username}\t{location}\n')
    