from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tâm Lý Học - Lê Bá Vũ</title>
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

        /* Hiệu ứng nền Cực quang (Aurora Background) */
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

        .blob-1 { width: 450px; height: 450px; background: #00ffcc; top: -10%; left: -10%; animation-delay: 0s; }
        .blob-2 { width: 500px; height: 500px; background: #0077ff; bottom: -15%; right: -10%; animation-delay: -5s; }
        .blob-3 { width: 350px; height: 350px; background: #9d00ff; top: 40%; left: 30%; animation-delay: -10s; }

        @keyframes floatBlob {
            0% { transform: translate(0px, 0px) scale(1); }
            50% { transform: translate(60px, 40px) scale(1.15); }
            100% { transform: translate(-40px, -50px) scale(0.9); }
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        header {
            text-align: center;
            padding: 50px 20px;
            background: rgba(13, 19, 33, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            margin-bottom: 40px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
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

        .section-title {
            font-size: 1.8rem;
            color: #38bdf8;
            margin: 40px 0 20px 0;
            border-left: 5px solid #00ffcc;
            padding-left: 15px;
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

        /* Hiệu ứng Spotlight Card */
        .card-spotlight {
            background: rgba(18, 25, 43, 0.75);
            backdrop-filter: blur(12px);
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

        .card-spotlight:hover::before { opacity: 1; }
        .card-content { position: relative; z-index: 2; }

        .card-spotlight h2 {
            color: #ffffff;
            font-size: 1.35rem;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card-spotlight p {
            color: #cbd5e1;
            font-size: 0.98rem;
            margin-bottom: 10px;
        }

        /* Khu vực Trắc nghiệm 20 câu */
        .quiz-container {
            background: rgba(18, 25, 43, 0.85);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 255, 204, 0.25);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.4);
            margin-top: 40px;
        }

        .quiz-intro {
            color: #94a3b8;
            margin-bottom: 30px;
            font-size: 1.05rem;
        }

        .question-card {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 22px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        .question-title {
            font-size: 1.05rem;
            font-weight: 600;
            color: #38bdf8;
            margin-bottom: 15px;
        }

        .options-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .option-label {
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(30, 41, 59, 0.6);
            padding: 12px 16px;
            border-radius: 8px;
            cursor: pointer;
            border: 1px solid transparent;
            transition: all 0.2s;
            font-size: 0.95rem;
        }

        .option-label:hover {
            background: rgba(0, 255, 204, 0.08);
            border-color: rgba(0, 255, 204, 0.3);
            color: #00ffcc;
        }

        .option-label input { accent-color: #00ffcc; }

        .submit-btn {
            display: block;
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #00ffcc, #0077ff);
            color: #05070e;
            font-weight: bold;
            font-size: 1.1rem;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 30px;
            transition: opacity 0.2s, transform 0.2s;
            box-shadow: 0 5px 20px rgba(0, 255, 204, 0.3);
        }

        .submit-btn:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }

        .quiz-result-box {
            background: rgba(15, 23, 42, 0.95);
            border: 2px solid #00ffcc;
            padding: 30px;
            border-radius: 12px;
            margin-top: 30px;
            display: none;
            animation: fadeIn 0.5s ease-out;
        }

        .quiz-result-box h3 {
            color: #00ffcc;
            font-size: 1.5rem;
            margin-bottom: 15px;
        }

        .quiz-result-box p {
            color: #e2e8f0;
            font-size: 1.05rem;
            line-height: 1.6;
        }

        footer {
            text-align: center;
            margin-top: 50px;
            padding: 25px;
            color: #64748b;
            font-size: 0.95rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <div class="aurora-bg">
        <div class="aurora-blob blob-1"></div>
        <div class="aurora-blob blob-2"></div>
        <div class="aurora-blob blob-3"></div>
    </div>

    <div class="container">
        <header>
            <h1>Tâm Lý Học</h1>
            <div class="author">Nghiên cứu & Thiết kế bởi: <span class="author-name">Lê Bá Vũ</span></div>
        </header>

        <h2 class="section-title">🧠 Các Khái Niệm & Hiệu Ứng Tâm Lý Cốt Lõi</h2>

        <div class="grid-layout">
            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🌟 Hiệu Ứng Hào Quang (Halo Effect)</h2>
                    <p>Ấn tượng tổng thể về một người (như ngoại hình, sự thân thiện) chi phối cách ta đánh giá các đặc điểm cụ thể của họ (trí tuệ, đạo đức).</p>
                </div>
            </div>

            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🌊 Trạng Thái Dòng Chảy (Flow State)</h2>
                    <p>Trạng thái tập trung tuyệt đối khi con người hòa mình hoàn toàn vào hoạt động say mê, giúp tối ưu hóa năng suất và mang lại hạnh phúc sâu sắc.</p>
                </div>
            </div>

            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🛡️ Cơ Chế Phòng Vệ Bản Ngã</h2>
                    <p>Các chiến lược vô thức mà tâm trí sử dụng để tự bảo vệ trước lo âu hoặc căng thẳng như phủ nhận, dồn nén và chuyển dịch.</p>
                </div>
            </div>

            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🔋 Nội Tâm & Hướng Ngoại</h2>
                    <p>Sự khác biệt cốt lõi nằm ở cách sạc lại năng lượng tinh thần: Người hướng nội cần không gian tĩnh lặng, người hướng ngoại cần giao tiếp xã hội.</p>
                </div>
            </div>

            <div class="card-spotlight">
                <div class="card-content">
                    <h2>👥 Hiệu Ứng Người Đứng Ngoài (Bystander Effect)</h2>
                    <p>Hiện tượng cá nhân ít có xu hướng giúp đỡ nạn nhân khi có sự hiện diện của nhiều người khác vì trách nhiệm bị phân tán đều cho đám đông.</p>
                </div>
            </div>

            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🎯 Thiên Kiến Xác Nhận (Confirmation Bias)</h2>
                    <p>Xu hướng tìm kiếm, chú ý và ghi nhớ thông tin củng cố niềm tin sẵn có của bản thân, đồng thời phớt lờ các bằng chứng trái chiều.</p>
                </div>
            </div>

            <div class="card-spotlight">
                <div class="card-content">
                    <h2>🎭 Hội Chứng Kẻ Giả Mạo (Imposter Syndrome)</h2>
                    <p>Tâm lý tự ti, luôn hoài nghi về năng lực bản thân và lo sợ một ngày nào đó bị phát hiện là "kẻ ăn may" dù đã đạt nhiều thành tựu lớn.</p>
                </div>
            </div>

            <div class="card-spotlight">
                <div class="card-content">
                    <h2>💊 Hiệu Ứng Giả Dược (Placebo Effect)</h2>
                    <p>Sức mạnh của niềm tin: Khi cơ thể trải qua sự cải thiện thực sự về thể chất hoặc tinh thần chỉ vì tin rằng mình nhận được phương pháp điều trị hiệu quả.</p>
                </div>
            </div>
        </div>

        <!-- Trắc nghiệm tâm lý 20 câu -->
        <div class="quiz-container">
            <h2 style="color: #ffffff; font-size: 1.6rem; margin-bottom: 10px;">✨ Bài Trắc Nghiệm Tâm Lý: Khám Phá Chân Dung Tính Cách (20 Câu)</h2>
            <p class="quiz-intro">Hãy chọn đáp án trung thực nhất với cảm nhận của bạn cho từng câu hỏi dưới đây để hệ thống tổng hợp báo cáo phân tích tâm lý cá nhân.</p>

            <form id="psychQuiz">
                <!-- Câu 1 -->
                <div class="question-card">
                    <div class="question-title">1. Khi gặp một thông tin mới trái ngược hoàn toàn với niềm tin lâu nay của bạn, bạn thường phản ứng thế nào?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q1" value="A"> A. Tìm hiểu kỹ nguồn gốc và bằng chứng khoa học trước khi đánh giá lại.</label>
                        <label class="option-label"><input type="radio" name="q1" value="B"> B. Cảm thấy khó chịu và có xu hướng bỏ qua hoặc bảo vệ quan điểm cũ.</label>
                        <label class="option-label"><input type="radio" name="q1" value="C"> C. Trò chuyện, thảo luận với người khác để xem họ nghĩ gì về vấn đề đó.</label>
                    </div>
                </div>

                <!-- Câu 2 -->
                <div class="question-card">
                    <div class="question-title">2. Trong một buổi thảo luận nhóm đông người, bạn thường có xu hướng gì?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q2" value="A"> A. Quan sát kỹ lưỡng cách mọi người tương tác rồi mới đưa ra ý kiến cốt lõi.</label>
                        <label class="option-label"><input type="radio" name="q2" value="B"> B. Chủ động dẫn dắt cuộc thảo luận và đưa ra định hướng cho nhóm.</label>
                        <label class="option-label"><input type="radio" name="q2" value="C"> C. Lắng nghe và hỗ trợ ý tưởng của người khác để giữ không khí hòa hợp.</label>
                    </div>
                </div>

                <!-- Câu 3 -->
                <div class="question-card">
                    <div class="question-title">3. Khi phải đưa ra quyết định quan trọng dưới áp lực thời gian, bạn dựa vào yếu tố nào nhất?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q3" value="A"> A. Phân tích logic rủi ro và lợi ích của từng phương án.</label>
                        <label class="option-label"><input type="radio" name="q3" value="B"> B. Trực giác và kinh nghiệm cá nhân trong quá khứ.</label>
                        <label class="option-label"><input type="radio" name="q3" value="C"> C. Tham khảo ý kiến từ những người có kinh nghiệm hoặc đáng tin cậy.</label>
                    </div>
                </div>

                <!-- Câu 4 -->
                <div class="question-card">
                    <div class="question-title">4. Bạn cảm thấy thế nào khi phải ở một mình trong suốt một cuối tuần dài?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q4" value="A"> A. Rất thoải mái và tận hưởng thời gian để sạc lại năng lượng.</label>
                        <label class="option-label"><input type="radio" name="q4" value="B"> B. Hơi nhàm chán và muốn tìm việc gì đó để kết nối với bên ngoài.</label>
                        <label class="option-label"><input type="radio" name="q4" value="C"> C. Bình thường, tùy thuộc vào việc lúc đó tôi có dự án cá nhân nào đang làm dở không.</label>
                    </div>
                </div>

                <!-- Câu 5 -->
                <div class="question-card">
                    <div class="question-title">5. Khi xem một bộ phim buồn hoặc bi kịch, phản ứng cảm xúc của bạn ra sao?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q5" value="A"> A. Hiểu rõ cấu trúc nghệ thuật của phim nhưng giữ lý trí ổn định.</label>
                        <label class="option-label"><input type="radio" name="q5" value="B"> B. Dễ dàng đồng cảm sâu sắc, thậm chí rơi nước mắt theo nhân vật.</label>
                        <label class="option-label"><input type="radio" name="q5" value="C"> C. Suy ngẫm về triết lý cuộc sống ẩn sau câu chuyện của bộ phim.</label>
                    </div>
                </div>

                <!-- Câu 6 -->
                <div class="question-card">
                    <div class="question-title">6. Khi nhận được lời khen ngợi lớn về công việc của mình, bạn thường nghĩ gì trong đầu?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q6" value="A"> A. Cảm thấy xứng đáng với nỗ lực và sự đầu tư thời gian đã bỏ ra.</label>
                        <label class="option-label"><input type="radio" name="q6" value="B"> B. Lo lắng liệu lần sau mình có duy trì được phong độ này không (dấu hiệu Imposter Syndrome).</label>
                        <label class="option-label"><input type="radio" name="q6" value="C"> C. Cảm kích và chia sẻ thành công đó cho những người đồng hành cùng mình.</label>
                    </div>
                </div>

                <!-- Câu 7 -->
                <div class="question-card">
                    <div class="question-title">7. Khi gặp một người mới quen có vẻ ngoài lịch lãm và tự tin, ấn tượng ban đầu của bạn là gì?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q7" value="A"> A. Tỉnh táo nhận biết đây có thể là Hiệu ứng hào quang và cần thêm thời gian tìm hiểu.</label>
                        <label class="option-label"><input type="radio" name="q7" value="B"> B. Có thiện cảm ngay lập tức và tin tưởng họ là người tài giỏi.</label>
                        <label class="option-label"><input type="radio" name="q7" value="C"> C. Giữ khoảng cách vừa phải, quan sát thái độ ứng xử thực tế của họ.</label>
                    </div>
                </div>

                <!-- Câu 8 -->
                <div class="question-card">
                    <div class="question-title">8. Bạn đối phó với sự chỉ trích hoặc góp ý tiêu cực từ người khác bằng cách nào?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q8" value="A"> A. Lọc bỏ cảm xúc cá nhân để xem xét phần nào góp ý đúng sự thật.</label>
                        <label class="option-label"><input type="radio" name="q8" value="B"> B. Cảm thấy bị tổn thương hoặc tự vệ trước những lời chê bai.</label>
                        <label class="option-label"><input type="radio" name="q8" value="C"> C. Trao đổi thẳng thắn để làm rõ nguyên nhân vấn đề.</label>
                    </div>
                </div>

                <!-- Câu 9 -->
                <div class="question-card">
                    <div class="question-title">9. Khi hoàn thành một mục tiêu lớn, cảm giác đầu tiên xuất hiện trong bạn là gì?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q9" value="A"> A. Sự thỏa mãn ngắn ngủi và nhanh chóng lập kế hoạch cho mục tiêu tiếp theo.</label>
                        <label class="option-label"><input type="radio" name="q9" value="B"> B. Niềm tự hào lớn và mong muốn chia sẻ niềm vui với mọi người.</label>
                        <label class="option-label"><input type="radio" name="q9" value="C"> C. Cảm giác nhẹ nhõm vì đã vượt qua được áp lực căng thẳng.</label>
                    </div>
                </div>

                <!-- Câu 10 -->
                <div class="question-card">
                    <div class="question-title">10. Bạn quản lý công việc và lịch trình hằng ngày của mình theo phong cách nào?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q10" value="A"> A. Lên danh sách chi tiết (To-do list) và tuân thủ thời gian nghiêm ngặt.</label>
                        <label class="option-label"><input type="radio" name="q10" value="B"> B. Linh hoạt xử lý theo cảm hứng và mức độ ưu tiên tại thời điểm đó.</label>
                        <label class="option-label"><input type="radio" name="q10" value="C"> C. Kết hợp giữa khung lịch cố định và sự uyển chuyển khi có việc phát sinh.</label>
                    </div>
                </div>

                <!-- Câu 11 -->
                <div class="question-card">
                    <div class="question-title">11. Khi một sự cố bất ngờ làm hỏng kế hoạch đã định, phản ứng tâm lý của bạn là gì?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q11" value="A"> A. Bình tĩnh tìm phương án thay thế (Plan B) ngay lập tức.</label>
                        <label class="option-label"><input type="radio" name="q11" value="B"> B. Cảm thấy hụt hẫng, bực bội và mất một khoảng thời gian để lấy lại bình tĩnh.</label>
                        <label class="option-label"><input type="radio" name="q11" value="C"> C. Coi đó là bài học kinh nghiệm và tùy cơ ứng biến.</label>
                    </div>
                </div>

                <!-- Câu 12 -->
                <div class="question-card">
                    <div class="question-title">12. Bạn đánh giá thế nào về trực giác (giác quan thứ sáu) của bản thân trong đời sống?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q12" value="A"> A. Trực giác chỉ có giá trị tham khảo, mọi thứ phải dựa trên dữ liệu thực tế.</label>
                        <label class="option-label"><input type="radio" name="q12" value="B"> B. Trực giác của tôi cực kỳ nhạy bén và thường xuyên đúng.</label>
                        <label class="option-label"><input type="radio" name="q12" value="C"> C. Trực giác là sự đúc kết tiềm thức từ những kinh nghiệm đã qua.</label>
                    </div>
                </div>

                <!-- Câu 13 -->
                <div class="question-card">
                    <div class="question-title">13. Khi phải thuyết trình hoặc đứng trước đám đông, cảm giác của bạn lúc đó ra sao?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q13" value="A"> A. Hơi hồi hộp ban đầu nhưng kiểm soát tốt nội dung trình bày.</label>
                        <label class="option-label"><input type="radio" name="q13" value="B"> B. Căng thẳng rõ rệt, tim đập nhanh và lo lắng bị phán xét.</label>
                        <label class="option-label"><input type="radio" name="q13" value="C"> C. Hào hứng và tận hưởng cơ hội được chia sẻ kiến thức.</label>
                    </div>
                </div>

                <!-- Câu 14 -->
                <div class="question-card">
                    <div class="question-title">14. Nguồn động lực lớn nhất thúc đẩy bạn tiến lên trong cuộc sống là gì?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q14" value="A"> A. Khát khao chinh phục tri thức và phát triển bản thân hoàn thiện hơn.</label>
                        <label class="option-label"><input type="radio" name="q14" value="B"> B. Sự công nhận từ gia đình, bạn bè và xã hội.</label>
                        <label class="option-label"><input type="radio" name="q14" value="C"> C. Sự tự do tài chính và chất lượng cuộc sống bình an.</label>
                    </div>
                </div>

                <!-- Câu 15 -->
                <div class="question-card">
                    <div class="question-title">15. Khi xảy ra mâu thuẫn trong mối quan hệ thân thiết, bạn thường chọn cách xử lý nào?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q15" value="A"> A. Chờ cả hai hạ nhiệt rồi ngồi lại phân tích vấn đề một cách khách quan.</label>
                        <label class="option-label"><input type="radio" name="q15" value="B"> B. Chủ động làm hòa ngay vì không muốn duy trì sự căng thẳng.</label>
                        <label class="option-label"><input type="radio" name="q15" value="C"> C. Đôi khi giữ khoảng cách để tự suy ngẫm về vai trò của mình trong mâu thuẫn.</label>
                    </div>
                </div>

                <!-- Câu 16 -->
                <div class="question-card">
                    <div class="question-title">16. Bạn cảm nhận về những thay đổi lớn trong cuộc sống (chuyển môi trường, đổi công việc) như thế nào?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q16" value="A"> A. Xem đó là cơ hội tuyệt vời để học hỏi và thích nghi.</label>
                        <label class="option-label"><input type="radio" name="q16" value="B"> B. Cảm thấy bất an và thích sự ổn định quen thuộc hơn.</label>
                        <label class="option-label"><input type="radio" name="q16" value="C"> C. Cân nhắc kỹ lưỡng lợi hại trước khi bước vào vùng an toàn mới.</label>
                    </div>
                </div>

                <!-- Câu 17 -->
                <div class="question-card">
                    <div class="question-title">17. Khi mua sắm một món đồ giá trị lớn, yếu tố nào chi phối quyết định của bạn nhiều nhất?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q17" value="A"> A. Tính năng kỹ thuật, độ bền và giá trị sử dụng lâu dài.</label>
                        <label class="option-label"><input type="radio" name="q17" value="B"> B. Thiết kế thẩm mỹ, cảm xúc yêu thích ngay từ cái nhìn đầu tiên.</label>
                        <label class="option-label"><input type="radio" name="q17" value="C"> C. Đánh giá từ cộng đồng và review của những người đã sử dụng.</label>
                    </div>
                </div>

                <!-- Câu 18 -->
                <div class="question-card">
                    <div class="question-title">18. Mức độ kiên nhẫn của bạn khi theo đuổi một mục tiêu dài hạn (như học một kỹ năng mới) ra sao?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q18" value="A"> A. Rất cao, tôi chia nhỏ mục tiêu và kiên trì thực hiện mỗi ngày.</label>
                        <label class="option-label"><input type="radio" name="q18" value="B"> B. Dễ bị nản nếu không thấy kết quả tiến bộ nhanh chóng.</label>
                        <label class="option-label"><input type="radio" name="q18" value="C"> C. Kiên nhẫn khi tìm thấy niềm vui trong quá trình thực hiện.</label>
                    </div>
                </div>

                <!-- Câu 19 -->
                <div class="question-card">
                    <div class="question-title">19. Khi vô tình mắc một sai lầm ngớ ngẩn trước mặt người khác, bạn phản ứng thế nào?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q19" value="A"> A. Cười trừ, tự nhận lỗi vui vẻ và rút kinh nghiệm nhanh chóng.</label>
                        <label class="option-label"><input type="radio" name="q19" value="B"> B. Cảm thấy ngại ngùng, cứ suy nghĩ mãi về lỗi lầm đó suốt nhiều ngày.</label>
                        <label class="option-label"><input type="radio" name="q19" value="C"> C. Phân tích nguyên nhân tại sao mình lại bất cẩn để tránh lặp lại.</label>
                    </div>
                </div>

                <!-- Câu 20 -->
                <div class="question-card">
                    <div class="question-title">20. Theo bạn, yếu tố quan trọng nhất để duy trì một trạng thái tinh thần lành mạnh là gì?</div>
                    <div class="options-list">
                        <label class="option-label"><input type="radio" name="q20" value="A"> A. Sự cân bằng giữa tư duy logic, công việc và nghỉ ngơi khoa học.</label>
                        <label class="option-label"><input type="radio" name="q20" value="B"> B. Sự thấu hiểu cảm xúc bản thân và tình yêu thương từ các mối quan hệ.</label>
                        <label class="option-label"><input type="radio" name="q20" value="C"> C. Khả năng tự chủ và chấp nhận những bất hoàn hảo của cuộc sống.</label>
                    </div>
                </div>

                <button type="button" class="submit-btn" onclick="calculateQuizResults()">🔍 Xem Báo Cáo Phân Tích Tâm Lý Của Bạn</button>
            </form>

            <div class="quiz-result-box" id="quizResultBox">
                <h3>📊 Kết Quả Phân Tích Tâm Lý Tổng Hợp</h3>
                <p id="resultText"></p>
            </div>
        </div>

        <footer>
            <p>&copy; 2026 Dự Án Tâm Lý Học | Phát triển bởi <strong>Lê Bá Vũ</strong></p>
        </footer>
    </div>

    <script>
        /* Hiệu ứng đốm sáng Spotlight Card */
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

        /* Hàm xử lý tính toán kết quả 20 câu hỏi trắc nghiệm */
        function calculateQuizResults() {
            const form = document.getElementById('psychQuiz');
            const formData = new FormData(form);
            
            let countA = 0;
            let countB = 0;
            let countC = 0;
            let answeredCount = 0;

            for (let [key, value] of formData.entries()) {
                answeredCount++;
                if (value === 'A') countA++;
                else if (value === 'B') countB++;
                else if (value === 'C') countC++;
            }

            const resultBox = document.getElementById('quizResultBox');
            const resultText = document.getElementById('resultText');

            if (answeredCount < 10) {
                alert('Vui lòng trả lời ít nhất 10 câu hỏi để hệ thống có đủ dữ liệu phân tích chính xác!');
                return;
            }

            resultBox.style.display = 'block';
            resultBox.scrollIntoView({ behavior: 'smooth' });

            let profileType = "";
            let description = "";

            if (countA >= countB && countA >= countC) {
                profileType = "🧠 Nhà Tư Duy Phân Tích & Logic (Analytic Thinker)";
                description = `Bạn có tổng số lựa chọn thiên về tư duy lý trí (${countA}/20 câu). Bạn sở hữu thế giới quan khách quan, có khả năng giải quyết vấn đề dựa trên dữ liệu thực tế, tư duy logic vững vàng và luôn giữ được cái đầu lạnh trước các biến cố căng thẳng.`;
            } else if (countB >= countA && countB >= countC) {
                profileType = "💖 Người Thấu Cảm & Trực Giác Cảm Xúc (Empathic & Intuitive)";
                description = `Bạn có tổng số lựa chọn thiên về cảm xúc và trực giác (${countB}/20 câu). Bạn là người cực kỳ nhạy bén, giàu lòng trắc ẩn, dễ đồng cảm sâu sắc với người xung quanh và có đời sống tinh thần vô cùng phong phú, tinh tế.`;
            } else {
                profileType = "⚖️ Nhà Thực Tế Uyển Chuyển & Cân Bằng (Pragmatic Balancer)";
                description = `Bạn có tổng số lựa chọn thiên về sự thích ứng linh hoạt (${countC}/20 câu). Bạn biết cách dung hòa giữa lý trí và cảm xúc, giỏi ứng biến trong mọi hoàn cảnh xã hội và luôn tìm kiếm sự bình an, hài hòa trong cuộc sống.`;
            }

            resultText.innerHTML = `<strong>Chân dung tâm lý chủ đạo của bạn:</strong> <span style="color: #00ffcc; font-size: 1.15rem;">${profileType}</span><br><br>${description}<br><br><em>Cảm ơn bạn đã hoàn thành bài trắc nghiệm nghiên cứu tâm lý học do Lê Bá Vũ biên soạn!</em>`;
        }
    </script>

</body>
</html>
"""


@app.route("/")
def home():
  return render_template_string(HTML_TEMPLATE)


if __name__ == "__main__":
  app.run(debug=True, port=5000)