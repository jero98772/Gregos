import seaborn as sns
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings("ignore")


diamonds = sns.load_dataset("diamonds")

diamonds.head()

diamonds.shape


diamonds.describe()
diamonds.describe(exclude=np.number)

# Extract feature and target arrays
X, y = diamonds.drop('price', axis=1), diamonds[['price']]
cats = X.select_dtypes(exclude=np.number).columns.tolist()
for col in cats:
   X[col] = X[col].astype('category')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)