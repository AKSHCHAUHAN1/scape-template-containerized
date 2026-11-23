FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=3000
WORKDIR /app
COPY app.py ./app.py
RUN useradd --system --uid 10001 appuser
USER 10001
EXPOSE 3000
CMD ["python", "app.py"]
