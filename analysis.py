import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Load data
df = pd.read_csv("melbourne_data_jobs_2025.csv")

print(f"Dataset loaded: {len(df)} rows")
print(f"\nColumns: {list(df.columns)}")
print(f"\nRole breakdown:\n{df['role'].value_counts()}")
print(f"\nMedian salary by role:\n{df.groupby('role')['salary_aud'].median().sort_values(ascending=False)}")
print(f"\nFastest growing roles:\n{df.groupby('role')['yoy_growth_pct'].mean().sort_values(ascending=False)}")

all_skills = pd.concat([df["top_skill_1"], df["top_skill_2"], df["top_skill_3"]])
print(f"\nTop 10 skills:\n{all_skills[all_skills != ''].value_counts().head(10)}")

print(f"\nSalary by experience level:")
exp_order = ["Graduate (0-1 yrs)", "Junior (1-3 yrs)", "Mid (3-5 yrs)", "Senior (5+ yrs)"]
print(df.groupby("experience_level")["salary_aud"].agg(["median","mean"]).reindex(exp_order))

print(f"\nWork arrangement split:\n{df['remote_friendly'].value_counts(normalize=True).mul(100).round(1)}")
print(f"\nTop industries by posting volume:\n{df['industry'].value_counts()}")
