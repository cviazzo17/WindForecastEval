"""Cast numpy.ndarray()s' type of float from"""

import os
import numpy as np

path_in = "./data"
path_out = "./data"

list_files = os.listdir(path_in)
print(list_files)

for file in list_files:
    full_name = os.path.join(path_in, file)
    data = np.load(full_name)

    u10m = data["U10M"]
    v10m = data["V10M"]
    lon = data["longitude"]
    lat = data["latitude"]

    u10m = u10m.astype("float32")
    v10m = v10m.astype("float32")
    ws10m = u10m**2 + v10m**2

    full_name_out = os.path.join(path_out, file)
    np.savez(full_name_out, W10M=ws10m, latitude=lat, longitude=lon)
