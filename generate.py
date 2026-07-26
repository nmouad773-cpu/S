import os
import subprocess
import threading
import time

CHANNELS = [{'id': 'bein_news', 'name': 'beIN Sports News', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917225.ts', 'group': 'beIN Sports'}, {'id': 'bein_1', 'name': 'beIN Sports 1', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917215.ts', 'group': 'beIN Sports'}, {'id': 'bein_2', 'name': 'beIN Sports 2', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917214.ts', 'group': 'beIN Sports'}, {'id': 'bein_3', 'name': 'beIN Sports 3', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917213.ts', 'group': 'beIN Sports'}, {'id': 'bein_4', 'name': 'beIN Sports 4', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917212.ts', 'group': 'beIN Sports'}, {'id': 'bein_5', 'name': 'beIN Sports 5', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917211.ts', 'group': 'beIN Sports'}, {'id': 'bein_6', 'name': 'beIN Sports 6', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917210.ts', 'group': 'beIN Sports'}, {'id': 'bein_7', 'name': 'beIN Sports 7', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917209.ts', 'group': 'beIN Sports'}, {'id': 'bein_8', 'name': 'beIN Sports 8', 'url': 'http://line.trxdnscloud.ru/live/1508358b7d/7b13892f97dc/1917208.ts', 'group': 'beIN Sports'}, {'id': 'thamanya_1', 'name': 'الثمانية 1', 'url': 'http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1898976.ts', 'group': 'Thamanya'}, {'id': 'thamanya_2', 'name': 'الثمانية 2', 'url': 'http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1898975.ts', 'group': 'Thamanya'}, {'id': 'thamanya_3', 'name': 'الثمانية 3', 'url': 'http://line.vpntxvpn.ru/live/1508358b7d/7b13892f97dc/1899054.ts', 'group': 'Thamanya'}, {'id': 'mbc_2', 'name': 'MBC 2', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7746.ts', 'group': 'MBC'}, {'id': 'mbc_3', 'name': 'MBC 3', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7745.ts', 'group': 'MBC'}, {'id': 'mbc_4', 'name': 'MBC 4', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/7744.ts', 'group': 'MBC'}, {'id': 'mbc_5', 'name': 'MBC 5', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/90929.ts', 'group': 'MBC'}, {'id': 'al_aoula', 'name': 'Al Aoula HD', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/891367.ts', 'group': 'Moroccan'}, {'id': 'maroc_2m', 'name': '2M Maroc', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/6736.ts', 'group': 'Moroccan'}, {'id': 'arryadia', 'name': 'Arryadia HD', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/969051.ts', 'group': 'Moroccan'}, {'id': 'nat_geo', 'name': 'National Geographic', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/880186.ts', 'group': 'Documentary'}, {'id': 'quran', 'name': 'القرآن الكريم', 'url': 'http://vpn.bimtrex.eu/live/2c16beb3ae/b28582fcb55a/2112498.ts', 'group': 'Islamic'}]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HLS_DIR = os.path.join(BASE_DIR, "hls")

def start_ffmpeg_stream(ch):
    ch_dir = os.path.join(HLS_DIR, ch["id"])
    os.makedirs(ch_dir, exist_ok=True)
    
    playlist_path = os.path.join(ch_dir, "index.m3u8")
    
    # FFmpeg command to pull raw TS stream and convert to HLS playlist (.m3u8) + segments (.ts)
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "warning",
        "-reconnect", "1", "-reconnect_at_eof", "1", "-reconnect_streamed", "1", "-reconnect_delay_max", "5",
        "-i", ch["url"],
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "128k",
        "-f", "hls",
        "-hls_time", "4",
        "-hls_list_size", "10",
        "-hls_flags", "delete_segments+append_list",
        "-hls_segment_filename", os.path.join(ch_dir, "seg_%03d.ts"),
        playlist_path
    ]
    
    print(f"[+] Starting restream for {ch['name']}...")
    try:
        process = subprocess.Popen(cmd)
        process.wait()
    except Exception as e:
        print(f"[-] Error streaming {ch['name']}: {e}")

def generate_master_m3u8(domain_url):
    content = "#EXTM3U\n"
    content += "#EXT-X-VERSION:3\n\n"
    
    for ch in CHANNELS:
        stream_url = f"{domain_url.rstrip('/')}/hls/{ch['id']}/index.m3u8"
        content += f'#EXTINF:-1 group-title="{ch["group"]}", {ch["name"]}\n'
        content += f'{stream_url}\n\n'
        
    master_path = os.path.join(BASE_DIR, "playlist.m3u8")
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    m3u_path = os.path.join(BASE_DIR, "playlist.m3u")
    with open(m3u_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[✔] Generated master playlist with restreamed links at: {master_path}")

if __name__ == "__main__":
    os.makedirs(HLS_DIR, exist_ok=True)
    
    # Get domain from environment or default
    domain = os.getenv("PAGES_URL", "https://USERNAME.github.io/REPOSITORY")
    generate_master_m3u8(domain)
    
    threads = []
    # Restream each channel in parallel
    for ch in CHANNELS:
        t = threading.Thread(target=start_ffmpeg_stream, args=(ch,), daemon=True)
        t.start()
        threads.append(t)
        time.sleep(1) # stagger launch
        
    # Keep main thread active for workflow duration (e.g., 30 mins segment capture)
    duration = int(os.getenv("STREAM_DURATION", "1800"))
    print(f"[*] Restreaming active for {duration} seconds...")
    time.sleep(duration)
