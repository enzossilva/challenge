## Python Active Scan

### Getting Started

#### This documentation is intended to serve how you can using the aplicattion to perform a security test.

### Introducing ZAP

#### First you need install the ZAP, select the appropriate installer from the https://www.zaproxy.org/download/ .

#### With Zap open, go to the "TOOLS" in menu and select "Manual Request Editor".<br> After that it will appaer the Menu of the Requisition and Response.

#### In the Request tab, you will see an example of an HTTP request. Replace the HTTP request details with your URL and related information.

### Example:

GET http://www.any_domain_name.org/path HTTP/1.1 <br>
host: www.any_domain_name.org <br>
user-agent: Mozilla/5.0 (Windows NT 10.0; rv:125.0) Gecko/20100101 Firefox/125.0<br>
pragma: no-cache <br>
cache-control: no-cache

### Change the method HTTP and the url that you would like Scan.

HEAD http://www.yourURL.com HTTP/1.1 <br>
host: "www.yourURL.com" <br>
user-agent: Mozilla/5.0 (Windows NT 10.0; rv:125.0) Gecko/20100101 Firefox/125.0 <br>
pragma: no-cache <br>
cache-control: no-cache <br>

#### After that you change the URL, click in Send. <br> And now you will see that response of the your Requisition. But it is not important in this moment. Now you can close the tab.

#### In the left side of the page click on dropdown Site to check the URL that you chose and make sure that is correct.

### Important

#### You can add as many URLs as you want to be stored and scan them in the future.

### Lets go use the your text compiler(VScode, Sublime...)

## Create an environment

#### macOS/Linux

#### In the terminal execute,<br> $ python3 -m venv .venv

#### Windows

` py -3 -m venv .venv`

### Activate the environment

#### macOS/Linux

` ./venv/bin/activate`

#### Windows

`  ./venv/Scripts/activate`

##### With Environment activate we need install the library to start the project.

## Library Instalation

### Install Flask

` pip install Flask`

#### from Flask lets call "request" and "url_for"

##### Requests allows you to send HTTP/1.1 requests extremely easily.

#### url_for is used to obtain a link (url) to a specific function with a dynamic form.

##### Flask, request and url_for now is installed. and the next step is running the aplication.

## Structure

### With the all files of the project installed, lets understand what they are.

#### The folder "templates" are the file that compose the HTML, in this case index.html is where the user will put the URL to scan, and list_scan.html where the scan results will be returned.

#### "**init**.py" is used to define and start the instance of our application.

#### "models.py" where you will store all the functions necessary for the application to work.

#### "view.py" serves to see what files and information will be displayed.

#### "controller.py" connects the data and where this data will be shown, in this case are models.py(data) and view.py(visualization).

#### "run.py" The routes to run the application is here. Where you define what name of the route and what Method HTTP that route will receive and be executed in the web.

## Run

### Open the run.py

#### In the terminal execute:

` python3 run.py`

### Open with Docker Compose

#### in the terminal execute:

`docker-compose up`

#### Now the application must be online and running on http://127.0.0.1:5000

#### To acess, press CTRL + click, and will redirect to web.

### Time to put the url that you would like Scan.

#### !Remember the url must be the same that you put in the Zap!

#### After you put the url in input, click in SEND to realize Active Scan.

#### Now you can see what alerts there are and what types of vulnerabilities they are. If you don't get any feedback, that site doesn't have vulnerabilities. This is possible to see what
