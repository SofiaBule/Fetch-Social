import requests

def fetch_social_media_data(handle_or_hashtag):
    # Make API request to fetch social media data
    url = f"https://api.example.com/socialmedia/{handle_or_hashtag}/data"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching social media data:", response.status_code)
        return None

social_media_data = fetch_social_media_data("example_handle")
print("Social Media Data:", social_media_data)
