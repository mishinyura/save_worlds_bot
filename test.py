import json
import re
import os

data = {

}
with open('./database/new_data_trans.json', 'r', encoding='utf-8') as file:
  data = json.load(file)


for key, val in data.items():
    lst = val["media_list"]

    for file_name in lst:
      if re.match('.*-Ivy.mp3', file_name):
        data[key]['media_list'].remove(file_name)
        os.remove(f'./media/{file_name}')

with open('./database/new_data_trans.json', 'w', encoding='utf-8') as file:
  json.dump(data, file, ensure_ascii=False)