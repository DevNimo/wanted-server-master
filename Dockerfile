FROM python:3.10.2
LABEL email="poi2003008@naver.com"
LABEL name="LEE SANG MIN"

ENV FLASK_APP run.py

ADD . /

RUN pip install -r requirments.txt

ENTRYPOINT ["python", "run.py"]