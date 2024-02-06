import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup


class JobScraperService:
    def __init__(self):
        self.url = "https://lobbyx.army/?search=python"

    def get_jobs(self):
        jobs = []
        try:
            response = requests.get(self.url)
        except Exception as e:
            print("Error getting jobs:")
            print(e)
            return jobs

        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        job_items = soup.find_all("a", class_="job-item")
        for job in job_items:
            job_id = job.parent.parent.get("id")
            if not self.is_job_new(job_id):
                return

            job_url = job.get("href")
            data = self.get_job_data(job_url)
            jobs.append(data)
        return jobs

    def get_job_data(self, job_url: str):
        try:
            response = requests.get(job_url)
        except Exception as e:
            print(f"Error while getting the job page: {job_url}")
            print(e)
            return {}

        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        logo = soup.find("div", class_="vacancy-logo-img")
        try:
            logo_url = re.findall(".*background *: *url\((.*)\)", logo["style"])[0]
        except Exception as e:
            logo_url = ""
            print(f"Error while getting the logo url {e}")

        job_data = {
            "title": soup.find("h1").text.strip(),
            "url": logo_url
        }
        vacancy_description = soup.find("div", class_="vacancy-description")
        elements = vacancy_description.find_all("h2")
        for element in elements:
            next_sibling = element.next_sibling
            while next_sibling.name not in ["p", "ul"]:
                next_sibling = next_sibling.next_sibling

            element_text = next_sibling.text.strip()
            texts = element_text.split("\n")
            job_data[element.text] = texts

        return job_data

    @staticmethod
    def is_job_new(job_id: str):
        # TODO: Implement this method
        # check if job id is in the database
        return True


if __name__ == "__main__":
    job_scraper_service = JobScraperService()
    jobs = job_scraper_service.get_jobs()
    pprint(jobs)
