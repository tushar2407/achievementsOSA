# Achievements OSA IIITD

> ## ** *Endpoints* **

## Authentication
    auth/login/ `POST`
    rest-auth/login/ `POST`
    rest-auth/registration/ `POST`

## Detials of user
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
                
        phone ` POST, GET, PATCH, DELETE `
            -> POST 
                - body :
                    {
                        "number":"910123456789"
                    }
                - resposne :
                    {
                        "id": 2,
                        "number": "910123456789",
                        "user": 3
                    }
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
                - response :
                    [
                        {
                            "id": 2,
                            "number": "910123456789",
                            "user": 3
                        }
                    ]
            -> GET
                /<id:int> (id of the phone number you want)
                - response : 
                    {
                        "id": 2,
                        "number": "910123456789",
                        "user": 3
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

## main
    main/api/
        tag ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the tag)
            -> GET
                / (returns a list of all the tags)
            -> GET
                /<id:int> (id of the tag you want)
        institution ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the institution)
            -> GET
                / (returns a list of all the institutions)
            -> GET
                /<id:int> (id of the institution you want)
        project ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the project)
            -> GET
                / (returns a list of all projects of the logged-in user)
                - resposne :
                    [
                        {
                            "id": 1,
                            "title": "asferf",
                            "description": "sdfsdf",
                            "startDate": "2021-06-21",
                            "endDate": "2021-07-21",
                            "field": "sdfsdf",
                            "domain": "werew",
                            "dateCreated": "2021-04-12T19:41:52.445507+05:30",
                            "addedBy": 3,
                            "mentors": [
                                4
                            ],
                            "students": [
                                1,
                                2
                            ],
                            "tags": [
                                1,
                                2
                            ],
                            "url":''
                        }
                    ]
            -> GET
                /<id:int> (id of the project you want)
                - response :
                    {
                        "id": 1,
                        "title": "asferf",
                        "description": "sdfsdf",
                        "startDate": "2021-06-21",
                        "endDate": "2021-07-21",
                        "field": "sdfsdf",
                        "domain": "werew",
                        "dateCreated": "2021-04-12T19:41:52.445507+05:30",
                        "addedBy": 3,
                        "mentors": [
                            4
                        ],
                        "students": [
                            1,
                            2
                        ],
                        "tags": [
                            1,
                            2
                        ],
                        "url":''
                    }
            -> POST
                - body : 
                    {
                        "title": "asferf",
                        "description": "sdfsdf",
                        "startDate": "2021-06-21",
                        "endDate": "2021-07-21",
                        "field": "sdfsdf",
                        "domain": "werew",
                        "mentors": [
                            4 -> staff ids
                        ],
                        "students": [
                            1,2 -> student ids
                        ],
                        "tags": [
                            1,2 -> tags ids
                        ],
                        "url":''
                    }
                - response :
                    {
                        "id": 1,
                        "title": "asferf",
                        "description": "sdfsdf",
                        "startDate": "2021-06-21",
                        "endDate": "2021-07-21",
                        "field": "sdfsdf",
                        "domain": "werew",
                        "dateCreated": "2021-04-12T19:41:52.445507+05:30",
                        "addedBy": 3,
                        "mentors": [
                            4
                        ],
                        "students": [
                            1,
                            2
                        ],
                        "tags": [
                            1,
                            2
                        ],
                        "url":''
                    }
        achievement ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the phone number)
            -> GET
                / (returns a list of all phone numbers of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
            -> POST 
                - body :
                    {
                        "title": "somrhtin",
                        "description": "sdfbos df sdg gdf gdf g",
                        "institution": "sudbfsd dgdfg",
                        "achievedDate": "2021-02-01",
                        "teamMembers": [
                            2,3,4 -> ids of users
                        ],
                        "tags": [
                            1 -> ids of tags
                        ],
                        "category" : <1,2,3,4,5,6>
                    }
                    // CATEGORY_CHOICES = (
                        (0, 'NA'),
                        (1,'intra college'), 
                        (2,'inter college'), 
                        (3,'district level'),
                        (4,'state level'), 
                        (5,'national level'), 
                        (6,'international level')
                    )
                - response : 
                    {
                        "id": 5,
                        "title": "somrhtin",
                        "description": "sdfbos df sdg gdf gdf g",
                        "technical": false,
                        "proof": null,
                        "institution": <education_id>,
                        "dateCreated": "2021-04-12T18:36:08.784337+05:30",
                        "achievedDate": "2021-02-01",
                        "approved": false,
                        "approvedBy": null,
                        "addedBy": 3,
                        "teamMembers": [
                            2,
                            3,
                            4
                        ],
                        "tags": [
                            1
                        ],
                        "category" : <1,2,3,4,5,6>
                    }
        search?q=''
            -> GET
                - response : {
                    'achievements': [],
                    'projects': []
                }
        graph
            -> GET
                - response : {
                    'achievements_category' : [],
                    'achievements_year' : [],
                    'projects_year' : [],
                }
    main/
        hompage `GET `
            - response :
                {
                    "student_achievements": [
                        {
                            "id": 5,
                            "title": "somrhtin",
                            "description": "sdfbos df sdg gdf gdf g",
                            "technical": false,
                            "proof": null,
                            "institution": "sudbfsd dgdfg",
                            "dateCreated": "2021-04-12T13:06:08.784Z",
                            "achievedDate": "2021-02-01",
                            "approved": false,
                            "approvedBy_id": null,
                            "addedBy_id": 3,
                            "teamMembers": [
                                2,
                                3,
                                4
                            ],
                            "tags": [
                                1
                            ]
                        }
                    ],
                    "staff_achievements": [],
                    "publications": [
                        {
                            "id": 5,
                            "title": "somrhtin",
                            "description": "sdfbos df sdg gdf gdf g",
                            "technical": false,
                            "proof": null,
                            "institution": "sudbfsd dgdfg",
                            "dateCreated": "2021-04-12T13:06:08.784Z",
                            "achievedDate": "2021-02-01",
                            "approved": false,
                            "approvedBy_id": null,
                            "addedBy_id": 3,
                             "teamMembers": [
                                2,
                                3,
                                4
                            ],
                            "tags": [
                                1
                            ]
                        }
                    ]
                }

    main/
        api/
            get-professors `GET`
            - response: {
                'professors' : [
                    {
                        '<staff_id>',
                        '<email1>'
                    },
                    {
                        '<staff_id2>',
                        '<email2>'
                    },
                    ...
                ]
            }
        api/    
            get-students `GET`
            - response: {
                'students' : [
                    {
                        '<user_id>',
                        '<email1>'
                    },
                    {
                        '<user_id2>',
                        '<email2>'
                    },
                    ...
                ]
            }
        api/    
            get-achievements-admin `GET`
            - response: {
                'unapproved' : [
                    {
                        '<achievement_id>',
                        '<title>',
                        '<description>',
                        '<technical>',
                        '<proof>',
                        '<institution>',
                        '<dateCreated>',
                        '<achievedDate>',
                        '<approved>',
                        '<approvedBy>',
                        '<addedBy>',
                        'mentors':[],
                        'teamMembers':[],
                        'tags':[],
                    },
                    ...
                ]
            }

## people
    people/api/
        department ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the department)
            -> GET
                / (returns a list of all departments of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
        education ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the education)
            -> GET
                / (returns a list of all educations of the logged-in user)
            -> GET
                /<id:int> (id of the phone number you want)
        skill ` POST, GET, PATCH, DELETE `
            -> PATCH
                /<id:int>/ (id of the skill)
            -> GET
                / (returns a list of all skills of the logged-in user)
            -> GET
                /<id:int> (id of the skill whose name you want)
        staff ` POST, GET, PATCH, DELETE `
            -> PATCH
                /1/ (will automatically take your user)
            -> GET
                /<id:int> (id of the staff)
            -> GET
                / (returns the details of the logged-in user)
        student ` POST, GET, PATCH, DELETE `
            -> PATCH
                /1/ (will automatically take your profile)
            -> GET
                /<id:int> (id of the student)
            -> GET
                / (returns the details of the logged-in user)
        recruiter ` POST, GET, PATCH, DELETE `
            -> PATCH
                /1/ (will automatically take your profile)
            -> GET
                /<id:int> (id of the recruiter)
            -> GET
                / (returns the details of the logged-in user)

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