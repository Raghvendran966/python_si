FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["profit_loss.py","avg.py]
ENTRYPOINT ["python3"]
