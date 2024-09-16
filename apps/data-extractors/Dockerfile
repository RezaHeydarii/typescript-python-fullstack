FROM python:3.12-slim


RUN apt update && apt -y install cron vim
WORKDIR /cronjob

COPY crontab /etc/cron.d/crontab
COPY . /cronjob/.

RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["cron", "-f"]