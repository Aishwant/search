#import BeautifulSoup

from google import google

query = raw_input("The question: ");

option = []

for i in range(0,3):
    s = "Option "+str(i+1)+": ";
    option.append(raw_input(s).lower())

num_page = 1

search_result = google.search(query, num_page)
r={}

for i in range(0,len(search_result)):
    print search_result[i]

    result = search_result[i].description.lower()
    if option[0] in result:
        try: r[option[0]]=r[option[0]]+1
        except: r[option[0]]=1
    if option[1] in result:
        try: r[option[1]]=r[option[1]]+1
        except: r[option[1]]=1
    if option[2] in result:
        try: r[option[2]]=r[option[2]]+1
        except: r[option[2]]=1

print len(search_result)
print r
