"""
@author: TanishqVarshney
"""
import pandas as pd
data = pd.read_csv("Profile Similarity.csv", usecols = ['H1'])
s=data.applymap(lambda x: str(x.replace('{','')))
s1=s.applymap(lambda x: str(x.replace('}','')))
s2=s1.applymap(lambda x: str(x.replace(',',' -1 ')))
lengths_ = s2.H1.map(lambda x: len(x))
s2["After"] = s2["H1"] + [" -2"*1 for i in lengths_]
s2["After"].to_csv(r'F:\cpt project\output1.txt', sep='\t', index=False)