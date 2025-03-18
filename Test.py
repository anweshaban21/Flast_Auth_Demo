from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication


@app.route("/codechef", methods=["POST"])
def get_codechef_profile():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    url = f"https://www.codechef.com/users/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        rating = soup.find("div", class_="rating-number")
        highest_rating = soup.find("small")
        stars = soup.find("span", class_="rating")
        global_rank = soup.find("a", href=lambda href: href and "rankings/global" in href)
        country_rank = soup.find("a", href=lambda href: href and "rankings/country" in href)

        # Handle None values
        rating = rating.text.strip() if rating else "N/A"
        highest_rating = highest_rating.text.strip().split()[-1] if highest_rating else "N/A"
        stars = stars.text.strip() if stars else "N/A"
        global_rank = global_rank.text.strip() if global_rank else "N/A"
        country_rank = country_rank.text.strip() if country_rank else "N/A"

        return jsonify({
            "username": username,
            "rating": rating,
            "stars": stars,
            "highest_rating": highest_rating,
            "global_rank": global_rank,
            "country_rank": country_rank
        })

    except AttributeError:
        return jsonify({"error": "Data extraction failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)
