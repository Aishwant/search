#import BeautifulSoup

from google import google


num_page = 1

search_result = google.search("which of the tv shows is still running", num_page)

print search_result[1]
print search_result[1].description

result = search_result[1].description.lower()

a = "black mirror" in result

print a
