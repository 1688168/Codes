import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
  # merge DataFrames 'project' and 'employee' 
  df = pd.merge(project, employee, how='left', on='employee_id')

  # group by 'project_id' and find the mean of the 'experience_years'
  result = df.groupby('project_id')['experience_years'].mean().round(2).rename('average_years').reset_index()

  return result