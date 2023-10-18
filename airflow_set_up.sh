sudo apt update

sudo apt upgrade

sudo apt install python3 python3-pip virtualenv python3-venv

#install mysql + create database + create user + grant all privilege to this user 

mkdir airflow_project

cd airflow_project

python3 -m venv airflow_env

source airflow_env/bin/activate

sudo pip install apache-airflow

airflow db init

mkdir /home/zakariae/airflow/dags

pip install mysqlclient

nano /home/zakariae/airflow/airflow.cfg

# sql_alchemy_conn = mysql://username:password@localhost:3306/database

# should already have mysql with database and user(with password)

airflow db init

airflow users create --username admin --firstname zakariae --lastname khd --role Admin --email factorielle0122333333@gmail.com



airflow webserver --port 8080 # new Terminal

airflow scheduler # new terminal







