from tkinter import Message
from langdetect import detect, detect_langs, lang_detect_exception
import os, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from base64 import urlsafe_b64decode, urlsafe_b64encode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

SCOPES = ["https://mail.google.com/"]
our_email = 'example@example.com'


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


def search_messages(service, query):
    result = service.users().messages().list(userId='me',q=query).execute()
    messages = []
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me',q=query,pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

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

def delete_messages(service, query):
    messages_to_delete = search_messages(service, query)
    return service.users().messages().batchDelete(userId='me',body={'ids':[msg['id'] for msg in messages_to_delete]}).execute()

def spammessage(service, message):
    service.users().messages().modify(userId='me',id=message['id'],body={'addLabelIds':['SPAM'],'removeLabelIds':['INBOX']}).execute()
    service.users().messages().trash(userId='me',id=message['id'])

def spamfilter(service,message,domain):
    filter = {'criteria':{'from':f'*@{domain}'},'action':{'addLabelIds':['SPAM'],'removeLabelIds':['INBOX']}}
    result = service.users().settings().filters().\
        create(userId='me', body=filter).execute()
    print('Created filter: %s' % result.get('id'))

def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def clean(text):
    return "".join(c if c.isalnum() else "_" for c in text)

def parse_parts(service, parts, folder_name, message):
    if parts:
        for part in parts:
            filename = part.get("filename")
            mimeType = part.get("mimeType")
            body = part.get("body")
            data = body.get("data")
            file_size = body.get("size")
            part_headers = part.get("headers")
            if part.get("parts"):
                parse_parts(service, part.get("parts"), folder_name, message)
            if mimeType == "text/plain":
                if data:
                    text = urlsafe_b64decode(data).decode()
                    print(text)
            elif mimeType == "text/html":
                if not filename:
                    filename = "index.html"
                filepath = os.path.join(folder_name, filename)
                print("Saving HTML to", filepath)
                with open(filepath, "wb") as f:
                    f.write(urlsafe_b64decode(data))
            else:
                for part_header in part_headers:
                    part_header_name = part_header.get("name")
                    part_header_value = part_header.get("value")
                    if part_header_name == "Content-Disposition":
                        if "attachment" in part_header_value:
                            print("Saving the file:", filename, "size:", get_size_format(file_size))
                            attachment_id = body.get("attachmentId")
                            attachment = service.users().messages() \
                                        .attachments().get(id=attachment_id, userId='me', messageId=message['id']).execute()
                            data = attachment.get("data")
                            filepath = os.path.join(folder_name, filename)
                            if data:
                                with open(filepath, "wb") as f:
                                    f.write(urlsafe_b64decode(data))

def read_message(service, message):
    msg = service.users().messages().get(userId='me',id=message['id'],format='full').execute()
    payload = msg['payload']
    headers = payload.get('headers')
    parts = payload.get('parts')
    folder_name = 'email'
    has_subject = False
    if headers:
        for header in headers:
            name = header.get('name')
            value = header.get('value')
            if name.lower() == 'from':
                print("From:", value)
            if name.lower() == 'to':
                print("To:", value)
            if name.lower() == 'subject':
                has_subject = True
                folder_name = value
                folder_counter = 0
                while os.path.isdir(folder_name):
                    folder_counter += 1
                    if folder_name[-1].isdigit() and folder_name[-2] == "_":
                        folder_name = f"{folder_name[:-2]}_{folder_counter}"
                    elif folder_name[-2:].isdigit() and folder_name[-3] == "_":
                        folder_name = f"{folder_name[:-3]}_{folder_counter}"
                    else:
                        folder_name = f"{folder_name}_{folder_counter}"
                os.mkdir(folder_name)
                print("Subject:", value)
            if name.lower() == 'date':
                print("Date:", value)
    if not has_subject:
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
    parse_parts(service, parts, folder_name, message)
    print("="*50)

def read_subject(service, message):
    msg = service.users().messages().get(userId='me',id=message['id'],format='full').execute()
    payload = msg['payload']
    headers = payload.get('headers')
    has_subject = False
    if headers:
        for header in headers:
            name = header.get('name')
            value = header.get('value')
            #if name.lower() == 'from':
                #print("From:", value)
            #if name.lower() == 'to':
                #print("To:", value)
            if name.lower() == 'subject':
                subject = value
                if not subject.strip() == '':
                    has_subject = True
                #print("Subject:", value)
            #if name.lower() == 'date':
                #print("Date:", value)
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
    #print(f'message object is {msg}')
    print(f'{"="*10}message subject is {read_subject(service, msg)}{"="*10}')
    #answer = input(f'message subject is {read_subject(service, msg)}, is this spam?> ')
    #if answer == 'y':
    #    spammessage(service,msg)
    #elif answer == 'n':
    #    pass
    try:
        detectsubjectlanguage(service, msg)
    except lang_detect_exception.LangDetectException:
        continue
