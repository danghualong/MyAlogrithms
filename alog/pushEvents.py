import json
import requests

class EventPusher(object):
    ACCESS_TOKEN_URL_FORMAT='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'
    USER_LIST_URL_FORMAT='https://api.weixin.qq.com/cgi-bin/user/get?access_token={0}&next_openid='
    PUSH_DATA_URL_FORMAT = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}'

    def __init__(self,config):
        self.app_id=config['appid']
        self.app_secret=config['appsecret']
        self.template_id=config['templateid']
    
    def getAccessToken(self):
        url=EventPusher.ACCESS_TOKEN_URL_FORMAT.format(self.app_id,self.app_secret)
        r=requests.get(url)
        data=json.loads(r.text)
        return data['access_token']
    def getUserList(self):
        token=self.getAccessToken()
        url=EventPusher.USER_LIST_URL_FORMAT.format(token)
        r=requests.get(url)
        jsonData=json.loads(r.text)
        return jsonData['data']['openid']

    def getWords(self):
        url = 'http://open.iciba.com/dsapi/'
        r = requests.get(url)
        return json.loads(r.text)

    def pushSingle(self,openId,words):
        msg={
            'touser': openId,
            'template_id': self.template_id,
            'url': words['fenxiang_img'],
            'data': {
                'content': {
                    'value': words['content'],
                    'color': '#0000CD'
                    },
                'note': {
                    'value': words['note'],
                    },
                'translation': {
                    'value': words['translation'],
                    }
            }
        }
        jsonMsg=json.dumps(msg)
        token=self.getAccessToken()
        url=EventPusher.PUSH_DATA_URL_FORMAT.format(token)
        r=requests.post(url,jsonMsg)
        return json.loads(r.text)

 
    
    def push(self):
        openIds=self.getUserList()
        words=self.getWords()
        for openId in openIds:
            print(openId)
            result=self.pushSingle(openId,words)
            if(result['errcode']==0):
                print('send to {0} OK'.format(openId))
            else:
                print('send to {0} failed'.format(openId))



config={
    'appid':'wx420e91a2ea122fde',
    'appsecret':'9b7ea5e3c19e74568b5a7d65fa949916',
    'templateid':'_EMKDGTd8bsYe0LcmcBUW2IGEQz5McktYTNXJs8OStM'
}
pusher=EventPusher(config)
pusher.push()