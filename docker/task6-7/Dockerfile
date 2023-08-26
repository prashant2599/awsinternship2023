FROM centos:7

RUN yum install -y httpd net-tools

COPY index.html /var/www/html/

CMD /usr/sbin/httpd -DFOREGROUND
