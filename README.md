### ShortLink

ShortLink is a URL shortening service where you enter a URL such as https://codesubmit.io/library/react and it returns a short URL such as http://short.est/GeAi9K.




## Installation

step 1 install docker from [ Here](https://docs.docker.com/get-docker/) 

step 2 clone the repository 

step 3 Inside your terminal excute the following command
```bash
sudo docker build -t tiny_docker:latest . 
```
this will create a docker image with the name tiny_docker 

step 4 run the built image 
```bash
sudo docker run -p 5000:5000 -d tiny_docker:latest
```
step5 go to your browser and run  http://127.0.0.1:5000/ 

Horayyy! server is live



if incase this does not work for your system somehow 
clone the repository to a local directory.

go to terminal and run 

```bash
conda env create --name envname --file=environments.yml
```
from within the conda environemnt 
 run the ***tinyurl.py*** file manually after giving the port 
 for example tinyurl.run(host=5000, debug=True)to access the server 




