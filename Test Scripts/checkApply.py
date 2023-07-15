# Click on the "Apply" button
driver.find_element_by_css_selector("#apply-button").click()

# Verify the redirect to the application form page
expected_url = "https://www.hashtag-ca.com/careers/application-form"
actual_url = driver.current_url

assert expected_url == actual_url
