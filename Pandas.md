### > Regular Expression and String Pattern Matching

[1517]

- raw string

```python
def valid*emails(users: pd.DataFrame) -> pd.DataFrame:
    # Note how we use a raw string (putting an `r` in front) to avoid having to escape the backslash
    # Also note that we escaped the `@` character, as it has a special meaning in some regex flavors
    return users[users["mail"].str.match(r"^[a-zA-Z]a-zA-Z0-9*.-]\*\@leetcode\.com$")]
```

[1527]

- regular expression for string pattern matching

```python
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].str.contains(r"\bDIAB1", regex=True)]
```

[177] Nth Highest Salary

```python
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[["salary"]].drop_duplicates()  #remove duplicate
    if len(df) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]}) # construct empty dataframe
    return df.sort_values("salary", ascending=False).head(N).tail(1) #sorting[["salary"]]
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Series </span>

# <span style="color:green">====================</span>

> Create Series

```python
# create series from dataframe column.
# here master.index is userId (series value) and master.birthDate become the index as date
birth_dates = pd.Series(master.index, index=master.birthDate)
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Input/Output</span>

# <span style="color:green">====================</span>

> write to pickle

```python
team_splits.to_pickle(os.path.join("..", "some_file_name"))
```

> read pickle

```python
df = pd.read_pickle(os.path.join('..', 'file.pickle'))
df.to_pickle(os.path.join("..", "filename.pickle"))
```

> read excel

```python
df=pd.read_excel(os.path.join(input_filename), index_col=0)

# read a column and make it a series
pokemon = pd.read_csv("pokemon.csv", usecols=["Name"]).squeeze("columns")
pokemon
```

# <span style="color:green">====================</span>

# <span style="color:blue"> prepare data/clean data</span>

# <span style="color:green">====================</span>

> which columns has null values

```python
df.isnull().any()
```

> which rows has null values

```python
df[df.isnull().any(axis=1)]

# Are there any rows with only null values?
df.isnull().all(axis=1).any()

# Are there any columns with no null values at all?
df.notnull().all()
```

> find unique count

```python
teams.nunique(y)
```

> set index

```python
scoring.reset_index(drop=True, inplace=True)
```

> count

```python
master["pos"].value_counts()
```

> find null count

```python
master["playerID"].pope(pd.isnull).value_count()
or
isnull(master["playerID"]).value_counts()
master = master.filter(regex="(playerID|pos|^birth)|(Namd$)")
```

> drop columns

```python
columns_to_keep=["c1", "c2", ...]
master.filter(columns_to_keep).head()

# Create a series containing indices for every 6th row
every_6th_row = pd.Series(range(5, len(df), 6))

# Are all these rows NOT null?
df['MIN_TEMP_GROUND'][every_6th_row].notnull().all()

# Are all other rows null?
# Q: Can you rewrite this line to use df.loc?
df['MIN_TEMP_GROUND'].drop(every_6th_row).isnull().all()
```

> dataframe memory size

```python
def mem_mib(df):
    print("{0:.2f} MiB").format(df.memory_usage().sum()/(1024*1024))
```

> drop rows

```python
master = master.dropna(subset=["playerID"], how="all")
```

> categorical

```python
pd.Categorical(master["pos"])
chicago["Department"] = chicago["Department"].astype("category")
```

# <span style="color:green">====================</span>

# <span style="color:blue"> filtering Data</span>

# <span style="color:green">====================</span>

```python
# filter by string containing
water_workers = chicago["Position Title"].str.lower().str.contains("water")
chicago[water_workers]

starts_with_civil = chicago["Position Title"].str.lower().str.startswith("civil")
chicago.loc[starts_with_civil]

ends_with_iv = chicago["Position Title"].str.lower().str.endswith("iv")
chicago[ends_with_iv]
```

> where

```python
# for those rows that is not true, filled with nan
heights.where(heights.between(pmin, pmax), inplace=True)

# convert nan to None before returning to http request
df = pd.DataFrame(d)
dumps(df.where(pd.notnull(df), None))) # this might not work for numerical values

# convert nan to None before returning to http request by introducing simplejson
import simplejson

response = df.to_dict('records')
simplejson.dumps(response, ignore_nan=True,default=datetime.datetime.isoformat)

```

> converting NaN to null

```python
df = pd.DataFrame({
  'words': ['on', 'off'],
  'lists': [
    [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
    [[np.nan], [np.nan], [np.nan]],
  'dicts': [
    {'S': {'val': 'A'}},
    {'S': {'val': np.nan}},
  ]
})

"""
If you convert it to a list of dicts, Pandas retains the native nan values:
"""

json.dumps(df.to_dict(orient='record'))

> [{
    "words": "on",
    "lists": [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
    "dicts": {"S": {"val": "A"}}
  },
  {
    "words": "off",
    "lists": [[NaN], [NaN], [NaN]],
    "dicts": {"S": {"val": NaN}}
  }]

"""
But if you have Pandas convert it straight to a JSON string, it'll sort that out for you:
"""
df.to_json(orient='records')

> [{
    "words": "on",
    "lists": [[1,1,1],[2,2,2],[3,3,3]],
    "dicts": {"S":{"val":"A"}}
  },
  {
    "words": "off",
    "lists": [[null],[null],[null]],
    "dicts": {"S":{"val":null}}
  }]
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Manipulating Data</span>

# <span style="color:green">====================</span>

`apply on Series`: operate on each cell of a series

```python
# ex 1:
train['name_length'] = train.name.apply(len)

# ex 2:
def my_function(my_list, position):
    return my_list[position]
- train.name.str.split(',').apply(my_function, position=0)
```

`apply on dataframe`: operate on columns

```python
# get max on each column (axis=0)
df.apply(max, axis=0)

# (apply on each row) which column (name) has the max value

df.apply(np.argmax, axis=1)
```

`applymap`: Operate on each cell

```python
# convert all values to flow
df.applymap(float)
```

> apply, map, applymap
> `map on series`: convert a series value to another value

```python
# create a new column that maps values on another column from string to num
train['sex_num'] = train.Sex.map({'female':0, 'male':1})
```

> drop duplicates

```python
df=df.drop_duplicates(keep='first')
```

### > unique values:

- nunique (Series or dataframe)

> merge_asof(df1, df2, by='category', on='col1', direction='forward', allow_exact_matches=False, tolerance=pd.Timedelta('1s))

- df1 left join df2
- on is default looking 'backward'

> drop duplicate

```python
df=df.drop_duplicates(subset=['SubportfolioID'], keep='first)
```

> copy dataframe

```python
df2 = df.copy()
```

> assign

```python
df_all = df_all.assign(column_name=lambda x: (x['col1']/x[`col2`]))
master = master.assign(birthDate = pd.to_datetime({'year': master.birthYear,
                                                   'month': master.birthMon,
                                                   'day': master.birthDay}))

master.master.drop(columns=['birthYear', 'birthMon', 'birthDay'])
```

```python
# We can use fillna() to fill in missing data based on the data that is present
df['MIN_TEMP_GROUND'].fillna(method='bfill', inplace=True)

# Now that we have no more nulls in MIN_TEMP_GROUND
# what are the dates where missing values occur?
df.loc[df.isnull().any(axis=1), 'YYYYMMDD'].drop_duplicates() # remove rows with null values

# Shortest solution: Just drop everything
nulls_dropped = df.dropna() #what are the rows being removed by dropna
nulls_dropped.info()
# Another idea: just drop rows that have less than 7 columns filled
# This leaves us with only two rows that contain null values
drop_thresh = df.dropna(thresh=7)
drop_thresh[drop_thresh.isnull().any(axis=1)]
```

> String manipulation

```python
# The most common first word in our job positions/titles
chicago["Position Title"].str.split(" ").str.get(0).value_counts() #get element from list
# Finding the most common first name among the employees

chicago["Name"].str.title().str.split(", ").str.get(1).str.strip().str.split(" ").str.get(0).value_counts()


# split a string and make each element as a column
chicago[["Last Name", "First Name"]] = chicago["Name"].str.split(",", expand=True)

# create multiple columns in one shot
chicago[["Primary Title", "Secondary Title"]] = chicago["Position Title"].str.split(" ", expand=True, n=1)
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Timestamp</span>

# <span style="color:green">====================</span>

> declare timestamp

```python
ts = pd.Timestamp("1997-03-04 14:21:54")

# get year from ts
ts.year

# get day_name from ts
ts.day_name()

# with timezone
tsz = tsz.tz_localize('America/Toronto')
Timestamp('1975-03-04 00:00:00-0500', tz='America/Toronto')

# convert datetime to string
string = master.birthDate.dt.strftime('%Y-%d-%m')
parsed = pd.to_datetime(string, format="%Yx%mxx%d", errors='coerce')
parsed = pd.to_datetime(string, format="%Yx%mxx%d", errors='ignore')

# from string to date - here convert a series of date_string to date-series
try:
    dates = pd.to_datetime(strings, format="%Yxx%mxx%d)
except Exception as e:
    print(e)



```

> Timedelta

```python
td = pd.Timedelta('3 days 02:13:10')

# timedelta components
diff.components
- diff = diff + '5H' - '10M'
- diff.round('10D')
- diff.round('1H')
```

> Period

```python
p = pd.Period('1999-03', 'M')
p.start_time
p.end_time
p.start_time < ts < p.end_time

birth_dates.resample('1M') # resample period, resize period
```

> add date to the whole series

```python
birth_date.shift(1, freq="D")
```

> Business date

```python
from pandas.tseries.offsets import BDay
p=birth_dates.index[2]
print(p.to_timestamp()+BDay(7))
```

# <span style="color:green">====================</span>

# <span style="color:blue"> pivot/melt/stack/unstack </span>

# <span style="color:green">====================</span>

> Stack/Unstack

```python
team_splits = team_splits.stack(level=0) #long format
team_splits.unstack(level=["year", "month"]).head() # wide format
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Groupby</span>

# <span style="color:green">====================</span>

> groupby, transform

> Transform groups

```python
def transform_df(source_df): # original dataframe
    group_dfs=[]
    # group and process each groupped dataframe
    for name, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:, 'medium'] = fill_values(group_df['medium])
        group_dfs.append(filled_df)
    new_df = pd.concat(group_dfs)
    return new_df

#> using built-in transform


# transform will call the function for each groupped dataframe
# transform called on a group-dataframe
# operating on each groupped dataframe
# here we only select a column from the group, so the function called by transform receives a series
grouped_medium = df.groupby('artist')['medium']
df.loc[:, 'medium'] = grouped_medium.transform(fill_values) #call transform on groupped dataframe.
```

> filtering groupby

```python
grouped_titles = df.groupby('titles')
condition = lambda x: len(x.index) > 1 # x should be the dataframe of a group
filtered_df = grouped_titles.filter(condition) # remove groups that has only 1 row
```

```python
grouped_titles = df.groupby('title')
# size of each group, count of each group
title_counts = grouped_titles.size().size().sort_values(ascending=False)
```

> groupby aggregation

```python
grouped_acq_year = df.groupby('artist')['acquisitionYear']
min_acquisition_year = grouped_acq_year.agg(np.min)
or
min_acquisition_year = grouped_acq_year.min()

```

> apply diff aggregation on diff column

```python
sector.agg("col1":"sum", "col2":"avg")
```

> Group by

```python
df=df.groupby('a_column', as_index=False)['the_column_to_aggregate'].sum()
g=athletes.groupby('nationality')[['gold','silver','bronze']]
g.sum()

# group on multiple columns
atheletes.groupby(['sport', 'nationality'])['gold'].sum()

# first, last -> first/last group row


```

> custom function on group

```python
# here custom_function takes a dataframe of a group (or series if only 1 column selected)
groupby.apply(custom_function)
```

> get dataframe of a group

```python
sectors.get_group("Energy")
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Multiindex</span>

# <span style="color:green">====================</span>

> create multiindex

```python
scoring.set_index(['playerID','year'])
```

> create multiindex from array

```python
months = team_splits.columns.map(lambda x: x[:3])
midx = pd.MultiIndex.from_arrays([months, metrics])
team_splits.columns = midx
```

> multiindex basic operations

```python
scoring.groupby(level=1)['goals'].max()
scoring.groupby(level='year')['goals'].max()
```

> multiindex object, multiindex slicing, multiindex sorting

```python
idx = pd.IndexSlice
scoring.sort_index() #sort before slicing
scoring.loc[idx['aaltoan01', 1997:2000], :]
scoring.loc[idx[:, 1997:2000], :]

# another sorting example
mi = mi.sort_index(level='year')
```

> is multiindex sorted

```python
mi.index.is_lexsorted()
```

> swap index level

```python
swapped = mi.swaplevel()

```

> multiindex number of level

```python
len(mi.index.levels)
or
mi.index.nlevels
```

> find index of max value in each group, groupby multiindex

```python
# this is returning max index of each group by year (remember this is grouping on multiindex)
mi.groupby(level="year")['G'].idxmax().head()

# how to find the whole row from dataframe that is with max value per some kind of groupping?
# retrieving the whole record by idx returned from idxmax
mi.loc[mi.groupby(level="year")['G'].idxmax()].head()
```

> get locations from index slicing

```python
# this is getting an list of index locations per a given multiindx slicing
loc = mi.index.get_loc((idx['aaltoan01':'adamscr01'], 1007:2000))
sliced = mi.iloc[locs, :]
```

> get many locs from multiindex; slicing multiindex and use it to retrive rows from original dataframe

```python
import numpy as np
def get_many_locs(df, slices):
    arr = np.empty(0, dtype="int")
    for s in slices:
        locs = df.index.get_locs((s))
        arr = np.concatenate((arr, locs))
    return arr


locs = get_many_locs(mi, (idx['aaltoan01':'adamscr01', 1997:2000],
                          idx['aaltoan01':'adamscr01', 2004:206]))

sliced = mi.iloc[locs, :]
```

> stack/undstack multiindex

```python
# transpose one level of multiIndex from columns to row (from wide to long dataframe)
team_splits = team_splits.stack(level=0)

# swaplevel, reorder level
team_splits = team_splits.swaplevel(1, 2)

team_splits = team_splits.reorder_level([2,0,1])

# transpose a row index to column
team_splits.unstack(level=['year', 'month'])
```

> change multiIndex name

```python
team_splits.index.levels[2].name="month"
```

# <span style="color:green">====================</span>

# <span style="color:blue"> formatting, styling</span>

# <span style="color:green">====================</span>

```python
# percentage, dollar sign, padding
- df.style.format.({'SumSales': '${0:,0f}'}, #thousand seperator
                    'PercSales':{:.0%}, # percent
                    'numSales':'{:0>3d}') #padding zero

# highlight max/min
df.style.highlight_max(subset=['col_list'], color="red")
df.style.highlight_between(left=5000, right=10000, subset=['col'])
df.style.highlight_quantiles(q_left=0.25, q_right=0.75, subset=['col'])

# applymap for cell color
def add_color(x):
    if x < 50:
        color='red'
    elif x < 100:
        color='yellow'
    else:
        color='blue'
    return f'background:{color}'

df.style.applymap(add_color, subset=['col_list'])
```

# <span style="color:green">====================</span>

# <span style="color:blue"> read from URL </span>

# <span style="color:green">====================</span>

```python
# post request
service='https://some_server'
endpoint="/some_end_point"
url=service+endpoint
json={'portfolioID': 100, 'AsOfDate:'mm/dd/yyyy'}
resp=request.post(url, json=json, verify=False)
hm=pd.DataFrame(resp.json(['data']))

# get request
args={}
resp = requests.get(url, params=args, verify=False)
data=pd.read_json(json.dumps(resp.json()['data']['report_data']), orient='records')
```

```

```
