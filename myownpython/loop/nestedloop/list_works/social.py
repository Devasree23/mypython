#make a suggesion list of the follower.

users=["sachin","dhoni","raina","rahul","kohli","sehwag"]

sachin_followers=["dhoni","raina","rahul"]

suggession=[]

for member in users:
    if member not in sachin_followers and member!="sachin":
        print(member)   
        suggession.append(member)
print(suggession)        