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

### usage
 enter url link and copy back short url in search box.

  *** no extra front end functionality implemnted*** 


### System design  

***data model used***: EncodeDecode class will create a hash(dictionary) database with O(1) complexity for querying under a session. 

***algorithm*** : base64 random key generator 


### Tasks done

-   implementation
    -   Language: **Python**
    -   Framework: **Flask**
    -   Two endpoints 
        -   /encode_url - Encodes a URL to a shortened URL
        -   /<short_url> - Decodes a shortened URL to its original URL.
-   encode/decode algorithm:counter with base62 which gives about permutaion of all letters and numbers(62)

-   basic API tests for both endpoints

### code structure 
![Model](code_structure.png)


### further improvement to consider 

-scalability with a distributed storage 

-better indexing for the storage perhaps when requests get exponentially high

-

### what i learned 

-a bit of flask and system design 
-refreshed on my python opp skills

### what i found difficult 
-relative importing (nomodule named "classname" :D spent more that 5 hours on this)

-pytest on poetry package manager(swithed to conda and unittest but could not complete the unit tests,found them a bit tricky to grasp )

i will learn practice more on unittesting REST apis

***at this stage i would be asking for help*** :) 

Feedback is much appreciated 

Cheers 




