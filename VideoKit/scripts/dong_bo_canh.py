#!/usr/bin/env python3
"""Đồng bộ danh sách cảnh trong du-an.json với các file kich-ban/canh-N-*.md (chỉ dùng thư viện chuẩn).

Chạy sau khi thêm, đổi tên hoặc xóa file kịch bản. Giữ nguyên các trường đã chỉnh tay của cảnh đã có (ví dụ `giu_them_giay`),
chỉ cập nhật tên, tệp kịch bản, tên tệp lời thoại và `du_kien_giay` (ước tính từ số ký tự lời dẫn).

    cd videos/<du-an> && python3 ../../VideoKit/scripts/dong_bo_canh.py && python3 ../../VideoKit/scripts/build_index.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import du_an  # noqa: E402
from tao_du_an import doc_canh  # noqa: E402

DA = du_an()
cfg_file = DA.goc / "du-an.json"
if not cfg_file.exists():
    sys.exit("Không thấy du-an.json (chạy trong thư mục dự án).")
cfg = DA.cfg
cu = {c["id"]: c for c in cfg.get("canh", [])}
moi = []
for c in doc_canh(DA.goc / cfg.get("thu_muc", {}).get("kich_ban", "kich-ban")):
    g = dict(cu.get(c["id"], {}))
    g.update({k: c[k] for k in ("id", "ten", "tep_kich_ban", "tep_loi_thoai", "du_kien_giay")})
    g.setdefault("giu_them_giay", 0)
    moi.append(g)
cfg["canh"] = moi
cfg_file.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Đã đồng bộ {len(moi)} cảnh:")
for c in moi:
    print(f"  {c['id']}: {c['ten']}  (ước tính giọng {c['du_kien_giay']}s)")
