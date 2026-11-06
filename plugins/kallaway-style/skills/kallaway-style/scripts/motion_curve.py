# Usage: python motion_curve.py video.mp4 start_s end_s
import sys
import cv2
import numpy as np

path, start, end = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
n = round(start * fps)
cap.set(cv2.CAP_PROP_POS_FRAMES, n)
prev, out = None, []
while n <= end * fps:
    ok, frame = cap.read()
    if not ok:
        break
    gray = cv2.cvtColor(cv2.resize(frame, (160, 90)), cv2.COLOR_BGR2GRAY).astype(np.float32)
    if prev is not None:
        out.append((n, float(np.abs(gray - prev).mean())))
    prev, n = gray, n + 1
best = max(out, key=lambda x: x[1])
print(f"fps={fps:.3f} fastest_frame={best[0]} t={best[0]/fps:.3f}s motion={best[1]:.1f}")
for frame_no, motion in out:
    print(f"{frame_no}\t{frame_no/fps:.3f}\t{motion:.1f}")
