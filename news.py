
#  News generator app


import requests
from bs4 import BeautifulSoup

def fetch_news(topic):
    api_key = "809cd6e1c47948d69ddd0f405915c30e"  # Your API key
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_full_article(url):
    # Request the article URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main article content (adjust as needed)
        article_body = soup.find('article')  # This might need adjustment for different websites
        if article_body:
            # Extract the text with proper line breaks
            full_text = article_body.get_text("\n", strip=True)  # Adding line breaks for better formatting
            return full_text
        else:
            return "Could not retrieve the full article content."
    else:
        return "Failed to retrieve the article."

def display_topics():
    topics = {
        "1": "Technology",
        "2": "Science",
        "3": "Health",
        "4": "Sports",
        "5": "Business",
        "6": "Entertainment"
    }

    print("Select a topic to fetch news:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return topics

def main():
    topics = display_topics()
    choice = input("Enter the number of your choice: ")

    if choice in topics:
        topic = topics[choice]
        print(f"\nFetching news for {topic}...\n")
        news = fetch_news(topic)

        if news:
            # Get the first article URL
            article = news['articles'][0]
            article_title = article['title']
            article_url = article['url']
            print(f"Title: {article_title}")
            print(f"URL: {article_url}\n")
            
            # Fetch the full article content
            full_article = fetch_full_article(article_url)
            print("\nFull Article Content:")
            print(full_article)
        else:
            print("Failed to retrieve news.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()































