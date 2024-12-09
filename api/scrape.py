import requests
from bs4 import BeautifulSoup

def handler(request):
    url = request.args.get("url")  # Get the URL to scrape from the request
    if not url:
        return "Error: No URL provided", 400

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    main_content = "\n".join(p.get_text(strip=True) for p in paragraphs)
    return main_content
