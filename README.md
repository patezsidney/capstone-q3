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

`POST /login`

```json
{
    "cpf": "11111111111",
    "password": "1234"
}
```
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

header {
    Authorization: Bearer token
}

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

header {
    Authorization: Bearer token
}

```json
[
    {

    }
]
```

### Get only student

`GET /students/:id`

header {
    Authorization: Bearer token
}

```json
[
    {

    }
]
```

### Update student

`PATCH /students/:id`

header {
    Authorization: Bearer token
}

```json
{

}
```

### Delete student

`DELETE /students/:id`

header {
    Authorization: Bearer token
}

---
## Employee

### Login

`POST /login`

```json
{
    "email": "lucira@email.com",
    "password": "1234"
}
```
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

header {
    Authorization: Bearer token
}

```json
{
    "name": "Jhon Doe",
    "email": "jhondoe11234@mail.com",
    "wage": 3020.90,
    "access_level": "admin",
    "password": "1234"
}
```
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

`GET /employees/:id`

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

`PATCH /employees/:id`

header {
    Authorization: Bearer token
}

```json
{
    "name": "John Doe",
    "email": "johndoe11234@mail.com"
}
```
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

header {
    Authorization: Bearer token
}

---

## Grades

### Create new grade

`Post /grades`

header {
    Authorization: Bearer token
}

```json
{
    "ativity": "debug",
    "grade": 10.0,
    "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "classrom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20" 
}
```
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

### Update grade

`PATCH /grades/:id`

header {
    Authorization: Bearer token
}

```json
{
    
}
```

### Delete grade

`DELETE /grades/:grade_id`

header {
    Authorization: Bearer token
}

---

## Books

### Create new book

`Post /books`

header {
    Authorization: Bearer token
}

```json
{
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2,
    "quantity": 1
}
```

### Get all books

`GET /books`

```json
[
 {
    "id": 1,
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2,
    "quantity": 1
  }
]
```

### Get only book

`GET /books/:id`

```json
[
 {
    "id": 1,
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2,
    "quantity": 1
  }
]
```

### Update book

`PATCH /books/:id`

header {
    Authorization: Bearer token
}

```json
{
    "name": "Hamburguer upgrade",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2,
    "quantity": 2
}
```

### Delete book

`DELETE /books/:id`

header {
    Authorization: Bearer token
}

---

## Classroom

### Create new classroom

`Post /classrooms`

header {
    Authorization: Bearer token
}

```json
{
    "name": "1A",
}
```
```json
{
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "1A"
}
```

### Get all classrooms

`GET /classrooms`

```json
[
  {
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "1A"
  },
  {
    "classroom_id": "1446d11e-6985-4979-8e7f-15d5ddf0a81f",
    "name": "1B"
  }
]
```

### Get only classroom

`GET /classrooms/:id`

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

`PATCH /classrooms/:id`

header {
    Authorization: Bearer token
}

```json
{
    "name": "2B",
}
```
```json
{
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "2B"
}
```

### Delete classroom

`DELETE /classrooms/:id`

header {
    Authorization: Bearer token
}

---

## Library

### Create new library

`Post /library`

header {
    Authorization: Bearer token
}

```json
{
    "name": "1A",
}
```
```json
{
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "1A"
}
```

### Get all library

`GET /library`

```json
[
  {
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "1A"
  },
  {
    "classroom_id": "1446d11e-6985-4979-8e7f-15d5ddf0a81f",
    "name": "1B"
  }
]
```

### Get only library

`GET /library/:id`

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

`PATCH /library/:id`

header {
    Authorization: Bearer token
}

```json
{
    "name": "2B",
}
```
```json
{
    "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
    "name": "2B"
}
```

### Delete library

`DELETE /library/:id`

header {
    Authorization: Bearer token
}

---