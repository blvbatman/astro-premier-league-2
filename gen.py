from datetime import datetime, timezone, timedelta

stream_url = "https://t.freetv.fun/live/astro-premier-league-2-tv.ts"

# Tính toán sequence tự động dựa trên thời gian thực hiện tại
target_duration = 4
now_epoch = int(datetime.now(timezone.utc).timestamp())
start_sequence = now_epoch // target_duration - 10  # Lùi lại vài segment để tạo độ trễ an toàn

start_time = datetime.now(timezone.utc) - timedelta(seconds=40)
mpegts_base = 767785031
mpegts_increment = target_duration * 90000

lines = [
    "#EXTM3U",
    "#EXT-X-VERSION:3",
    "## Created with GitHub Actions Auto Packager",
    f"#EXT-X-MEDIA-SEQUENCE:{start_sequence}",
    "#EXT-X-INDEPENDENT-SEGMENTS",
    f"#EXT-X-TARGETDURATION:{target_duration}",
]

num_segments = 10
for i in range(num_segments):
    seq = start_sequence + i
    current_mpegts = mpegts_base + (i * mpegts_increment)
    current_time = start_time + timedelta(seconds=(i * target_duration))
    time_str = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    if i == 0:
        lines.append(f"#USP-X-TIMESTAMP-MAP:MPEGTS={current_mpegts},LOCAL={time_str}")
    
    lines.append(f"#EXT-X-PROGRAM-DATE-TIME:{time_str}")
    lines.append(f"#EXTINF:{target_duration}, no desc")
    lines.append(stream_url)

# Lưu thành file playlist.m3u8
with open("astro-premier-league-2.m3u8", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Generated playlist.m3u8 successfully!")
