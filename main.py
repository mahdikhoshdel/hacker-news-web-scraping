from bs4 import BeautifulSoup
import requests

# Get data from Hacker news website
response = requests.get("https://news.ycombinator.com/")
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    a_tag = article_tag.find("a", href=True)
    if a_tag:
        text = a_tag.text
        article_texts.append(text)
        link = a_tag["href"]
        article_links.append(link)

# list of scores for articles based on points in hacker news
article_upvote = [
    int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")
]
maximum_rate_index = article_upvote.index(max(article_upvote))

print(article_texts[maximum_rate_index])
print(article_links[maximum_rate_index])
print("Score news: ", article_upvote[maximum_rate_index])
