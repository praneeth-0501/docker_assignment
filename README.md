# docker_assignment
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
