# **Achievements OSA IIITD**

## Technologies

FMS Portal IIITD is powered by a number of technologies:

- [Django] - high-level Python Web framework
- [PostgreSQL] - a powerful, open source object-relational database system
- [DjangoRestFramework] - a powerful and flexible toolkit to but RESTful APIs.
## Setup

1. To clone and run, you'll need Git, [Python] v3.0+ and [PostgreSQL] v9+ installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/tushar2407/achievementsOSA.git

# Go into the repository
$ cd achievementsOSA

# Install dependencies in a virtualenv
$ pip install -r requirements.txt
```

2. For environment variables check out .env.examples in achievements folder and create .env file for your own variables

```bash
# Create .env file
$ vim .env
```

The databse variables are from [PostgreSQL] database setup.


3. You are good to go just start the server after making migrations.

```bash
# Make migrations
$ python manage.py makemigrations

# Migrate the changes
$ python manage.py migrate

# Start the server
$ python manage.py runserver
```

Server by default starts in development mode at http://127.0.0.1:8000/

## Development

Great setting it all up! Let's contribute now. You'll need to learn Django basics to work on the app.

1. Make sure to start from the master branch and update your local repositories.

```bash
# Start from master
$ git checkout master

# Stay updated
$ git pull
```

2. Create a new branch for each bug fix or issue. Rest is basic.

```bash
# Create new branch keep qoutes
$ git checkout -b "YOUR_NEW_BRANCH"
```

## Deployment

Once the code is on the server we can nginx with gunicorn to host the app. Refer [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) for more information.

## License

MIT

## Authentication
    auth/login/ `POST`
        - 'osa_token' set in the cookies
    rest-auth/login/ `POST`
        - can be used for custom testing
    rest-auth/registration/ `POST`
        - can be used for custom testing

## For every request:
    Header
        Authorization : Token <token>

### Users:
- username = harshkumar; password = hadron43
- username = tusharmohan; password = tushar2407
- username = rajivratnshah; password = rajivsirmidas
- (superuser) username = admin; password = admin

## TODO
    -[X] Endpoint for approval
    -[X] Search functionality
    -[X] Add social mdeia handles in profile
    -[X] add privacy field for email and numbers

## Future Work
    - [ ] The Serializers can be nested for a few models which are handled in views explicitly otherwise.
    - [ ] A recruiter Profile can be made and this app can work as `Reculta` portal
    - [ ] Award application flow can be set 
    - [ ] Search funcionality can be extended 

---
[django]: https://docs.djangoproject.com/
[postgresql]: https://www.postgresql.org/
[twitter bootstrap]: https://getbootstrap.com/
[jquery]: http://jquery.com
[font awesome]: https://github.com/FortAwesome/Font-Awesome
[python]: https://www.python.org/download/releases/3.0/
[django compressor]: https://django-compressor.readthedocs.io/en/stable/
[djangorestframework]: https://www.django-rest-framework.org/
