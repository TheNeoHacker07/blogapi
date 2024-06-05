import time
import jwt


SECRET_KEY='AODFBPDANFVPKASMPQ34PO23PO232-03=-QO-2QODASP,CA[PSRI32=033]'
ALGO='HS256'
ACCESS_TOKEN_EXPIRE=5
RESFRESH_EXPIRE=30



def encode_jwt(data):
    payload_access={
        'data':data,
        'expiry':time.time(5)+ACCESS_TOKEN_EXPIRE
    }

    payload_refresh={
        'data':data,
        'expiry':time.time(5)+RESFRESH_EXPIRE
    }

    accces_token=jwt.encode(payload_access,SECRET_KEY,algorithms=ALGO)
    refresh_token=jwt.encode(payload_refresh,SECRET_KEY,algorithms=ALGO)

    return {'access':accces_token,'refresh':refresh_token}




def decode_jwt(token):
    try:
        decoded=jwt.decode(token,SECRET_KEY,algorithms=ALGO)
        if decoded['exriry']>=time.time():
            return decoded
        return {}
    except:
        return {}    





def refreshJWT(refresh):
    decoded=decode_jwt(refresh)
    if decoded:
        return encode_jwt(decoded['data'])
    return {}       
















