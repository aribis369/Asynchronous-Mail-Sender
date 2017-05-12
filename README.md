# Asynchronous-Mail-Sender
The program serves the need to have a asynchronous mail sender using flask, smtplib and celery.
Celery is used to execute the program independently outside the flask app without blocking the flask app until 
entire process for a user is finished. This makes our app much faster and prevents blockage of stream.
## Language Used
```sh
python3
```
## Dependencies
* flask
* redis/rabbitmq
* flask
* smtplib
## Installion
installing flask, celery
```sh
pip3 install flask
pip3 install celery
```
### for broker rabbitmq or redis cab be used
rabbitmq installation
```sh
sudo apt-get install rabbitmq-server
```
OR 
redis installation
```sh
pip3 install redis
```
## Usage
1. setup all dependencies
2. put **a.py** and **async.py** in a directory
3. open a terminal in that diretory and write the command: ``` celery -A a worker --loglevel=info ```
   now we can see the processes queued in celery.
4. now we have to run **async.py** .for that we write the command: ``` python3 async.py ```
5. now we have the **async.py** running on **localhost**
6. now we connect our **localhost** to the script in the html file of **contact us page**
7. if app deployed somewhere then connect the script in the contact us page with the domain name where the app is deployed.

### Improvements always open
Always feel free to contribute to this project
