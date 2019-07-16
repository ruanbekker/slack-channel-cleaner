# slack-channel-cleaner
Python Script to Remove Slack Messages. 

## About

I am using a free-plan slack workspace, and I needed a way to clean some of my slack channels such as notifications, builds channels without delete/recreating them.


## Authentication

Create your app at https://api.slack.com/apps and set the application token as:

```
app_token = 'xoxo....'
```

## Usage

List your slack channels:

```
>>> slack_channels = list_channels()
>>> slack_channels
{u'system_events': u'ABCDEFGHI', u'test': u'BBCDEFGHI', ...
```

Get all the messages from the slack channel that you want to delete. The method 2 parameters, channel_id and the timestamp where it needs to start deleting from (in hours). In this case a hour from now to the last message:

```
>>> timestamps = list_message_timestamps_by_channel(slack_channels['test'], delete_from_in_hours(1))
>>> timestamps
[u'1563309768.000400', u'1563309754.000300',...
```

Pass the timestamps with the slack channel id as parameters to this method:

```
>>> delete_messages_by_batch_timestamps(slack_channels['test'], timestamps)
message deleted
message deleted
message deleted
message deleted
message deleted
message deleted
```

## Rate Limiting

The delete method uses Tier3, which gives you +- 50 calls a minute:
- https://api.slack.com/docs/rate-limits#tier_t3

I have set logic that if the list of timestamps are more than 50, it will delay 1.22 seconds between each delete call, 1 second for less than 50, more than 30 and no delay for less than 30 
