import selenium
from selenium import webdriver
import pandas as pd

def linkedin(skill,loc,exp,wd):
	url = 'https://www.linkedin.com/jobs/search/?keywords='
	url_skill = ' '.join(skill.split())
	url = url + url_skill + '&location=' + loc
	wd.get(url)
	try:
	    # container = wd.find_element_by_id("jobs-search__results-list")
	    lst = wd.find_elements_by_class_name("result-card")
	except:
	    pass
	data = [['Title','Company','ctc','experience','location','Description','skills_required','link']]
	i = 0
	for li in lst:
	    try:
	        name = li.find_element_by_class_name("result-card__title").text
	        link = li.find_element_by_class_name("result-card__full-card-link").get_attribute("href")
	    except:
	        continue
	    exp = 'Not Available'
	    try:
	        company = li.find_element_by_class_name("result-card__subtitle-link").text
	    except:
	        company = 'Not Available'
	    try:
	        loc = li.find_element_by_class_name("job-result-card__location").text
	    except:
	        loc = 'Not Available'
	    try:
	        jd = li.find_element_by_class_name("job-result-card__snippet").text
	    except:
	        jd = 'Not Available'
	    req_skills = 'Not Available'
	    sal = 'Not Available'
	    data.append([name,company,sal,exp,loc,jd,req_skills,link])
	    i+=1
	    if i==10:
	        break
	return pd.DataFrame(data[1:],columns=data[0])