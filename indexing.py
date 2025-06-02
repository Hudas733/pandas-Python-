import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv",)
df
#if gusto mo maging index yung isang column
import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv",index_col = "Brand")
df

#GUSTO MO DALAWA INDEX COLUMN MO
import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\products-100.csv")
df.set_index(['Name', 'Brand'], inplace=True)
df.sort_index()
pd.set_option('display.max.columns', 100)
df


#SORT
import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\world_population.csv")
df.set_index(['Continent', 'Country'],inplace=True)
df.sort_index()
df.loc['Africa']


#Merg,Join and Concatenate

import pandas as pd
df1 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\LOTR.csv")
df1

import pandas as pd
df2 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\LOTR 2.csv")
df2
df1.merge(df2,on=['FellowshipID','FirstName'])

#OUTER JOIN
import pandas as pd
df1 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\LOTR.csv")
df1.merge(df2, how = 'outer')
df1.merge(df2, how = 'left')
df1.merge(df2, how = 'right')
df1.merge(df2, how = 'cross')
df3 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix='_left', rsuffix='_right', how = 'outer')
df3
#CONCAT
pd.concat([df1,df2])
pd.concat([df1,df2],join='inner')
pd.concat([df1,df2],join='outer')
import pandas as pd
df2 = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\LOTR 2.csv")
df2