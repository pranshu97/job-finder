import selenium
from selenium import webdriver
import pandas as pd

def indeed(skill,loc,exp,wd):
	url = 'https://www.indeed.co.in/jobs?q='
	url_skill = '+'.join(skill.split())
	url = url + url_skill + '&l=' + loc
	wd.get(url)
	data = [['Title','Company','CTC','Experience','Location','Description','Required Skills','link']]
	try:
	    container = wd.find_element_by_id("resultsCol")
	    divs = container.find_elements_by_xpath('div[@class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')
	except:
	    return pd.DataFrame(columns=data[0])
	for i, div in enumerate(divs):
	    try:
	        title = div.find_element_by_class_name("title").find_element_by_tag_name("a")
	        name = title.text
	        link = title.get_attribute("href")
	    except:
	        continue
	    try:
	        company = div.find_element_by_class_name("company").text
	    except:
	        company='Not Available'
	    try:
	        sal = div.find_element_by_class_name("salaryText").text
	    except:
	        sal = 'Not Available'
	    try:
	        location = div.find_element_by_xpath('//div[@class="location accessible-contrast-color-location"]').text
	    except:
	        location='Not Available'
	    try:
	        jd = div.find_element_by_class_name("summary").text
	    except:
	        jd = 'Not Available'
	    exp = 'Not Available'
	    req_skills = 'Not Available'
	    data.append([name,company,sal,exp,location,jd,req_skills,link])
	    if i==15:
	        break
	return pd.DataFrame(data[1:],columns=data[0])