# 사용할 BASE IMAGE
FROM python:3.8.8

# 현재 디렉토리(.)의 내용을 컨테이너 내의 /app 폴더로 복사
COPY . /app

# 작업 위치, /app 폴더에 파일이 있으므로 작업위치를 /app으로 설정
WORKDIR /app

# 이미지의 프로젝트에 필요한 패키지 및 shell 명령어 실행
# 패키지가 많을 경우 requirements.txt 이용
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install --no-cache-dir -r requirements.txt

#컨테이너 포트 번호
EXPOSE 5000

# CMD를 이용해 app.py run
CMD ["python3", "./app.py"]
