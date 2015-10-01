import requests
import dill as pickle
import pandas as pd

'''
Nicolas Cage's page is the following: http://www.boxofficemojo.com/people/chart/?id=nicolascage.htm

'''
###url = 'http://www.boxofficemojo.com/people/chart/?id=nicolascage.htm'

#response = requests.get(url)

response.status_code

#with open('nc_webpage.pkl', 'w') as picklefile:
#    pickle.dump(response, picklefile)

with open("nc_webpage.pkl", 'r') as picklefile: 
    response = pickle.load(picklefile)

#print response.text

page = response.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(page)

#print soup

#print soup.prettify()

#print soup.find_all(text = 'Nicolas Cage')

#print soup.find(text = 'Nicolas Cage').parent

nc_name = soup.h1.text

#print soup.find_all(text = 'Left Behind (2014)')[0].parent.parent

nc_tables = soup.find_all('table')

movie_line = soup.find_all('table')[1].find_all('tr')[0].find_all('td')[0].find_all('tr')
#print movie_line

all_movie_html_block_1 = soup.find_all('table')[1].find_all('tr')[0].find_all('td')[0].find_all('tr')
all_movie_html_block_2 = soup.find_all('table')[3].find_all('tr')

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

movie_table1 = movie_table(all_movie_html_block)
movie_table2 = movie_table(all_movie_html_block_adj)
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