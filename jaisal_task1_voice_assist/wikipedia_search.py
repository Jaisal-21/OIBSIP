import requests


def search_wikipedia(query):

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            f"{query.replace(' ', '_')}"
        )

        response = requests.get(
            url,
            headers=headers
        )

        if response.status_code == 200:

            data = response.json()

            return data.get(
                "extract",
                "No information found."
            )

        return "No information found."

    except Exception as e:
        print("Wikipedia Error:", e)

        return "Wikipedia search failed."