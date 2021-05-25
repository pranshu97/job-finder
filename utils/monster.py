import selenium
from selenium import webdriver
import pandas as pd

def monster(skill,loc,exp,wd):
	url = 'https://www.monsterindia.com/srp/results?query='
	url_skill = '%20'.join(skill.split())
	url=url+url_skill+'&locations='+loc+'&experienceRanges='+exp+'~'+exp+'&experience='+exp
	wd.get(url)
	data = [['Title','Company','ctc','experience','location','Description','skills_required','link']]
	try:
	    container = wd.find_elements_by_xpath('//div[@class="srp-right-part"]/div[@class="srp-left"]/div/div/div')[2]
	    divs = container.find_elements_by_class_name("card-apply-content")
	except:
	    return pd.DataFrame(columns=data[0])
	i = 0
	for div in divs:
	    try:
	        title = div.find_element_by_class_name("medium").find_element_by_tag_name("a")
	        name = title.text
	        link = title.get_attribute("href")
	    except:
	        continue
	    try:
	        company = div.find_element_by_class_name("company-name").find_element_by_tag_name("a").text
	    except:
	        company = 'Not Available'
	    try:
	        location = div.find_elements_by_class_name("loc")[0].text
	    except:
	        location = 'Not Available'
	    try:
	        exp = div.find_elements_by_class_name("loc")[1].text
	    except:
	        exp = 'Not Available'
	    try:
	        ctc = div.find_elements_by_class_name("loc")[2].text
	    except:
	        ctc = 'Not Available'
	    try:
	        jd = div.find_element_by_class_name("job-descrip").text
	    except:
	        jd = 'Not Available'
	    try:
	        req_skills = div.find_element_by_class_name("descrip-skills").text
	        req_skills = req_skills[9:]
	    except:
	        req_skills = 'Not Available'
	    data.append([name,company,ctc,exp,location,jd,req_skills,link])
	    i+=1
	    if i==10:
	        break
	return pd.DataFrame(data[1:],columns=data[0])

