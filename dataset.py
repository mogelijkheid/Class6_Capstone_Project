import pandas as pd
import numpy as np


df = pd.read_pickle('auto4.pkl')


def make(most=False):
    make_list = df.make.unique()
    if most:
        most_brand = df.make.value_counts().index.to_list()[0]
        sorted_makes = np.sort(make_list)
        # returns most value index number
        return sorted_makes.tolist().index(most_brand)
    else:
        return np.sort(make_list)


def model(make, most=False):
    model_list = df.model[df.make == make].unique()
    if most:
        most_model = df.model[df.make == make].value_counts().index.to_list()[
            0]
        sorted_makes = np.sort(model_list)
        # returns most value index number
        return sorted_makes.tolist().index(most_model)
    else:
        return np.sort(model_list)