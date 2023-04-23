from langdetect import detect, detect_langs, lang_detect_exception
import os, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://mail.google.com/"]
our_email = 'PUTEMAILHERE@EMAIL.COM'
#Replace with email being used

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
            #credentials.json is generated from the Google Cloud Console, and allows logging in to the API as a developer
            creds = flow.run_local_server(port=0)
        with open("token.pickle","wb") as token:
            pickle.dump(creds,token)
    return build('gmail','v1',credentials=creds)
    #This line creates an instance of the service; it is essentially logging into an email client

service = gmail_authenticate()

def list_message(service):
    result = service.users().messages().list(userId='me').execute()
    #'me' can be used in place of typing out the entire email address. This line retrieves a list of all messages in a user's inbox.
    messages = []
    if 'messages' in result:
        messages.extend(result['messages'])
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        #Results are paginated, so this line and the following lines check each page of results.
        result = service.users().messages().list(userId='me',pageToken=page_token).execute()
        if 'messages' in result:
            messages.extend(result['messages'])
    return messages

def spammessage(service, message):
    service.users().messages().modify(userId='me',id=message['id'],body={'addLabelIds':['SPAM'],'removeLabelIds':['INBOX']}).execute()
    service.users().messages().trash(userId='me',id=message['id'])
    #This function takes a message object and modifies it to remove the 'INBOX' label and add the 'SPAM' label, and then moves it to the trash.
    #I have it moving the emails to the trash in case my boss's wife decides to go back and look for specific emails that could have been incorrectly marked as spam.

#def spamfilter(service,message,domain):
#    filter = {'criteria':{'from':f'*@{domain}'},'action':{'addLabelIds':['SPAM'],'removeLabelIds':['INBOX']}}
#    result = service.users().settings().filters().\
#        create(userId='me', body=filter).execute()
#    print('Created filter: %s' % result.get('id'))
#I left this in in case I need to use it again; if the spam bombing happens again, I will likely start blocking entire domains instead of just reporting as spam.

def read_subject(service, message):
    msg = service.users().messages().get(userId='me',id=message['id'],format='full').execute()
    #This line retrieves a message by its id and assigns it to a variable.
    payload = msg['payload']
    headers = payload.get('headers')
    #These two lines retrieve the headers from the message, to pull info from.
    has_subject = False
    if headers:
        for header in headers:
            name = header.get('name')
            value = header.get('value')
            if name.lower() == 'subject':
                subject = value
                has_subject = True
    #These lines retrieve specifically the subject line of the message.
    if not has_subject:
        pass
    return subject
#This entire function serves one purpose: to process each message individually and return its subject line for processing.

def detectsubjectlanguage(service, message):
    subject = read_subject(service, message)
    test = detect_langs(subject)
    #I originally planned to just use the 'detect()' function of the langdetect library, but this allows for a better margin of error.
    #Instead of just returning whatever is the most likely language of the input, it returns an array of possibilities with their probabilities as well.
    #The downside to this function is that it returns a list of Language objects, instead of a dictionary.
    listoflangs = []
    for i in test:
        listoflangs.append(i.__dict__['lang'])
        #For each subject line, I had the function grab every possible language from the detection results and add it to a list. This way, if English was not in the list, I could mark this message as spam.
        if not i.__dict__['lang'] == 'en':
            pass
        #I only wanted to watch the probability that the message was English, so if the language wasn't English I ignored it.
        elif i.__dict__['lang'] == 'en' and not i.__dict__['prob'] > 0.50:
            print(f'{"X"*10}THIS MESSAGE HAS A <50% CHANCE OF BEING ENGLISH, DELETING{"X"*10}')
            #I personally really love console output for scripts like this. It allows me to see in real time how quickly the program is running,
            #and it allows me to make my own error messages as well so I know what I'm looking at if something goes wrong.
            spammessage(service,message)
        elif i.__dict__['lang'] == 'en' and i.__dict__['prob'] >= 0.50:
            print(f'probability of english subject is equal to or greater than 50%, keeping')
            continue
    if not 'en' in listoflangs:
        spammessage(service,message)
        print(f'english not in potential languages, deleting')

for message in list_message(service):
    msg = service.users().messages().get(userId='me',id=message['id']).execute()
    #This function is the main loop. It retrieves all messages in the user's inbox, reads their subject lines, determines whether
    #the subject line is likely in English, and processes it accordingly.
    print(f'{"="*10}message subject is {read_subject(service, msg)}{"="*10}')
    #This line combined with my previous print statements gave me the ability to see how accurate the langdetect library really was,
    #which informed me on how much I should tweak the margin of error.
    try:
        detectsubjectlanguage(service, msg)
    except lang_detect_exception.LangDetectException:
    #This, as far as I'm aware, is kind of a catch-all exception. I ran into this a few times with messages with no subject line,
    #messages with only spaces as the subject line, etc.
        continue