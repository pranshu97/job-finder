import selenium
from selenium import webdriver
import pandas as pd

def timejobs(skill,loc,exp,wd):
	url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='
	url_skill = '+'.join(skill.split())
	url = url + url_skill + '&txtLocation=' + loc + '&cboWorkExp1=' + exp
	wd.get(url)

	try:
	    js = 'document.getElementById("closeId").click();'
	    wd.execute_script(js)
	except:
	    pass
	try:
	    container = wd.find_element_by_class_name("new-joblist")
	    lst = container.find_elements_by_class_name("job-bx")
	except:
	    return pd.DataFrame(columns=data[0])
	data = [['Title','Company','CTC','Experience','Location','Description','Required Skills','link']]
	for i,li in enumerate(lst):
	    try:
	        title = li.find_element_by_class_name("clearfix").find_element_by_tag_name("a")
	        name = title.text
	        link = title.get_attribute("href")
	    except:
	        continue
	    try:
	        company = li.find_element_by_class_name("joblist-comp-name").text
	    except:
	        company = 'Not Available'
	    try:
	        exp = li.find_element_by_class_name("top-jd-dtl").find_elements_by_tag_name("li")[0].text
	        exp = exp[12:]
	    except:
	        exp = 'Not Available'
	    try:
	        try:
	            loc = li.find_element_by_class_name("top-jd-dtl").find_elements_by_tag_name("li")[2].text
	        except:
	            loc = li.find_element_by_class_name("top-jd-dtl").find_elements_by_tag_name("li")[1].text
	        loc = loc[12:]
	    except:
	        loc = 'Not Available'
	    try:
	        ele = li.find_element_by_class_name("rupee").text
	        sal = li.find_element_by_class_name("top-jd-dtl").find_elements_by_tag_name("li")[1].text
	        sal = sal[2:]
	    except:
	        sal = 'Not Available'
	    try:
	        jd = li.find_element_by_class_name("list-job-dtl").find_elements_by_tag_name("li")[0].text
	    except:
	        jd = 'Not Available'
	    try:
	        req_skills = li.find_element_by_class_name("list-job-dtl").find_elements_by_tag_name("li")[1].text
	    except:
	        req_skills = 'Not Available'
	    data.append([name,company,sal,exp,loc,jd,req_skills,link])
	    if i==15:
	        break
	return pd.DataFrame(data[1:],columns=data[0])