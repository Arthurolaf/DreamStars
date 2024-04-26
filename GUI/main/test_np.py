import numpy as np
import pandas as pd
empty = {"l_control_panel":[],"c_control_panel":[],"r_control_panel":[]}
df = pd.DataFrame(empty)
for i in range(4):
    new_list = []
    for j in range(3):
        new_list.append((i,j))
    df.loc[len(df)] = new_list
    print(new_list)
print(df)
