# API para gerênciamento interno de escola

#### Capstone Q3 - Kenzie Academy Brasil

<br>

## Sobre a aplicação:

Um sistema para auxilio na administração de uma escola, com funcionalidades para controle de faltas, notas, biblioteca entre outos. Essa aplicação tem como foco escolas de ensino fundamental e médio.

<hr />
<h2>Desenvolvedores</h2>

<div style="display: flex">
<img src="https://avatars.githubusercontent.com/u/48024940?s=400&u=917f38c9afb6526bbda4135d749a22d1c5dfd580&v=4" style="width: 100px; border-radius: 50%;"/>

<img src="https://avatars.githubusercontent.com/u/85950646?v=4" style="width: 100px; border-radius: 50%;margin-left:10px;"/>

<img src="https://avatars.githubusercontent.com/u/71736180?v=4" style="width: 100px; border-radius: 50%;margin-left:10px;"/>

<img src="https://avatars.githubusercontent.com/u/4825970?v=4" style="width: 100px; border-radius: 50%;margin-left:10px;"/>

<img src="https://avatars.githubusercontent.com/u/65559844?v=4" style="width: 100px; border-radius: 50%;margin-left:10px;"/>

<img src="https://avatars.githubusercontent.com/u/85639170?v=4" style="width: 100px; border-radius: 50%;margin-left:10px;"/>
</div>

<hr />

## Base_URL

https://piaget-system.herokuapp.com/api

---
## Students


### Login

`POST /students/login`

REQUEST FORMAT
```json
{
    "cpf": "11111111111",
    "password": "1234"
}
```
RESPONSE FORMAT STATUS 200
```json
{
  "registration_student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
  "name": "felipe",
  "contact_name": "Rosita",
  "contact_email": "rosita@email.com",
  "cpf": "11111111111",
  "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
  "api_key": "1230"
}
```

`GET /students/profile`
>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
{
  "registration_student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
  "name": "felipe",
  "contact_name": "Rosita",
  "contact_email": "rosita@email.com",
  "cpf": "11111111111",
  "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
  "api_key": "1230"
}
```

### Create new student

`POST /students/register`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "name" : "Uzumake Naruto",
    "contact_name" : "Umino Iruka",
    "contact_email" : "IrukaTeacher@ninjaschool.com",
    "cpf" : "99999999999",
    "birth_date" : "1999/05/26",
    "gender" : "Masculino",
    "photo" : "alt.png",
    "password" : "viladafolhaoculta",
    "classroom_id" : "51df51e0-00a7-49e3-9f2e-0405574f5c20"       
}
```
RESPONSE FORMAT STATUS 201
```json
{
    "id": "e1623b44-080c-4d3f-82d0-6237ff6f9077",
    "name" : "Uzumake Naruto",
    "contact_name" : "Umino Iruka",
    "contact_email" : "IrukaTeacher@ninjaschool.com",
    "cpf" : "99999999999",
    "birth_date" : "1999/05/26",
    "gender" : "Masculino",
}
```

### Get all students

`GET /students`

>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
[
  {
    "id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "felipe",
    "cpf": "11111111111",
    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
    "contact_name": "Rosita",
    "contact_email": "rosita@email.com",
    "gender": "Feminino"
  },
  {
    "id": "1d5225ef-5638-4397-9989-e604a2cceca0",
    "name": "matheus",
    "cpf": "11111111112",
    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
    "contact_name": "Sirlei",
    "contact_email": "sirlei@email.com",
    "gender": "Feminino"
  },
  {
    "id": "7dc82c28-4766-4bff-829b-2198a2e1ef98",
    "name": "rafael",
    "cpf": "11111111113",
    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
    "contact_name": "Maria",
    "contact_email": "maria@email.com",
    "gender": "Feminino"
  },
  {
    "id": "2a465bd0-22cd-45e7-9fd1-142dee2cca78",
    "name": "renato",
    "cpf": "11111111114",
    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
    "contact_name": "Maria",
    "contact_email": "mariaa@email.com",
    "gender": "Feminino"
  },
  {
    "id": "e1623b44-080c-4d3f-82d0-6237ff6f9077",
    "name": "Uzumake Naruto",
    "cpf": "99999999999",
    "birth_date": "Wed, 26 May 1999 00:00:00 GMT",
    "contact_name": "Umino Iruka",
    "contact_email": "IrukaTeacher@ninjaschool.com",
    "gender": "Masculino"
  }
]
```

### Get only student

`GET /students/:id`

>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
{
    "id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "felipe",
    "cpf": "11111111111",
    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
    "contact_name": "Rosita",
    "contact_email": "rosita@email.com",
    "gender": "M"
}
```

### Update student

`PATCH /students/:student_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "gender": "M"
}
```
RESPONSE FORMAT STATUS 202
```json
{
    "id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "felipe",
    "cpf": "11111111111",
    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
    "contact_name": "Rosita",
    "contact_email": "rosita@email.com",
    "gender": "Masculino"
}
```

### Delete student

`DELETE /students/:id`

>header {
    Authorization: Bearer token
}

---
## Employee

### Login

`POST /login`

REQUEST FORMAT
```json
{
    "email": "lucira@email.com",
    "password": "1234"
}
```
RESPONSE FORMAT STATUS 200
```json
{
  "employee_id": "b70c93e0-a6c0-43f1-8c7b-ea3b1b3f00f4",
  "name": "lucira",
  "email": "lucira@email.com",
  "wage": 4000.0,
  "access_level": "admin",
  "api_key": "1234"
}
```

### Create new employee

`Post /employees`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "name": "Jhon Doe",
    "email": "jhondoe11234@mail.com",
    "wage": 3020.90,
    "access_level": "admin",
    "password": "1234"
}
```
RESPONSE FORMAT STATUS 201
```json
{
    "employee_id": "32e20b1f-340f-447a-b019-c0b7353d1f82",
    "name": "Jhon Doe",
    "email": "jhondoe11234@mail.com",
    "wage": 3020.9,
    "access_level": "admin"
}
```

### Get all employees

`GET /employees`

RESPONSE FORMAT STATUS 200
```json
{
    "result": [
        {
            "employee_id": "b70c93e0-a6c0-43f1-8c7b-ea3b1b3f00f4",
            "name": "lucira",
            "email": "lucira@email.com",
            "wage": 4000.0,
            "access_level": "admin"
        },
    ]
}
```

### Get only employee

`GET /employees/:employee_id`

RESPONSE FORMAT STATUS 200
```json
{
    "employee_id": "b70c93e0-a6c0-43f1-8c7b-ea3b1b3f00f4",
    "name": "lucira",
    "email": "lucira@email.com",
    "wage": 4000.0,
    "access_level": "admin"
}
```

### Update employee

`PATCH /employees/:employee_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "name": "John Doe",
    "email": "johndoe11234@mail.com"
}
```
RESPONSE FORMAT STATUS 202
```json
{
    "employee_id": "32e20b1f-340f-447a-b019-c0b7353d1f82",
    "name": "John Doe",
    "email": "johndoe11234@mail.com",
    "wage": 3020.9,
    "access_level": "admin"
}
```

### Delete employee

`DELETE /employees/:id`

>header {
    Authorization: Bearer token
}

---

## Grades

### Create new grade

`Post /grades`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "ativity": "debug",
    "grade": 10.0,
    "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "classrom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20" 
}
```
RESPONSE FORMAT STATUS 201
```json
{
  "ativity": "debug",
  "grade": 10.0,
  "student": {
    "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "felipe"
  },
  "classrom": {
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "1A"
  }
}
```
### Get all grades

`GET /grades`

RESPONSE FORMAT STATUS 200
```json
[
  {
    "ativity": "codar",
    "grade": 9.0,
    "student": {
      "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
      "name": "felipe"
    },
    "classrom": {
      "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
      "name": "1A"
    }
  }
]
```

### Get only grade

`GET /grades/:student_id`

RESPONSE FORMAT STATUS 200
```json
[
    {
        "ativity": "codar",
        "grade": 9.0,
        "student": {
            "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
            "name": "felipe"
        },
        "classrom": {
            "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
            "name": "1A"
        }
    }
]
```

### Get grade student

`GET /grades/student`
>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
{
    "grades_class": "1A",
    "school_subject": "React",
    "grade": 9.0
}
```

### Update grade

`PATCH /grades/:grade_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "grade": "10.0"
}
```
RESPONSE FORMAT STATUS 202
```json
{
  "ativity": "codar",
  "grade": 10.0,
  "student": {
    "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "felipe"
  },
  "classrom": {
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "1A"
  }
}
```

### Delete grade

`DELETE /grades/:grade_id`

>header {
    Authorization: Bearer token
}

---

## Books

### Create new book

`Post /books/register`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "title": "Harry Potter - E A Pedra Filosofal",
    "author": "J.K. Rowling",
    "quantity": 4
}
```
RESPONSE FORMAT STATUS 201
```json
{
    "title": "Harry Potter - E A Pedra Filosofal",
    "author": "J.K. Rowling",
    "quantity": 4
}
```

### Get all books

`GET /books`

RESPONSE FORMAT STATUS 200
```json
[
  {
    "title": "Harry Potter - E A Pedra Filosofal",
    "author": "J.K. Rowling",
    "quantity": 5
  },
  {
    "title": "Harry Potter E A Câmara Dos Segredos",
    "author": "J.K. Rowling",
    "quantity": 3
  },
  {
    "title": "Harry Potter E A Criança Amaldiçoada - Parte 1",
    "author": "J.K. Rowling",
    "quantity": 5
  },
  {
    "title": "Harry Potter E A Criança Amaldiçoada - Parte 2",
    "author": "J.K. Rowling",
    "quantity": 5
  }
]
```

### Get only book

`GET /books/:book_id`

RESPONSE FORMAT STATUS 200
```json
{
  "title": "Harry Potter E A Câmara Dos Segredos",
  "author": "J.K. Rowling",
  "quantity": 3
}
```

### Update book

`PATCH /books/:book_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "title": "Excel nunca mais"
}
```
RESPONSE FORMAT STATUS 202
```json
{
    "title": "Excel Nunca Mais",
    "author": "J.K. Rowling",
    "quantity": 3
}
```

### Delete book

`DELETE /books/:id`

>header {
    Authorization: Bearer token
}

---

## Classroom

### Create new classroom

`Post /classrooms`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "name": "1A",
}
```
RESPONSE FORMAT STATUS 201
```json
{
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "1A"
}
```

### Get all classrooms

`GET /classrooms`

RESPONSE FORMAT STATUS 200
```json
{
  "result": [
    {
      "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
      "1A": [
        {
          "materia": "react",
          "teacher": "paulo"
        },
        {
          "materia": "javascript",
          "teacher": "chrystian"
        }
      ]
    },
    {
      "classroom_id": "1446d11e-6985-4979-8e7f-15d5ddf0a81f",
      "1B": [
        {
          "materia": "python",
          "teacher": "chrystian"
        }
      ]
    },
    {
      "classroom_id": "cf43d8ca-37a8-4140-bc97-32192e151a27",
      "2A": [
        {
          "materia": "node",
          "teacher": "paulo"
        }
      ]
    },
    {
      "classroom_id": "3df783ee-d140-47cd-9c65-213b830a7ca6",
      "2B": [
        {
          "materia": "python",
          "teacher": "chrystian"
        }
      ]
    }
  ],
  "page": 1,
  "total_number_of_pages": 1
}
```

### Get only classroom

`GET /classrooms/:classroom_id`

RESPONSE FORMAT STATUS 200
```json
{

    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "1A": [
        {
        "teacher": "Paulo",
        "school_subject": "React",
        "students": [
                {
                    "name": "Arthur"
                },
                {
                    "name": "Sidney"
                }
            ]
        }
    ]
}
```

### Update classroom

`PATCH /classrooms/:classroom_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "name": "2B",
}
```
RESPONSE FORMAT STATUS 202
```json
{
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "2B"
}
```

### Delete classroom

`DELETE /classrooms/:id`

>header {
    Authorization: Bearer token
}

---

## Library

### Create new library

`Post /library/rental`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "employee_id":"3f5e5df3-651b-46ec-9c42-be4a863f974a",
    "book_id":"2fc09626-8a2c-4ef7-b59d-4a56e77e5714",
    "student_id":"51df51e0-00a7-49e3-9f2e-0405574f5c20"
}
```
RESPONSE FORMAT STATUS 201
```json
{
    "library_id": "ce3e70be-bb53-4289-8751-1efed4014bd4",
    "librarian": "paulo",
    "book": "Harry Potter - E a pedra filosofal",
    "student": "felipe",
    "data_withdraw": "Thu, 10 Mar 2022 00:00:00 GMT",
    "data_accurrancy": "Fri, 25 Mar 2022 00:00:00 GMT"
}
```

### Get all library

`GET /library`

RESPONSE FORMAT STATUS 200
```json
[
    {
        "library_id": "3554e9f0-8208-4e99-81c1-d79f3caf891c",
        "librarian": "matheus",
        "book": "Harry Potter - E a pedra filosofal",
        "student": "felipe",
        "data_withdraw": "Sat, 01 Feb 2020 00:00:00 GMT",
        "data_return": "Sat, 15 Feb 2020 00:00:00 GMT",
        "data_accurrancy": "Sat, 15 Feb 2020 00:00:00 GMT"
    },
]
```

### Get only library

`GET /library/:library_id`

RESPONSE FORMAT STATUS 200
```json
[
    {
        "library_id": "3554e9f0-8208-4e99-81c1-d79f3caf891c",
        "librarian": "matheus",
        "book": "Harry Potter - E a pedra filosofal",
        "student": "felipe",
        "data_withdraw": "Sat, 01 Feb 2020 00:00:00 GMT",
        "data_return": "Sat, 15 Feb 2020 00:00:00 GMT",
        "data_accurrancy": "Sat, 15 Feb 2020 00:00:00 GMT"
    },
]
```

### Update library

`PATCH /library/:library_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "book_id": "081c575b-a38f-4f41-bf15-2593cd58ab93"
}
```
RESPONSE FORMAT STATUS 202
```json
{
  "library_id": "3554e9f0-8208-4e99-81c1-d79f3caf891c",
  "librarian": "matheus",
  "book": "Excel Nunca Mais",
  "student": "felipe",
  "data_withdraw": "Sat, 01 Feb 2020 00:00:00 GMT",
  "data_return": "Sat, 15 Feb 2020 00:00:00 GMT",
  "data_accurrancy": "Sat, 15 Feb 2020 00:00:00 GMT"
}
```
### Update library return

`PATCH /library/return/:library_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json

```
RESPONSE FORMAT STATUS 202
```json
{
  "library_id": "c2c414b7-f972-424b-8243-246b7c942e28",
  "librarian": "paulo",
  "book": "Harry Potter - E a pedra filosofal",
  "student": "felipe",
  "data_withdraw": "Thu, 10 Mar 2022 00:00:00 GMT",
  "data_return": "Thu, 10 Mar 2022 00:00:00 GMT",
  "data_accurrancy": "Fri, 25 Mar 2022 00:00:00 GMT"
}
```

### Get library unreturned rental

`Get /library/unreturned_rental`

>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
[
    [
        {
            "rental_id": "ce3e70be-bb53-4289-8751-1efed4014bd4",
            "book": "Harry Potter - E a pedra filosofal",
            "date_withdrawal": "Thu, 10 Mar 2022 00:00:00 GMT",
            "date_return": null,
            "student": "felipe",
            "librarian": "paulo"
        }
    ]
]
```
### Get library rented by id

`GET /library/rented/<student_id>`

>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
[
    {
        "student": "felipe",
        "book": "Harry Potter - E a pedra filosofal",
        "date_accurancy": "Fri, 25 Mar 2022 00:00:00 GMT"
    }
]
```
### Get library rented for students

`GET /library/rented_for_student/<student_id>`

>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
[
    {
        "student": "felipe",
        "book": "Harry Potter - E a pedra filosofal",
        "date_accurancy": "Sat, 15 Feb 2020 00:00:00 GMT"
    },
    {
        "student": "felipe",
        "book": "Harry Potter - E a pedra filosofal",
        "date_accurancy": "Fri, 25 Mar 2022 00:00:00 GMT"
    }
]
```
### Delete library

`DELETE /library/:id`

>header {
    Authorization: Bearer token
}

---

## Absence

### Create new absence

`Post /absences`

>header {
    Authorization: Bearer token
}
REQUEST FORMAT
```json
{
    "date": "02/02/2020",
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "student_id": "1d5225ef-5638-4397-9989-e604a2cceca0"
}
```
RESPONSE FORMAT STATUS 201
```json
{
    "absence_id": "12f9efee-4010-4ec2-8370-1873f4ec0a60",
    "date": "02/02/2020",
    "justify": false,
    "classroom": "1A",
    "student": "Matheus",
    "school_subject": "React"
}
```

### Get all absences

`GET /absences`

RESPONSE FORMAT STATUS 200
```json
[
  {
    "absence_id": "b20dfcbb-f121-41ef-bf96-cb988d68a35a",
    "date": "15/02/2020",
    "justify": false,
    "classroom": "1A",
    "student": "Matheus",
    "school_subjec": "React"
  },
  {
    "absence_id": "9cf30ce0-6925-4ff1-9bbf-f27bd7916782",
    "date": "15/02/2020",
    "justify": true,
    "classroom": "1A",
    "student": "Matheus",
    "school_subjec": "React"
  },
  {
    "absence_id": "494925c7-7399-44e2-a00e-653581145979",
    "date": "15/02/2020",
    "justify": false,
    "classroom": "1A",
    "student": "Felipe",
    "school_subjec": "React"
  },
  {
    "absence_id": "d98c6e17-d6ce-4432-bc31-b10418a7cf44",
    "date": "15/02/2020",
    "justify": false,
    "classroom": "2A",
    "student": "Renato",
    "school_subjec": "Node"
  }
]
```

### Get only absence

`GET /absences/:absence_id`

RESPONSE FORMAT STATUS 200
```json
[
  {
    "absence_id": "494925c7-7399-44e2-a00e-653581145979",
    "date": "15/02/2020",
    "justify": false,
    "classroom": "1A",
    "student": "Felipe",
    "school_subject": "React"
  }
]
```

### Get absence student

`GET /absences/student`
>header {
    Authorization: Bearer token
}

RESPONSE FORMAT STATUS 200
```json
{
    "absence_class": "1A",
    "school_subject": "React",
    "absence_date": "10/03/2020"
}
```

### Update absence

`PATCH /absences/:absence_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json

```
RESPONSE FORMAT STATUS 202
```json
{
  {
    "absence_id": "b20dfcbb-f121-41ef-bf96-cb988d68a35a",
    "date": "15/02/2020",
    "justify": true,
    "classroom": "1A",
    "student": "Matheus",
    "school_subject": "React"
  }  
}
```

### Delete absence

`DELETE /absences/:id`

>header {
    Authorization: Bearer token
}

---

## School_subject

### Create new school_subject

`Post /school_subjects/register`

>header {
    Authorization: Bearer token
}
REQUEST FORMAT
```json
{
    "school_subject":"Matemática do 1º ano A do ensino médio",
    "employee_id": "6d4b0f4d-a418-432e-a112-b44527ea33d4", 
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20"
}
```
RESPONSE FORMAT STATUS 201
```json
{
    "school_subject_id": "031a682f-2971-479e-b8ae-8f449734259a",
    "school_subject": "Matemática do 1º ano A do ensino médio",
    "classroom": "1A",
    "teacher": "chrystian"
}
```

### Get all school_subjects

`GET /school_subjects`

RESPONSE FORMAT STATUS 200
```json
[
  {
    "school_subject_id": "62921285-ac00-4f38-ab44-356cdea16631",
    "school_subject": "React",
    "classroom": "1A",
    "teacher": "Paulo"
  },
  {
    "school_subject_id": "19c9807c-d818-4bc5-8d80-c66ad5ff253f",
    "school_subject": "Python",
    "classroom": "1B",
    "teacher": "Chrystian"
  },
  {
    "school_subject_id": "c3280110-1a25-40cb-8573-b20f9f14b200",
    "school_subject": "Node",
    "classroom": "2A",
    "teacher": "Paulo"
  },
  {
    "school_subject_id": "73e8e3e6-db7a-4cae-9ae6-74f4d0e87d66",
    "school_subject": "Python",
    "classroom": "2B",
    "teacher": "Chrystian"
  },
  {
    "school_subject_id": "73e8e3e6-db7a-4cae-9ae6-74f4d0e87d67",
    "school_subject": "Javascript",
    "classroom": "1A",
    "teacher": "Chrystian"
  }
]
```

### Update school_subject

`PATCH /school_subjects/edit/:school_subject_id`

>header {
    Authorization: Bearer token
}

REQUEST FORMAT
```json
{
    "school_subject": "React Native"
}
```
RESPONSE FORMAT STATUS 202
```json
{
  "school_subject_id": "62921285-ac00-4f38-ab44-356cdea16631",
  "school_subject": "React Native",
  "classroom": "1A",
  "teacher": "paulo"
}
```

### Delete school_subject

`DELETE /school_subjects/:id`

>header {
    Authorization: Bearer token
}

---