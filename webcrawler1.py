import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
if not results:
    print("Could not find ResultsContainer in the page.")
else:
    job_elements = results.find_all("div", class_="Card_Content")
    if not job_elements:
        print("No job elements found.")
    for job_element in job_elements:
        title = job_element.find("h2", class_="title")
        company = job_element.find("h3", class_="company")
        location = job_element.find("p", class_="location")
        if title and company and location:
            print(title.text.strip())
            print(company.text.strip())
            print(location.text.strip())
            print()
        else:
            print("Missing field in job element.")
