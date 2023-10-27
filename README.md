<h1>Facebook Clone Django Backend</h1>

# Rest API for the facebook clone backend built with Python Django and PostgreSQL.

# To get started you will need to install the dependencies and docker daemon is requierment

```shell
docker-compose build
```

# Then after that you'll type

```shell
docker-compose exec build sh

python manage.py makemigrations
python manage.py migrate
```

# Thereafter you'll now turn on the server using the following command:

```shell
docker-compose up
```

then you can check http://localhost:8000/swagger for the API documentation and to set the admin username and password do the following

```shell
docker-compose exec build sh
python manage.py createsuperuser
```


