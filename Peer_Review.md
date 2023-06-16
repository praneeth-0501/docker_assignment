# Rahul Review

## Docker Task
1. In this task steps followed by rahul is very much similar to my steps. But he created only 2 tasks for validating entry entry he checked in postgres container.
2. Instead of that we can validate the entry by creating the task. Task should run any select query on the table he created. If this task runs well then entry is validated.
#### Describing steps
1. First, he created a dag with two tasks. Then by using docker compose command he started airfow container. 
2. From webui he created a connection with postgres.
3. Then he trigger the dag.

## Kubernetes steps
1. He created a custom docker image which contains postgres image and all the installation commands required to connect with airflow. This step is little bit different with my process.
2. By using kubectl command he deployes the postgres pod.
3. Then he started postgres service.
4. Then he deployed airflow pod and started airflow service.
5. Now he created dag in airflow container.
6. Triggered the dag in webui.
