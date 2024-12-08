from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def google_search(search_term):
    """
    Perform a simple Google search and print the first few result 
    
    Prerequisites:
    - Install required libraries:
      pip install selenium webdriver-manager
    """
    # Setup Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # go toGoogle
        driver.get('https://www.google.com')
        
        # Find search input box
        search_box = driver.find_element(By.NAME, 'q')
        
        # Type search term
        search_box.send_keys(search_term)
        
        #  ENTER to search
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results to load
        time.sleep(5)
        
        # print first 5 result titles
        results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        print(f"Search Results for '{search_term}':")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # close browser
        driver.quit()

if __name__ == '__main__':
    google_search('python automation')