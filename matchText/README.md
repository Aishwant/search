### The program matches Text and produces results based on data provided in the input and through google search.


## Installation of Google search Api library

### pip install Google-Search-API
### pip install Google-Search-API --upgrade
<br />
search_result = google.search("query",num_of_page) #storing the specified page results in the variable
<br />
GoogleResult: <br />
    search_result.name # The title of the link<br />
    search_result.link # The external link<br />
    search_result.google_link # The google link<br />
    search_result.description # The description of the link<br />
    search_result.thumb # The link to a thumbnail of the website (NOT implemented yet)<br />
    search_result.cached # A link to the cached version of the page<br />
    search_result.page # What page this result was on (When searching more than one page)<br />
    search_result.index # What index on this page it was on<br />
    search_result.number_of_results # The total number of results the query returned<br />

