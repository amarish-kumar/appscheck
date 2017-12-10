# appscheck

A project developed with an intention to check the status of running application/api services in your local system or online services

# How to run

You can also check this pretty guide at [https://hygull.github.io/appscheck/](https://hygull.github.io/appscheck/) OR
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


```
You will see 1 file named app_status.html that will open automatically in your default browser(if config is OK).

This HTML will show the status of your apps/services saying UP/DOWN if config is properly construted.
```
