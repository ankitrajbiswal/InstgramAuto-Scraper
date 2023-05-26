import instaloader
 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
#bot.login(user="Your_username",passwd="Your_password") #Use this code to log-in to your account.


def getBasicInfo():
    profileid = input('Enter the userid of the profile\n')
    # Loading the profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, profileid)
    print("Username: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers Count: ", profile.followers)
    print("Following Count: ", profile.followees)
    print("Bio: ", profile.biography)
    print("External URL: ", profile.external_url)   
    print('\n')
    
def searchInformation():
    searchitem = input('Enter the search keyword\n')
    # Provide the search query here
    search_results = instaloader.TopSearchResults(bot.context, searchitem)
    print('\n')
    # Iterating over the extracted usernames
    for username in search_results.get_profiles():
        print(username)
        
    print('\n')
    # Iterating over the extracted hashtags
    for hashtag in search_results.get_hashtags():
        print(hashtag)
    
    print('\n')

def downloadPost():
    useerid = input('Enter the userid of the profile\n')
    # Loading a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, useerid)
    
    # Retrieving all posts in an object
    posts = profile.get_posts()
    count = 0
    # Iterating and downloading all the individual posts
    for index, post in enumerate(posts, 1):
        if count < 5:
            bot.download_post(post, target=f"{profile.username}_{index}")
            count+=1
        else:
            break
    
if __name__ == '__main__':
    option = '0'
    while option != '4':
        option = input('Select YOur option\n1)Get Profile Info\n2)Search for Top profiles and Hastags\n3)Download Profile Posts\n4)Exit\n')
        if option == '1':
            getBasicInfo()
        elif option == '2':
            searchInformation()
        elif option == '3':
            downloadPost()
        elif option == '4':
            exit
        else:
            print('Wrong input please try again\n')
