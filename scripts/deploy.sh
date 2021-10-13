echo 'Pull new version from github'
git pull origin master

echo 'down old version'
docker-compose down

echo 'up new version'
docker-compose up --build -d test_nginx
