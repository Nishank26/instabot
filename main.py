import requests

response = requests.get('https://jsonbin.io/b/59d0f30408be13271f7df29c').json()

#APP_ACESS_TOKEN = '62291d9fc85c4b528be401e158122828'
APP_ACESS_TOKEN = '1283068475.b8ae6ad.891ec2bf276f4a11aa2c2f8475364900'
BASE_URL ='https://api.instagram.com/v1/'

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') %(APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        print 'request sucessfull'
        print user_info['data']['username']
    else:
        print 'Status code other than 200 received!'