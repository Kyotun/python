import pandas as pd
import random

data = pd.read_csv("intermediate/flash_card_app/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {'French': 'partie', 'English': 'part'}
print(data_dict)
new_data = [element for element in data_dict if element != current_card]
print("AAAAAAAAA")
new_data_df = pd.DataFrame(new_data).to_csv()
