# -*- coding: utf-8 -*-
"""Torrent-Downloader-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PUguJ7pooSJbPX-ER67fa4IQf0CuiWRf
"""

from google.colab import drive
drive.mount('/content/drive/')

!python -m pip install --upgrade pip setuptools wheel
!python -m pip install lbry-libtorrent
!apt-get install python3-libtorrent

link = 'magnet:?xt=urn:btih:cf0a609211ac434321ed354b0430f913c20f1f5d&dn=Assassins.Creed.Valhalla.Repack-EMPRESS'

import libtorrent as lt
import time
import datetime

ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/content/drive/My Drive/To Be Tested/',
    'storage_mode': lt.storage_mode_t(2),
    # 'paused': False,
    # 'auto_managed': True,
    # 'duplicate_is_error': True
    }

print(link)

handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

begin = time.time()

print(datetime.datetime.now())

print ('Downloading Metadata...')
while (not handle.has_metadata()):
    time.sleep(1)
print ('Got Metadata, Starting Torrent Download...')

print("Starting", handle.name())

while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    print (f"\rStatus: {' '.join(str(s.state).split('_')).title()} {round(s.progress * 100, 2)}% Peers: {s.num_peers} "
            f"(⬇ {s.download_rate // 1000}kb/s ⬆ {s.upload_rate // 1000}kB/s)", end="")
    time.sleep(1)

end = time.time()
print(f"\n{handle.name()} COMPLETE")

print(f"Elapsed Time: {(end - begin) // 60} minutes, {round((end - begin) % 60)} seconds")

print(datetime.datetime.now())

"""
function ClickConnect(){
console.log("Working");
document.querySelector("colab-toolbar-button").click()
}setInterval(ClickConnect,600000)
"""