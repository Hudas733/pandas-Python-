import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\Flavors.csv")
df

import pandas as pd
df = pd.read_csv(r"C:\Users\nicor\OneDrive\Desktop\demo python\Flavors.csv")
df
df.groupby('Base Flavor').min()
df.groupby('Base Flavor').mean(numeric_only = True)
df.groupby('Base Flavor').max()
df.groupby('Base Flavor').sum()
df.groupby('Base Flavor').agg({'Flavor Rating': ['mean','max','count','min'],'Texture Rating':['mean','max','count','min']})
df
df.groupby(['Base Flavor', 'Liked']).mean(numeric_only=True)
df.groupby('Base Flavor').describe()