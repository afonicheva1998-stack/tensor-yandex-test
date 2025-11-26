FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ ./src/
ENTRYPOINT ["python", "-m", "pytest", "src/tests/", "-v", "--html=report.html", "--self-contained-html"]