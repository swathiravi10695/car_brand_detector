import pandas as pd
import json
data = pd.read_csv("./train_labels.csv")
y = data[['class_id','class_name']]
classes_names = y['class_name'].unique()
classes_names.sort()
pbtxt_content = ""
for i, class_name in enumerate(classes_names):
    pbtxt_content = (
        pbtxt_content
        + "item {{\n    id: {0}\n    name: '{1}'\n}}\n\n".format(
            i + 1, class_name
        )
    )
pbtxt_content = pbtxt_content.strip()
with open('./label_map.pbtxt', "w") as f:
    f.write(pbtxt_content)