#!/usr/bin/env python

# modified from:
# https://developers.google.com/api-client-library/python/samples/authorized_api_cmd_line_calendar.py

import httplib2
import os
import sys
import time
import datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    # get last 30 days
    epoch_time = time.time()
    start_time = epoch_time - 2629743  # 30 days ago
    end_time = epoch_time + 12 * 3600  # 12 hours in the future
    tz_offset = - time.altzone / 3600
    if tz_offset < 0:
        tz_offset_str = "-%02d00" % abs(tz_offset)
    else:
        tz_offset_str = "+%02d00" % abs(tz_offset)
    start_time = datetime.datetime.fromtimestamp(start_time).strftime("%Y-%m-%dT%H:%M:%S") + tz_offset_str
    end_time = datetime.datetime.fromtimestamp(end_time).strftime("%Y-%m-%dT%H:%M:%S") + tz_offset_str
    print("Getting calendar events between: " + start_time + " and " + end_time)

    eventsResult = service.events().list(
        calendarId='primary', timeMin=start_time, timeMax=end_time, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')

    for event in events:
        start = event['start'].get('date')
        summary = event['summary']

        if 'Oncall' in event['summary']:
            print(start, summary)

if __name__ == '__main__':
    main()
