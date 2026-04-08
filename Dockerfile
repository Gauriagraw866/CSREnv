FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install openenv-core>=0.2.0

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
