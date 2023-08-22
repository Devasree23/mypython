movies={"2018":5,"keralastory":3,"neymar":4,"kgf":5,"arm":4}
#print all movies
#top rated movie 
#sort the movies with respect to the rating

print(movies.keys())

print(max(movies,key=lambda k:movies.get(k)))
rate=sorted(movies,reverse=True,key=lambda m:movies.get(m))
print(rate)