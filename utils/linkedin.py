import selenium
from selenium import webdriver
import pandas as pd

def linkedin(skill,loc,exp,wd):
	url = 'https://www.linkedin.com/jobs/search/?keywords='
	url_skill = ' '.join(skill.split())
	url = url + url_skill + '&location=' + loc
	wd.get(url)
	data = [['Title','Company','CTC','Experience','Location','Description','Required Skills','link']]
	try:
		lst = wd.find_element_by_class_name("jobs-search__results-list")
		lst = lst.find_elements_by_tag_name('li')
	except:
	    return pd.DataFrame(columns=data[0])
	for i,li in enumerate(lst):
		try:
			name = li.find_element_by_class_name("base-search-card__title").text
			link = li.find_element_by_class_name("base-card__full-link").get_attribute("href")
		except:
		    continue
		exp = 'Not Available'
		try:
			company = li.find_element_by_class_name("base-search-card__subtitle").text
		except:
		    company = 'Not Available'
		try:
			loc = li.find_element_by_class_name("job-search-card__location").text
		except:
		    loc = 'Not Available'
		try:
			jd = li.find_element_by_class_name("job-search-card__benefits").text
		except:
		    jd = 'Not Available'
		req_skills = 'Not Available'
		sal = 'Not Available'
		data.append([name,company,sal,exp,loc,jd,req_skills,link])
		if i==15:
			break
	return pd.DataFrame(data[1:],columns=data[0])