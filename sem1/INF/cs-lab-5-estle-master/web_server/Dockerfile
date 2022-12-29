FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y apache2

RUN echo -n > /var/www/html/index.html
RUN echo "<html> \n\
<head>	\n\
  <title> I love Docker! </title> \n\
</head> \n\
<body> \n\
  <p> Hello world! I'm Ilia Abdulov and I study at ITMO University! </p> \n\
</body> \n\
</html>" > /var/www/html/index.html

EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]

RUN echo "ServerName localhost" >> /etc/apache2/ports.conf
