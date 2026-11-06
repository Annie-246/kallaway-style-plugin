# Usage: python sfx_probe.py file1 file2 ...
import sys
import librosa
import numpy as np

for f in sys.argv[1:]:
    stereo, sr = librosa.load(f, sr=48000, mono=False)
    y = librosa.to_mono(stereo)
    env = librosa.feature.rms(y=y, frame_length=1024, hop_length=240)[0]
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=240)[0]
    peak_db = 20 * np.log10(np.abs(stereo).max() + 1e-9)
    t_energy = np.argmax(env) * 240 / sr
    t_transient = np.argmax(np.abs(y)) / sr
    above = np.where(env > env.max() * 0.1)[0] * 240 / sr
    print(f"{f}: dur={len(y)/sr:.2f}s peak={peak_db:.1f}dB t_energy={t_energy:.3f}s "
          f"t_transient={t_transient:.3f}s body={above[0]:.2f}-{above[-1]:.2f}s "
          f"bright={centroid.mean():.0f}Hz")
