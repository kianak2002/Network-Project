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

## Data
the data used here is ram_usage_percentage, cpu_usage_percentage, and cpu_frequency. 

### report
you can find the report [here](https://github.com/kianak2002/Network-Project/blob/main/report_networkProject_9831006.pdf) in persian.
