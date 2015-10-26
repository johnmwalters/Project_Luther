y, X = dmatrices('after_mean_gross ~ before_mean_gross + nc_movies', data=analysis_frame2, return_type='dataframe')


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)


model = sm.OLS(y_train, X_train)
results = model.fit()

results.summary()


get_ipython().magic(u'matplotlib inline')
cols = ['after_movie_count', 'before_movie_count']
pd.scatter_matrix(analysis_frame2[cols], figsize=(10, 10))
cols = ['after_mean_gross', 'before_mean_gross']
pd.scatter_matrix(analysis_frame2[cols], figsize=(10, 10))


count_list = range(1,6)

def analysis_loop(count_list):
    frame_list = []
    nc_dates = calc_comp_actor_df[calc_comp_actor_df['name'] == 'Nicolas Cage']
    nc_dates_list = nc_dates['date'].tolist()
    for x in count_list:
        date_range = x*300
        analysis_frame = date_loop(nc_dates_list, date_range)
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
        analysis_frame['name_date'] = zip(analysis_frame['name'], analysis_frame['date'])
        analysis_frame['nc_movies'] = analysis_frame.name_date.apply(lambda x: x in zip_list)
        frame_list.append(analysis_frame)
    return frame_list

count_list = range(1,11)
all_models = analysis_loop(count_list)


results = []
models = []
for frame in all_models:  #list of frames #originally labeled all_models
    y, X = dmatrices('after_mean_gross ~ before_mean_gross + nc_movies', data=frame, return_type='dataframe')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)
    model = sm.OLS(y_train, X_train)
    models.append(model)
    results.append(model.fit())

len(results), len(models)
adj_r_sq = []

for i in range(len(results)):
    adj_r_sq.append(results[i].rsquared_adj)
plt.figure(figsize = (10, 3))
plt.plot(adj_r_sq)

plt.title('Adjusted R-squared vs Date Range (Gross)')
plt.ylabel('R-squared')
plt.xlabel('Date Range')  
plt.gcf()
plt.savefig('r squared gross.png')


adj_r_sq


# ### Model 4 observes the affect Nicolas Cage has on individuals before and after 1200 days (approx 3 years) 


y, X = dmatrices('after_mean_gross ~ before_mean_gross + nc_movies', data=all_models[4], return_type='dataframe')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
model = sm.OLS(y_train, X_train)
results = model.fit()
results.summary()


cols = ['after_movie_count', 'before_movie_count']
pd.scatter_matrix(all_models[4][cols], figsize=(10, 10))
cols = ['after_mean_gross', 'before_mean_gross']
pd.scatter_matrix(all_models[4][cols], figsize=(10, 10))


results = []
models = []
for frame in all_models:  #list of frames #originally labeled all_models
    y, X = dmatrices('after_movie_count ~ before_movie_count + nc_movies', data=frame, return_type='dataframe')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)
    model = sm.OLS(y_train, X_train)
    models.append(model)
    results.append(model.fit())

len(results), len(models)
adj_r_sq = []

for i in range(len(results)):
    adj_r_sq.append(results[i].rsquared_adj)
plt.figure(figsize = (10, 3))
plt.plot(adj_r_sq)
plt.title('Adjusted R-squared vs Date Range (Count)')
plt.ylabel('R-squared')
plt.xlabel('Date Range')  
plt.gcf()
plt.savefig('r squared count.png')


y, X = dmatrices('after_movie_count ~ before_movie_count + nc_movies', data=all_models[4], return_type='dataframe')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
model = sm.OLS(y_train, X_train)
results = model.fit()
results.summary()

results = []
models = []
for frame in all_models:  #list of frames #originally labeled all_models
    y, X = dmatrices('after_movie_count ~ before_movie_count + before_mean_gross + nc_movies', data=frame, return_type='dataframe')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)
    model = sm.OLS(y_train, X_train)
    models.append(model)
    results.append(model.fit())

len(results), len(models)
adj_r_sq = []

for i in range(len(results)):
    adj_r_sq.append(results[i].rsquared_adj)
plt.figure(figsize = (10, 3))
plt.plot(adj_r_sq)
plt.title('Adjusted R-squared vs. Nicolas Affect Date Range')

y, X = dmatrices('after_movie_count ~ before_movie_count + before_mean_gross + nc_movies', data=all_models[4], return_type='dataframe')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
model = sm.OLS(y_train, X_train)
results = model.fit()
results.summary()


results = []
models = []
for frame in all_models:  #list of frames #originally labeled all_models
    y, X = dmatrices('after_total_gross ~ before_total_gross + nc_movies', data=frame, return_type='dataframe')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)
    model = sm.OLS(y_train, X_train)
    models.append(model)
    results.append(model.fit())

len(results), len(models)
adj_r_sq = []

for i in range(len(results)):
    adj_r_sq.append(results[i].rsquared_adj)
plt.figure(figsize = (10, 3))
plt.plot(adj_r_sq)
plt.title('Adjusted R-squared vs. Nicolas Affect Date Range')


y, X = dmatrices('after_total_gross ~ before_total_gross + nc_movies', data=all_models[3], return_type='dataframe')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
model = sm.OLS(y_train, X_train)
results = model.fit()
results.summary()


cols = ['after_total_gross', 'before_total_gross']
pd.scatter_matrix(all_models[3][cols], figsize=(10, 10))


groups = all_models[4].groupby('nc_movies')

# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group.before_mean_gross, group.after_mean_gross, marker='o', linestyle='', ms=5, label=name)
ax.legend()
plt.ylabel('After Mean Gross')
plt.xlabel('Before Mean Gross')
plt.title('Average Gross with Nicolas Cage')
plt.gcf()
plt.savefig('avg gross.png')
plt.show()


groups = all_models[4].groupby('nc_movies')

# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group.before_movie_count, group.after_movie_count, marker='o', linestyle='', ms=5, label=name)
ax.legend()
plt.ylabel('After Count')
plt.xlabel('Before Count')
plt.title('Number of Movies Because of Cage')
plt.gcf()
plt.savefig('count.png')
plt.show()

y, X = dmatrices('after_movie_count ~ before_movie_count + before_mean_gross + nc_movies', data=all_models[4], return_type='dataframe')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
model = sm.OLS(y_train, X_train)
results = model.fit()
results.summary()


predicts = results.predict(X_test)
predicts


mse = mean_squared_error(y_test, predicts)



results = []
models = []
for frame in all_models:  #list of frames #originally labeled all_models
    y, X = dmatrices('np.sqrt(after_movie_count) ~ np.sqrt(before_movie_count) + nc_movies', data=frame, return_type='dataframe')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)
    model = sm.OLS(y_train, X_train)
    models.append(model)
    results.append(model.fit())

len(results), len(models)
adj_r_sq = []

for i in range(len(results)):
    adj_r_sq.append(results[i].rsquared_adj)
plt.figure(figsize = (10, 3))
plt.plot(adj_r_sq)
#plt.plot(range(1, 16), adj_r_sq)
plt.title('Adjusted R-squared vs. Nicolas Affect Date Range')



groups = all_models[4].groupby('nc_movies')

# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group.before_movie_count, group.after_movie_count, marker='o', linestyle='', ms=5, label=name)
ax.legend()
plt.ylabel('After Count')
plt.xlabel('Before Count')
plt.title('Number of Movies Because of Cage')
plt.gcf()
plt.savefig('count.png')
plt.show()