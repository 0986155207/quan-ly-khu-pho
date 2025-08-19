import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings
import os

def get_all_sheets_data():
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
    ]

    CREDS_FILE = os.path.join(settings.BASE_DIR, 'credentials.json')

    try:
        creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
        client = gspread.authorize(creds)
        spreadsheet = client.open("chatbot25")
    except Exception as e:
        print(f"Lỗi kết nối hoặc xác thực: {e}")
        return None

    all_data = []
    # Lặp qua tất cả các sheet có trong file
    for worksheet in spreadsheet.worksheets():
        # Lấy tất cả giá trị dưới dạng danh sách của các danh sách (list of lists)
        list_of_lists = worksheet.get_all_values()

        # Bỏ qua nếu sheet có ít hơn 2 dòng (chỉ có tiêu đề hoặc trống)
        if len(list_of_lists) < 2:
            continue

        # Lấy tên các cột tiêu đề từ dòng đầu tiên
        headers = [header.strip().lower() for header in list_of_lists[0]]

        # Xác định vị trí cột 'câu hỏi' và 'câu trả lời' (linh hoạt với nhiều tên gọi)
        question_col_index = -1
        answer_col_index = -1

        possible_question_headers = ['câu hỏi', 'cauhoi', 'cauhoividu']
        possible_answer_headers = ['câu trả lời', 'traloi', 'traloichitiet']

        for i, header in enumerate(headers):
            if header in possible_question_headers:
                question_col_index = i
            if header in possible_answer_headers:
                answer_col_index = i

        # Nếu tìm thấy cả hai cột tiêu đề cần thiết
        if question_col_index != -1 and answer_col_index != -1:
            # Lặp qua các dòng dữ liệu thật (bỏ qua dòng tiêu đề)
            for row in list_of_lists[1:]:
                if len(row) > max(question_col_index, answer_col_index):
                    question = row[question_col_index]
                    answer = row[answer_col_index]

                    # Chỉ thêm vào nếu cả câu hỏi và trả lời đều có nội dung
                    if question and answer:
                        record = {
                            'câu hỏi': question,
                            'câu trả lời': answer
                        }
                        all_data.append(record)

    return all_data