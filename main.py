import time
from bs4 import BeautifulSoup
import requests


print('Put the skill you want to search ')
skill_to_search = input('>')
print(f'Searching job without {skill_to_search} skill')
def find_job():
    html_text = requests.get('https://theprotocol.it/filtry/python;t/warszawa;wp').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('a',class_='ListItem_l6of9et')

    for index, job in enumerate(jobs):
        skills =  job.find('div',class_='container_cnnybke commonChip_c1it4rqw chip_c3dkdv4 expectedTechnologies chip_c1geuvfz mediumClass_mqh87v0')
        company_name = job.find('h2',class_='titleText_t1280ha4').text
        level = job.find('span',class_='Label_l1fs6hs4').text
        more_info = job['href']
        
        if skill_to_search not in skills:
            with open(f'D:/PythonDev/WebScrappers/JobScrap/{index}.txt','w') as f:
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.text.strip()}")
                print(f"More Info: {more_info}")
                print(f"Level: {level}")
                print(f"--------------------------------------------")
                f.write(f"Company Name: {company_name.strip()}")
                f.write(f"Required Skills: {skills.text.strip()}")
                f.write(f"More Info: {more_info}")
                f.write(f"Level: {level}")
            print(f'File saved{index}')

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 5
        time.sleep(20)