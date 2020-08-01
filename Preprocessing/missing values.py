
# Pandas Dataframe

# Find columns that have nans
train.isnull().any()

# For each column fill the nans with mean of that column
train.fillna(train.mean())
