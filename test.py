from pywebpush import *
from json import loads
import datetime

sub_chrome = loads('{"endpoint":"https://fcm.googleapis.com/fcm/send/eH-pJvXfxOc:APA91bFrLxpa1E6469qhzWeCu9DEFH6fqJtWN-E-XlRp2xLuiVh-lJR1UUpMr2-8Hy4ZTQTS7SxG5jRjmoXpb6GiuZ8Q886QBSpzI-iq9JxH4GiwLV4q6jCg6AnejfgdNWvMpUOUU_yd","keys":{"p256dh":"BIyg3m1R8_W5TyhIKx3xkEnkOObddsqT2nm4-5x1vHTBUJuitzLjGQiqj2TsYt1WnxNDkLdJVZPHs7L_cHULMWM=","auth":"UNoYfekz9FT-mYt88Aa4jw=="}}')
sub_firefox = loads('{"endpoint":"https://updates.push.services.mozilla.com/wpush/v2/gAAAAABZc8XbTCziigH1hSr2gb_cJSvpi6jOByrsMy_g7glNNYq_8avE7yiz83c969H9POsjO3ClzAtEdUbwUX2dQ1gDEF8Zb6-r5-enl0yh9aa1fjIDRQWo0PvscDCbmfNOT421E2pGoskVrulP9gsUaJDC8rXMDZaV_QiRv9UA1C83tScfVmg","keys":{"auth":"GK-hUtxkxsH3Cd_pNqU4Bw","p256dh":"BFRQEoe5XltMmeG_OtBi8AKpNi1XdAb6cnCOV3bCyK3Q7pXz8lqaDJPkmQoFAn-6JiL4ukw8Ug-h8NLw552P_m0"}}')

vapid_claims = loads('{"sub":"mailto:shao.zhongren@gmail.com","aud":"https://fcm.googleapis.com","exp":"ExpirationTimestamp"}')
now = datetime.datetime.utcnow()
vapid_claims['exp'] = (now - datetime.datetime(1970, 1, 1)).total_seconds() + 1000

res = webpush(sub_chrome, "this is from wsl", vapid_private_key="/home/shaoz/private_key.pem", vapid_claims=vapid_claims)
print(res)

