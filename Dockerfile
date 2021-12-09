FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install streamlit

CMD ["streamlit", "run", "./main.py"]