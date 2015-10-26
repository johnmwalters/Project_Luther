'''
actor_page_loop loops through all actors on a list to capture their list of movies using the
actor_movie_table function

all_movies retrieves a list of lists consisting of all the movies found on all the actor's pages
'''

def actor_page_loop(actor_list):
    all_movies = []
    for row in actor_list:
        url = row[1]
        response = requests.get(url)
        while response.status_code != 200:
            if response.status_code == 403:
                break
            print "Waiting for webpage to respond"
            print url
            time.sleep(randint(1,10))
        page = response.text
        soup = BeautifulSoup(page)
        actor_page = row[0]
        try:
            movie_desc_block = soup.find_all('table')[1].find_all('tr')[0].find_all('td')[0].find_all('tr')
            movie_list = actor_movie_table(actor_page, movie_desc_block)
        except:
            movie_list = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]
        all_movies = all_movies + movie_list
    return all_movies