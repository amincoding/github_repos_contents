# A programe made by amin abdedaiem 
#
# 14:15 wednesday the 24th 2021
#
# find out what a repository - of any one in github - contains 
#
# buy just providing his user name 
#
###################################################################
 
# import requests and bs4
import requests as rq
from bs4 import BeautifulSoup as bs

# ask the user for the user_name
github_user_name = input("Enter the repository username : ")

url = 'https://github.com/'+github_user_name

r = rq.get(url)
soup = bs(r.content, 'html.parser')

target = github_user_name+'?tab=followers'

followers = soup.findAll(github_user_name)
print(followers)


# github_user_name+'?tab=followers'


