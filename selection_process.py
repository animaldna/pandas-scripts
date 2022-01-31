import pandas as pd
import os

# collate all data
data_set = {}
for root, dirs, files in os.walk('/root/devops/'):
    for filename in files:
        subj = filename.split('.')[0]
        data = pd.read_csv(os.path.join(root, filename), sep=' ', header=None, names=['Name', 'Surname', 'Score'])
        try:
            data_set[subj] = pd.concat([data_set[subj], data])    
        except KeyError:
            data_set[subj] = data

sorted_data = sorted(data_set.items())

for subject in sorted_data:
    print(f'{subject[0]}:')
    final_score = subject[1].sort_values('Score', ascending=False).iloc[0:4, 0:2].to_csv(sep=" ", index=False, header=False)
    print(final_score)
