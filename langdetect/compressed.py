from langdetect import detect, detect_langs, lang_detect_exception
import os, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://mail.google.com/"]
our_email = 'PUTEMAILHERE@EMAIL.COM'


def gmail_authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle','rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle","wb") as token:
            pickle.dump(creds,token)
    return build('gmail','v1',credentials=creds)

service = gmail_authenticate()

def list_message(service):
    result = service.users().messages().list(userId='me').execute()
    messages = []
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me',pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

def spammessage(service, message):
    service.users().messages().modify(userId='me',id=message['id'],body={'addLabelIds':['SPAM'],'removeLabelIds':['INBOX']}).execute()
    service.users().messages().trash(userId='me',id=message['id'])

#def spamfilter(service,message,domain):
#    filter = {'criteria':{'from':f'*@{domain}'},'action':{'addLabelIds':['SPAM'],'removeLabelIds':['INBOX']}}
#    result = service.users().settings().filters().\
#        create(userId='me', body=filter).execute()
#    print('Created filter: %s' % result.get('id'))

def read_subject(service, message):
    msg = service.users().messages().get(userId='me',id=message['id'],format='full').execute()
    payload = msg['payload']
    headers = payload.get('headers')
    has_subject = False
    if headers:
        for header in headers:
            name = header.get('name')
            value = header.get('value')
            if name.lower() == 'subject':
                subject = value
                has_subject = True
    if not has_subject:
        pass
    return subject

def detectsubjectlanguage(service, message):
    subject = read_subject(service, message)
    test = detect_langs(subject)
    listoflangs = []
    for i in test:
        listoflangs.append(i.__dict__['lang'])
        if not i.__dict__['lang'] == 'en':
            pass
        elif i.__dict__['lang'] == 'en' and not i.__dict__['prob'] > 0.50:
            print(f'{"X"*10}THIS MESSAGE HAS A <50% CHANCE OF BEING ENGLISH, DELETING{"X"*10}')
            spammessage(service,message)
        elif i.__dict__['lang'] == 'en' and i.__dict__['prob'] >= 0.50:
            print(f'probability of english subject is equal to or greater than 50%, keeping')
            continue
    if not 'en' in listoflangs:
        spammessage(service,message)
        print(f'english not in potential languages, deleting')

for message in list_message(service):
    msg = service.users().messages().get(userId='me',id=message['id']).execute()
    print(f'{"="*10}message subject is {read_subject(service, msg)}{"="*10}')
    try:
        detectsubjectlanguage(service, msg)
    except lang_detect_exception.LangDetectException:
        continue
