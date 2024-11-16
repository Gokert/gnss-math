FROM python:latest

COPY . .

RUN pip install -r requirement.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]