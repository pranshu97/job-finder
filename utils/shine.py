import selenium
from selenium import webdriver
import pandas as pd

def shine(skill,loc,exp,wd):
	url = 'https://www.shine.com/job-search/'
	url_skill = '-'.join(skill.split())
	url = url + url_skill + '-jobs-in-' + loc
	wd.get(url)

	try:
	    js = f'document.getElementById("id_loc").value="{loc}";'
	    js += f'document.getElementsByClassName("submit")[0].click();'
	    wd.execute_script(js)
	except:
	    pass

	data = [['Title','Company','ctc','experience','location','Description','skills_required','link']]
	try:
	    container = wd.find_element_by_id("id_results")
	    lst = container.find_elements_by_class_name("result-display__profile")
	except:
	    return pd.DataFrame(columns=data)

	i = 0
	for li in lst:
	    try:
	        title = li.find_element_by_tag_name("a")
	        link = title.get_attribute("href")
	    except:
	        continue
	    try:
	        experience = li.find_element_by_class_name("cls_jobexperience").text
	        e = int(experience[0])
	        exp = int(exp)
	        if e!=exp and e!=exp-1 and e!=exp+1:
	            continue
	    except:
	        exp = 'Not Available'
	    try:
	        company = li.find_element_by_class_name("cls_jobcompany").text
	    except:
	        company = 'Not Available'
	    try:
	        loc = li.find_element_by_class_name("snp_loc").text
	    except:
	        loc = 'Not Available'
	    try:
	        jd = li.find_element_by_class_name("srcresult").text
	    except:
	        jd = 'Not Available'
	    try:
	        req_skills = li.find_element_by_class_name("cls_jobskill").text
	    except:
	        req_skills = 'Not Available'
	    sal = 'Not Available'
	    data.append([name,company,sal,exp,loc,jd,req_skills,link])
	    i+=1
	    if i==10:
	    	break
	return pd.DataFrame(data[1:],columns=data[0])