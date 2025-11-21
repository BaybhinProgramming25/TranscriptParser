.PHONY: dir  

dir:
	- docker-compose down 
	- docker-compose build 
	- docker-compose up -d 