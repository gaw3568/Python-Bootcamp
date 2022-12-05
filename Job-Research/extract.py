from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("h2", itemprop="title")
        companys = soup.find_all("span", class_="companyLink")
        job_list = {}

        for job, company in zip(jobs,companys):
            # Add job & company in job_list dictionary
            job_list[job.get_text().strip()] = company.get_text().strip()
    
        for job, company in job_list.items():
            print(f"Job : {job}")
            print(f"Company : {company}")
            print("\n")

    else:
        print("Can't get jobs.")

language = input("Enter programming language : ")
extract_jobs(language)