import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_book_data():
    """
    Scrape book information from a sample bookstore website
    (which can be scraped!) --> 'Books to Scrape' sample website
    and convert to a pandas DataFrame

    """
    # setup Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # lists to store scraped data
    book_titles = []
    book_prices = []
    book_availability = []
    
    try:
        driver.get('http://books.toscrape.com/')
        
        # Wait book elements 
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product_pod'))
        )
        
        # find all book elements
        books = driver.find_elements(By.CLASS_NAME, 'product_pod')

        for book in books[:10]:  # first 10 books
            # get title, price, availability
            title = book.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
            book_titles.append(title)
            price = book.find_element(By.CLASS_NAME, 'price_color').text
            book_prices.append(price)
            availability = book.find_element(By.CLASS_NAME, 'instock').text
            book_availability.append(availability)

        df = pd.DataFrame({
            'Title': book_titles,
            'Price': book_prices,
            'Availability': book_availability
        })
        
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        # close the browser
        driver.quit()

if __name__ == '__main__':
    books_dataframe = scrape_book_data()
    
    if books_dataframe is not None:
        print(books_dataframe)
        
        # Optional
        books_dataframe.to_csv('scraped_books.csv', index=False)
        print("\nData saved to scraped_books.csv")
        
        
# obs: this script is just getting the first results from the main 
# page, for sections modificate according to necessity