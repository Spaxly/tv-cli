#!/usr/bin/python

import httpx
import re
import subprocess
from bs4 import BeautifulSoup as bs
from fzf import fzf_prompt

client = httpx.Client(headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})

host = "https://ustvgo.tv"

r=client.get(host)
soup = bs(r.text,"html.parser")
channel_links=[i["href"] for i in soup.select("ol li a")]

channel_names=[i.text for i in soup.select("ol li a")]



channel = fzf_prompt(channel_names)
channel_url = channel_links[channel_names.index(channel)]

r= client.get(channel_url)
iframe= re.findall(r"<iframe src='(.*?)'",r.text)[0]

r=client.get(f"{host}{iframe}",headers={"Referer":channel_url})
try:
    streaming_link = re.findall(r"hls_src='(.*?)'",r.text)[0]
except:
    print("[*]Not available")
    exit()

mpv = subprocess.Popen(["mpv",
                        f"{streaming_link}",
                        f"--force-media-title={channel}"])
mpv.wait()
mpv.kill()

