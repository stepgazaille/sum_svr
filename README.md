# Summarizer Web API
## Description
A Web API that accepts texts as input and returns summaries.

## Requirements
Main requirement:
- Python 3.6

A more detailed list of requirements can be found in [requirements.txt](requirements.txt).

## Setup
The quickest way to get up-and-running is to install [Docker](https://www.docker.com/) and use the provided docker image:
```
# Pull docker image:
docker pull stepgazaille/sum_svr

# Or, build docker image:
docker build -t stepgazaille/sum_svr .
```
Use the following commands if you must run the server locally:
```
pip install -r requirements.txt
python -m nltk.downloader punkt
```

## Installation
Execute the following command to start the summarizing server in docker container:
```
docker run -d -p 5000:5000 stepgazaille/sum_svr
```
You can verify that the server is running by executing the ```docker ps``` command.

To stop the server, first identify its contrainer ID using the ```docker ps``` command and then kill the container:
```
$ docker kill [CONTAINER ID]
```

Alternatively, execute the following commands start the server locally:
```
python app.py
```


## Test
Requests can be sent to the server using tools such as [Postman](https://www.getpostman.com/).
Request exemple (server running locally):
```
POST /lead3 HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
{
	"doc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
}
```


## Cleanup
To remove the sum_svr Docker image, first identify its image ID using the ```docker image ls``` command and then remove the image using the following command (make sure the container is not running first):
```
$ docker image rm [IMAGE ID] -f
```