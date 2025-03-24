import os
import numpy as np

path_in = "./outputs/bias_test"

list_files = os.listdir(path_in)
print(list_files)

for file in list_files:
    full_name = os.path.join(path_in, file)
    data = np.load(full_name)
    np.savez(
        full_name, lon=data["lon"], lat=data["lat"], test_result=data["test_result"]
    )
