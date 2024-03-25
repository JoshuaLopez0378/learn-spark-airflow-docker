FROM apache/airflow:2.7.1-python3.11

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk
    # && apt-get clean

# Installed after some tests, research more if libc6-i386 needed
# RUN apt-get install libc6-i386


# Set JAVA_HOME environment variable, reminder: in reference it was arm64, not amd64 but current image and install
# redirects amd64, double check java env with: update-alternatives --list java after run
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

USER airflow

RUN pip3 install apache-airflow apache-airflow-providers-apache-spark pyspark
RUN pip3 install openpyxl
# RUN pip3 install xlrd