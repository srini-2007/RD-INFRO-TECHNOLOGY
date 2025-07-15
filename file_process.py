import pandas as pd
import json
import os
df=pd.read_csv("data.csv")
print("Original Data")
print(df)
df_clean=df.dropna()
output_dir="output"
os.makedirs(output_dir,exist_ok=True)
output_path=os.path.join(output_dir,"data.json")
df_clean.to_json(output_path,orient="records",indent=4)
print("\nCleaed Data saved to",output_path)