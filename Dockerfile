FROM python:3.12-slim 
COPY . /app 
WORKDIR /app
EXPOSE 8001
RUN apt-get update 
RUN chmod +x /app/entrypoint.sh
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "/app/entrypoint.sh" ]