users = {}            # username -> user info
posts = []            # list of post dictionaries
post_id = 1           # numbering posts for easy reference

def mainmenu():
    while True:
        print('Main Menu:')
        print('#1: Create a user')
        print('#2: Make a post')
        print('#3: View your feed')
        print('#4: Like the posts')
        print('#5: Exit')
        print('#6: Edit your bio')
        answer= input('Enter a number 1-6:')
        
        print('---------------------------')

       
        if answer == '1':
            createuser()
        elif answer == '2':
            makeapost()
        elif answer == '3':
            viewfeed()
        elif answer == '4':
            likeapost()
        elif answer == '5':
            print("Goodbye. Don't talk to me anymore, we're done.")
            break
        elif answer == '6':
            edityourbio()
        else:
            print('Try again buddy')

def createuser():
     
    user = input('Enter a username: ')
    bio = input('Enter your bio: ')

    print('---------------------------')

    print('Your user has been created!')   
    users[user] = {
        'bio': bio,
        'followers': 0,
    }

    print('User: ' + user)
    print('Bio: ' + bio)
    print('Followers: 0')
    print('---------------------------')
        

def makeapost():
    global post_id
    
    user = input('Type in your username: ')
    
    if user not in users:
        print('There is no such username')     
        return
    content = input('Make your post:')

    post= {
        "id": post_id,
        "user": user,
        "text": content,
        "likes": 0
    }
    print('---------------------------')    
    posts.append(post)

    print('You have created your post.')
    post_id += 1
    print('---------------------------')


def viewfeed():
    if not posts:
        print('You are too early for posts.')
        return
    
    print('Your Feed:')
    print('---------------------------')    
    for post in posts:
        print("Post Number: " + str(post["id"]))
        print("User: " + post["user"])
        print("Content: " + post["text"])
        print("Likes: " + str(post["likes"]))
        print('---------------------------')
    


def likeapost():
    if not posts:
        print('You are too early for posts.')
        return
    
    likepost=int(input('Please type in the number of a post to like it: '))
    
    for i in posts:
        if likepost == i['id']:
            i["likes"] += 1
            print('You have liked the post number:', likepost)
            break
        
    print('---------------------------')        
                
def edityourbio():
    username = input('Enter a username you want to edit: ')
    
    if username not in users:
        print('there is no such user')
        return
    
    newbio = input('Write your new bio: ')
    
    users[username]['bio'] = newbio

    print('You have changed your bio.')
    print('---------------------------')
    print('Here is your new user:')
    print('User: ' + username)
    print('Bio: ' + newbio)
    print('Followers: 0')
    print('---------------------------')
    

        
    
    
mainmenu()
