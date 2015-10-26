def movie_desc_table(movie_name, all_movie_html_block):
    movie_table = []
    movie_html_block = []
    movie_attribute = []
    movie_items = []
    movie = []
    contributor_desc = ""
    for x in range(len(all_movie_html_block)): #len(all_movie_html_block)
        movie_items = [] #this is cleared out as we reloop through the list to append new individual movie attributes
        movie_html_block = all_movie_html_block[x] #individual blocks from all_movie_html_block
        movie = movie_name
        for i in range(1, len(movie_html_block.find_all('a'))):
            movie_role = movie_html_block.find_all('a')[0].text
            name = movie_html_block.find_all('a')[i].text
            try:
                movie_html = movie_html_block.find_all('a')[i]['href']
            except:
                movie_html = ""
            movie_items =[movie, name, movie_role, movie_html] #movie_role, 
            movie_table.append(movie_items)
    return movie_table