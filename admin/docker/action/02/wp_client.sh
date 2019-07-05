#! /bin/bash

SQL_CID=$(docker create -e MYSQL_ROOT_PASSWORD=quiet mysql:5)
docker start $SQL_CID

MAILER_CID=$(docker create dockerinaction/ch2_mailer)
docker start $MAILER_CID

#DB_CID=$(docker run -d -e MYSQL_ROOT_PASSWORD=quiet mysql:5) # 唯一性？
#MAILER_CID=$(docker run -d dockerinaction/ch2_mailer)


CLIENT_ID="$1"
if [ ! -n "$CLIENT_ID" ];then
    echo "Client Id not set"
    exit 1
fi

WP_CID=$(docker create \
    --link $DB_CID:mysql \
    --name wp_$CLIENT_ID \
    -p 80 \
    -v /run/lock/apache2/ -v /run/apache2/ \
    -e WORDPRESS_DB_NAME=$CLIENT_ID \
    --read-only wordpress:4
)
docker start $WP_CID


AGENT_CID=$(docker create \
    --name agent_$CLIENT_ID \
    --link $WP_CID:insideweb \
    --link $MAILER_CID:insidemailer \
    dockerinaction/ch2_agent
)
docker start $AGENT_CID
