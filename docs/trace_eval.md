# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Bá Chính  
> **Mã Sinh Viên / Mã Học viên:** 2A202602654  
> **Chủ đề Lựa chọn:** 3.1: Trợ lý Kiểm định Chất lượng (QC Assistant)  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Có, trợ lý phải thực hiện tuần tự: Tra cứu -> đối chiếu -> tạo phiếu Rework   |
| **2. Tool Interaction** | 4 / 5 | Có, Hệ thống phải kết nối với DataBase để đọc ghi dữ liệu.   |
| **3. Dynamic Decision** | 4 / 5 | Có, luồng xử lý rẽ nhánh linh hoạt theo dữ liệu sống. Ví dụ sẽ bỏ qua các dữ liệu lỗi đã tạo phiếu rework trước đó.  |
| **4. Long Horizon Goal** | 4 / 5 | Có, Hệ thống phải giữ mục tiêu tạo phiếu Rework đến cuối. Không bị rơi ngữ cảnh ngay cả khi bị ngắt quãng để chờ con người xác nhận.  |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | Bài toán rất phù hợp triển khai Agentic System. |


---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "3d và ca đêm",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "query_defect_data",
    "arguments": {
      "defect_type": "3D",
      "shift": "ca đêm"
    },
    "observation": {
      "status": "NOT_FOUND",
      "message": "Không tìm thấy dữ liệu"
    },
    "latency_ms": 1105.6
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** _5_ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** _5_ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
