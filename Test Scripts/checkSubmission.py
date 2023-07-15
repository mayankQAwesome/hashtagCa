# Fill in the required fields with valid data
driver.find_element_by_css_selector("#name").send_keys("John Doe")
driver.find_element_by_css_selector("#email").send_keys("john.doe@example.com")
driver.find_element_by_css_selector("#phone").send_keys("1234567890")

# Click on the "Submit" button
driver.find_element_by_css_selector("#submit-button").click()

# Verify the successful submission
# Add assertions or checks here based on the expected behavior
