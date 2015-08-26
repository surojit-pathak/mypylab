#! /usr/bin/python

import httplib2
import pprint
import mimetypes
import os
import sys

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

# Copy your credentials from the console
CLIENT_ID = '1071542987209-poklfnk3m3aruhvm67uni3afnbrkpplr.apps.googleusercontent.com'
CLIENT_SECRET = '92XpzOa7WIlP93IEjw4k9wdk'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                           redirect_uri=REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)
# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

def put_file (FILENAME, title, parent_id, desc='A test document'):
    # Insert a file
    extn = FILENAME.split('.')[-1]
    try:
       mimetype = mimetypes.types_map['.' + extn ]
    except KeyError:
       mimetype = 'text/plain'

    media_body = MediaFileUpload(FILENAME, mimetype=mimetype, resumable=True)
    body = {
	    'title': title,
	    'description': desc,
            'parents': [{'id': parent_id}],
            'mimeType': mimetype
            # 'mimeType': 'text/plain'
    }

    file = drive_service.files().insert(body=body, media_body=media_body).execute()
    # pprint.pprint(file)
    # print FILENAME, title, parent_id

def create_folder (title, parent_id, desc='A test folder'):
    # Insert a folder
    # print title, parent_id
    if parent_id == None:
        body = {
	    'title': title,
	    'description': desc,
	    'mimeType': 'application/vnd.google-apps.folder'
        }
    else: 
        body = {
	    'title': title,
	    'description': desc,
            'parents': [{'id': parent_id}],
	    'mimeType': 'application/vnd.google-apps.folder'
        }
   

    dir = drive_service.files().insert(body=body).execute()
    return dir['id']
    # import uuid; return str(uuid.uuid4().get_hex().upper()[0:6])


def list_files(path, parent_id):
    # print ("List for path - %s" %path)
    tdir = path.split('/')[-1]
    present = create_folder(title=tdir, parent_id=parent_id)

    dirnames = []
    for (dirpath, dirnames, filenames) in os.walk(path):
         if filenames != None:
             for file in [f for f in filenames if not f.startswith('.')]:
                 # print dirpath + '/' + file
                 put_file(dirpath + '/' + file, file, present)
         break

    if len(dirnames) != 0:
        for dir in [d for d in dirnames if not d.startswith('.')]:
            list_files(path + '/' + dir, parent_id=present)
        

if __name__ == "__main__":
    print "Enter the name of the folder to be uploaded"
    path = raw_input()
    path = path.rstrip('/')
    print "Enter the file-Id of the parent folder"
    parent_id=raw_input()
    if parent_id == '':
        parent_id = None
    list_files(path, parent_id=parent_id)
    
   
