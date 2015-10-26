
'''
Nicolas Cage's page is the following: http://www.boxofficemojo.com/people/chart/?id=nicolascage.htm
'''

url = 'http://www.boxofficemojo.com/people/chart/?id=nicolascage.htm'
response = requests.get(url)
response.status_code

with open('nc_webpage.pkl', 'w') as picklefile:
    pickle.dump(response, picklefile)

with open("nc_webpage.pkl", 'r') as picklefile: 
    response = pickle.load(picklefile)

page = response.text
soup = BeautifulSoup(page)
all_movie_html_block_1 = soup.find_all('table')[1].find_all('tr')[0].find_all('td')[0].find_all('tr')
all_movie_html_block_2 = soup.find_all('table')[3].find_all('tr')
movie_table1 = actor_movie_table('Nicolas Cage', all_movie_html_block_1)
movie_table2 = actor_movie_table('Nicolas Cage', all_movie_html_block_2)
col = ['date', 'date_url', 'movie', 'movie_url', 'studio', 'studio_url', 'gross', 'gross_url', 'theaters_g', 'theaters_g_url', 'opening', 'opening_url', 'theaters_o', 'theaters_o_url', 'rank', 'rank_url','name']
nc_movies_1 = pd.DataFrame(movie_table1, columns = col)
nc_movies_1['date_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['date_url']
nc_movies_1['movie_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['movie_url']
nc_movies_1['studio_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['studio_url']
nc_movies_1['gross_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['gross_url']
nc_movies_1['theaters_g_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['theaters_g_url']
nc_movies_1['opening_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['opening_url']
nc_movies_1['theaters_o_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['theaters_o_url']
nc_movies_1['rank_url'] = 'http://www.boxofficemojo.com/'+nc_movies_1['rank_url']

'''
Loop through Nicolas Cage movies to find people who have worked with him
'''

loop_df = nc_movies_1['movie_url'].values
nc_colab = movie_page_loop(loop_df)


'''
Only grab actors who have worked with Nicolas Cage
'''

nc_actors = []
actor_stuff = []
for row in nc_colab:
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

all_actor_movies = actor_page_loop(unique_loop)

col = ['date', 'date_url', 'movie', 'movie_url', 'studio', 'studio_url', 'gross', 'gross_url', 'theaters_g', 'theaters_g_url', 'opening', 'opening_url', 'theaters_o', 'theaters_o_url', 'rank', 'rank_url','name']
all_actor_movies_df = pd.DataFrame(all_actor_movies, columns = col)
all_actor_movies_df['date_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['date_url']
all_actor_movies_df['movie_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['movie_url']
all_actor_movies_df['studio_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['studio_url']
all_actor_movies_df['gross_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['gross_url']
all_actor_movies_df['theaters_g_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['theaters_g_url']
all_actor_movies_df['opening_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['opening_url']
all_actor_movies_df['theaters_o_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['theaters_o_url']
all_actor_movies_df['rank_url'] = 'http://www.boxofficemojo.com'+all_actor_movies_df['rank_url']

loop_df = all_actor_movies_df['movie_url'].values
movies_df_nonnc = movie_page_loop(loop_df)


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


all_actors = []
actor_stuff = []
for movie, name, role, url in new_table:
    if role == u'Actors:':
        if url == "":
            url = ""
        else:
            url = "http://www.boxofficemojo.com"+url
            actor_stuff = [movie, name, role, url]
            all_actors.append(actor_stuff)


all_actors_loop = []
for movie, name, role, url in all_actors:
    name = name.replace('*','')
    url =  url
    all_actors_loop.append([name,url])

all_actors_dict = {}
for row in all_actors_loop:
    all_actors_dict[row[0]] = row[1]

unique_all_actors = []
for actor in all_actors_dict:
    unique_all_actors.append([actor, all_actors_dict[actor]])
    
comp_actor_movies = actor_page_loop(unique_all_actors)


col = ['date', 'date_url', 'movie', 'movie_url', 'studio', 'studio_url', 'gross', 'gross_url', 'theaters_g', 'theaters_g_url', 'opening', 'opening_url', 'theaters_o', 'theaters_o_url', 'rank', 'rank_url','name']
comp_actor_df = pd.DataFrame(comp_actor_movies, columns = col)
comp_actor_df['date'] = comp_actor_df['date'].apply(pd.to_datetime) 
comp_actor_df = comp_actor_df[comp_actor_df.date != 'N/A']
comp_actor_df['gross'] = (comp_actor_df['gross'].replace('[\$,)]','', regex=True).replace( '[(]','-', regex=True ).convert_objects(convert_numeric=True).astype(float))
comp_actor_df['name'] = comp_actor_df['name'].str.replace('*', '')
calc_comp_actor_df = comp_actor_df[['name','movie','date','gross']]

def date_loop(date_list, date_range):
    df_final = pd.DataFrame()
    for date in date_list:
        date_before_bound = relevant_dates[relevant_dates.date < date]#.sort('date', ascending = False)
        date_before = date_before_bound[date_before_bound.date > date-timedelta(days = date_range)].sort('date', ascending = False)
        date_after_bound = relevant_dates[relevant_dates.date > date].sort('date', ascending = False)
        date_after = date_after_bound[date_after_bound.date < date + timedelta(days = date_range)].sort('date', ascending = False)
        groupby_before = date_before.groupby('name')#.mean('gross')
        date_before_count = groupby_before.count(['movie']).reset_index()
        date_before_sum = groupby_before.sum().reset_index()
        date_before_mean = groupby_before.mean().reset_index()
        col = ['name', 'before_movie_count', 'before_total_gross', 'before_mean_gross']
        date_before_summary = pd.DataFrame(columns = col)
        date_before_summary['name'] = date_before_count['name']
        date_before_summary['before_movie_count'] = date_before_count['movie']
        date_before_summary['before_total_gross'] = date_before_sum['gross']
        date_before_summary['before_mean_gross'] = date_before_mean['gross']
        date_before_summary['date'] = date
        groupby_after = date_after.groupby('name')#.mean('gross')
        date_after_count = groupby_after.count(['movie']).reset_index()
        date_after_sum = groupby_after.sum().reset_index()
        date_after_mean = groupby_after.mean().reset_index()
        col = ['name', 'after_movie_count', 'after_total_gross', 'after_mean_gross']
        date_after_summary = pd.DataFrame(columns = col)
        date_after_summary['name'] = date_after_count['name']
        date_after_summary['after_movie_count'] = date_after_count['movie']
        date_after_summary['after_total_gross'] = date_after_sum['gross']
        date_after_summary['after_mean_gross'] = date_after_mean['gross']
        date_after_summary['date'] = date
        date_summary = pd.merge(left=date_before_summary, right=date_after_summary, how='outer', on = ['name', 'date'])
        df_final = df_final.append(date_summary, ignore_index = True)
    df_final = df_final.dropna()
    return df_final


date_boundry_upper = calc_comp_actor_df[calc_comp_actor_df.date < datetime(2016,1,1)].sort('date', ascending = False)
relevant_dates = date_boundry_upper[date_boundry_upper.date > datetime(1970,1,1)].sort('date', ascending = True)
relevant_dates

comparison_nc_df = calc_comp_actor_df[calc_comp_actor_df['name'] == 'Nicolas Cage']
comparison_nc_df = comparison_nc_df[['movie', 'date']].reset_index()
comparison_nc_df = comparison_nc_df[['movie', 'date']]
compare_frame_test = comparison_nc_df['movie'].tolist()
comparison_actor_df = calc_comp_actor_df
comparison_actor_df['nc_movie'] = comparison_actor_df[['movie']].isin(compare_frame_test)
comparison_actor_df[comparison_actor_df['nc_movie'] == True]
## This is a frame of actors, movies, and dates where they were in movies with Nicolas Cage
nc_actor_frame = comparison_actor_df[comparison_actor_df['nc_movie'] == True]
nc_actor_list = nc_actor_frame[['name','date']]
actor_list = nc_actor_list['name'].tolist()
date_list = nc_actor_list['date'].tolist()
zip_list = zip(actor_list, date_list)
analysis_frame2 = analysis_frame
analysis_frame2['name_date'] = zip(analysis_frame['name'], analysis_frame['date'])
analysis_frame2['nc_movies'] = analysis_frame.name_date.apply(lambda x: x in zip_list)
analysis_frame2[analysis_frame2['nc_movies'] == True]
analysis_frame2.head()



