# Click on the "Apply" button
driver.find_element_by_css_selector("#apply-button").click()

# Verify the pre-filled job code in the application form
expected_job_code = "QAE001"
actual_job_code = driver.find_element_by_css_selector("#job-code").get_attribute("value")

assert expected_job_code == actual_job_code
