import os
from datetime import datetime

# 1. 설정: 관리할 폴더 이름
FOLDER_NAME = "prompt-log"

def setup_folder():
    """폴더가 없으면 생성"""
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print(f"✅ 폴더 생성 완료: {FOLDER_NAME}")

def create_new_prompt(file_format="md", version="v1.0"):
    """새로운 프롬프트 기록 파일을 생성"""
    date_str = datetime.now().strftime("%y%m%d")
    file_name = f"{date_str}_{version}_Upgrade_Log.{file_format}"
    file_path = os.path.join(FOLDER_NAME, file_name)
    
    if os.path.exists(file_path):
        print(f"⚠️ 이미 동일한 파일이 존재: {file_name}")
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            if file_format == "md":
                f.write(f"# Prompt Upgrade Log ({date_str})\n\n## Version: {version}\n\n### 변경 사항\n- \n\n### 프롬프트 내용\n```\n내용을 입력하세요\n```")
        print(f"📝 새 파일 생성: {file_path}")

if __name__ == "__main__":
    setup_folder()
    # 실행 시 새로운 마크다운 파일 생성 (원하는 형식으로 변경 가능)
    create_new_prompt(file_format="md")