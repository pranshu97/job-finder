import selenium
from selenium import webdriver
import pandas as pd

def shine(skill,loc,exp,wd):
	url = 'https://www.shine.com/job-search/'
	url_skill = '-'.join(skill.split())
	url = url + url_skill + '-jobs-in-' + loc
	wd.get(url)

	data = [['Title','Company','CTC','Experience','Location','Description','Required Skills','link']]
	try:
		container = wd.find_element_by_id("id_results")
		lst = container.find_elements_by_class_name("result-display__profile")
	except:
	    return pd.DataFrame(columns=data)

	for i,li in enumerate(lst):
		try:
			title = li.find_element_by_tag_name("a")
			link = title.get_attribute("href")
			name = title.text
		except:
		    continue
		try:
			experience = li.find_elements_by_class_name("result-display__profile__years")[0].text #[0]
		except:
		    exp = 'Not Available'
		try:
			company = li.find_element_by_class_name("result-display__profile__company-name").text
		except:
			company = 'Not Available'
		try:
			loc = li.find_elements_by_class_name("result-display__profile__years")[1].text
		except:
			loc = 'Not Available'
		jd = 'Not Available'
		req_skills = 'Not Available'
		sal = 'Not Available'
		data.append([name,company,sal,experience,loc,jd,req_skills,link])
		if i==15:
			break
	return pd.DataFrame(data[1:],columns=data[0])