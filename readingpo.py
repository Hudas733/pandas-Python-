import pandas as pd

df1 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\tutorial_csv.csv")


import pandas as pd
df = pd.read_table(r"C:\Users\nicor\OneDrive\Desktop\demo python\raw data\chatgpt.txt", sep = ',')
df  


import pandas as pd
df3= pd.read_excel(r"C:\Users\nicor\OneDrive\Desktop\demo python\Inventory-Records-Sample-Data.xlsx", sheet_name = 'Sheet2')
df3
df3['name']
df3.loc[5]


import pandas as pd
df1 = pd.read_json(r"C:\Users\nicor\OneDrive\Desktop\demo python\sample-json-files-sample1.json")
df1['city']

import pandas as pd
df2 = pd.read_excel(r"C:\Users\nicor\OneDrive\Desktop\demo python\Inventory-Records-Sample-Data.xlsx")
df2

#FILTERING COLUMNS AND ROWS
#FILTERING ORDERING

import pandas as pd

df4 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv")
df4[df4['Category'].str.contains('Laptops')]

import pandas as pd
df4 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv")
categories = ['Cleaning Supplies','Kitchen Appliances']
df4[df4['Category'].isin(categories)]

import pandas as pd

df5 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv")
df6 = df5.set_index('Category')
df6


#FILTER KUNG ANOING COLUMN LANG YUNG LALABAS
import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv")
df1 = df.filter(items =['Name','Brand'])
df1

import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv")
df.filter(items= ['Name'])
