From python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["tail","-f","/dev/null"]

CMD ["python", "app.py"]