from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tâm Lý Học Hiện Đại - Lê Bá Vũ</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: #05070e;
            color: #f1f5f9;
            line-height: 1.7;
            padding: 40px 20px;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        /* Hiệu ứng nền Cực quang (Aurora Background) chuyển động mượt mà */
        .aurora-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            overflow: hidden;
            background: #05070e;
        }

        .aurora-blob {
            position: absolute;
            filter: blur(100px);
            opacity: 0.25;
            border-radius: 50%;
            animation: floatBlob 15s infinite alternate ease-in-out;
        }

        .blob-1 {
            width: 450px;
            height: 450px;
            background: #00ffcc;
            top: -10%;
            left: -10%;
            animation-delay: 0s;
        }

        .blob-2 {
            width: 500px;
            height: 500px;
            background: #0077ff;
            bottom: -15%;
            right: -10%;
            animation-delay: -5s;
        }

        .blob-3 {
            width: 350px;
            height: 350px;
            background: #9d00ff;
            top: 40%;
            left: 30%;
            animation-delay: -10s;
        }

        @keyframes floatBlob {
            0% { transform: translate(0px, 0px) scale(1); }
            50% { transform: translate(60px, 40px) scale(1.15); }
            100% { transform: translate(-40px, -50px) scale(0.9); }
        }

        .container {
            max-width: 1050px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        header {
            text-align: center;
            padding: 50px 20px;
            background: rgba(13, 19, 33, 0.6);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            margin-bottom: 40px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            animation: fadeInDown 0.8s ease-out;
        }

        h1 {
            background: linear-gradient(135deg, #00ffcc 0%, #38bdf8 50%, #0077ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.8rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 12px;
            font-weight: 800;
        }

        .author {
            color: #94a3b8;
            font-size: 1.15rem;
        }

        .author-name {
            color: #00ffcc;
            font-weight: bold;
            text-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
        }

        .grid-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin-bottom: 30px;
        }

        @media (max-width: 768px) {
            .grid-layout { grid-template-columns: 1fr; }
        }

        /* Hiệu ứng Spotlight Card tương tác chuột */
        .card-spotlight {
            background: rgba(18, 25, 43, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.07);
            padding: 30px;
            border-radius: 16px;
            position: relative;
            overflow: hidden;
            transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.3s ease;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .card-spotlight:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(0, 255, 204, 0.12);
            border-color: rgba(0, 255, 204, 0.3);
        }

        /* Tâm sáng di chuyển theo chuột trên card */
        .card-spotlight::before {
            content: '';
            position: absolute;
            top: var(--y, 0);
            left: var(--x, 0);
            transform: translate(-50%, -50%);
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(0, 255, 204, 0.15), transparent 70%);
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
            z-index: 1;
        }

        .card-spotlight:hover::before {
            opacity: 1;
        }

        .card-content {
            position: relative;
            z-index: 2;
        }

        .card-spotlight h2 {
            color: #ffffff;
            font-size: 1.45rem;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card-spotlight p {
            color: #cbd5e1;
            font-size: 1rem;
            margin-bottom: 12px;
        }

        /* Khu vực Trắc nghiệm */
        .quiz-container {
            grid-column: span 2;
            background: rgba(18, 25, 43, 0.85);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 255, 204, 0.25);
            padding: 35px;
            border-radius: 16px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.4);
        }

        @media (max-width: 768px) {
            .quiz-container { grid-column: span 1; }
        }

        .quiz-container h2 {
            color: #ffffff;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }

        .question-box {
            font-size: 1.15rem;
            font-weight: 600;
            color: #38bdf8;
            margin-bottom: 25px;
            line-height: 1.6;
        }

        .options-group {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 25px;
        }

        .option-btn {
            background: rgba(30, 41, 59, 0.8);
            color: #e2e8f0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 15px 20px;
            border-radius: 10px;
            cursor: pointer;
            text-align: left;
            font-size: 1rem;
            transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .option-btn:hover {
            background: rgba(0, 255, 204, 0.12);
            border-color: #00ffcc;
            color: #00ffcc;
            transform: translateX(6px);
            box-shadow: 0 5px 15px rgba(0, 255, 204, 0.15);
        }

        .quiz-result {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid #00ffcc;
            padding: 20px;
            border-radius: 10px;
            color: #00ffcc;
            font-weight: 500;
            display: none;
            animation: fadeInUp 0.4s ease-out;
            box-shadow: inset 0 0 15px rgba(0, 255, 204, 0.1);
        }

        footer {
            text-align: center;
            margin-top: 50px;
            padding: 25px;
            color: #64748b;
            font-size: 0.95rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <!-- Hiệu ứng nền chuyển động cực quang -->
    <div class="aurora-bg">
        <div class="aurora-blob blob-1"></div>
        <div class="aurora-blob blob-2"></div>
        <div class="aurora-blob blob-3"></div>
    </div>

    <div class="container">
        <header>
            <h1>Tâm Lý Học Hiện Đại</h1>
            <div class="author">Nghiên cứu & Thiết kế bởi: <span class="author-name">Lê Bá Vũ</span></div>
        </header>

        <div class="grid-layout">
            <!-- Thẻ 1 -->
            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🧠 Hiệu Ứng Hào Quang (Halo Effect)</h2>
                    <p>Là một lỗi tư duy nhận thức phổ biến, trong đó ấn tượng tổng thể của chúng ta về một người ảnh hưởng trực tiếp đến cách ta đánh giá các đặc điểm cụ thể của họ.</p>
                    <p><em>Ví dụ:</em> Nếu ai đó có ngoại hình sáng sủa, ta thường có xu hướng ngầm gán cho họ tính cách thông minh và đáng tin cậy hơn thực tế.</p>
                </div>
            </div>

            <!-- Thẻ 2 -->
            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🌊 Trạng Thái Dòng Chảy (Flow State)</h2>
                    <p>Được định nghĩa là trạng thái tập trung tuyệt đối khi con người hòa mình hoàn toàn vào một hoạt động say mê.</p>
                    <p>Khi đạt trạng thái Flow, thời gian trôi đi nhanh hơn, năng suất đạt mức tối đa và mang lại cảm giác hạnh phúc sâu sắc.</p>
                </div>
            </div>

            <!-- Thẻ 3 -->
            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🛡️ Cơ Chế Phòng Vệ Bản Ngã</h2>
                    <p>Theo trường phái phân tâm học, đây là những chiến lược vô thức mà tâm trí sử dụng để tự bảo vệ trước lo âu hoặc cảm giác căng thẳng.</p>
                    <p>Các hình thức phổ biến: <em>Phủ nhận (Denial)</em>, <em>Dồn nén (Repression)</em> và <em>Chuyển dịch (Displacement)</em>.</p>
                </div>
            </div>

            <!-- Thẻ 4 -->
            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🔋 Năng Lượng Xã Hội: Nội Tâm & Hướng Ngoại</h2>
                    <p>Sự khác biệt cốt lõi không nằm ở việc nói nhiều hay ít, mà ở <strong>cách sạc lại năng lượng tinh thần</strong>.</p>
                    <p>Người hướng nội nạp lại năng lượng qua không gian yên tĩnh một mình, trong khi người hướng ngoại được kích thích khi giao tiếp xã hội.</p>
                </div>
            </div>
        </div>

        <!-- Trắc nghiệm tâm lý tương tác -->
        <div class="quiz-container">
            <h2>✨ Trắc Nghiệm Nhanh: Phong Cách Xử Lý Cảm Xúc</h2>
            <div class="question-box" id="quizQuestion">Khi đối mặt với một áp lực hoặc căng thẳng lớn trong cuộc sống, phản ứng đầu tiên của bạn là gì?</div>
            
            <div class="options-group" id="quizOptions">
                <button class="option-btn" onclick="answerQuiz(1)">🎯 A. Dành thời gian ở một mình để suy ngẫm, phân tích nguyên nhân và tự giải quyết.</button>
                <button class="option-btn" onclick="answerQuiz(2)">🤝 B. Tìm kiếm sự chia sẻ, tâm sự ngay với bạn bè hoặc người thân để vơi bớt.</button>
                <button class="option-btn" onclick="answerQuiz(3)">⚡ C. Chuyển hướng sự chú ý sang hoạt động giải trí (xem phim, nghe nhạc, thể thao).</button>
            </div>

            <div class="quiz-result" id="quizResult"></div>
        </div>

        <footer>
            <p>&copy; 2026 Dự Án Tâm Lý Học | Phát triển bởi <strong>Lê Bá Vũ</strong></p>
        </footer>
    </div>

    <script>
        /* JavaScript tạo hiệu ứng đốm sáng (Spotlight) di chuyển theo chuột trên Card */
        const cards = document.querySelectorAll('.card-spotlight');
        cards.forEach(card => {
            card.addEventListener('mousemove', e => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                card.style.setProperty('--x', `${x}px`);
                card.style.setProperty('--y', `${y}px`);
            });
        });

        function answerQuiz(choice) {
            const resultBox = document.getElementById('quizResult');
            resultBox.style.display = 'block';
            
            if (choice === 1) {
                resultBox.innerHTML = "🎯 <strong>Phong cách hướng nội phân tích:</strong> Bạn giải quyết vấn đề bằng tư duy logic và thế giới nội tâm sâu sắc. Sự tĩnh lặng là liều thuốc chữa lành tốt nhất cho bạn.";
            } else if (choice === 2) {
                resultBox.innerHTML = "🤝 <strong>Phong cách tương tác xã hội:</strong> Bạn giải tỏa cảm xúc thông qua sự kết nối và sẻ chia. Sự thấu cảm từ người khác giúp bạn nhanh chóng lấy lại cân bằng.";
            } else if (choice === 3) {
                resultBox.innerHTML = "⚡ <strong>Phong cách chuyển hướng năng lượng:</strong> Bạn có cơ chế tự vệ linh hoạt bằng cách tách biệt căng thẳng ra khỏi không gian sinh hoạt qua các hoạt động giải trí tích cực.";
            }
        }
    </script>

</body>
</html>
"""


@app.route("/")
def home():
  return render_template_string(HTML_TEMPLATE)


import os

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)