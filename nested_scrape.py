import requests
import dill as pickle
import pandas as pd
from bs4 import BeautifulSoup


'''
Nicolas Cage's page is the following: http://www.boxofficemojo.com/people/chart/?id=nicolascage.htm
'''

#url = 'http://www.boxofficemojo.com/people/chart/?id=nicolascage.htm'

#response = requests.get(url)

#response.status_code

#with open('nc_webpage.pkl', 'w') as picklefile:
#    pickle.dump(response, picklefile)

with open("nc_webpage.pkl", 'r') as picklefile: 
    response = pickle.load(picklefile)

#print response.text

page = response.text
soup = BeautifulSoup(page)

all_movie_html_block_1 = soup.find_all('table')[1].find_all('tr')[0].find_all('td')[0].find_all('tr')
all_movie_html_block_2 = soup.find_all('table')[3].find_all('tr')


'''
Test to see if new movie_table works
def movie_table(all_movie_html_block):
    movie_table = []
    movie_html_block = []
    movie_attribute = []
    movie_items = []
    for x in range(1, len(all_movie_html_block)):
        movie_items = [] #this is cleared out as we reloop through the list to append new individual movie attributes
        movie_html_block = all_movie_html_block[x] #individual blocks from all_movie_html_block
        for i in range(0, len(movie_html_block.find_all('td'))):
            movie_attribute = movie_html_block.find_all('td')[i].text
            movie_items.append(movie_attribute)
            try:
                movie_html = movie_html_block.find_all('td')[i].a['href']
            except:
                movie_html = ""
            movie_items.append(movie_html)
        movie_table.append(movie_items)
    return movie_table
'''

movie_table1 = actor_movie_table('Nicolas Cage', all_movie_html_block_1)
movie_table2 = actor_movie_table('Nicolas Cage', all_movie_html_block_2)
col = ['date', 'date_url', 'movie', 'movie_url', 'studio', 'studio_url', 'gross', 'gross_url', 'theaters_g', 'theaters_g_url', 'opening', 'opening_url', 'theaters_o', 'theaters_o_url', 'rank', 'rank_url']
nc_movies_1 = pd.DataFrame(movie_table1, columns = col)
nc_movies_1['date_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['date_url']
nc_movies_1['movie_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['movie_url']
nc_movies_1['studio_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['studio_url']
nc_movies_1['gross_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['gross_url']
nc_movies_1['theaters_g_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['theaters_g_url']
nc_movies_1['opening_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['opening_url']
nc_movies_1['theaters_o_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['theaters_o_url']
nc_movies_1['rank_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['rank_url']
col = ['rank', 'rank_url', 'movie', 'movie_url', 'studio', 'studio_url','adjusted_gross', 'adjusted_gross_url', 'adjusted_opening', 'adjusted_opening_url', 'date', 'date_url']
nc_movies_2 = pd.DataFrame(movie_table2, columns = col)
nc_movies_2['date_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['date_url']
nc_movies_2['movie_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['movie_url']
nc_movies_2['studio_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['studio_url']
nc_movies_2['gross_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['gross_url']
nc_movies_2['theaters_g_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['theaters_g_url']
nc_movies_2['opening_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['opening_url']
nc_movies_2['theaters_o_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['theaters_o_url']
nc_movies_2['rank_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['rank_url']

'''
Loop through Nicolas Cage movies to find people who have worked with him
'''

#with open('jw_webpage.pkl', 'w') as picklefile:
#    pickle.dump(response, picklefile)

#with open("jw_webpage.pkl", 'r') as picklefile: 
#    response = pickle.load(picklefile)

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

#col = ['movie', 'role', 'name', 'name_url']
#movie_df = pd.DataFrame([], columns = col)

def movie_page_loop(loop_df):
    nc_movies = []
    for row in loop_df:
        url = row
        print url
        response = requests.get(url)
        page = response.text
        soup = BeautifulSoup(page)
        #Sets the block that we are looking at that contains the contributors for the film
        try:
            movie_name = soup.find_all('b')[1].text
            movie_desc_block = soup.find(text = 'The Players').parent.parent.find_all('table')[0].find_all('tr')
            movie = movie_desc_table(movie_name, movie_desc_block)
        except:
            movie = ["","","",""] #future note, need to change so I don't need to fix later
        nc_movies.append(movie)
    return nc_movies

loop_df = nc_movies_1['movie_url'].values
movies_df = movie_page_loop(loop_df)

'''
Checkpoint to pick up from work to get list of people who have worked with Nicolas Cage
'''

# Create a list pickle file so I don't have to scrape again

#with open('nc_actors.pkl', 'w') as picklefile:
#    pickle.dump(movies_df, picklefile)

with open("nc_actors.pkl", 'r') as picklefile: 
    movies_df = pickle.load(picklefile)
    
#movies_df[:5]

'''
Only grab actors who have worked with Nicolas Cage
'''

nc_actors = []
actor_stuff = []
for row in movies_df:
    for movie, name, role, url in row:
        if role == u'Actors:':
            if url == "":
                url = ""
            else:
                url = "http://www.boxofficemojo.com"+url
            actor_stuff = [movie, name, role, url]
            nc_actors.append(actor_stuff)

'''
Manipulate output list to create a new list to loop through to find out more information about actors that
have worked with Nicolas Cage
'''

loop_df = []
for row in nc_actors:
    name = row[1].replace('*','')
    url =  row[3]
    loop_df.append([name,url])

loop_dict = {}
for row in loop_df:
    loop_dict[row[0]] = row[1]

unique_loop = []
for actor in loop_dict:
    unique_loop.append([actor, loop_dict[actor]])

'''
Create dataset of movies of actors that have worked with Nicolas Cage
'''

def actor_movie_table(nc_actor, all_movie_html_block):
    movie_table = []
    movie_html_block = []
    movie_attribute = []
    movie_items = []
    all_movies = []
    for x in range(1, len(all_movie_html_block)):
        movie_html_block = all_movie_html_block[x]
        movie_items = []
        for i in range(0, len(movie_html_block.find_all('td'))):
            movie_attribute = movie_html_block.find_all('td')[i].text
            movie_items.append(movie_attribute)
            try:
                movie_html = movie_html_block.find_all('td')[i].a['href']
            except:
                movie_html = ""
            attribute_info = [movie_attribute, movie_html]
            movie_items.append(movie_html)
        movie_table.append(movie_items)
    all_movies = all_movies + movie_table
    return all_movies

def actor_page_loop(loop_df):
    actor_movies = []
    all_movies = []
    for row in loop_df:
        url = row[1]
        print url
        response = requests.get(url)
        page = response.text
        soup = BeautifulSoup(page)
        nc_actor = row[0]
        movie_desc_block = soup.find_all('table')[1].find_all('tr')[0].find_all('td')[0].find_all('tr')
        movie_list = actor_movie_table(nc_actor, movie_desc_block)
        all_movies = all_movies + movie_list
    return all_movies

all_actor_movies = actor_page_loop(unique_loop)

col = ['date', 'date_url', 'movie', 'movie_url', 'studio', 'studio_url', 'gross', 'gross_url', 'theaters_g', 'theaters_g_url', 'opening', 'opening_url', 'theaters_o', 'theaters_o_url', 'rank', 'rank_url']
all_actor_movies_df = pd.DataFrame(all_actor_movies, columns = col)
all_actor_movies_df['date_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['date_url']
all_actor_movies_df['movie_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['movie_url']
all_actor_movies_df['studio_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['studio_url']
all_actor_movies_df['gross_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['gross_url']
all_actor_movies_df['theaters_g_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['theaters_g_url']
all_actor_movies_df['opening_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['opening_url']
all_actor_movies_df['theaters_o_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['theaters_o_url']
all_actor_movies_df['rank_url'] = 'http://www.boxofficemojo.com/'+all_actor_movies_df['rank_url']

loop_df = all_actor_movies_df['movie_url'].values
movies_df_nonnc = movie_page_loop(loop_df)

with open('all_actors.pkl', 'w') as picklefile:
    pickle.dump(movies_df_nonnc, picklefile)

with open("all_actors.pkl", 'r') as picklefile: 
    movies_df_nonnc = pickle.load(picklefile)

new_table = []
for row in movies_df_nonnc:
    for x in row:
        new_table.append(x)

list_1 = []
list_2 = []
for row in new_table:
    if type(row) == type([]):
        list_1.append(row)
    else:
        list_2.append(row)

col = ['movie', 'name', 'role', 'url']
all_movies_df = pd.DataFrame(list_1, columns = col)
all_movies_df['url'] = 'http://www.boxofficemojo.com'+all_movies_df['url']