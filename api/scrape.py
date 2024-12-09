from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get("url")
    
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            main_content = "\n\n".join(p.get_text(strip=True) for p in paragraphs)
            return jsonify({"content": main_content})
        else:
            return jsonify({"error": f"Failed to fetch the page. Status code: {response.status_code}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handler(event, context):
    return app(event, context)
