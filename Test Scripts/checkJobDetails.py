# Open the link
driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")

# Verify job details
expected_title = "Quality Assurance Engineer"
expected_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
expected_requirements = "1. Minimum 2 years of experience in software testing..."
actual_title = driver.find_element_by_css_selector("#job-title").text
actual_description = driver.find_element_by_css_selector("#job-description").text
actual_requirements = driver.find_element_by_css_selector("#job-requirements").text

assert expected_title == actual_title
assert expected_description == actual_description
assert expected_requirements == actual_requirements
