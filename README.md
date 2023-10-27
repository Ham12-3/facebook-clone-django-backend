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









![backend-3](https://github.com/Ham12-3/facebook-clone-django-backend/assets/93613316/9bb552b0-1230-4f94-b8bb-424cf6b9f058)
![django-1](https://github.com/Ham12-3/facebook-clone-django-backend/assets/93613316/1cc43212-611a-4049-ae1d-ed0f53b9cea4)
![backend-2](https://github.com/Ham12-3/facebook-clone-django-backend/assets/93613316/57706cce-4304-4004-bb0f-6f54b872ac5a)
