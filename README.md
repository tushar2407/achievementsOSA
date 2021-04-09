# Achievements OSA IIITD

> ## ** *Endpoints* **

## Authentication
    rest-auth/login/ `POST`
    rest-auth/registration/ `POST`

## Detials of user
    auth/api/
        profile ` POST, GET, PATCH, DELETE `
            -> PATCH
                /1/ (will automatically take your profile)
            -> GET
                /<id:int> (id of the profile)
            -> GET
                / (returns the id of the logged-in user)
        phone ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)

## main
    main/api/
        tag ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
        project ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
        achievement ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)

## people
    people/api/
        department ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
        education ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
        skill ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
        staff ` POST, GET, PATCH, DELETE `
            -> PATCH
                /1/ (will automatically take your profile)
            -> GET
                /<id:int> (id of the profile)
            -> GET
                / (returns the id of the logged-in user)
        student ` POST, GET, PATCH, DELETE `
            -> PATCH
                /1/ (will automatically take your profile)
            -> GET
                /<id:int> (id of the student)
            -> GET
                / (returns the id of the logged-in user)
        recruiter ` POST, GET, PATCH, DELETE `

<hr>

## for every request:
    Header
        Authorization : Token <token>

---
### Users:
- username = harshkumar; password = hadron43
- username = tusharmohan; password = tushar2407
- username = rajivratnshah; password = rajivsirmidas
- (superuser) username = admin; password = admin

# TODO
    - Endpoint for approval
    - Search functionality
    - Add social mdeia handles in profile
    - add privacy field for email and numbers