from typing_extensions import final
from pyvirtualdisplay import Display
from utils import naukri
from utils import monster
from utils import indeed
from utils import timejobs
from utils import shine
from utils import linkedin
from selenium import webdriver
import pandas as pd


def job_scraper(skill, loc, exp):
	# # FOR LINUX
	display = Display(visible=0, size=(800, 800))  
	display.start()
	DRIVER_PATH = './chrome_driver/linux/chromedriver'

	# # FOR WINDOWS
	# DRIVER_PATH = './chrome_driver/windows/chromedriver.exe'

	try:
		wd = webdriver.Chrome(executable_path=DRIVER_PATH,)
		print("\nPLEASE WAIT...\n")
		data = [['Title','Company','CTC','Experience','Location','Description','Required Skills','link']]
		try:
			naukri_data = naukri(skill,loc,exp,wd)
			final_data = naukri_data
			print('Retrieval from naukri.com successfull')
		except:
			final_data = pd.DataFrame(columns=data)
			print('Failed to retrieve from naukri.com')
		try:
			monster_data = monster(skill,loc,exp,wd)
			final_data = pd.concat([final_data,monster_data],axis=0,ignore_index=True)
			print('Retrieval from monster.com successfull')
		except:
			print('Failed to retrieve from monster.com')
		try:
			indeed_data = indeed(skill,loc,exp,wd)
			final_data = pd.concat([final_data,indeed_data],axis=0,ignore_index=True)
			print('Retrieval from indeed.com successfull')
		except:
			print('Failed to retrieve from indeed.com')
		try:
			time_data = timejobs(skill,loc,exp,wd)
			final_data = pd.concat([final_data,time_data],axis=0,ignore_index=True)
			print('Retrieval from timejobs.com successfull')
		except:
			print('Failed to retrieve from timesjob.com')
		try:
			shine_data = shine(skill,loc,exp,wd)
			final_data = pd.concat([final_data,shine_data],axis=0,ignore_index=True)
			# final_data = pd.concat([shine_data],axis=0,ignore_index=True)
			print('Retrieval from shine.com successfull')
		except:
			print('Failed to retrieve from shine.com')

		try:
			linkedin_data = linkedin(skill,loc,exp,wd)
			final_data = pd.concat([final_data,linkedin_data],axis=0,ignore_index=True)
			print('Retrieval from linkedin successfull')
		except:
			print('Failed to retrieve from linkedin')
		try:
			wd.close()
		except:
			pass
		return final_data.to_dict()
	except:
		wd.close()
		print("\n\n\nFAILED TO RETRIEVE DATA. Chrome Driver Error.")
		return {}