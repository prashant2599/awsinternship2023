FROM python:3.8
RUN apt-get update && apt-get install -y espeak 
RUN pip install pyttsx3  
COPY textspeech.py /speech/ 
WORKDIR /speech 
CMD ["python", "textspeech.py"]
