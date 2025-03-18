import requests
from bs4 import BeautifulSoup

def get_codechef_profile(username):
    url = f"https://www.codechef.com/users/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    
    # Print response content to debug
    print(response.text[:1000])  # Print first 1000 characters of the page

    if response.status_code != 200:
        return {"error": "User not found"}

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

    except AttributeError:
        return {"error": "Data extraction failed"}

    return {
        "username": username,
        "rating": rating,
        "stars": stars,
        "highest_rating": highest_rating,
        "global_rank": global_rank,
        "country_rank": country_rank
    }

# Example Usage
print(get_codechef_profile("anweshaban21"))
