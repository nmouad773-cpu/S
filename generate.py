import os

# قائمة القنوات
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

def generate_files():
    domain = os.getenv("PAGES_URL", "https://nmouad773-cpu.github.io/REPOSITORY")
    
    content = "#EXTM3U\n#EXT-X-VERSION:3\n\n"
    for ch in CHANNELS:
        # رابط البث المحوّل HLS
        m3u8_link = f"{domain.rstrip('/')}/hls/{ch['id']}/index.m3u8"
        content += f'#EXTINF:-1 group-title="{ch["group"]}", {ch["name"]}\n{m3u8_link}\n\n'
        
    # إنشاء الملفات فوراً
    with open("playlist.m3u8", "w", encoding="utf-8") as f:
        f.write(content)
        
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(content)

    print("Done generating playlist files successfully!")

if __name__ == "__main__":
    generate_files()
