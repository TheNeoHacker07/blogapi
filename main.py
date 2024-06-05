import time
from jwt_handler import encode_jwt,decode_jwt,refreshJWT


user={'email':'adfsd','username':'hello','id':1}

#получаем токены
jwt_token=encode_jwt(user) 
print(jwt_token)
time.sleep(6)


#прилетает декодированный токен,если время не истекло,если время жизни токена истекло прилетает пустой dict
decoded=decode_jwt(jwt_token['access'])
print(decoded)
new_jwt_token=refreshJWT(jwt_token['refesh'])

print(new_jwt_token)






