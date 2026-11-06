# Usage: python voice_margin.py cues.json voice.wav cues_yield.json
import json
import subprocess
import sys
import numpy as np

SR, WIN, MARGIN = 48000, 9600, 6.0


def read(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()


cues = json.load(open(sys.argv[1], encoding="utf-8"))
voice = read(sys.argv[2])
for c in cues:
    x = read(c["file"])
    if c.get("trim_end_s"):
        x = x[: int(c["trim_end_s"] * SR)]
    x = x * 10 ** ((c["target_db"] - c["file_peak_db"]) / 20)
    start = int((c["t"] - c["anchor_s"]) * SR)
    if start < 0:
        x, start = x[-start:], 0
    power = np.convolve(x ** 2, np.ones(WIN) / WIN, "same")
    mid = int(np.argmax(power))
    a, b = start + max(mid - WIN // 2, 0), start + mid + WIN // 2
    window = voice[a:b]
    voice_db = 10 * np.log10((window ** 2).mean() + 1e-12) if len(window) else -99.0
    margin = voice_db - 10 * np.log10(power[mid] + 1e-12)
    drop = max(MARGIN - margin, 0)
    c["ceiling_db"] = c["target_db"]
    c["target_db"] = round(c["target_db"] - drop, 1)
    print(f"{c['t']:7.3f} {c['family']:9} margin={margin:6.1f} {c['ceiling_db']} -> {c['target_db']}"
          f"{'  (ha hon 6 dB)' if drop > 6 else ''}")
json.dump(cues, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
