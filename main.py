import requests

def fetch_leetcode_stats(username):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json"
    }
    
    query = """
    {
      matchedUser(username: "%s") {
        username
        submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
        profile {
          ranking
          reputation
        }
      }
    }
    """ % username

    response = requests.post(url, json={"query": query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("data", {}).get("matchedUser"):
            user_data = data["data"]["matchedUser"]
            return {
                "username": user_data["username"],
                "ranking": user_data["profile"]["ranking"],
                "reputation": user_data["profile"]["reputation"],
                "problems_solved": {
                    "easy": user_data["submitStatsGlobal"]["acSubmissionNum"][1]["count"],
                    "medium": user_data["submitStatsGlobal"]["acSubmissionNum"][2]["count"],
                    "hard": user_data["submitStatsGlobal"]["acSubmissionNum"][3]["count"],
                    "total": user_data["submitStatsGlobal"]["acSubmissionNum"][0]["count"]
                }
            }
        else:
            return {"error": "User not found"}
    else:
        return {"error": f"Failed to fetch data (Status Code: {response.status_code})"}

# Example Usage
username = "anwe_techie"
stats = fetch_leetcode_stats(username)
print(stats)
