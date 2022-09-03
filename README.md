# Network-Project
Project for Network course instructed by Dr.[Babak Sadegheiyan](https://aut.ac.ir/cv/2102/BABAK-SADEGHIYAN?slc_lang=en&&cv=2102&mod=scv)

### structure
there are two files here. one for server and one for the client. 

## server

creates a socket and connects to the client. 
reads the data recieving from the client.
depict the data on Promotheus.
If there is no data, it will print "no more data" and gets data again.

## client

creates a socket and gets the required data and sends them to the server.
If the connection weren't established, it will print "retrying..." and tries again in 3 seconds

<img width="641" alt="Screen Shot 2022-09-03 at 1 15 54 PM" src="https://user-images.githubusercontent.com/61980014/188263305-752107ba-42e6-4c5b-8a9e-1f37b15fbd3d.png">


## Data
the data used here is ram_usage_percentage, cpu_usage_percentage, and cpu_frequency. 

### report
you can find the report [here](https://github.com/kianak2002/Network-Project/blob/main/report_networkProject_9831006.pdf) in persian.


## Result on Prometheus
### ram usage

<img width="641" alt="Screen Shot 2022-09-03 at 1 16 08 PM" src="https://user-images.githubusercontent.com/61980014/188263357-070284a2-1975-40e9-95c3-1400120ebf99.png">

### cpu usage

<img width="641" alt="Screen Shot 2022-09-03 at 1 16 13 PM" src="https://user-images.githubusercontent.com/61980014/188263362-2bd5d2b3-796e-42b3-9b85-8f194d25d660.png">

### cpu frequency (consistent)

<img width="641" alt="Screen Shot 2022-09-03 at 1 16 23 PM" src="https://user-images.githubusercontent.com/61980014/188263380-9e20df10-f7a6-4e4b-be90-45569de696c4.png">
