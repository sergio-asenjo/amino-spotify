import amino
import credentials

client = amino.Client()
print(client.login(email=credentials.EMAIL, password=credentials.PWD))
subclient = amino.SubClient(comId=credentials.COM_ID, profile=client.profile)

blogs = subclient.get_recent_blogs().blogId
for _ in range(30):
    for bid in blogs:
        bloginfo = subclient.get_blog_info(blogId=bid)
        uid = bloginfo.json['blog']['author']['uid']
        if uid not in credentials.IGNORED_USERS:
            subclient.like_blog(bid)
    token = blogs.nextPageToken
    blogs = subclient.get_recent_blogs(pageToken=token).blogId