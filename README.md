# crud-application-using-flask-and-mysql
A simple CRUD application using Flask and MySQL

### Built With

* Python
* Python Libraries: flask and pymysql
* MySQL
* AdminLTE 2

### Running server.py
```
python3.5 server.py

```
Open http://your-host-ip-address:8181 in browser.

### Running on Docker

Pull image:
```
docker pull muhammadhanif/crud-flask-mysql

```
Run:
```
docker run -it --name crud-flask-mysql -p 80:80 muhammadhanif/crud-flask-mysql
```
Open http://your-host-ip-address in browser.

Or you can execute the following [docker-compose](https://raw.githubusercontent.com/muhammadhanif/crud-application-using-flask-and-mysql/master/docker-compose/docker-compose.yaml):

```
version: '2'
services:

  phonebook-mysql:
    container_name: phonebook-mysql
    image: muhammadhanif/phonebook:mysql

  phonebook-flask:
    container_name: phonebook-flask
    image: muhammadhanif/phonebook:flask
    ports:
      - "8181:8181"
    working_dir: /hnf/source_code
    command: python server.py
    links: 
    - phonebook-mysql
```

&nbsp;
After executing, you will have 2 running cointainers on your Docker host: phonebook-flask and phonebook-mysql. For accessing the web application, open your browser and go to http://your-docker-host-ip-address:8181
