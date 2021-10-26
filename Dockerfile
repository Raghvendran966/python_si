FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["d2.py,area.py"]
ENTRYPOINT ["python3"]
