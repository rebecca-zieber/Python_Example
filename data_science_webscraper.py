import requests
from bs4 import BeautifulSoup
from os.path import exists
from csv import writer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Identify experience and education levels for data science jobs on Glassdoor,
as well as desired tools/technologies.

Search specifications:
	- Keyword: Data Science
	- Location: Seattle, WA
	- Job Type: Full-time
	- Date Listed: Last Day

Desired information:
	- Job Title
	- Company Name
	- Experience
	- Education
	- Tools/Technologies
"""

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
gd_url = 'https://www.glassdoor.com/Job/seattle-data-science-jobs-SRCH_IL.0,7_IC1150505_KO8,20.htm?jobType=fulltime&fromAge=1'
driver.get(gd_url)

# Bypass webpage authentication
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
}
request = requests.get(gd_url, headers=header)
page_soup = BeautifulSoup(request.content, 'html.parser')

filename = "glassdoor_dataset.csv"
file_exists = exists(filename)
if not file_exists:
	fwriter = open(filename, "w")
	headers = "Company_Name,Job_Title\n"
	fwriter.write(headers)
	fwriter.close()

containers = page_soup.findAll("li", {"class":"react-job-listing job-search-key-nhtksm eigr9kq0"})

for container in containers:
	company = container.findAll("div", {"class":"d-flex justify-content-between align-items-start"})
	company_name = company[0].a.span.text.strip()
	company_name = company_name.replace(",", "|")

	title = page_soup.findAll("a", {"class":"jobLink job-search-key-1rd3saf eigr9kq1"})
	title_name = title[0].span.text.strip()
	title_name = title_name.replace(",", "|")

	with open(filename, 'a') as file_object:
		writer_object = writer(file_object)
		writer_object.writerow([str(company_name), str(title_name)])
		file_object.close()

driver.quit()
