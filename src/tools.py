"""
🛠️ TOOL DEFINITIONS & NATIVE JSON SCHEMAS (Chuẩn OpenAPI / MCP Specification)
Định nghĩa các Tool Schemas chuẩn hóa dùng cho Native Tool Calling API của LLM.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA
# ==============================================================================

TOOLS_SCHEMA = [
    # --- TOOL 1: TRA CỨU LỖI ---
    {
        "name": "query_defect_data",
        "description": "Tra cứu danh sách các ca lỗi gán nhãn dựa trên loại lỗi và ca làm việc.",
        "parameters": {
            "type": "object",
            "properties": {
                "defect_type": {
                    "type": "string",
                    "description": "Loại lỗi cần tìm (ví dụ: '2D', '3D')"
                },
                "shift": {
                    "type": "string",
                    "description": "Ca làm việc (ví dụ: 'ca đêm', 'ca ngày')"
                }
            },
            "required": ["defect_type", "shift"] 
        }
    },
    
    # --- TOOL 2: TẠO PHIẾU REWORK (HÀNH ĐỘNG NHẠY CẢM) ---
    {
        "name": "create_rework_ticket",
        "description": "Tạo phiểu Rework cho các ca lỗi đã được tra cứu, với mức độ ưu tiên chỉ định",
        "parameters": {
            "type": "object",
            "properties": {
                "defect_ids": {
                    "type": "string", 
                    "description": "Danh sách mã ca lỗi cần tạo phiếu (ví dụ: 'ERR-001, ERR-002')"
                },
                "priority": {
                    "type": "string", 
                    "description": "Mức độ ưu tiên của phiếu Rework (ví dụ: 'Cao', 'Thấp')"
                }
            },
            "required": ["defect_ids", "priority"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

# Bổ sung Database mẫu cho QC Assistant
MOCK_DATABASE = {
    "ERR-001": {
        "product_name": "Bo mạch chủ X1",
        "defect_type": "2D",
        "shift": "ca đêm",
        "status": "chưa xử lý",
        "inspector": "Nguyễn Văn QC"
    },
    "ERR-002": {
        "product_name": "Màn hình OLED",
        "defect_type": "3D",
        "shift": "ca ngày",
        "status": "chưa xử lý",
        "inspector": "Trần Thị QA"
    },
    "ERR-003": {
        "product_name": "Bo mạch chủ X1",
        "defect_type": "2D",
        "shift": "ca đêm",
        "status": "chưa xử lý",
        "inspector": "Nguyễn Văn QC"
    }
}

def execute_query_defect_data(defect_type: str, shift: str) -> str:
    """Tra cứu lỗi từ MOCK_DATABASE."""

    defect_type_normalized = defect_type.strip().upper()
    shift_normalized = shift.strip().lower()

    results = []

    for err_id, info in MOCK_DATABASE.items():

        if (
            info["defect_type"].strip().upper() == defect_type_normalized
            and info["shift"].strip().lower() == shift_normalized
        ):
            record = {
                "defect_id": err_id,
                **info
            }

            results.append(record)

    if results:
        return json.dumps(
            {
                "status": "SUCCESS",
                "data": results
            },
            ensure_ascii=False
        )

    return json.dumps(
        {
            "status": "NOT_FOUND",
            "message": "Không tìm thấy dữ liệu phù hợp."
        },
        ensure_ascii=False
    )

def execute_create_rework_ticket(defect_ids: str, priority: str) -> str:
    """Tạo phiếu Rework và cập nhật trạng thái lỗi."""

    id_list = [
        item.strip().upper()
        for item in defect_ids.split(",")
        if item.strip()
    ]

    updated_ids = []
    skipped_ids = []
    not_found_ids = []

    for err_id in id_list:

        if err_id not in MOCK_DATABASE:
            not_found_ids.append(err_id)
            continue

        if MOCK_DATABASE[err_id]["status"] == "đã tạo phiếu":
            skipped_ids.append(err_id)
            continue

        MOCK_DATABASE[err_id]["status"] = "đã tạo phiếu"
        MOCK_DATABASE[err_id]["rework_priority"] = priority

        updated_ids.append(err_id)

    return json.dumps(
        {
            "status": "SUCCESS",
            "updated_ids": updated_ids,
            "skipped_ids": skipped_ids,
            "not_found_ids": not_found_ids,
            "message": (
                f"Đã tạo phiếu Rework mức độ {priority} "
                f"cho các mã: {', '.join(updated_ids) if updated_ids else 'Không có'}"
            )
        },
        ensure_ascii=False
    )


# ==============================================================================
# 3. ROUTER & DISPATCHER (MCP SERVER INTEGRATION)
# ==============================================================================

# Router gọi tool thực tế
TOOL_ROUTER = {
    "query_defect_data": execute_query_defect_data,
    "create_rework_ticket": execute_create_rework_ticket
}

# Bổ sung hàm Dispatcher bắt buộc của Lab để MCP Server có thể gọi
def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)