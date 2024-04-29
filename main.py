from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open the Click Counter website
driver.get("https://clickcounter.io")

# Find the counter element
counter_element = driver.find_element(By.ID, "currentValue")

# Record the start time
start_time = time.time()

# Set the counter to 2024
target_count = 2024
driver.execute_script(f"arguments[0].innerText = '{target_count}'", counter_element)

print(f"The counter has been set to {target_count}.")

# Wait until the counter reaches 2024
while int(counter_element.text.strip()) < 2024:
    time.sleep(1)  # Check the counter every second

# Record the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time

print(f"The counter reached 2024 in {duration:.2f} seconds.")

# Wait for an additional 10 seconds
time.sleep(10)

# Close the browser
driver.quit()
