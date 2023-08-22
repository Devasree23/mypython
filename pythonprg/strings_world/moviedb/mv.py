from json import load
with open("C:\\Users\\vaisa\\OneDrive\\Desktop\\pythonprg\\strings_world\\moviedb\\data.json","r",encoding="UTF-8")as f:
    data=load(f)
#no of movies    
print(len(data))
print("------------------------------------------")

#movie names 
for u in data:
    print(u.get("title"))  
print("------------------------------------------")

#print movie highest runtime

runtime_high_movie=max(data,key=lambda m:int(m.get("runtime")))    
print(runtime_high_movie) 

#print all geners
#movie name with generes comedy
#movie name with generes comedy or fantasy
# yearvise movie count{1988:5,188:4}
print("------------------------------------------")

all_genres={g for m in data for g in m.get("genres")}
print(all_genres)
print("------------------------------------------")
comedy_movies=[c.get("title") for c in data for g in c.get("genres")if g=="Comedy"] 
print(comedy_movies)   
print("------------------------------------------")

comedy_movies=[c.get("title") for c in data for g in c.get("genres")if g=="Fantasy" or g=="Comedy"] 
print(set(comedy_movies))  
print("------------------------------------------")

genre_filter={m.get("title") for m in data for g in m.get("genres") if g in["Comedy","Fantasy"]}
print(genre_filter)
print("------------------------------------------")

yc={}
for m in data:
    year=m.get("year")
    if year in yc:
        yc[year]+=1
    else:
        yc[year]=1
print(yc)

print(max(yc,key=lambda k:yc.get(k)))
print(min(yc,key=lambda k:yc.get(k)))