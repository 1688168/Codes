$${\color{orange} Python Notes}$$

> How to print python dictionary

```
print(json.dumps(data, indent=4))
```

> How to return PANDAS dataframe as JSON for HTTP response

```
json_data=json.loads(df_data.to_json(orient='records'))
```

> How to convert NAN to None from dataframe

```
df_new = df_old.astype(object).where(df_old.notna(), None)
df_data.replace('N/A', np.nan, inplace=True) # replace 'N/A' with np.nan
df = df.replace({np.nan: None}) # replace non with python  None
```

> How to limit split num

```
_id, rest = log.split(" ", maxsplit=1)
```

> Pandas how to rename

```
df.rename(columns={'old_name':'new_name'}, inplace=True)
```

> Pandas how to apply for new column

```
df['new_col']=df.apply(func, axis=1)
```

> get current directory

```
curr_path = os.path.dirname(os.path.abspath(__file__))
```

> How to skip test case

```
@unittest.skip("some comments)
def test_something(self):
    pass
```

> Named Tuple

```
- namedtuple(typename, field_names)
ex:
- Declaring namedtuple
  Student = namedtuple('Student', ['name', 'age', 'DOB'])

- Instanciating
  S = Student('Nandini', '19', '2541997')

- Accessing
  print(S.name)


```

> How to make python HTTP post call with parameter

```
res = requests.post(url, data=json.dumps({'key1': val1, 'key2': val2}), verify=False)
```

> OrderedDict

```
- self.cache.move_to_end(key)
- self.cache.popitem(last=False)
- self.cache.pop(key)
```

> convert string to date
```
datetime.datetime.strptime(as_of_date, '%Y-%m-%d')
```
> convert date to string
```
datetime.datetime.today().strftime('%Y%m%d')
```

> regular expression, pattern matchin
```
pattern = r".*swap.*"
match = re.search(pattern, security_type.lower(), flag=re.IGNORECASE)
if match:
  print("matched)
else:
  print("unmatched")
```

> jupyter notebook setup
```
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
```

> json in sql server
```
create table schema.table_name
(
  AsOfDate datetime2 default getdate(),
  Report nvarchar(max) constraint [constraintName] check (isjson(Report)=1)
  ...
  constraint PK_Name PRIMARY KEY CLUSTERED (f1, f2)
)
```

> Dataframe style, Dataframe to HTML, Dataframe to PDF
* https://github.com/liannewriting/YouTube-videos-public/blob/main/generate-reports-with-python-sp500/generate_reports_with_python.ipynb

> list unpacking
```
colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *other = colors
```

> http request
```
res=requests.get(url, verify=False, params={'key1': val1, 'key2': val2})
if res.status_code !=200:
  print("handle failed status")

res = requests.post(url, json={})
if res.status_code !=200:
  print("handle failed status")

```

> Git
```git
git blame -W -M3 -- filename //ignore white space
git blame revision^ -W -M3 -- file.py //check one revision before this one
git show revision_num
git blame -L line_num,+2 fileName.py
git blame --since=1.week filename.py

# how to remove indentation
url?w=1
```

> how to print python dictionary  
```python
print("received event: " + json.dumps(event))
```