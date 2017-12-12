# appscheck

A project developed with an intention to check the status of running application/api services in your local system or online services

# Python Version

Python 2.7.13

# How to run

You can also check this pretty guide at [https://hygull.github.io/appscheck/](https://hygull.github.io/appscheck/) **OR**
look at the following 

* Create any directory somewhere in your system and cd inside that

* git clone https://github.com/hygull/appscheck.git

* cd appscheck

```
Specify your commands to check the status of your applications/services in the config.json

Provide proper command to open **app_status.html** file. Do not specify the file path just only 
change should be in the command preferred to open file 

eg. 
	open/xdg-open

Provide the name of your environment, eg. RLQA-01 etc. that will be reflected in the dynamically generated HTML template.
```

* python main.py


# Output 

12 Dec 2017, Tue

```
You will see 1 file named app_status.html that will open automatically in your default browser(if config is OK).

This HTML will show the status of your apps/services saying UP/DOWN if config is properly construted.
```

```
rle509@rle509:~/Ubentry/RelevanceLab/Coding/Python/appscheck$ python main.py 

*********************************APIS*********************************************

|--------------------------------------------------------------------------------|
Workflow Engine
|(1) Hitting =>http://localhost:6767/api/v1/workflow                             |
|DOWN                                                                            |
|--------------------------------------------------------------------------------|
Notification Engine
|(2) Hitting =>http://localhost:3002/api/v1/notify                               |
|DOWN                                                                            |
|--------------------------------------------------------------------------------|
Magento
|(3) Hitting =>http://13.89.188.246/genesisV2/admin                              |
|UP, STATUS CODE => 200                                                          |
|--------------------------------------------------------------------------------|
Genesis
|(4) Hitting =>http://localhost:3000                                             |
|DOWN                                                                            |
|--------------------------------------------------------------------------------|
Bot Engine
|(5) Hitting =>http://localhost:2687                                             |
|DOWN                                                                            |
|--------------------------------------------------------------------------------|

**********************************SERVICES******************************************
|(1) Hitting =>service mongodb status                                            |
[u'service', u'mongodb', u'status']
● mongodb.service - High-performance, schema-free document-oriented database
   Loaded: loaded (/etc/systemd/system/mongodb.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2017-12-11 19:14:42 IST; 16h ago
 Main PID: 954 (mongod)
    Tasks: 19
   Memory: 84.2M
      CPU: 40.873s
   CGroup: /system.slice/mongodb.service
           └─954 /usr/bin/mongod --quiet --config /etc/mongod.conf

Dec 11 19:14:42 rle509 systemd[1]: Started High-performance, schema-free document-oriented database.
exit_code 0
|UP, STATUS CODE => 200                                                          |
|--------------------------------------------------------------------------------|
|(2) Hitting =>service docker status                                             |
[u'service', u'docker', u'status']
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2017-12-12 10:17:44 IST; 1h 52min ago
     Docs: https://docs.docker.com
 Main PID: 948 (dockerd)
    Tasks: 21
   Memory: 59.2M
      CPU: 21.731s
   CGroup: /system.slice/docker.service
           ├─ 948 /usr/bin/dockerd -H fd://
           └─1423 containerd -l unix:///var/run/docker/libcontainerd/docker-containerd.sock --metrics-interval=0 --st

Dec 12 10:17:43 rle509 dockerd[948]: time="2017-12-12T10:17:43.424419997+05:30" level=info msg="Firewalld running: fa
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.239410121+05:30" level=info msg="Default bridge (docke
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.472133697+05:30" level=info msg="Loading containers: d
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.548094694+05:30" level=warning msg="Couldn't run aupli
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.913348806+05:30" level=warning msg="failed to retrieve
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.934174062+05:30" level=warning msg="failed to retrieve
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.957431323+05:30" level=info msg="Daemon has completed 
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.957484085+05:30" level=info msg="Docker daemon" commit
Dec 12 10:17:44 rle509 dockerd[948]: time="2017-12-12T10:17:44.965980918+05:30" level=info msg="API listen on /var/ru
Dec 12 10:17:44 rle509 systemd[1]: Started Docker Application Container Engine.
exit_code 0
|UP, STATUS CODE => 200                                                          |
|--------------------------------------------------------------------------------|
|(3) Hitting =>service mysql status                                              |
[u'service', u'mysql', u'status']
● mysql.service - MySQL Community Server
   Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2017-12-12 10:17:44 IST; 1h 52min ago
  Process: 973 ExecStartPost=/usr/share/mysql/mysql-systemd-start post (code=exited, status=0/SUCCESS)
  Process: 953 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exited, status=0/SUCCESS)
 Main PID: 972 (mysqld)
    Tasks: 28
   Memory: 202.8M
      CPU: 4.234s
   CGroup: /system.slice/mysql.service
           └─972 /usr/sbin/mysqld

Dec 11 19:14:42 rle509 systemd[1]: Starting MySQL Community Server...
Dec 12 10:17:44 rle509 systemd[1]: Started MySQL Community Server.
exit_code 0
|UP, STATUS CODE => 200                                                          |
|--------------------------------------------------------------------------------|
|(4) Hitting =>service nginx status                                              |
[u'service', u'nginx', u'status']
● nginx.service
   Loaded: not-found (Reason: No such file or directory)
   Active: inactive (dead)
exit_code 3
|DOWN, STATUS CODE => 200                                                        |
|--------------------------------------------------------------------------------|
|(5) Hitting =>service apache2 status                                            |
[u'service', u'apache2', u'status']
● apache2.service - LSB: Apache2 web server
   Loaded: loaded (/etc/init.d/apache2; bad; vendor preset: enabled)
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: active (running) since Mon 2017-12-11 19:14:53 IST; 16h ago
     Docs: man:systemd-sysv-generator(8)
  Process: 1150 ExecStart=/etc/init.d/apache2 start (code=exited, status=0/SUCCESS)
    Tasks: 6
   Memory: 21.9M
      CPU: 344ms
   CGroup: /system.slice/apache2.service
           ├─1323 /usr/sbin/apache2 -k start
           ├─1387 /usr/sbin/apache2 -k start
           ├─1388 /usr/sbin/apache2 -k start
           ├─1389 /usr/sbin/apache2 -k start
           ├─1390 /usr/sbin/apache2 -k start
           └─1391 /usr/sbin/apache2 -k start

Dec 11 19:14:48 rle509 systemd[1]: Starting LSB: Apache2 web server...
Dec 11 19:14:48 rle509 apache2[1150]:  * Starting Apache httpd web server apache2
Dec 11 19:14:53 rle509 apache2[1150]:  *
Dec 11 19:14:53 rle509 systemd[1]: Started LSB: Apache2 web server.
exit_code 0
|UP, STATUS CODE => 200                                                          |
|--------------------------------------------------------------------------------|
Trying to send mail to =>  rishikesh.agrawani@relevancelab.com
Mail successfully sent
Trying to send mail to =>  rishidev-rel@crymail2.com
Mail successfully sent
Opening HTML
```

Thanks