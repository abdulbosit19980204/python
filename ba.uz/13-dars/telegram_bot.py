import requests

API_TOKEN = '6189703946:AAGb1TA2yDg-sdu0c_AIDn39_07AuzvlZgE'
CHAT_ID = 1209619850
# API_URL = 'https://api.telegram.org/bot{}/getMe'.format(API_TOKEN)
# API_URL = 'https://api.telegram.org/bot{}/getUpdates'.format(API_TOKEN)
API_URL = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=ishlar yaxshimi?'.format(API_TOKEN, CHAT_ID)
respose = requests.get(API_URL)
print(respose.json())

"""
{'ok': True, 'result': {'id': 6189703946, 'is_bot': True, 'first_name': 'tmscoder', 
'username': 'tmscoderbot', 'can_join_groups': True, 'can_read_all_group_messages': False,
 'supports_inline_queries': False}}

"""
"""
{'ok': True, 'result': [{'update_id': 389398452,
 'message': {'message_id': 136, 'from':
  {'id': 1209619850, 'is_bot': False, 'first_name': "To'ychiyev Abdulbosit (عبد الباسط)",
   'username': 'abdulbosit_tatu', 'language_code': 'en'},
    'chat': {'id': 1209619850, 'first_name': "To'ychiyev Abdulbosit (عبد الباسط)", 'username': 'abdulbosit_tatu', 'type': 'private'}, 'date': 1703346079, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}, {'update_id': 389398453, 'message': {'message_id': 137, 'from': {'id': 1209619850, 'is_bot': False, 'first_name': "To'ychiyev Abdulbosit (عبد الباسط)", 'username': 'abdulbosit_tatu', 'language_code': 'en'}, 'chat': {'id': 1209619850, 'first_name': "To'ychiyev Abdulbosit (عبد الباسط)", 'username': 'abdulbosit_tatu', 'type': 'private'}, 'date': 1703346082, 'text': 'hello'}}]}

"""
