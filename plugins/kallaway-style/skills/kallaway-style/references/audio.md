# Âm thanh

Số đo gốc: `references/precise-measurements.md` §4, §5. Luật cao nhất vẫn là L1–L23 trong `references/sfx-rules.md`.

Tên loại tiếng trong file này suy ra từ phổ tần, không ai nghe trực tiếp. Mốc thời gian và mức dB là số đo.

## Kallaway làm gì

| Việc | Số video | Dựng thế nào |
|---|---|---|
| Nhạc chạy dưới cả đồ hoạ lẫn mặt người, không hạ khi có giọng (no ducking) | 4/4 | `volume` cố định, không sidechain |
| Giọng cao hơn nhạc, trung vị 13,5–19,6 dB | 4/4 | `music.volume` 0,10–0,20 |
| SFX gắn với đồ hoạ đổi trạng thái; cắt thường về mặt người không có tiếng | 4/4 | Không đặt SFX ở cú cắt thường |
| Tắt nhạc dưới câu chốt trên mặt người, cắt chết, vào lại ở cú cắt sau | 3/4 | `music.drops` |
| Riser dừng đúng lúc nhạc tắt, kèm zoom hoặc đổi khung mặt | 2/4 | Riser kết thúc đúng frame cắt |
| Nhạc chạy tới khung cuối, không fade | 3/4 | Template chỉ ramp 2 khung |
| Trống chỉ chơi trong SPLIT | 1/4 rõ (v2) | `drumsOnlyInSplit`, tuỳ bài |
| Pop trên từng chip, trễ +0,14 s sau chip | 1/4 (v2) | Chỉ dùng khi danh sách là điểm nhấn |
| Im hoàn toàn đoạn cảnh báo trước CTA | 1/4 (v4 68,7–75,5) | Một `drops` dài |

Bốn video có bốn bảng tiếng khác nhau. Không có "bộ SFX Kallaway" cố định:

| Video | SFX | Cách dùng |
|---|---|---|
| v1 | 3 whoosh trầm + 3 riser | Ít nhất, chỉ cho chuyển động lớn |
| v2 | Boom trầm + pop | Boom khi đồ hoạ vào, pop trên chip, đỉnh trễ 0,08–0,30 s |
| v3 | ~15 whoosh mềm + 3 riser | Mỗi lần sân khấu đổi bố cục một whoosh |
| v4 | Impact, whoosh, tiếng trượt cao độ | Âm thanh diễn theo hình: "decay" cao độ tụt, "dive" tiếng biến mất |

Chọn một bảng theo nội dung và giữ nguyên cả video (E9). Mặc định dùng bảng của v3: whoosh mềm cho chuyển động sân khấu.

Cảnh FULL đầu tiên sau hook: v1 và v3 gần im hẳn, v2 và v4 còn lớp pluck rất nhỏ. Mặc định tắt hẳn bằng `drops`, vì `plan_skeleton` đã làm sẵn.

## Làm trong template

- `prep_music.py` tách bài nhạc thành `music/rest.wav` (bass+other) và `music/drums.wav`.
- `plan.music`: `rest` + `drums` + `volume` + `drops` + `drumsOnlyInSplit`.
- Bài không có trống (pad): chỉ cần `src`, bỏ `drums`.
- `plan.sfx[]` là thứ template phát. `dur` (giây, tuỳ chọn) cắt tiếng dứt khoát, dùng cho riser dừng chết.

## Quy trình SFX

Làm sau khi hình đã chốt, không làm song song. 

Mỗi tiếng là một dòng trong `public/cues.json` (định dạng ở mục dưới). Nguồn sự thật là file này, `plan.sfx` được sinh từ nó.

1. **Lấy mốc từ plan, không đoán.** Mốc animation có sẵn trong `plan.json`.
2. **Lượt 1, whoosh.** Mỗi chuyển động sân khấu lớn (camera, morph, push, timeline lia) một whoosh. Đỉnh rơi vào frame nhanh nhất: `python "$S/motion_curve.py" out/draft.mp4 <đầu> <cuối>`.
3. **Lượt 2, texture.** Chỉ cho sự kiện đáng nhấn: impact khi đồ hoạ lớn vào, không gõ theo từng chip (E1).
4. **Lượt 3, riser.** Tối đa 3 riser, mỗi riser gắn một `drops` và dừng đúng frame nhạc tắt.
5. **Đo tiếng.** `python "$S/sfx_probe.py" <các biến thể>`, lấy `t_energy` làm `anchor_s`, `peak` làm `file_peak_db`.
6. **Nhường giọng và nạp vào plan.** Chạy trong `public/`:

```bash
cd "<…>/kallaway/public"
python "$S/voice_margin.py" cues.json source/<file giọng> cues_yield.json
python "$S/cues_to_plan.py" --project ".."
```

`voice_margin.py` hạ mọi tiếng chưa dưới giọng 6 dB. Báo người dùng những tiếng bị hạ trên 6 dB.

## Định dạng cue

`public/cues.json` là một mảng, mỗi tiếng một dòng. `rule` là mã trong bảng L1–L23 (`references/sfx-rules.md`):

```json
[{"t": 12.40, "family": "whooshes", "file": "sfx/whoosh.mp3", "anchor_s": 0.19, "file_peak_db": -10.1,
  "target_db": -12, "trim_end_s": null, "event": "Tiêu đề trượt vào", "rule": "L1"}]
```

`t` là mốc trên hình (giây). `anchor_s` và `file_peak_db` lấy từ `sfx_probe.py`. `trim_end_s` là điểm cắt tính theo thời gian trong file tiếng, `null` nếu dùng nguyên clip.

## Ánh xạ sang luật SFX L1–L23

| Sự kiện Kallaway | Luật | Làm gì | File gợi ý (tìm trên myinstants) |
|---|---|---|---|
| Khung đầu (tiêu đề hook bật) | **L5** boom nhẹ | sub-boom tại frame 0, ≥6 dB dưới giọng | `big-boom-sub-drop`, `deep-bass-boom-cinematic` |
| Push / camera bay lớn / thu vào điện thoại / đổi bố cục sân khấu | **L1** whoosh nhẹ | đỉnh ở frame nhanh nhất | `deep-swoosh` |
| Đồ hoạ lớn vào, reveal lớn | **L4** impact vừa | tối đa 1–3 lần cả video | `bass-impact` |
| Trước câu chốt | **L3 → L15** | riser 0,5–1 s dừng chết đúng lúc nhạc tắt | `cinematic-suspense-riser` với `trim_end_s` |
| Cảnh FULL đầu tiên sau hook | **L15** | im nhạc (tối đa 2 lần L15/video, tính cả lần này) | — |
| Morph, clip/thẻ đổi chỗ, badge bay lên header | **L1** | whoosh dải rộng, mềm, 0,3–0,6 s, đỉnh giữa morph | `deep-swoosh` (cắt 0,6–2,2 s), một mẫu cho mọi morph |
| Orbit bắt đầu quay / lưới reel bật | **L1** | một whoosh cho cả cụm (E1) | như trên |
| Thanh tiến trình chạy | không (hoặc **L17** nếu là đếm số thật) | mẫu 4 để im | — |
| Vật đổi màu sang xanh = "đạt" | **L10** (tuỳ chọn, rất nhỏ) | mẫu gốc để im | — |
| Cắt SPLIT↔FULL thường, jump cut, chấm/trang bật | **L23 / không** | KHÔNG SFX | — |
| Chip trong danh sách | không; pop nếu danh sách là điểm nhấn | pop trễ +0,14 s như v2, một mẫu tiếng | — |

Mẫu đo được 5–25 tiếng/phút (v1 ~5, v3 và v4 ~11–13, v2 ~25 trên 39 s). Guide giới hạn 3–6 điểm/phút ở đoạn nhiều phần tử. Giữ giới hạn của guide trừ khi người dùng đổi.

Nguồn tải: **myinstants trước, ElevenLabs sau**. Dựng xong liệt kê SFX + mốc + mã luật + các khoảng im nhạc.

### Quy tắc áp nguyên (`references/sfx-rules.md`)
- **Một loại sự kiện = một loại tiếng** cho cả video (E9).
- **Một khoảnh khắc = một SFX chính** (E8): morph có whoosh thì logo/chip hiện trong morph đó không thêm pop.
- **Không đặt đỉnh SFX đè âm tiết quan trọng** (tên sản phẩm, con số): xê dịch vài chục ms (E4).
- **Nghe thử bằng loa điện thoại**; sub-boom gần như không nghe trên loa điện thoại (E11) nên đừng để điểm nhấn chỉ dựa vào trầm.
- **archive.org KHÔNG dùng cho SFX** (người dùng đã nghe thử và không ưng), chỉ cho ảnh/clip minh hoạ.
- Ghi nguồn SFX vào `sfx-credits.csv`.

## Mức âm lượng
- Giọng chuẩn hoá cuối −14 LUFS.
- Nhạc rest khoảng −14…−20 dB dưới giọng; drums có thể to hơn rest 3–4 dB.
- Whoosh −10…−12 dB, texture −6…−7 dB, riser −5 dB là mức trần. Mọi tiếng phải dưới giọng ít nhất 6 dB tại chỗ chồng lên lời.

## Hoàn thiện
`ffmpeg -i out/draft.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy -c:a aac -b:a 192k out/final.mp4`
Render Remotion: đặt `TEMP`/`TMP` sang ổ còn trống (mỗi lần render chép cả `public/` vào thư mục tạm, đã từng làm đầy ổ C).
