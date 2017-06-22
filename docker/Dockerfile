FROM nathonfowlie/centos-jre
VOLUME /tmp
ADD test-0.1.0.jar app.jar
ADD libmsc64.so /lib64/libmsc64.so
ADD lame lame
#RUN sh -c 'touch /tmp/lame'
RUN chmod 777 /tmp/lame
#RUN export LD_LIBRARY_PATH= /tmp/lib
ENV JAVA_OPTS=""
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./uexitrandom -jar /tmp/app.jar" ]
