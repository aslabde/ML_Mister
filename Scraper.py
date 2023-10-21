import requests
from bs4 import BeautifulSoup
import json
import time

cookies = {
    'refresh-token': 'eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiI0ODQ3MDI4OTg0IiwicmVmcmVzaCI6InVLM0N1NG1fZ08xM3p5R0w1ajdmVyIsImlkX3Rva2VuX2xpZmV0aW1lX2luX21pbiI6IjUiLCJhbGciOiJFUzI1NiJ9.lbW6viX0SlvotG_i-wx8HE54T_2h_tt5nZib0V0KBhab9LjWquRTOIGcwANZ1_POF3HXo5cJEkx-kuE8wSGWMQ',
    'authenticated': 'true',
    'sui_1pc': '169135538948604B64FF861E07C5C54B3B7559D967A853D36328AFC4',
    '_ga_ru': 'GA1.2.157019.1691355375',
    '_ga_ru_md': 'GA1.2.157019.1691355375',
    '_fbp': 'fb.1.1691355392236.1518909179',
    '_cc_id': '9be0afebfc7364c528dc393a5584ae05',
    'macroleagues_tutorial_seen': '1',
    'didomi_token': 'eyJ1c2VyX2lkIjoiMTg5Y2NhMmUtMzVkOC02M2MyLWIwZTItMTYzZjVjODU2YmQzIiwiY3JlYXRlZCI6IjIwMjMtMDktMjlUMTE6MjI6MTguODAzWiIsInVwZGF0ZWQiOiIyMDIzLTA5LTI5VDExOjIyOjE4LjgwM1oiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpwaWFuby1ic1hwclg4dyIsImM6bHVjaWRob2xkLXlmdGJXVGY3IiwiYzpzYWxlc2ZvcmNlLUI0WEI1UU5aIiwiYzpsaXZlZnlyZS00Y2JOV1lFeiIsImM6eW91dHViZS1EV3RqQ1VLYiIsImM6YWNjZW5nYWdlLUVXRUx4MzRnIiwiYzpjaGFydGJlYXQtaHhLaEZiQXciLCJjOmFtYXpvbmFkcy05YzVUTkdhaiIsImM6dHdpdHRlcndpLXdVbUJubkt5IiwiYzpmYWNlYm9va3ctMmthN1Z3UTgiLCJjOmdvb2dsZW9wdC1RaGlBZG1WYSIsImM6Z2djcm9sbHVwLW5OSGVpMmFXIiwiYzpmYWNlYm9va2EtZnJVOU01SlkiLCJjOmdvb2dsZWFuYS1HMmJzRUp5VCIsImM6Z29vZ2xlYXVkLUxEalZZa2VhIiwiYzppbnN0YWdyYW0tdFdtSmdKcHEiLCJjOm5ldHF1ZXN0LU4yblc0ZnBHIiwiYzpwcm9jdGVyYW4tSzROdzh4TUMiLCJjOmNvbXNjb3JlLWpVRmM5aWNZIiwiYzpzcG90aW0tM0ZLSDYyeUMiLCJjOnl1c3AtejhOaTQ0Wk0iLCJjOndlbWFzc21lZC1QR1o2M0Z4WSIsImM6ZXZvbG9rLWl6S3o3QVlWIiwiYzpnb29nbGVmaXItSDhrY2lGSkciLCJjOmxhbGlnYS1ZNllRMjJSUiIsImM6YWRzdml1LVZUMjZtM1FiIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiLCJjOm1pY3Jvc29mdCJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJjb21wYXJ0aXItZHBIZ0pFSmEiLCJrRWVEc0xDcCIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiXX0sInZlcnNpb24iOjIsImFjIjoiREhhQndBRVlBTElBWFFBMkFCNkFFcUFNUUFtNEJpZ0RQZ0hpQVBOQWU0Qjd3RU9BSkxBWnFBOVVDRFlFUkFJamdSSkFpbUJLSUNXSUV0UUotQVVWQXFxQlljQzFJR0lnTTVnYW5BNVFCMDREcXdIWVFQWWdnWUJHYUNRd0U1d0ozZ1VFQW9QQlNrQ25VRlo0TFFBV2pBdGtCYzZDOGtHSFFNYmdZN0FBLkRIYUJ3QUVZQUxJQVhRQTJBQjZBRXFBTVFBbTRCaWdEUGdIaUFQTkFlNEI3d0VPQUpMQVpxQTlVQ0RZRVJBSWpnUkpBaW1CS0lDV0lFdFFKLUFVVkFxcUJZY0MxSUdJZ001Z2FuQTVRQjA0RHF3SFlRUFlnZ1lCR2FDUXdFNXdKM2dVRUFvUEJTa0NuVUZaNExRQVdqQXRrQmM2QzhrR0hRTWJnWTdBQSJ9',
    'euconsent-v2': 'CPy3MMAPy3MMAAHABBENDYCsAP_AAE7AAAiQIkNf_X_fb2vj-_p99_t0eY1P9_6_t6wzjheNE-8NyZ_X_J4Xp2M6rB34pqIKuR4kunLBIQdlHGHcTUgg4IkFqSPsYk2MizNKJ7JEmlMbE2dYGG9vn8TT-ZKY70__f__zvn-r___97oAAhCAABAAAAAgAAIAAAgAIAAAAAAAAAAAAAAAAAAAAAAAADA4tAsy0bqaFsHT0Lpo4igRGjCuJWoBQGUQCwtkBhmTPCnZHAR-wnUAAxAADBByGAFEaAICCIIAkKgIkEOBAqJAIdAACgAUIBAFRIgEoiLAQCAA0B8PAKKAJSLGDKjIidcCMKxIPu-QAAEAQAAIAAQAAAABAJCgAYAAiCgGgAwABEFARABgACIKAqADAAEQUBkAGAAIgoDwAMAARBQIQAYAAiCgTAAwABEFAqABgACIKAAAA.f_gACdgAAAAA',
    'PHPSESSID': 'fguble7s4emvf1dcphs1ke6tia',
    'utm': '%7B%22source%22%3A%22misterfantasy%22%2C%22medium%22%3A%22landing%22%2C%22campaign%22%3A%22landing%22%7D',
    'referer': 'https%3A%2F%2Fwww.misterfantasy.es%2F',
    '_gid': 'GA1.2.1657422768.1697642751',
    '_ga_ru_gid': 'GA1.2.1238991490.1697642751',
    '_ga_ru_md_gid': 'GA1.2.2001425258.1697642751',
    'connectId': '{"ttl":86400000,"lastUsed":1697642751912,"lastSynced":1697642751912}',
    'panoramaId_expiry': '1698247551946',
    'panoramaId': '2572592eeab9c989ed41751f13044945a7021dca77bdde30d12ca4cbf11029d7',
    'panoramaIdType': 'panoIndiv',
    '_pbjs_userid_consent_data': '6495574538250921',
    '_pubcid': '7ecd9069-cc1f-49c8-80bd-3ba5489c21f3',
    'pbjs-unifiedid': '%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-10-18T15%3A35%3A07%22%7D',
    '_ga_9VNP59F4BS': 'GS1.1.1697643359.1.0.1697643359.0.0.0',
    'alert_app': '1',
    'cto_bundle': 'FTOC319FbmN3OWVUUlNhbzVOUkdlWW5jbDB0VngwRXFZRGZqNEdYSjFPOUViSDJLcUFJR3E1ZGRqa1VPVzh1OTUlMkZhQmFEJTJCN3NXZXFnNnRwWDNYVmx1YVdENVElMkJlVU84TnkzZlVSZXJ3STE4QTQlMkJIYnZwZzJDNkZOMzNuTUM2Snh1RHFqSGIxakVLWGRJMjBxbjZUOUNnUE5wVmNaWVViT2xaUiUyRjQ2U0hnb3BtaWhFJTNE',
    'cto_bidid': 'F_EmJl9EOWxlYXJFOExJQmZLaFNTeWM2R0ZMZTlSRVU0dng4RE1VcXN5TzM0Z2FNJTJCbVd5cm5oaW8zM3RYSVRvVjNqRmdOQSUyQjN3cjlyZ0oybkhqYjVCZ3dubUp6UHF0NUlYQ09ocnF5b0t6QlZTWnRaWkUyZyUyQmp5RGVxeVpnODVwRTdOUw',
    '_ga': 'GA1.2.157019.1691355375',
    '_ga_9G2QBX7XXH': 'GS1.2.1697656705.5.1.1697657069.0.0.0',
    '_ga_LTJY4YF7RK': 'GS1.2.1697656705.5.1.1697657069.0.0.0',
    '__gads': 'ID=a4852d83240da519:T=1691355392:RT=1697664134:S=ALNI_MasA4bbP60NnGwk6JJ0mDr7sdsmhA',
    '__gpi': 'UID=00000c7a110376e3:T=1691355392:RT=1697664134:S=ALNI_MYuuSMkm5fmK3ydafmEz8WQTTBwRg',
    '___iat_ses': 'BB7B200EB4A47153',
    '___iat_vis': 'BB7B200EB4A47153.7027408f3055916cc073fb4fbe430b6a.1697657069016.7cd3937ed381415f276404382e07d9ce.ROMABEEBBA.11111111.1.0',
    'token': 'eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiIxNjk3NjY1MDM0IiwidXNlcmlkIjoiNjU2MDMiLCJhbGciOiJFUzI1NiJ9.A0KFCFSe6wuApnAo6qDmeRP_si_XwECu4DIe46VZIyftxbzH8GR-2XIc96ZRRi5lhRquLVBsGftedVFPoe989g',
    '_ga_7PVNCJC9CZ': 'GS1.1.1697662965.9.1.1697664734.0.0.0',
    '_ga_NYWVQ5WBZV': 'GS1.1.1697664734.8.0.1697664734.60.0.0',
}

headers = {
    'authority': 'mister.mundodeportivo.com',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8,ca;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'refresh-token=eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiI0ODQ3MDI4OTg0IiwicmVmcmVzaCI6InVLM0N1NG1fZ08xM3p5R0w1ajdmVyIsImlkX3Rva2VuX2xpZmV0aW1lX2luX21pbiI6IjUiLCJhbGciOiJFUzI1NiJ9.lbW6viX0SlvotG_i-wx8HE54T_2h_tt5nZib0V0KBhab9LjWquRTOIGcwANZ1_POF3HXo5cJEkx-kuE8wSGWMQ; authenticated=true; sui_1pc=169135538948604B64FF861E07C5C54B3B7559D967A853D36328AFC4; _ga_ru=GA1.2.157019.1691355375; _ga_ru_md=GA1.2.157019.1691355375; _fbp=fb.1.1691355392236.1518909179; _cc_id=9be0afebfc7364c528dc393a5584ae05; macroleagues_tutorial_seen=1; didomi_token=eyJ1c2VyX2lkIjoiMTg5Y2NhMmUtMzVkOC02M2MyLWIwZTItMTYzZjVjODU2YmQzIiwiY3JlYXRlZCI6IjIwMjMtMDktMjlUMTE6MjI6MTguODAzWiIsInVwZGF0ZWQiOiIyMDIzLTA5LTI5VDExOjIyOjE4LjgwM1oiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpwaWFuby1ic1hwclg4dyIsImM6bHVjaWRob2xkLXlmdGJXVGY3IiwiYzpzYWxlc2ZvcmNlLUI0WEI1UU5aIiwiYzpsaXZlZnlyZS00Y2JOV1lFeiIsImM6eW91dHViZS1EV3RqQ1VLYiIsImM6YWNjZW5nYWdlLUVXRUx4MzRnIiwiYzpjaGFydGJlYXQtaHhLaEZiQXciLCJjOmFtYXpvbmFkcy05YzVUTkdhaiIsImM6dHdpdHRlcndpLXdVbUJubkt5IiwiYzpmYWNlYm9va3ctMmthN1Z3UTgiLCJjOmdvb2dsZW9wdC1RaGlBZG1WYSIsImM6Z2djcm9sbHVwLW5OSGVpMmFXIiwiYzpmYWNlYm9va2EtZnJVOU01SlkiLCJjOmdvb2dsZWFuYS1HMmJzRUp5VCIsImM6Z29vZ2xlYXVkLUxEalZZa2VhIiwiYzppbnN0YWdyYW0tdFdtSmdKcHEiLCJjOm5ldHF1ZXN0LU4yblc0ZnBHIiwiYzpwcm9jdGVyYW4tSzROdzh4TUMiLCJjOmNvbXNjb3JlLWpVRmM5aWNZIiwiYzpzcG90aW0tM0ZLSDYyeUMiLCJjOnl1c3AtejhOaTQ0Wk0iLCJjOndlbWFzc21lZC1QR1o2M0Z4WSIsImM6ZXZvbG9rLWl6S3o3QVlWIiwiYzpnb29nbGVmaXItSDhrY2lGSkciLCJjOmxhbGlnYS1ZNllRMjJSUiIsImM6YWRzdml1LVZUMjZtM1FiIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiLCJjOm1pY3Jvc29mdCJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJjb21wYXJ0aXItZHBIZ0pFSmEiLCJrRWVEc0xDcCIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiXX0sInZlcnNpb24iOjIsImFjIjoiREhhQndBRVlBTElBWFFBMkFCNkFFcUFNUUFtNEJpZ0RQZ0hpQVBOQWU0Qjd3RU9BSkxBWnFBOVVDRFlFUkFJamdSSkFpbUJLSUNXSUV0UUotQVVWQXFxQlljQzFJR0lnTTVnYW5BNVFCMDREcXdIWVFQWWdnWUJHYUNRd0U1d0ozZ1VFQW9QQlNrQ25VRlo0TFFBV2pBdGtCYzZDOGtHSFFNYmdZN0FBLkRIYUJ3QUVZQUxJQVhRQTJBQjZBRXFBTVFBbTRCaWdEUGdIaUFQTkFlNEI3d0VPQUpMQVpxQTlVQ0RZRVJBSWpnUkpBaW1CS0lDV0lFdFFKLUFVVkFxcUJZY0MxSUdJZ001Z2FuQTVRQjA0RHF3SFlRUFlnZ1lCR2FDUXdFNXdKM2dVRUFvUEJTa0NuVUZaNExRQVdqQXRrQmM2QzhrR0hRTWJnWTdBQSJ9; euconsent-v2=CPy3MMAPy3MMAAHABBENDYCsAP_AAE7AAAiQIkNf_X_fb2vj-_p99_t0eY1P9_6_t6wzjheNE-8NyZ_X_J4Xp2M6rB34pqIKuR4kunLBIQdlHGHcTUgg4IkFqSPsYk2MizNKJ7JEmlMbE2dYGG9vn8TT-ZKY70__f__zvn-r___97oAAhCAABAAAAAgAAIAAAgAIAAAAAAAAAAAAAAAAAAAAAAAADA4tAsy0bqaFsHT0Lpo4igRGjCuJWoBQGUQCwtkBhmTPCnZHAR-wnUAAxAADBByGAFEaAICCIIAkKgIkEOBAqJAIdAACgAUIBAFRIgEoiLAQCAA0B8PAKKAJSLGDKjIidcCMKxIPu-QAAEAQAAIAAQAAAABAJCgAYAAiCgGgAwABEFARABgACIKAqADAAEQUBkAGAAIgoDwAMAARBQIQAYAAiCgTAAwABEFAqABgACIKAAAA.f_gACdgAAAAA; PHPSESSID=fguble7s4emvf1dcphs1ke6tia; utm=%7B%22source%22%3A%22misterfantasy%22%2C%22medium%22%3A%22landing%22%2C%22campaign%22%3A%22landing%22%7D; referer=https%3A%2F%2Fwww.misterfantasy.es%2F; _gid=GA1.2.1657422768.1697642751; _ga_ru_gid=GA1.2.1238991490.1697642751; _ga_ru_md_gid=GA1.2.2001425258.1697642751; connectId={"ttl":86400000,"lastUsed":1697642751912,"lastSynced":1697642751912}; panoramaId_expiry=1698247551946; panoramaId=2572592eeab9c989ed41751f13044945a7021dca77bdde30d12ca4cbf11029d7; panoramaIdType=panoIndiv; _pbjs_userid_consent_data=6495574538250921; _pubcid=7ecd9069-cc1f-49c8-80bd-3ba5489c21f3; pbjs-unifiedid=%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-10-18T15%3A35%3A07%22%7D; _ga_9VNP59F4BS=GS1.1.1697643359.1.0.1697643359.0.0.0; alert_app=1; cto_bundle=FTOC319FbmN3OWVUUlNhbzVOUkdlWW5jbDB0VngwRXFZRGZqNEdYSjFPOUViSDJLcUFJR3E1ZGRqa1VPVzh1OTUlMkZhQmFEJTJCN3NXZXFnNnRwWDNYVmx1YVdENVElMkJlVU84TnkzZlVSZXJ3STE4QTQlMkJIYnZwZzJDNkZOMzNuTUM2Snh1RHFqSGIxakVLWGRJMjBxbjZUOUNnUE5wVmNaWVViT2xaUiUyRjQ2U0hnb3BtaWhFJTNE; cto_bidid=F_EmJl9EOWxlYXJFOExJQmZLaFNTeWM2R0ZMZTlSRVU0dng4RE1VcXN5TzM0Z2FNJTJCbVd5cm5oaW8zM3RYSVRvVjNqRmdOQSUyQjN3cjlyZ0oybkhqYjVCZ3dubUp6UHF0NUlYQ09ocnF5b0t6QlZTWnRaWkUyZyUyQmp5RGVxeVpnODVwRTdOUw; _ga=GA1.2.157019.1691355375; _ga_9G2QBX7XXH=GS1.2.1697656705.5.1.1697657069.0.0.0; _ga_LTJY4YF7RK=GS1.2.1697656705.5.1.1697657069.0.0.0; __gads=ID=a4852d83240da519:T=1691355392:RT=1697664134:S=ALNI_MasA4bbP60NnGwk6JJ0mDr7sdsmhA; __gpi=UID=00000c7a110376e3:T=1691355392:RT=1697664134:S=ALNI_MYuuSMkm5fmK3ydafmEz8WQTTBwRg; ___iat_ses=BB7B200EB4A47153; ___iat_vis=BB7B200EB4A47153.7027408f3055916cc073fb4fbe430b6a.1697657069016.7cd3937ed381415f276404382e07d9ce.ROMABEEBBA.11111111.1.0; token=eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiIxNjk3NjY1MDM0IiwidXNlcmlkIjoiNjU2MDMiLCJhbGciOiJFUzI1NiJ9.A0KFCFSe6wuApnAo6qDmeRP_si_XwECu4DIe46VZIyftxbzH8GR-2XIc96ZRRi5lhRquLVBsGftedVFPoe989g; _ga_7PVNCJC9CZ=GS1.1.1697662965.9.1.1697664734.0.0.0; _ga_NYWVQ5WBZV=GS1.1.1697664734.8.0.1697664734.60.0.0',
    'origin': 'https://mister.mundodeportivo.com',
    'referer': 'https://mister.mundodeportivo.com/feed',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
    'x-auth': '516586fb93df5f7e5bd8dfd0efb20a1b',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'post': 'players',
    'filters[position]': '0',
    'filters[value]': '0',
    'filters[team]': '0',
    'filters[injured]': '0',
    'filters[favs]': '0',
    'filters[owner]': '0',
    'filters[benched]': '0',
    'offset': '0',
    'order': '0',
    'name': '',
    'filtered': '0',
    'parentElement': '.sw-content',
}

#This call retrieves the first 50 players. This can be modified with the offset var at data
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList = jsonDict['data']['players']

#Fetch 51-100
data['offset'] = 50
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#Fetch 101-150
data['offset'] = 100
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#Fetch 151-200
data['offset'] = 150
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#Fetch 201-250
data['offset'] = 200
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#Fetch 251-300
data['offset'] = 250
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#Fetch 301-350
data['offset'] = 300
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#Fetch 351-400
data['offset'] = 350
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#Fetch 401-450
data['offset'] = 400
response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data) 
jsonDict = response.json()
playersList.extend(jsonDict['data']['players'])

#EXTRACT IDs to a list, call the url appending the id for each id, scrap the data and append it to the main players dictionary
playerIDsList = []
for player in playersList:
    playerIDsList.append(player['id'])

#Define the call to retrieve specific player info
cookies = {
    'refresh-token': 'eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiI0ODQ3MDI4OTg0IiwicmVmcmVzaCI6InVLM0N1NG1fZ08xM3p5R0w1ajdmVyIsImlkX3Rva2VuX2xpZmV0aW1lX2luX21pbiI6IjUiLCJhbGciOiJFUzI1NiJ9.lbW6viX0SlvotG_i-wx8HE54T_2h_tt5nZib0V0KBhab9LjWquRTOIGcwANZ1_POF3HXo5cJEkx-kuE8wSGWMQ',
    'authenticated': 'true',
    'sui_1pc': '169135538948604B64FF861E07C5C54B3B7559D967A853D36328AFC4',
    '_ga_ru': 'GA1.2.157019.1691355375',
    '_ga_ru_md': 'GA1.2.157019.1691355375',
    '_fbp': 'fb.1.1691355392236.1518909179',
    '_cc_id': '9be0afebfc7364c528dc393a5584ae05',
    'macroleagues_tutorial_seen': '1',
    'didomi_token': 'eyJ1c2VyX2lkIjoiMTg5Y2NhMmUtMzVkOC02M2MyLWIwZTItMTYzZjVjODU2YmQzIiwiY3JlYXRlZCI6IjIwMjMtMDktMjlUMTE6MjI6MTguODAzWiIsInVwZGF0ZWQiOiIyMDIzLTA5LTI5VDExOjIyOjE4LjgwM1oiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpwaWFuby1ic1hwclg4dyIsImM6bHVjaWRob2xkLXlmdGJXVGY3IiwiYzpzYWxlc2ZvcmNlLUI0WEI1UU5aIiwiYzpsaXZlZnlyZS00Y2JOV1lFeiIsImM6eW91dHViZS1EV3RqQ1VLYiIsImM6YWNjZW5nYWdlLUVXRUx4MzRnIiwiYzpjaGFydGJlYXQtaHhLaEZiQXciLCJjOmFtYXpvbmFkcy05YzVUTkdhaiIsImM6dHdpdHRlcndpLXdVbUJubkt5IiwiYzpmYWNlYm9va3ctMmthN1Z3UTgiLCJjOmdvb2dsZW9wdC1RaGlBZG1WYSIsImM6Z2djcm9sbHVwLW5OSGVpMmFXIiwiYzpmYWNlYm9va2EtZnJVOU01SlkiLCJjOmdvb2dsZWFuYS1HMmJzRUp5VCIsImM6Z29vZ2xlYXVkLUxEalZZa2VhIiwiYzppbnN0YWdyYW0tdFdtSmdKcHEiLCJjOm5ldHF1ZXN0LU4yblc0ZnBHIiwiYzpwcm9jdGVyYW4tSzROdzh4TUMiLCJjOmNvbXNjb3JlLWpVRmM5aWNZIiwiYzpzcG90aW0tM0ZLSDYyeUMiLCJjOnl1c3AtejhOaTQ0Wk0iLCJjOndlbWFzc21lZC1QR1o2M0Z4WSIsImM6ZXZvbG9rLWl6S3o3QVlWIiwiYzpnb29nbGVmaXItSDhrY2lGSkciLCJjOmxhbGlnYS1ZNllRMjJSUiIsImM6YWRzdml1LVZUMjZtM1FiIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiLCJjOm1pY3Jvc29mdCJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJjb21wYXJ0aXItZHBIZ0pFSmEiLCJrRWVEc0xDcCIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiXX0sInZlcnNpb24iOjIsImFjIjoiREhhQndBRVlBTElBWFFBMkFCNkFFcUFNUUFtNEJpZ0RQZ0hpQVBOQWU0Qjd3RU9BSkxBWnFBOVVDRFlFUkFJamdSSkFpbUJLSUNXSUV0UUotQVVWQXFxQlljQzFJR0lnTTVnYW5BNVFCMDREcXdIWVFQWWdnWUJHYUNRd0U1d0ozZ1VFQW9QQlNrQ25VRlo0TFFBV2pBdGtCYzZDOGtHSFFNYmdZN0FBLkRIYUJ3QUVZQUxJQVhRQTJBQjZBRXFBTVFBbTRCaWdEUGdIaUFQTkFlNEI3d0VPQUpMQVpxQTlVQ0RZRVJBSWpnUkpBaW1CS0lDV0lFdFFKLUFVVkFxcUJZY0MxSUdJZ001Z2FuQTVRQjA0RHF3SFlRUFlnZ1lCR2FDUXdFNXdKM2dVRUFvUEJTa0NuVUZaNExRQVdqQXRrQmM2QzhrR0hRTWJnWTdBQSJ9',
    'euconsent-v2': 'CPy3MMAPy3MMAAHABBENDYCsAP_AAE7AAAiQIkNf_X_fb2vj-_p99_t0eY1P9_6_t6wzjheNE-8NyZ_X_J4Xp2M6rB34pqIKuR4kunLBIQdlHGHcTUgg4IkFqSPsYk2MizNKJ7JEmlMbE2dYGG9vn8TT-ZKY70__f__zvn-r___97oAAhCAABAAAAAgAAIAAAgAIAAAAAAAAAAAAAAAAAAAAAAAADA4tAsy0bqaFsHT0Lpo4igRGjCuJWoBQGUQCwtkBhmTPCnZHAR-wnUAAxAADBByGAFEaAICCIIAkKgIkEOBAqJAIdAACgAUIBAFRIgEoiLAQCAA0B8PAKKAJSLGDKjIidcCMKxIPu-QAAEAQAAIAAQAAAABAJCgAYAAiCgGgAwABEFARABgACIKAqADAAEQUBkAGAAIgoDwAMAARBQIQAYAAiCgTAAwABEFAqABgACIKAAAA.f_gACdgAAAAA',
    'utm': '%7B%22source%22%3A%22misterfantasy%22%2C%22medium%22%3A%22landing%22%2C%22campaign%22%3A%22landing%22%7D',
    'referer': 'https%3A%2F%2Fwww.misterfantasy.es%2F',
    'panoramaId_expiry': '1698247551946',
    'panoramaId': '2572592eeab9c989ed41751f13044945a7021dca77bdde30d12ca4cbf11029d7',
    'panoramaIdType': 'panoIndiv',
    '_pbjs_userid_consent_data': '6495574538250921',
    '_pubcid': '7ecd9069-cc1f-49c8-80bd-3ba5489c21f3',
    'pbjs-unifiedid': '%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-10-18T15%3A35%3A07%22%7D',
    'alert_app': '1',
    '_ga_9VNP59F4BS': 'GS1.1.1697666612.2.0.1697666612.0.0.0',
    'PHPSESSID': '67i6a9krr54l4kuijqtctt67ra',
    '_gid': 'GA1.2.423315046.1697822835',
    '_ga_ru_gid': 'GA1.2.1601217808.1697822835',
    '_ga_ru_md_gid': 'GA1.2.2033282420.1697822835',
    'connectId': '{"ttl":86400000,"lastUsed":1697822835681,"lastSynced":1697822835681}',
    'cto_bundle': 'JsBKkV9FbmN3OWVUUlNhbzVOUkdlWW5jbDBvWEtrYmR6SXY2cWl1U3NrcmU0SUJnbUIyam1jQncweEdhTERKQSUyRkJ2OGs1Nk9xTXE1TDBYRFBUN05BYkZCcDJ1aWRla0xHOGlBZEp5ZTc2VzRURGltSnZ1N2hWaWZaOG5xT2JiNjZGQkx2WFZSWGdmUWk2YUFEckdPYnBhWk5NNXh6NXZzTWxoJTJGZDhMWXJ2V0FwOUhzbG40bm8xcmNldVIwS0s3VVg3Z1N4cGlkVG1ZS1FHYkR1SHBUZHdPUW8wUSUzRCUzRA',
    'cto_bidid': 'guP56V9EOWxlYXJFOExJQmZLaFNTeWM2R0ZMZTlSRVU0dng4RE1VcXN5TzM0Z2FNJTJCbVd5cm5oaW8zM3RYSVRvVjNqRmdqTGk2alFrNDlzcyUyRmNyVERZZlM4JTJCR0F3JTJGeWlNOGVhM2d6Q3ltMVprQlM3RWlyVW5ydnZ0ZncxRGdPamlLTEpNYlNJbUNzelpDM2N1OHRRRSUyQmNqVnZBJTNEJTNE',
    '__gads': 'ID=a4852d83240da519:T=1691355392:RT=1697829767:S=ALNI_MasA4bbP60NnGwk6JJ0mDr7sdsmhA',
    '__gpi': 'UID=00000c7a110376e3:T=1691355392:RT=1697829767:S=ALNI_MYuuSMkm5fmK3ydafmEz8WQTTBwRg',
    '_ga': 'GA1.3.157019.1691355375',
    '_gid': 'GA1.3.423315046.1697822835',
    '_ga_9G2QBX7XXH': 'GS1.2.1697829767.8.1.1697829785.0.0.0',
    '_ga_LTJY4YF7RK': 'GS1.2.1697829767.8.1.1697829785.0.0.0',
    '_ga': 'GA1.2.157019.1691355375',
    '___iat_ses': '44FD7A75802E6686',
    '___iat_vis': '44FD7A75802E6686.8a288cb1b3bd94026be81ab59c6dcf91.1697829785588.5925367413a2e2a7f1afb6abc3434f01.ROMABEEBBA.11111111.1.0',
    '_dc_gtm_UA-1457125-1': '1',
    '_ga_NYWVQ5WBZV': 'GS1.1.1697829766.11.1.1697830997.60.0.0',
    'token': 'eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiIxNjk3ODMxMjk3IiwidXNlcmlkIjoiNjU2MDMiLCJhbGciOiJFUzI1NiJ9.-2E2g72M2gw0PpK45ZvR-_ddUo6wekw7LqZy6kIU9X-f4CTjhFA4vwTFXPJwmEiAIdppgQftIK6eKVCIVdtCYw',
    '_ga_7PVNCJC9CZ': 'GS1.1.1697829763.11.1.1697831010.0.0.0',
}

headers = {
    'authority': 'mister.mundodeportivo.com',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8,ca;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'refresh-token=eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiI0ODQ3MDI4OTg0IiwicmVmcmVzaCI6InVLM0N1NG1fZ08xM3p5R0w1ajdmVyIsImlkX3Rva2VuX2xpZmV0aW1lX2luX21pbiI6IjUiLCJhbGciOiJFUzI1NiJ9.lbW6viX0SlvotG_i-wx8HE54T_2h_tt5nZib0V0KBhab9LjWquRTOIGcwANZ1_POF3HXo5cJEkx-kuE8wSGWMQ; authenticated=true; sui_1pc=169135538948604B64FF861E07C5C54B3B7559D967A853D36328AFC4; _ga_ru=GA1.2.157019.1691355375; _ga_ru_md=GA1.2.157019.1691355375; _fbp=fb.1.1691355392236.1518909179; _cc_id=9be0afebfc7364c528dc393a5584ae05; macroleagues_tutorial_seen=1; didomi_token=eyJ1c2VyX2lkIjoiMTg5Y2NhMmUtMzVkOC02M2MyLWIwZTItMTYzZjVjODU2YmQzIiwiY3JlYXRlZCI6IjIwMjMtMDktMjlUMTE6MjI6MTguODAzWiIsInVwZGF0ZWQiOiIyMDIzLTA5LTI5VDExOjIyOjE4LjgwM1oiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpwaWFuby1ic1hwclg4dyIsImM6bHVjaWRob2xkLXlmdGJXVGY3IiwiYzpzYWxlc2ZvcmNlLUI0WEI1UU5aIiwiYzpsaXZlZnlyZS00Y2JOV1lFeiIsImM6eW91dHViZS1EV3RqQ1VLYiIsImM6YWNjZW5nYWdlLUVXRUx4MzRnIiwiYzpjaGFydGJlYXQtaHhLaEZiQXciLCJjOmFtYXpvbmFkcy05YzVUTkdhaiIsImM6dHdpdHRlcndpLXdVbUJubkt5IiwiYzpmYWNlYm9va3ctMmthN1Z3UTgiLCJjOmdvb2dsZW9wdC1RaGlBZG1WYSIsImM6Z2djcm9sbHVwLW5OSGVpMmFXIiwiYzpmYWNlYm9va2EtZnJVOU01SlkiLCJjOmdvb2dsZWFuYS1HMmJzRUp5VCIsImM6Z29vZ2xlYXVkLUxEalZZa2VhIiwiYzppbnN0YWdyYW0tdFdtSmdKcHEiLCJjOm5ldHF1ZXN0LU4yblc0ZnBHIiwiYzpwcm9jdGVyYW4tSzROdzh4TUMiLCJjOmNvbXNjb3JlLWpVRmM5aWNZIiwiYzpzcG90aW0tM0ZLSDYyeUMiLCJjOnl1c3AtejhOaTQ0Wk0iLCJjOndlbWFzc21lZC1QR1o2M0Z4WSIsImM6ZXZvbG9rLWl6S3o3QVlWIiwiYzpnb29nbGVmaXItSDhrY2lGSkciLCJjOmxhbGlnYS1ZNllRMjJSUiIsImM6YWRzdml1LVZUMjZtM1FiIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiLCJjOm1pY3Jvc29mdCJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJjb21wYXJ0aXItZHBIZ0pFSmEiLCJrRWVEc0xDcCIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIixudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwiYzppbmZlY3Rpb3VzLW1lZGlhIiwiYzpzbWFydGJpZC1QZkRhRXA4YiIsImM6dHVyYm8iLCJjOmFmZmlsaW5ldCIsImM6eWFuZGV4IiwiYzptYWNyb21pbGwtQUJCUEU4cHEiLCJjOnNjb290YS1FVkN3cnlDZCIsImM6bWVkaWFpbnRlbC1Sd3FtajZiQSIsImM6ZW5zaWdodGVuIiwiYzpqdy1wbGF5ZXIiLCJjOmh1cnJhLXRyYWNrZXIiXX0sInZlcnNpb24iOjIsImFjIjoiREhhQndBRVlBTElBWFFBMkFCNkFFcUFNUUFtNEJpZ0RQZ0hpQVBOQWU0Qjd3RU9BSkxBWnFBOVVDRFlFUkFJamdSSkFpbUJLSUNXSUV0UUotQVVWQXFxQlljQzFJR0lnTTVnYW5BNVFCMDREcXdIWVFQWWdnWUJHYUNRd0U1d0ozZ1VFQW9QQlNrQ25VRlo0TFFBV2pBdGtCYzZDOGtHSFFNYmdZN0FBLkRIYUJ3QUVZQUxJQVhRQTJBQjZBRXFBTVFBbTRCaWdEUGdIaUFQTkFlNEI3d0VPQUpMQVpxQTlVQ0RZRVJBSWpnUkpBaW1CS0lDV0lFdFFKLUFVVkFxcUJZY0MxSUdJZ001Z2FuQTVRQjA0RHF3SFlRUFlnZ1lCR2FDUXdFNXdKM2dVRUFvUEJTa0NuVUZaNExRQVdqQXRrQmM2QzhrR0hRTWJnWTdBQSJ9; euconsent-v2=CPy3MMAPy3MMAAHABBENDYCsAP_AAE7AAAiQIkNf_X_fb2vj-_p99_t0eY1P9_6_t6wzjheNE-8NyZ_X_J4Xp2M6rB34pqIKuR4kunLBIQdlHGHcTUgg4IkFqSPsYk2MizNKJ7JEmlMbE2dYGG9vn8TT-ZKY70__f__zvn-r___97oAAhCAABAAAAAgAAIAAAgAIAAAAAAAAAAAAAAAAAAAAAAAADA4tAsy0bqaFsHT0Lpo4igRGjCuJWoBQGUQCwtkBhmTPCnZHAR-wnUAAxAADBByGAFEaAICCIIAkKgIkEOBAqJAIdAACgAUIBAFRIgEoiLAQCAA0B8PAKKAJSLGDKjIidcCMKxIPu-QAAEAQAAIAAQAAAABAJCgAYAAiCgGgAwABEFARABgACIKAqADAAEQUBkAGAAIgoDwAMAARBQIQAYAAiCgTAAwABEFAqABgACIKAAAA.f_gACdgAAAAA; utm=%7B%22source%22%3A%22misterfantasy%22%2C%22medium%22%3A%22landing%22%2C%22campaign%22%3A%22landing%22%7D; referer=https%3A%2F%2Fwww.misterfantasy.es%2F; panoramaId_expiry=1698247551946; panoramaId=2572592eeab9c989ed41751f13044945a7021dca77bdde30d12ca4cbf11029d7; panoramaIdType=panoIndiv; _pbjs_userid_consent_data=6495574538250921; _pubcid=7ecd9069-cc1f-49c8-80bd-3ba5489c21f3; pbjs-unifiedid=%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-10-18T15%3A35%3A07%22%7D; alert_app=1; _ga_9VNP59F4BS=GS1.1.1697666612.2.0.1697666612.0.0.0; PHPSESSID=67i6a9krr54l4kuijqtctt67ra; _gid=GA1.2.423315046.1697822835; _ga_ru_gid=GA1.2.1601217808.1697822835; _ga_ru_md_gid=GA1.2.2033282420.1697822835; connectId={"ttl":86400000,"lastUsed":1697822835681,"lastSynced":1697822835681}; cto_bundle=JsBKkV9FbmN3OWVUUlNhbzVOUkdlWW5jbDBvWEtrYmR6SXY2cWl1U3NrcmU0SUJnbUIyam1jQncweEdhTERKQSUyRkJ2OGs1Nk9xTXE1TDBYRFBUN05BYkZCcDJ1aWRla0xHOGlBZEp5ZTc2VzRURGltSnZ1N2hWaWZaOG5xT2JiNjZGQkx2WFZSWGdmUWk2YUFEckdPYnBhWk5NNXh6NXZzTWxoJTJGZDhMWXJ2V0FwOUhzbG40bm8xcmNldVIwS0s3VVg3Z1N4cGlkVG1ZS1FHYkR1SHBUZHdPUW8wUSUzRCUzRA; cto_bidid=guP56V9EOWxlYXJFOExJQmZLaFNTeWM2R0ZMZTlSRVU0dng4RE1VcXN5TzM0Z2FNJTJCbVd5cm5oaW8zM3RYSVRvVjNqRmdqTGk2alFrNDlzcyUyRmNyVERZZlM4JTJCR0F3JTJGeWlNOGVhM2d6Q3ltMVprQlM3RWlyVW5ydnZ0ZncxRGdPamlLTEpNYlNJbUNzelpDM2N1OHRRRSUyQmNqVnZBJTNEJTNE; __gads=ID=a4852d83240da519:T=1691355392:RT=1697829767:S=ALNI_MasA4bbP60NnGwk6JJ0mDr7sdsmhA; __gpi=UID=00000c7a110376e3:T=1691355392:RT=1697829767:S=ALNI_MYuuSMkm5fmK3ydafmEz8WQTTBwRg; _ga=GA1.3.157019.1691355375; _gid=GA1.3.423315046.1697822835; _ga_9G2QBX7XXH=GS1.2.1697829767.8.1.1697829785.0.0.0; _ga_LTJY4YF7RK=GS1.2.1697829767.8.1.1697829785.0.0.0; _ga=GA1.2.157019.1691355375; ___iat_ses=44FD7A75802E6686; ___iat_vis=44FD7A75802E6686.8a288cb1b3bd94026be81ab59c6dcf91.1697829785588.5925367413a2e2a7f1afb6abc3434f01.ROMABEEBBA.11111111.1.0; _dc_gtm_UA-1457125-1=1; _ga_NYWVQ5WBZV=GS1.1.1697829766.11.1.1697830997.60.0.0; token=eyJhbGciOiJFUzI1NiJ9.eyJleHAiOiIxNjk3ODMxMjk3IiwidXNlcmlkIjoiNjU2MDMiLCJhbGciOiJFUzI1NiJ9.-2E2g72M2gw0PpK45ZvR-_ddUo6wekw7LqZy6kIU9X-f4CTjhFA4vwTFXPJwmEiAIdppgQftIK6eKVCIVdtCYw; _ga_7PVNCJC9CZ=GS1.1.1697829763.11.1.1697831010.0.0.0',
    'origin': 'https://mister.mundodeportivo.com',
    'referer': 'https://mister.mundodeportivo.com/feed',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1',
    'x-auth': '516586fb93df5f7e5bd8dfd0efb20a1b',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'post': 'players',
    'id': '444',
    'clone': '0',
    'comments': '0',
}

#call the url appending the id for each id  
timestr = time.strftime("%Y%m%d-%H%M%S")
Players_Raw_Output_Date = "Players_Raw_Output_Date"+timestr
file = open(Players_Raw_Output_Date,'w')
file.close()

playersIDsTestList = ['444', '1', '53113']

file = open(Players_Raw_Output_Date,'a')
#for id in playersIDsTestList:
playersDataRawList = {}
for id in playersIDsTestList:
    data['id'] = id
    response = requests.post('https://mister.mundodeportivo.com/ajax/sw', cookies=cookies, headers=headers, data=data)    
    jsonResponse = response.json()
    #playersDataRawList.update(jsonResponse['data']['player'])
    #playersDataRawList.update(jsonResponse['data']['away'])
    #playersDataRawList.update(jsonResponse['data']['home'])
    #playersDataRawList.update(jsonResponse['data']['next_match'])
    #playersDataRawList.update(jsonResponse['data']['player_extra'])
    #TODO additional logic can be applied here to create the events required data
    playersDataRawList[id+"_Player"] = jsonResponse['data']['player']
    playersDataRawList[id+"_Away"] = jsonResponse['data']['away']
    playersDataRawList[id+"_Home"] = jsonResponse['data']['home']
    playersDataRawList[id+"_Next_match"] = jsonResponse['data']['next_match'] 
    playersDataRawList[id+"_Player_extra"] = jsonResponse['data']['player_extra']

    pointsList=jsonResponse['data']['points']
    match=len(pointsList)
    matchID=1
    while match > 0:
        playersDataRawList[str(id)+"_J"+str(matchID)]=pointsList[match -1]
        match -= 1
        matchID += 1
   
    #write output to a file Players_Raw_Output_Date
    file.write("\n")
    file.write(json.dumps(playersDataRawList))
    playersDataRawList.clear()

file.close()

