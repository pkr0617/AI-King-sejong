import React, { useState } from "react";
import "./App.css"; // ✅ 외부 CSS 연결

export default function App() {
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");

  const handleTranslate = () => {
    setOutputText(`${inputText}`);
  };
  function translateText() {
    const input = document.getElementById("inputText").value;
    document.getElementById("outputText").value = input;
  }
  const handleCopy = () => {
    navigator.clipboard.writeText(outputText);
    navigator.clipboard
      .writeText(output.value)
      .then(() => {
        alert("복사되었습니다!");
      })
      .catch(() => {
        alert("복사에 실패했습니다 😢");
      });
  };

  return (
    <div className="container">
      <header className="header">
        <img src="\/AI-king.jpeg\" alt="Ai-King" className="Ai-King" />
        {/* 왕관 이미지 들어갈 자리 */}
        {/* 예시: <img src=\"/your-crown.png\" alt=\"왕관\" className=\"crown\" /> */}
        <h1>중세국어 번역기</h1>
        <p>세종대왕과 함께하는 옛 한글 번역 여행</p>
      </header>

      <div className="translator-box">
        <label>중세국어</label>
        <textarea
          placeholder="번역할 중세국어 문장을 입력하세요..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />

        <label>현대국어</label>
        <textarea
          placeholder="AI가 번역한 결과가 여기에 표시됩니다."
          readOnly
          value={outputText}
        />

        <div className="button-group">
          <button onClick={handleTranslate}>번역하기</button>
          <button onClick={handleCopy}>복사</button>
        </div>
      </div>
    </div>
  );
}
