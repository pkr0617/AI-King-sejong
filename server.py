# server.py
from flask import Flask, request, jsonify , render_template
from flask_cors import CORS
from replace_old_jamo_dataset2 import load_mapping, replace_text
from compose_hcj_to_hangul_dataset2 import compose_text
from openai import OpenAI

openai_api_key = "https://github.com/pkr0617/AI-King-sejong/security/secret-scanning/unblock-secret/34xz13Lznux2MSZQG1pzcLbWcwo"
client = OpenAI(api_key=openai_api_key)

def gpt_translate(text):
    response = client.chat.completions.create( 
        model="ft:gpt-4.1-nano-2025-04-14:cps:oldhangeul-translator5:CWx0xRHA",
        messages=[
            {"role": "system", "content": "너는 중세국어를 현대국어로 번역하는 AI야."},
            {"role": "user", "content": text}
        ]
    )
    # 응답 결과 접근 방식도 약간 변경됩니다.
    return response.choices[0].message.content

app = Flask(__name__)
CORS(app)  # React나 HTML에서 요청 허용

# CSV 불러오기
mapping = load_mapping("map/combined_old_mapped.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")

    # 1️⃣ 중세국어 자모 → 현대 자모로 변환
    replaced = replace_text(text, mapping)

    # 2️⃣ 현대 자모 → 완성형으로 결합
    composed = compose_text(replaced)

    # ⚙️ (여기에 GPT API 호출 코드 나중에 추가 가능)
    translated_text = gpt_translate(composed)

    return jsonify({"result": translated_text})

if __name__ == "__main__":
    app.run(debug=True)

# 디버그 핀: 529-986-693
# 필요한 패키지: pip install flask flask-cors openai jamo