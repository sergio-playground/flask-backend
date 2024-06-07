import requests
import os
from dotenv import load_dotenv

def run():
    issues = []
    shortIDs = []
    org_slug = os.environ["ORG_SLUG"]
    token = os.environ["SENTRY_TOKEN"]
    project_id = os.environ["PROJECT_ID"]
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f'Bearer {token}'
    }
    
    url = f'https://sentry.io/api/0/organizations/{org_slug}/issues/'
    for issue in issues:
        response = requests.get(f'{url}/{issue}/', headers = headers)
        if response is not None and response.status_code in [200,201,202]:
            data = response.json()
            if "shortId" in data:
                shortIDs.append(data["shortId"])
    

    discover_query = f'https://{org_slug}.sentry.io/discover/homepage/?field=issue&field=count%28%29&name=All+Events&project={project_id}&query=issue%3A%5B'
    for index, shortID in enumerate(shortIDs):
        discover_query += f'{shortID}'
        if index+1 != len(shortIDs):
            discover_query += '%2C'

    discover_query += "%5D&sort=-count%28%29&statsPeriod=90d&yAxis=count%28%29"

    print(discover_query)

if __name__ == "__main__":
    load_dotenv()
    run()
