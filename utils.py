#!/usr/bin/env python
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        import json
    except ImportError:
        import simplejson as json
    try:
        api = KavenegarAPI('6134444E6B4E737163327A6C56616C6E6A624535417A436E66686D67616D6E32624549755A3433367146453D')
        params = {
            'sender': '10004346',
            'receptor': phone_number,
            'message': f'{code}  is your code in bliss'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
