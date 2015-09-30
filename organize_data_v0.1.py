import pandas as pd 

def coactor_list():
	cols = ['name', 'nc_movie', 'release_date', 'nc_gross', 'date_early', 'date_late']
	df = pd.read_csv('turnstile_150627.txt', names=cols, header=True)

def coactor_movies():
	cols = ['name', 'movie', 'sec_degree_actor', 'gross', 'release_date']