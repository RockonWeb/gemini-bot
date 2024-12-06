import httpx

proxy_url = "http://TQDcLFzD:beBUzDkf@172.252.110.215:64676"
url = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe"

with httpx.Client(proxies={"http://": proxy_url, "https://": proxy_url}, timeout=30) as client:
    response = client.get(url)
    print(response.json())
