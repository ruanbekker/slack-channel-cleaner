import requests
import time
import datetime

app_token = ''

def delete_from_in_hours(hours_in_int):
    now = datetime.datetime.now()
    response = (now - datetime.timedelta(hours=hours_in_int)).strftime("%s")
    return response
    
def list_channels():
    channel_data = {}
    params = {}
    params['token'] = app_token
    response = requests.get('https://slack.com/api/conversations.list', params=params).json()
    for items in response['channels']:
        channel_data[items['name']] = items['id']
    return channel_data

def post_message(channel_id, message, username, emoji):
    params = {}
    params['token'] = app_token
    params['channel'] = channel_id
    params['text'] = message
    params['username'] = username
    params['icon_emoji'] = emoji
    response = requests.post('https://slack.com/api/chat.postMessage', params=params).json()
    return response

def list_message_timestamps_by_channel(channel_id, latest):
    timestamps = []
    params = {}
    params['token'] = app_token
    params['channel'] = channel_id
    params['latest'] = latest
    response = requests.get('https://slack.com/api/conversations.history', params=params).json()
    for item in response['messages']:
        timestamps.append(item['ts'])
    return timestamps

def delete_messages_by_timestamp(channel_id, timestamp):
    params = {}
    params['token'] = app_token
    params['channel'] = channel_id
    params['ts'] = timestamp
    response = requests.post('https://slack.com/api/chat.delete', params=params).json()
    return response

def delete_messages_by_batch_timestamps(channel_id, timestamp_list):
    params = {}
    params['token'] = app_token
    params['channel'] = channel_id
    if type(timestamp_list) == list and len(timestamp_list) > 50:
        for each_ts in timestamp_list:
            time.sleep(1.22)
            params['ts'] = each_ts
            response = requests.post('https://slack.com/api/chat.delete', params=params).json()
            if response['ok'] == True:
                print('message deleted')
                
    if type(timestamp_list) == list and len(timestamp_list) < 50 and len(timestamp_list) > 40:
        for each_ts in timestamp_list:
            time.sleep(1)
            params['ts'] = each_ts
            response = requests.post('https://slack.com/api/chat.delete', params=params).json()
            if response['ok'] == True:
                print('message deleted')
                
    if type(timestamp_list) == list and len(timestamp_list) < 30:
        for each_ts in timestamp_list:
            params['ts'] = each_ts
            response = requests.post('https://slack.com/api/chat.delete', params=params).json()
            if response['ok'] == True:
                print('message deleted')
                
    return True
