import jwt
import datetime
from django.conf import settings

class JwtController:
    
    def __init__(self, token_type, token=None):
        self._secret_key = settings.PYJWT_SECRET_KEY
        self._token = token

        self._token_type_list = ['access', 'refresh', 'webSocket']

        if token_type in self._token_type_list:
            self._token_type = token_type

        else:
            #참고: 프로그래밍 단계에서 에러 처리
            raise Exception('Please make token_type correct')

    def createPayload(self, user_info):
        if self._token_type == "access":
            user_info['iat'] = datetime.datetime.utcnow()
            user_info['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=180)


        return user_info

    def createJwtToken(self, payload):
        encoded_jwt = jwt.encode(payload, self._secret_key, algorithm='HS256')
        self._token = encoded_jwt

        return encoded_jwt

    def verifyJwtToken(self):
        try:
            decoded_jwt = jwt.decode(self._token, self._secret_key, algorithms='HS256')
        except jwt.InvalidSignatureError:
            return False, {'info': 'signiture_err'}
        except jwt.ExpiredSignatureError:
            return False, {'info': 'expired'}
        except Exception as e:
            return False, {'info': str(e)}

        return True, decoded_jwt


def createJwtTokenWithInfo(user_info:dict, token_type:str='access'):
    """
        JWT token 생성
        user_info = {
            "name": "..."
            "email": "..."
            ...
        }

        return => token str
    """
    jwtController = JwtController(token_type)
    payload = jwtController.createPayload(user_info)
    access_token = jwtController.createJwtToken(payload)
    print('create jwtToken success')
    return access_token

def verifyJwtToken(token_type:str, token:str):
    """
        JWT 체크
        token_type => access
        token => jwt String

        return => True, False 및 토큰 내용 or 에러코드 반환
    """
    jwtController = JwtController(token_type, token)
    
    return jwtController.verifyJwtToken()
