import instaloader
from instaloader import  Profile
from datetime import datetime
from itertools import dropwhile, takewhile 

percentage=0
users = []

# Create an instance of Instaloader class
ig = instaloader.Instaloader()

#req_user = input("Enter your username: ")
username= "aesir_8k"
#password= input("Enter your password: ")
ig.login('newid01234', 'abcdef')


# # Load a profile from an Instagram handle
# profile  = instaloader.Profile.from_username(ig.context, username)


# # user = profile .username
# # no_of_post =  profile .mediacount 
# # no_of_followers = profile .followers 
# # no_of_following =  profile .followees
# # bio = profile .biography
# # links = profile .external_url
# # private = profile.is_private # displays True, if private account 
# # ig.download_profile(username, profile_pic=True) 
# # posts = profile.get_posts()
# # for index, post in enumerate(posts, 1):
# #     ig.download_post(post, target=f"{profile.username}_{index}")


# # for following in profile.get_followers(): #Following 
# #     print(following)



# # for followers in profile.get_followees(): #Followers
# #     print(followers) 



# print(user,no_of_followers,no_of_following,bio,links,private)
