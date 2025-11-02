# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from replace_old_jamo_dataset2 import load_mapping, replace_text
from compose_hcj_to_hangul_dataset2 import compose_text

app = Flask(__name__)
CORS(app)  # React나 HTML에서 요청 허용

# CSV 불러오기
mapping = load_mapping("combined_old_mapped.csv")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")

    # 1️⃣ 중세국어 자모 → 현대 자모로 변환
    replaced = replace_text(text, mapping)

    # 2️⃣ 현대 자모 → 완성형으로 결합
    composed = compose_text(replaced)

    # ⚙️ (여기에 GPT API 호출 코드 나중에 추가 가능)
    translated_text = composed  # 임시로 그대로 반환

    return jsonify({"result": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
