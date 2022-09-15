import os
from string import ascii_uppercase

from pandas import DataFrame
from sklearn import datasets


n_features = 5
n_samples = 1000
target = "Target"
features = list(ascii_uppercase)[:n_features]

X, y = datasets.make_classification(
    n_samples=n_samples,
    n_features=n_features,
    n_informative=5,
    n_repeated=0,
    n_redundant=0,
    n_classes=5,
    random_state=42,
)

df = DataFrame(data=X, columns=features)
df[target] = y
df.head()

df.to_csv(os.path.join("dataset2.csv"), index=False)
