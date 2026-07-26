import os
import subprocess
import threading
import time

CHANNELS = [
    {"id": "bein_news", "name": "beIN Sports News", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917225.ts", "group": "beIN Sports"},
    {"id": "bein_1", "name": "beIN Sports 1", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917215.ts", "group": "beIN Sports"},
    {"id": "bein_2", "name": "beIN Sports 2", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917214.ts", "group": "beIN Sports"},
    {"id": "bein_3", "name": "beIN Sports 3", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917213.ts", "group": "beIN Sports"},
    {"id": "bein_4", "name": "beIN Sports 4", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917212.ts", "group": "beIN Sports"},
    {"id": "bein_5", "name": "beIN Sports 5", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917211.ts", "group": "beIN Sports"},
    {"id": "bein_6", "name": "beIN Sports 6", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917210.ts", "group": "beIN Sports"},
    {"id": "bein_7", "name": "beIN Sports 7", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917209.ts", "group": "beIN Sports"},
    {"id": "bein_8", "name": "beIN Sports 8", "url": "http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917208.ts", "group": "beIN Sports"},
    {"id": "thamanya_1", "name": "الثمانية 1", "url": "http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1898976.ts", "group": "Thamanya"},
    {"id": "thamanya_2", "name": "الثمانية 2", "url": "http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1898975.ts", "group": "Thamanya"},
    {"id": "thamanya_3", "name": "الثمانية 3", "url": "http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1899054.ts", "group": "Thamanya"},
    {"id": "mbc_2", "name": "MBC 2", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7746.ts", "group": "MBC"},
    {"id": "mbc_3", "name": "MBC 3", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7745.ts", "group": "MBC"},
    {"id": "mbc_4", "name": "MBC 4", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7744.ts", "group": "MBC"},
    {"id": "mbc_5", "name": "MBC 5", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/90929.ts", "group": "MBC"},
    {"id": "al_aoula", "name": "Al Aoula HD", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/891367.ts", "group": "Moroccan"},
    {"id": "maroc_2m", "name": "2M Maroc", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/6736.ts", "group": "Moroccan"},
    {"id": "arryadia", "name": "Arryadia HD", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/969051.ts", "group": "Moroccan"},
    {"id": "nat_geo", "name": "National Geographic", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/880186.ts", "group": "Documentary"},
    {"id": "quran", "name": "القرآن الكريم", "url": "http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/2112498.ts", "group": "Islamic"}
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HLS_DIR = os.path.join(BASE_DIR, "hls")

def start_ffmpeg(ch):
    ch_dir = os.path.join(HLS_DIR, ch["id"])
    os.makedirs(ch_dir, exist_ok=True)
    playlist_path = os.path.join(ch_dir, "index.m3u8")

    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error",
        "-reconnect", "1", "-reconnect_at_eof", "1", "-reconnect_streamed", "1",
        "-i", ch["url"],
        "-c", "copy",
        "-f", "hls",
        "-hls_time", "6",
        "-hls_list_size", "20",
        "-hls_flags", "delete_segments",
        playlist_path
    ]

    try:
        subprocess.run(cmd)
    except Exception as e:
        print(f"Error streaming {ch['name']}: {e}")

def create_master_playlists(domain):
    content = "#EXTM3U\n#EXT-X-VERSION:3\n\n"
    for ch in CHANNELS:
        stream_url = f"{domain.rstrip('/')}/hls/{ch['id']}/index.m3u8"
        content += f'#EXTINF:-1 group-title="{ch["group"]}", {ch["name"]}\n{stream_url}\n\n'
    
    with open(os.path.join(BASE_DIR, "playlist.m3u8"), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(BASE_DIR, "playlist.m3u"), "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    os.makedirs(HLS_DIR, exist_ok=True)
    domain = os.getenv("PAGES_URL", "https://nmouad773-cpu.github.io/REPOSITORY")
    create_master_playlists(domain)

    # تشغيل عملية البث لجميع القنوات بالتوازي
    threads = []
    for ch in CHANNELS:
        t = threading.Thread(target=start_ffmpeg, args=(ch,), daemon=True)
        t.start()
        threads.append(t)
        time.sleep(0.3)

    # ابقاء البث شغالاً لمدة 30 دقيقة قبل الانتقال للـ Workflow التالي
    run_duration = int(os.getenv("STREAM_DURATION", "1800"))
    time.sleep(run_duration)
