#Build Images
docker build -t service1 api1
docker build -t service2 api2

#Create Docker Network
docker network create apinetwork

#Run containers
docker run -d -p 5000:5000 --network apinetwork --name service1 service1
docker run -d -p 5001:5001 --network apinetwork --name service2 service2