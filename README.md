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


### Create new student

`POST /students`

header {
    Authorization: Bearer token
}

```json
{
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2
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
    "id": 1,
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2
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
    "id": 1,
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2
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
    "name": "Hamburguer upgrade",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2
}
```

### Delete student

`DELETE /students/:id`

header {
    Authorization: Bearer token
}

---
## Employee

### Create new employee

`Post /employees`

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

### Get all employees

`GET /employees`

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

### Get only employee

`GET /employees/:id`

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

### Update employee

`PATCH /employees/:id`

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
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2,
    "quantity": 1
}
```

### Get all grades

`GET /grades`

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

### Get only grade

`GET /grades/:id`

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

### Update grade

`PATCH /grades/:id`

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

### Delete grade

`DELETE /grades/:id`

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
    "name": "Hamburguer",
    "category": "Sanduíches",
    "price": 7.99,
    "userId": 2,
    "quantity": 1
}
```

### Get all classrooms

`GET /classrooms`

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

### Get only classroom

`GET /classrooms/:id`

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

### Update classroom

`PATCH /classrooms/:id`

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

### Delete classroom

`DELETE /classrooms/:id`

header {
    Authorization: Bearer token
}

---