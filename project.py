import pandas as pd
df=pd.read_excel("Retail-Supply-Chain-Sales-Dataset.xlsx")
print(df.head())
print()
print(df.shape)
print()
print(df.columns)
print(df.info())
print("\n Missing Values\n")
print(df.isnull().sum())
print("\n Statistics \n")
print(df.describe())
print("Total_Sales=",round(df["Sales"].sum(),2))
print("Total_Profit=",round(df["Profit"].sum(),2))
print("Total_Orders=",df["Order ID"].nunique())
print("Total_Customers=",df["Customer ID"].nunique())
print(df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)
print(df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)
print(df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
print(df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values()
      .head(10)
)
print(df["Returned"].value_counts())
df["Shipping Days"]=(
    df["Ship Date"]-df["Order Date"]).dt.days
print(df["Shipping Days"].describe())
print(df.groupby("Ship Mode")["Shipping Days"]
      .mean()
      .sort_values()
)
print(
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
print(df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)
df["Year"]=df["Order Date"].dt.year
print(
    df.groupby("Year")["Sales"]
    .sum()
    )
print(df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)
print(df["Shipping Days"].sort_values(ascending=False).head(20))
