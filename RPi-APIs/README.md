# Independet Study
IoT research for wireless sensor networks. 

Setup: RPi as Master node for data collection from slaves. 

Motivation: Creating APIs for integration of sensors data in network. 

Creating server of Raspberry PI and developing APIs with python-flask. 

### Set up python-flask on Raspberry pi 
1. Installing pip
```bash
pi@raspberrypi ~ $ sudo apt-get install python-pip
```
2. Installing Flask 
```bash
pi@raspberrypi ~ $ sudo pip install flask
```

### Run Server
```bash 
pi@raspberrypi ~ $ sudo python helloworld.py
 * Running on http://0.0.0.0:80/ 
 * Restarting with reloader
 
```
Server will start at ip of host (you can find that by __ifconfig__)

### APIs

__Projects__ : dictonary 
``` json 
"projects": [
    {
      "date": "04-28-2017", 
      "description": "Hello World", 
      "id": 1, 
      "time": "Morning", 
      "title": "test"
    }, 
    {
      "date": "4-29-2017", 
      "description": "test GET APIs", 
      "id": 2, 
      "time": "12:00 am", 
      "title": "GET"
    }
    ]
```

 #### GET
 ``` curl
 mark42@starkindustries ~ $ curl -i http://localhost:port/test/api/v1.0/dt
 Out:
 HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 310
Server: Werkzeug/0.9.6 Python/2.7.9
Date: Sat, 29 Apr 2017 04:15:50 GMT

{
  "projects": [
    {
      "date": "04-28-2017", 
      "description": "Hello World", 
      "id": 1, 
      "time": "Morning", 
      "title": "test"
    }, 
    {
      "date": "4-29-2017", 
      "description": "test GET APIs", 
      "id": 2, 
      "time": "12:00 am", 
      "title": "GET"
    }
  ]
}% 

mark42@starkindustries ~ $ curl -i http://localhost:port/test/api/v1.0/dt/1 (get by id number)
Out :
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 142
Server: Werkzeug/0.9.6 Python/2.7.9
Date: Sat, 29 Apr 2017 04:18:27 GMT

{
  "project": {
    "date": "04-28-2017", 
    "description": "Hello World", 
    "id": 1, 
    "time": "Morning", 
    "title": "test"
  }
}% 
```

#### POST
``` curl
mark42@starkindustries ~ $ curl -i -H "Content-Type: application/json" -X POST -d '{"title":"POST API","description":"Add entry in dict"}' http://localhost:port/test/api/v1.0/dt
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 136
Server: Werkzeug/0.9.6 Python/2.7.9
Date: Sat, 29 Apr 2017 04:20:06 GMT

{
  "project": {
    "date": "2017-04-29", 
    "description": "Add entry in dict", 
    "id": 3, 
    "time": "04:15:43", 
    "title": "POST API"
  }
}% 
```

#### PUT
``` curl
mark42@starkindustries ~ $ curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Project 3"}' http://localhost:port/test/api/v1.0/dt/3
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 137
Server: Werkzeug/0.9.6 Python/2.7.9
Date: Sat, 29 Apr 2017 04:25:08 GMT

{
  "project": {
    "date": "2017-04-29", 
    "description": "Add entry in dict", 
    "id": 3, 
    "time": "04:15:43", 
    "title": "Project 3"
  }
}% 
```
#### DELETE
```curl
mark42@starkindustries ~ $ curl -i -H "Content-Type: application/json" -X DELETE http://localhost:port/test/api/v1.0/dt/3
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 20
Server: Werkzeug/0.9.6 Python/2.7.9
Date: Sat, 29 Apr 2017 04:27:38 GMT

{
  "result": true
}% 
```

