def movie_page_loop(loop_df):
    nc_movies = []
    for row in loop_df:
        url = row
        response = requests.get(url)
        while response.status_code != 200:
            if response.status_code == 403:
                break
            print "Waiting for webpage to respond"
            print url
            time.sleep(randint(1,10))
        page = response.text
        soup = BeautifulSoup(page)
        #Sets the block that we are looking at that contains the contributors for the film
        try:
            movie_name = soup.find_all('b')[1].text
            movie_desc_block = soup.find(text = 'The Players').parent.parent.find_all('table')[0].find_all('tr')
            movie = movie_desc_table(movie_name, movie_desc_block)
        except:
            movie = [["","","",""]]
        nc_movies.append(movie)
    return nc_movies