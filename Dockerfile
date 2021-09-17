FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["d1.py",]
ENTRYPOINT ["python3"]
