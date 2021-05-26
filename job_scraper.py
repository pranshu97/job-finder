from typing_extensions import final
from pyvirtualdisplay import Display
from utils import naukri, monster, indeed, timejobs, shine, linkedin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import logging

logging.basicConfig(filename='app.log', filemode='a')

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def job_scraper(skill, loc, exp):
	# # FOR LINUX
	display = Display(visible=0, size=(200, 200))  
	display.start()
	DRIVER_PATH = './chrome_driver/linux/chromedriver'

	# # FOR WINDOWS
	# DRIVER_PATH = './chrome_driver/windows/chromedriver.exe'

	try:
		wd = webdriver.Chrome(executable_path=DRIVER_PATH,options=set_chrome_options())
		# print("\nPLEASE WAIT...\n")
		logging.info('Starting scraper.')
		data = [['Title','Company','CTC','Experience','Location','Description','Required Skills','link']]
		try:
			naukri_data = naukri(skill,loc,exp,wd)
			final_data = naukri_data
			# print('Retrieval from naukri.com successfull')
			logging.info('Retrieval from naukri.com successfull')
		except  Exception as e:
			final_data = pd.DataFrame(columns=data)
			logging.warning(f'Failed to retrieve from naukri.com: {e}')
			# print('Failed to retrieve from naukri.com')
		try:
			monster_data = monster(skill,loc,exp,wd)
			final_data = pd.concat([final_data,monster_data],axis=0,ignore_index=True)
			# print('Retrieval from monster.com successfull')
			logging.info('Retrieval from monster.com successfull')
		except Exception as e:
			# print('Failed to retrieve from monster.com')
			logging.warning(f'Failed to retrieve from monster.com {e}')
		try:
			indeed_data = indeed(skill,loc,exp,wd)
			final_data = pd.concat([final_data,indeed_data],axis=0,ignore_index=True)
			# print('Retrieval from indeed.com successfull')
			logging.info('Retrieval from indeed.com successfull')
		except Exception as e:
			# print('Failed to retrieve from indeed.com')
			logging.warning(f'Failed to retrieve from indeed.com: {e}')
		try:
			time_data = timejobs(skill,loc,exp,wd)
			final_data = pd.concat([final_data,time_data],axis=0,ignore_index=True)
			# print('Retrieval from timejobs.com successfull')
			logging.info('Retrieval from timejobs.com successfull')
		except Exception as e:
			# print('Failed to retrieve from timesjob.com')
			logging.warning(f'Failed to retrieve from timesjob.com: {e}')
		try:
			shine_data = shine(skill,loc,exp,wd)
			final_data = pd.concat([final_data,shine_data],axis=0,ignore_index=True)
			# print('Retrieval from shine.com successfull')
			logging.info('Retrieval from shine.com successfull')
		except Exception as e:
			# print('Failed to retrieve from shine.com')
			logging.warning(f'Failed to retrieve from shine.com: {e}')
		try:
			linkedin_data = linkedin(skill,loc,exp,wd)
			final_data = pd.concat([final_data,linkedin_data],axis=0,ignore_index=True)
			# print('Retrieval from linkedin successfull')
			logging.info('Retrieval from linkedin successfull')
		except Exception as e:
			# print('Failed to retrieve from linkedin')
			logging.warning(f'Failed to retrieve from linkedin: {e}')
		try:
			wd.close()
		except Exception as e:
			logging.error(f'Failed to close web driver: {e}')
		return final_data.to_dict()
	except Exception as e:
		wd.close()
		# print("\n\n\nFAILED TO RETRIEVE DATA. Chrome Driver Error.")
		logging.critical(f"FAILED TO RETRIEVE DATA: {e}")
		return {}