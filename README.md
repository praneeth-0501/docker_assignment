# Docker Task
1. Initially, DAG is created with a schedule of timedelta days equal to 1.
2. Three tasks are created which creates, inserts and run a query in postgres.
3. The first task was named createtable_task which creates a table in postgres.
4. The second task was named insert_rows_task which insert the rows in above created table.
5. The third task was named query_task which runs a query on table. This task validates the entry in postgres.
6. Now start the airflow containers but using docker compose command and docker-compose.yaml file.
```
docker-compose up -d
```
7. Open the web-UI. In connections create a postgres connection as shown below.
<img width="1419" alt="Screenshot 2023-06-13 at 11 57 55 AM" src="https://github.com/praneeth-0501/docker_assignment/assets/123532043/6eb65ce4-9561-4b21-947f-1bc618ee783d">
8. Once connection is created trigger the above created dag.
<img width="965" alt="Screenshot 2023-06-13 at 11 58 23 AM" src="https://github.com/praneeth-0501/docker_assignment/assets/123532043/58ddf97f-a1d8-4ce6-80ae-92533e18066e">

9. You can validate the entry by checking in postgres container also.

<img width="461" alt="Screenshot 2023-06-13 at 12 01 11 PM" src="https://github.com/praneeth-0501/docker_assignment/assets/123532043/cd4c5407-d329-4bfe-acc1-75278acc082c">

# Kubernetes task
1. Initially create a yaml file for deployment of postgres container. Here, postgres pod is created with 1 replica and considering latest postgres image.
2. By using kubectl command deploy the postgres pod.
```
kubectl apply -f postgresdb-deploy.yaml 
```
3. For connecting postgres and airflow install the dependencies in postgres container. Run below commands to open postgres container terminal.
```
minikube ssh
docker ps
docker exec -it <container> bin/bash
```
```
apt-get -y update
apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
tar -xf Python-3.7.12.tgz
cd /Python-3.7.12
./configure --enable-optimizations
make -j $(nproc)
make altinstall
apt-get install libpq-dev
pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@localhost:5432/airflow
airflow db init
airflow users create -u airflow -p airflow -f praneeth -l praneeth -e praneeth@gmail.com -r Admin
```
