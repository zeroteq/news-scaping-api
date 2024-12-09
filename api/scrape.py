import requests
from bs4 import BeautifulSoup
import traceback

def handler(request):
    try:
        url = request.args.get("url")  # Get the URL to scrape from the request
        if not url:
            return "Error: No URL provided", 400

        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        main_content = "\n".join(p.get_text(strip=True) for p in paragraphs)

        return main_content

    except Exception as e:
        error_message = f"Error: {str(e)}\n{traceback.format_exc()}"
        return error_message, 500
