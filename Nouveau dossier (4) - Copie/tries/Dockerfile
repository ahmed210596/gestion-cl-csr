FROM docker.elastic.co/beats/filebeat:8.8.2
USER root
COPY ./filebeat.yml /usr/share/filebeat/filebeat.yml
#RUN chmod 777 /usr/share/filebeat/filebeat.yml
USER filebeat
CMD filebeat -e -strict.perms=false


 


# Other Dockerfile instructions

