from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Quick check
print(df.head())
print(df.shape)

# Ensure figs directory exists
os.makedirs("figs", exist_ok=True)

# Make a boxplot of Median Income (MedInc)
plt.figure(figsize=(6, 4))
df["MedInc"].plot(kind="box")
plt.title("Boxplot of Median Income")
plt.ylabel("Median Income")

# Save figure
plt.savefig("figs/boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

print("Saved boxplot to figs/boxplot.png")

pip install -r requirements.txt
cd path/to/A01

python src/boxplot.py

git add figs/boxplot.png
git commit -m "Add boxplot figure"
git push
