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