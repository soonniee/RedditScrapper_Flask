import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
subreddits = []
def redit_scrapper(url):
    result = requests.get(url,headers = headers).text
    result = BeautifulSoup(result,"html.parser")
    posts = result.find_all("div",{"class":"Post"})
    # print(posts)
    for post in posts:
        post_dict={}
        title = post.find("div",{"class":"_1poyrkZ7g36PawDueRza-J"}).find("div",{"class":"_2INHSNB8V5eaWp4P0rY_mE"}).find("h3").text
        link = post.find("div",{"class":"_1poyrkZ7g36PawDueRza-J"}).find("div",{"class":"_2INHSNB8V5eaWp4P0rY_mE"}).find("a")['href']
        link = f"https://reddit.com{link}"
        votes = post.find("div",{"class":"_1E9mcoVn4MYnuBQSVDt1gC"}).find("div",{"class":"_3a2ZHWaih05DgAOtvu6cIo"}).text
        post_dict={
            'title':title,
            'link':link,
            'votes':votes
        }
        subreddits.append(post_dict)
    return subreddits