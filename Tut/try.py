import joblib
import numpy as np
import pandas as pd
k=joblib.load("Tut\colors_info.pkl")
#print(k['center_col'])
colors = pd.read_csv("Tut\ColorCodes.csv")
X = colors.copy()
X.drop(columns=['Color'],inplace=True)

clusters = k['clusters']
center_col = k['center_col']
centroids = k['centroids']

col = input()

def get_colors(col):
    rgbval = [X.iloc[i] for i in range(colors.shape[0]) if colors['Color'][i].lower() == col]
    distances = []
    for i in range(10):
        distances.append(np.linalg.norm(centroids[i] - rgbval, axis=1))
        
    return clusters[center_col[np.argmin(distances)]]

