from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the web driver (change the path to your WebDriver executable)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open YouTube
driver.get("https://www.youtube.com")

try:
    # Find the search input field
    search_box = driver.find_element_by_name("search_query")

    # Enter the search query and submit
    search_box.send_keys("Python programming tutorial")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(3)

    # Verify search results
    video_results = driver.find_elements_by_css_selector(".style-scope ytd-video-renderer")
    
    if len(video_results) > 0:
        print("Search results found:")
        for idx, video in enumerate(video_results):
            video_title = video.find_element_by_id("video-title").text
            print(f"{idx + 1}. {video_title}")
    else:
        print("No search results found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser window
    driver.quit()
