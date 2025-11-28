FROM python:3

WORKDIR /app
COPY . .

RUN pip install uv 
RUN uv venv
RUN pip install groq
RUN pip install -r requirements.txt

CMD ["python", "main.py"]