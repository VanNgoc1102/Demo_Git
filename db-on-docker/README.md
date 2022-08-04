C:\Users\Admin\youtube\youtube_comments\python\new_comments.json

docker-compose up
docker-compose ps
docker-compose stop
docer-compose rm
docker-compose start

docker exec -it db-on-docker_mysql-dev_1 bash
mysql -uroot -ppassword -hmysql-dev sql-comments
show databases ;
use  sql-comments;
select * from new_comments;

