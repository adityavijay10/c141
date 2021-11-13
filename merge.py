import csv
headers=[]
with open('movies.csv',encoding='utf-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    header1=data[0]
    all_movies=data[1:]

with open('movie_links.csv',encoding='utf-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    header2=data[0]
    all_movies_links=data[1:]

header1.append('imdb_link')

with open('final.csv','a+',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(header1)

for movie_item in all_movies:
    poster_found=any(movie_item[6]in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_items in  all_movies_links:
           if movie_item[6]==movie_link_items[0]:
               movie_item.append(movie_link_items[1])
            #    print(len(movie_item))
               if len(movie_item)==23:
                   #print(movie_item)
                   with open('final.csv','a+',encoding='utf-8') as f:
                        writer=csv.writer(f)
                        writer.writerow(movie_item)



