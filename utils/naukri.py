#PASS WEBDRIVER IN PARAMETERS 
import selenium
from selenium import webdriver
import pandas as pd

def naukri(skill,loc,exp,wd):
	url = 'https://www.naukri.com/'
	url_skill = '-'.join(skill.split())
	url = url + url_skill + '-jobs-in-' + loc + '?experience=' + str(exp)
	wd.get(url)
	data = [['Title','Company','CTC','Experience','Location','Description','Required Skills','link']]
	try:
	    div = wd.find_element_by_class_name("list")
	    article = div.find_elements_by_tag_name("article")
	except:
	    return pd.DataFrame(columns=data[0])
	for i,art in enumerate(article):
	    try:
	        a = art.find_elements_by_tag_name("a")
	        name = a[0].text
	        link = a[0].get_attribute("href")
	        company = a[1].text
	    except:
	        continue
	    try:
	        ul = art.find_elements_by_tag_name("ul")
	        li = ul[0].find_elements_by_tag_name("li")
	        try:
	            experience = li[0].text
	        except:
	            experience = "Not Available"
	        try:
	            ctc = li[1].text
	        except:
	            ctc = "Not Available"
	        try:
	            location = li[2].text
	        except:
	            location = loc
	        try:
	            lst = [i for i in ul[1].text.split('\n')]
	            req_skills = ' '.join(lst)
	        except:
	            req_skills = "Not Available"
	    except:
	        continue
	    try:
	        div = art.find_elements_by_tag_name("div")
	        jd = div[3].text
	    except:
	        jd = "Not Available"
	    data.append([name,company,ctc,experience,location,jd,req_skills,link])
	    if i==15:
	    	break
	return pd.DataFrame(data[1:],columns=data[0])

