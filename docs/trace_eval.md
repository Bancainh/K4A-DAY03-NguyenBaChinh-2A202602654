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

> ⚠️ **YÊU CẦU NGHIỆM THU:** Hệ thống đã được cấu hình sử dụng OpenAI API thật và thực thi toàn bộ test suite bằng lệnh `python src/app.py --all`.

Đoạn trace tiêu biểu dưới đây là Test Case TC03, thể hiện đầy đủ quá trình ReAct multi-step: Agent tra cứu dữ liệu lỗi, nhận Observation từ MCP Server, sau đó tiếp tục gọi Tool thứ hai để tạo phiếu Rework.

```json
[
  {
    "step": 1,
    "query": "Tìm các ca lỗi 2D trong ca đêm và tự động tạo phiếu Rework mức độ Cao cho toàn bộ danh sách tìm được.",
    "action_type": "TOOL_EXECUTION",
    "thought": "OpenAI quyết định gọi công cụ 'query_defect_data' với tham số: {\"defect_type\": \"2D\", \"shift\": \"ca đêm\"}",
    "tool_name": "query_defect_data",
    "arguments": {
      "defect_type": "2D",
      "shift": "ca đêm"
    },
    "observation": {
      "status": "SUCCESS",
      "data": [
        {
          "defect_id": "ERR-001"
        },
        {
          "defect_id": "ERR-003"
        }
      ]
    }
  },
  {
    "step": 2,
    "action_type": "TOOL_EXECUTION",
    "thought": "OpenAI quyết định gọi công cụ 'create_rework_ticket' với các defect ID nhận được từ Observation.",
    "tool_name": "create_rework_ticket",
    "arguments": {
      "defect_ids": "ERR-001, ERR-003",
      "priority": "Cao"
    },
    "observation": {
      "status": "SUCCESS",
      "updated_ids": [
        "ERR-001",
        "ERR-003"
      ],
      "message": "Đã tạo phiếu Rework mức độ Cao cho các mã: ERR-001, ERR-003"
    }
  },
  {
    "step": 3,
    "action_type": "FINAL_ANSWER",
    "output": "Phiếu Rework mức độ Cao đã được tạo thành công cho ERR-001 và ERR-003."
  }
]
```

Trace trên chứng minh Agent không dừng lại sau Tool Call đầu tiên mà tiếp tục sử dụng Observation từ MCP Server để quyết định Action kế tiếp, đúng mô hình ReAct `Thought -> Action -> Observation -> Final Answer`.


---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** _5_ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** _5_ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
