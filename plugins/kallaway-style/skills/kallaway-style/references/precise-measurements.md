# Số đo chính xác (lượt soi thứ 2, 27/10/2026)

Đo trên 3 mẫu gốc bằng script: diff từng khung (24/25 fps = 40–42 ms/khung), mốc từng chữ của Whisper, tách nguồn âm thanh bằng Demucs (htdemucs: drums / bass / other / vocals). Số liệu ở đây **thay thế** mọi chỗ mâu thuẫn trong các file khác.

## 1. Thời điểm

| Hiện tượng | Số đo | Cách dựng |
|---|---|---|
| Phụ đề đổi chữ | lệch so với mốc bắt đầu của chữ: trung vị **−3 ms** (v1), +20 ms (v2), −20 ms (v3); p25–p75 trong ±40 ms | bật đúng `word.s`, không sớm, không trễ |
| Số từ mỗi lần hiện phụ đề | **1,13 / 1,41 / 1,11** → gần như luôn 1 từ | tiếng Việt: 1 từ ghép (1–2 âm tiết) mỗi lần; tốc độ đổi ≈ 2,5–3 lần/giây |
| Cắt đổi bố cục (SPLIT↔FULL) | rơi **80–180 ms TRƯỚC** chữ đầu câu mới (trung vị ~110 ms): 11,417→"But"11,50 · 22,50→22,60 · 32,08→32,26 · 41,67→41,78 · 52,54→52,64 · 61,17→61,28 · 67,58→67,66 | ranh giới segment = `firstWord.s − 0.11`; cú cắt nằm trong khoảng nghỉ, năng lượng giọng tại cắt tụt ~7 dB |
| Nhãn/chip bật | 4–6 khung (≈170–250 ms) trước từ khóa | `at = word.s − 0.2` |
| Graphic đầu tiên sau khi quay về SPLIT | bật ở **khung đầu tiên** sau cắt (không chờ) | |

## 2. Chữ (đo pixel khung 1080×1920)

| Thành phần | Đo được | Suy ra |
|---|---|---|
| Tiêu đề 2 dòng (v1 0,9 s) | chữ hoa cao 48 px; baseline dòng 1 y=205, dòng 2 y=266 → cách **61 px**; khe mực giữa dòng 13 px | cỡ ≈ 66 px, **line-height 0,92** |
| Tiêu đề mẫu 3 | chữ hoa 37 px, baseline cách 53 px | cỡ ≈ 50 px, line-height ~1,05 |
| Tiêu đề sans + serif (v1 5 s) | khối cao 103 px (y 266–368), sans chữ hoa ~55 px | sans 76 px; serif ×1,32, cùng baseline |
| Vị trí tiêu đề | đỉnh mực y = 116–160 (tối) / 158 (sáng) | `titleTop` ≈ 120–150 |
| Phụ đề SPLIT | đỉnh chữ có nét lên y = **1219**, cao nét lên 45 px | cỡ ≈ **60 px**, tâm ~1243 |
| Phụ đề FULL | x-height 37 px, y 1143–1194 | cỡ ≈ **68 px** (to hơn SPLIT), tâm ~1170 |
| Hộp đỏ dòng 1 (v2) | cao 46 px cho chữ ~56 px; dòng 2 cách 10 px | đệm dọc hộp ≈ 0,06em |

## 3. Hình ảnh thật được đưa vào thế nào

- **Phần lớn là video đang chạy** (reel phát luôn các cảnh cắt bên trong, ~0,3 s/cảnh), không phải ảnh tĩnh. Lưới reel ở v3 0–3 s là 6 video cùng chạy.
- Lối vào: **cắt cứng** (xuất hiện ngay ở 1 khung, thường kèm camera đang lia) hoặc **mờ dần ≤5 khung** từ tối. Ảnh đơn không nhấp nháy; tường reel và clip có khung thì có (v2 2,32 s, v4 19,33 s).
- Sau khi vào: **zoom chậm liên tục** (Ken Burns, ~3–6% trong 1–2 s), viền mảnh sáng + glow trắng nhẹ, bo góc ~14–20 px.
- Ảnh chụp giao diện (IG insights, trang profile) đặt trong thẻ bo góc, rồi **vẽ đè** lên (đường retention neon, nhãn chú thích bật trên reel: "Curiosity hook").
- Ghi chú serif cạnh hình: gõ ra từng chữ cái, chậm (~25 ký tự/giây), màu xám sáng.
- Khi cắt từ FULL vào một cảnh có băng chuyền, camera **đang lia sẵn** từ khung đầu (nhoè ngang ~10 khung).

## 4. Âm thanh (tách nguồn)

**Nhạc**
- v1: pad synth không trống. v2, v3: **beat hip-hop 808** (kick có cao độ trượt xuống, ~130 BPM, mỗi kick cách 0,92 s), hi-hat, pluck.
- **Cảnh FULL đầu tiên sau hook tắt lớp bass/trống** (−76…−82 dB): v1 1,75–3,96 · v2 5,72–9,64 · v3 3,04–4,63. v1 và v3 gần im hẳn; v2 và v4 còn lớp pluck rất nhỏ (−36…−50 dB).
- v2: **trống chỉ chơi trong SPLIT** (drums FULL −54…−76 dB, SPLIT −29…−50 dB).
- Nhạc/beat **vào lại đúng khung cắt FULL→SPLIT**, cú kick/hit đầu tiên nằm trong 0–300 ms sau cắt (lớp drums tăng +35…+50 dB). Cắt SPLIT→FULL thì không có gì.
- Ngắt giữa video: v1 25,8–27,0 · 55,2–56,0; v3 29,9–31,7 · 75,6–78,8; v4 im suốt 68,7–75,5 trước CTA. Nhạc tắt **cắt chết**, không fade.

**SFX (chỉ v1 có tách bạch được, vì nhạc v1 không có trống)**
| Thời điểm | Tiếng | Hình |
|---|---|---|
| 0,05 s | sub-boom 30–300 Hz, ngân ~0,7 s | khung đầu |
| 13,15 s | boom/whoosh trầm ~0,5 s | push cụm thẻ → biểu đồ |
| 25,2→25,8 s | rền trầm + riser 2–10 kHz tăng dần, **cắt chết** tại drop | camera zoom vào 70% |
| 37,85 s | sub-boom | chip "Contrast Moment" |
| 54,9→55,2 s | rền trầm, cắt chết vào khoảng lặng | trước "the climax doesn't happen…" |
Đúng riêng cho v1: không có SFX dải cao, mọi SFX dưới 300 Hz trừ riser. Ba video còn lại khác, xem §5.

## 5. Lượt soi 3 (05/11/2026): 4 mẫu, có phản biện độc lập

Chi tiết và bằng chứng: `style-synthesis.md`. Số ở đây thắng các mục trên khi mâu thuẫn.

| Số đo | v1 | v2 | v3 | v4 |
|---|---|---|---|---|
| Mặt người toàn màn | 29% | 29,5% | 29,9% | 27% |
| Cắt mặt↔sân khấu mỗi phút | 14,6 | 10,8 | 9,2 | 6,0 |
| Đoạn dài nhất không có mặt | 9,5 s | 9,8 s | 15,6 s | 30 s |
| Từ / thời gian phát âm | 4,46 | 4,44 | 3,76 | 3,71 |
| Giọng trên nhạc (trung vị) | 13,5 dB | 19,6 dB | 17 dB | 15 dB |
| Chấm lưới | 18,6 px | ~40 px | 18,6 px | 15,4 px |
| Phụ đề SPLIT, tâm y / cao | 1241 / 44 | 1286 / 38 | 1276 / 42 | 1259 / 42 |
| Phụ đề FULL, tâm y / cao | 1156 / 50 | 1281 / 48 | 1210 / 49 | 1231 / 49 |

- 37/48 cú cắt rơi trong 0–6 khung trước chữ đầu câu. Cắt giữa câu chủ yếu là lúc đi vào đồ hoạ.
- Đường cong đo được: v1 (.5,.05,.15,1), v2 (.3,0,.15,1), v3 (.3,0,.1,1), v4 (.48,0,0,1). Chung: vào nhanh, đuôi dài. Mẫu 2 có một lần vượt đích 19 px ở lưới tài liệu, còn lại không.
- Chuyển động nhanh có nhoè ở v1, v3, v4; v2 không có.
- Font vẫn là suy đoán: gần nhất Inter Tight và Instrument Serif Italic, chưa chồng chữ để xác nhận.
