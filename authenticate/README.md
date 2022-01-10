# **Authenticate App**
Takes care of the `Login` system and the `Profile` of the user in the `Achievements` app.

Endpoints for :
    
    - Profile
    - Approving a user as staff/admin/student
    - Login
    - Logout

## **Endpoints**

    auth/api/
        profile ` POST, GET, PATCH, DELETE `
            -> PATCH
                /1/ (will automatically take your profile)
                - respnse :
                    {
                        "id": 1,
                        "dob": "2020-01-05",
                        "age": 19,
                        "designation": 1,
                        "gender": 2,
                        "address": "asdas",
                        "group": "abc",
                        "user": 2,
                        "skills": [
                            1
                        ]
                    }
            -> GET
                /<id:int> (id of the profile)
                - response :
                    {
                        "id": 1,
                        "dob": "2020-01-05",
                        "age": 19,
                        "designation": 1,
                        "gender": 2,
                        "address": "asdas",
                        "group": "abc",
                        "user": 2,
                        "skills": [
                            1
                        ]
                    }
            -> GET
                / (returns the id of the logged-in user)
                - response : 
                    {
                        "id": 1,
                        "dob": "2020-01-05",
                        "age": 19,
                        "designation": 1,
                        "gender": 2,
                        "address": "asdas",
                        "group": "abc",
                        "user": 2,
                        "skills": [
                            1
                        ]
                    }
                
        approve-users `POST, GET`
            -> GET
                - response :
                    {
                        'profiles' : []
                    }
            -> POST
                - body : 
                    {
                        'user' : <id>,
                        'designation' : 'staff'/'student'/'admin'
                    }
                - response : {}
