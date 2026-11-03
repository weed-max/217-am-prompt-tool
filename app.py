import json
import os
import streamlit as st

# Định nghĩa các mảng thông số (Ma trận xoay vòng)
PILLARS = [
    {
        "name": "Pillar A1 — Misty Lakes & Rivers (Hồ mờ sương)",
        "prompt": "a lone Vietnamese woman with long dark hair standing by a vast misty lake during a cool blue hour twilight, overcast misty atmosphere, deep charcoal shadows, desaturated cool slate gray and steel blue tones",
    },
    {
        "name": "Pillar A2 — Wild Coastlines & Cliffs (Bờ biển hoang sơ)",
        "prompt": "a lone Vietnamese woman with long dark hair standing on a wild rocky coastline during overcast twilight, crashing waves, deep charcoal shadows, desaturated cool-muted blue and gray tones",
    },
    {
        "name": "Pillar A3 — Pine Forests (Rừng thông sương mù)",
        "prompt": "a lone Vietnamese woman with long dark hair walking through a quiet pine forest in Da Lat covered in thick fog, deep charcoal shadows, desaturated cool-muted tones",
    },
    {
        "name": (
            "Pillar B — Luxury Indoor Spaces (Không gian penthouse tối giản)"
        ),
        "prompt": "a young Vietnamese woman with long hair sitting by a large floor-to-ceiling glass window of a luxury penthouse overlooking a rainy night city skyline, soft ambient lighting, deep charcoal shadows, desaturated cool-muted tones",
    },
    {
        "name": (
            "Pillar C — Urban Life & Architecture (Đô thị hiện đại đêm mưa)"
        ),
        "prompt": "a young Vietnamese woman with long dark hair walking along a modern glass pedestrian bridge at night, wet asphalt reflecting cool street lights, cool slate gray and desaturated blue color grading",
    },
]

CAMERAS = [
    "Profile Lakeside Seated Silhouette (Góc nghiêng ngồi bên bờ hồ)",
    "Over-The-Shoulder Ocean Horizon View (Góc nhìn qua vai hướng biển)",
    "Deep Forest Canopy Upward Glance (Góc ngước nhìn dưới vòm lá rừng già)",
    (
        "Distant Cinematic Landscape Silhouette / Pure Nature Shot (Góc siêu"
        " xa thiên nhiên)"
    ),
    (
        "Moody Over-The-Head / High-Angle Environmental Shot (Góc cao chụp"
        " hắt xuống)"
    ),
    "Rear-View Full Body / Medium Shot (Góc từ phía sau lấy trọn dáng)",
]

HAIRS = [
    "Style 1: Minimalist Metallic Claw Clip (Kẹp càng cua kim loại)",
    "Style 2: Half-Up Half-Down (Buộc nửa đầu bằng dây ruy băng lụa)",
    "Style 3: Casual Single Side Braid (Tết lỏng lệch một bên)",
    "Style 4: Low Ponytail (Buộc đuôi ngựa thấp)",
    "Style 5: Minimalist Hair Stick (Trâm cài tối giản)",
]

WARDROBES = [
    "Set 1: Black silk slip dress & oversized tailored black blazer",
    "Set 2: Black premium linen shirt & black wide-leg trousers",
    "Set 3: Minimalist white fine-knit maxi dress",
    "Set 4: High-street black trench coat & dark denim",
    "Set 5: Black cashmere turtleneck & pleated silk midi skirt",
    "Set 6: Classic white tailored shirt & dark trousers",
]

STATE_FILE = "rotation_state.json"


def load_state():
  if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
      return json.load(f)
  return {
      "last_pillar_index": 0,
      "last_camera_index": 0,
      "last_hair_index": 0,
      "last_wardrobe_index": 0,
  }


def save_state(state):
  with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=4)


# Giao diện Streamlit
st.title("🎬 2:17 AM - Anti-Repetition Prompt Generator")
st.write(
    "Tool tự động xoay vòng thông số, đảm bảo không bao giờ bị trùng lặp giữa các"
    " lần tạo."
)

state = load_state()

if st.button("🚀 Tạo Prompt Mới (Tự động xoay vòng)"):
  # Thuật toán tự động tịnh tiến vòng tròn (Modulo arithmetic)
  state["last_pillar_index"] = (state["last_pillar_index"] + 1) % len(PILLARS)
  state["last_camera_index"] = (state["last_camera_index"] + 1) % len(CAMERAS)
  state["last_hair_index"] = (state["last_hair_index"] + 1) % len(HAIRS)
  state["last_wardrobe_index"] = (state["last_wardrobe_index"] + 1) % len(
      WARDROBES
  )

  save_state(state)
  st.success("Đã cập nhật tổ hợp thông số mới không trùng lặp!")

# Hiển thị kết quả hiện tại
curr_pillar = PILLARS[state["last_pillar_index"]]
curr_camera = CAMERAS[state["last_camera_index"]]
curr_hair = HAIRS[state["last_hair_index"]]
curr_wardrobe = WARDROBES[state["last_wardrobe_index"]]

st.subheader("📌 Thông số đã chọn cho lần này:")
st.markdown(f"**- Bối cảnh (Pillar):** {curr_pillar['name']}")
st.markdown(f"**- Góc máy (Camera):** {curr_camera}")
st.markdown(f"**- Kiểu tóc (Hair):** {curr_hair}")
st.markdown(f"**- Trang phục (Wardrobe):** {curr_wardrobe}")

# Tổng hợp thành English Prompt hoàn chỉnh
final_prompt = (
    f"A cinematic moody shot, 9:16 aspect ratio, {curr_pillar['prompt']}, {curr_camera},"
    f" {curr_hair}, wearing {curr_wardrobe}. Moody cool-muted color system,"
    f" deep charcoal shadows, desaturated cool slate gray and steel blue"
    f" tones, low contrast, cinematic composition, crisp 4K resolution,"
    f" photorealistic, anti-AI look."
)

st.subheader("✨ English Image-Generation Prompt:")
st.code(final_prompt, language="text")
