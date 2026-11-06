# Kallaway Style – plugin dựng video cho Claude Code

Plugin giúp Claude Code dựng video dọc 9:16 kiểu Kallaway từ một video bạn nói trước camera:

- Minh hoạ neon vẽ riêng cho từng ý (icon tự vẽ, biểu đồ, timeline, morph)
- Thẻ người nói bo góc dưới đáy, đầu nhô ra khỏi khung
- Caption chạy theo từng chữ, tiêu đề sans đậm + serif nghiêng + hộp đỏ
- Cắt cứng ở câu chuyển ý, nhạc ngắt trước điểm reveal, thumbnail cùng style

Chia sẻ bởi **Nhật Dương** · [Facebook](https://www.facebook.com/nhatduong.vn) · [YouTube](https://www.youtube.com/@Under30vn) · [TikTok](https://www.tiktok.com/@nhatduong.vn)

Đây là plugin do cộng đồng làm theo phong cách dựng của Kallaway, không liên kết với Kallaway.

## Cài đặt

Chạy một lệnh trong terminal. Lệnh này cài plugin và **bật tự động cập nhật** trên máy bạn.

**Windows (PowerShell):**

```powershell
curl.exe -fsSL https://raw.githubusercontent.com/Annie-246/kallaway-style-plugin/main/install.js | node -
```

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/Annie-246/kallaway-style-plugin/main/install.js | node -
```

Khởi động lại Claude Code sau khi cài.

### Cài trong Claude Code

Nếu không muốn chạy lệnh ở terminal, gõ lần lượt trong Claude Code:

```
/plugin marketplace add https://github.com/Annie-246/kallaway-style-plugin.git
/plugin install kallaway-style@nhat-duong-plugins
```

Cách này **chưa bật** tự động cập nhật. Muốn bật: gõ `/plugin`, vào tab **Marketplaces**, chọn `nhat-duong-plugins`, chọn **Enable auto-update**.

## Dùng

Mở Claude Code trong thư mục chứa video của bạn và nói:

> Dựng video này theo style Kallaway

Hoặc gọi trực tiếp `/kallaway-style:kallaway-style`.

Claude làm theo quy trình: cắt thô → bạn duyệt → lên plan → vẽ graphic → render → thumbnail.

## Cần có

- [Claude Code](https://claude.com/claude-code)
- Node.js 18+ (Remotion được cài tự động khi tạo dự án, mỗi dự án tốn vài trăm MB)
- Python 3.10+ và ffmpeg
- `pip install faster-whisper opencv-python pillow numpy rembg`
- Tuỳ chọn để tách nhạc 2 lớp: `pip install demucs torch librosa soundfile`

## Cập nhật

Bản mới tự về máy trong phiên Claude Code sau, sau khi bạn gửi tin nhắn đầu tiên, trễ tối đa khoảng 10 phút. Khi thấy báo `Plugin updated`, gõ `/reload-plugins` hoặc mở lại Claude Code.

Muốn cập nhật ngay: `claude plugin update kallaway-style@nhat-duong-plugins`

Gỡ cài đặt: `claude plugin uninstall kallaway-style@nhat-duong-plugins`

## Giấy phép

- Mã nguồn và tài liệu trong repo này: [MIT](LICENSE).
- Font trong `assets/fonts`: SIL Open Font License, văn bản ở [THIRD_PARTY](THIRD_PARTY).
- Icon trong `assets/icons`: xem `assets/icons/LICENSE.txt`.
- Remotion có giấy phép riêng: miễn phí cho cá nhân và công ty nhỏ, xem [remotion.dev/license](https://www.remotion.dev/license).
