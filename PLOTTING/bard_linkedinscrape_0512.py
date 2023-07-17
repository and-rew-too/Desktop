from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from bs4 import BeautifulSoup
import time


#info below
#https://maoviola.medium.com/a-complete-guide-to-web-scraping-linkedin-job-postings-ad290fcaa97f
#https://stackoverflow.com/questions/72854116/selenium-attributeerror-webdriver-object-has-no-attribute-find-element-by-cs
#https://www.scrapingbee.com/blog/web-scraping-youtube/
#https://selenium-python.readthedocs.io/locating-elements.html#locating-elements

#PATH = input("https://www.linkedin.com/jobs/search/?currentJobId=3588916686&f_WT=3&geoId=103644278&keywords=test%20engineer")
#USERNAME = input("andrewhu98@berkeley.edu")
#PASSWORD = input("C0llegeru1e$")
#print(USERNAME)
#print(PASSWORD)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.linkedin.com/login')
email_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
email_input.send_keys('andrewhu98@berkeley.edu')
password_input.send_keys('C0llegeru1e$')
password_input.send_keys(Keys.ENTER)
time.sleep(4)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3588916686&f_WT=3&geoId=103644278&keywords=test%20engineer")
soup = BeautifulSoup(driver.page_source, 'html.parser')


jobs_lists = driver.find_element(By.CLASS_NAME,"jobs-search-results-list")
jobs = jobs_lists.find_elements(By.TAG_NAME,("li")) # return a list

print(type(jobs))
#len(jobs)

job_id = []
job_title = []
location = []
for job in jobs:
    job_id0 = job.get_attribute("data-row")
    job_id.append(job_id0)

#    location0 = job.find_element(By.CLASS_NAME,"artdeco-entity-lockup__subtitle ember-view").text   #.text
#    location.append(location0)


 #   job_title0 = job.find_element(By.CLASS_NAME,("h3").get_attribute("innerText"))
 #   job_title.append(job_title0)

jd = []
seniority = []
for item in range(len(jobs)):
#    job_func0 = []
#    industries0 = []
    # clicking job to view job details
#    job_click_path = f’ / html / body / main / div / section[2] / ul / li[{item + 1}] / img’
  #  driver.find_element(By.XPATH()).click()
    #this works for no login job_click_path =f"/html/body/div[1]/div/main/section[2]/ul/li[{item+1}]/div/a"
    job_click_path = f"/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{item+1}]/div/div[1]"
    job_click = job.find_element(By.XPATH,job_click_path).click()
    time.sleep(6)

    #qualifications_section = job.find_element(By.CSS_SELECTOR,"css=div[title='jobs-description__content.jobs-description-content']")
    #qualifications_section = job.find_element(By.XPATH,("/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[4]/article/div/div[1]"))
    qualifications_section = driver.find_element_by_id("job-details-2973930316")
    qualifications_text = qualifications_section.text

print(qualifications_text)