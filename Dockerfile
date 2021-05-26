FROM python:3.7-slim
COPY . /app
WORKDIR /app

RUN apt-get update && \
apt install -y ./chrome_driver/linux/google-chrome-stable_current_amd64.deb && \
apt-get install -y xvfb libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1

# set display port to avoid crash
ENV DISPLAY=:99

RUN pip install -U --no-cache-dir pip && \
pip install -U --no-cache-dir -r requirements.txt

EXPOSE 5001
CMD [ "gunicorn", "-b 0.0.0.0:5001", "-w 2", "-t 150", "wsgi:app"]
