
#Base Image to use
FROM python:3.10.12-slim

RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential

#Expose port 8080
EXPOSE 8080

#Copy Requirements.txt file into app directory
COPY requirements.txt app/requirements.txt

#install all requirements in requirements.txt
RUN pip install -r app/requirements.txt

#Copy all files in current directory into app directory
COPY . /app

#Change Working Directory to app directory
WORKDIR /app

#Run the application on port 8080
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableWebsocketCompression=false", "--server.enableXsrfProtection=false", "--server.headless=true"]
