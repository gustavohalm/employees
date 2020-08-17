### Employees API

#### Run

```
  $ python manage.py migrate
  $ python manage.py runserver
```


### URL: http://localhost:8000
#### GET /api/employe/
##### Response
```
    [
        {
            "id": 0,
            "name": "Nome do Empregado",
            "departament": "Departamento"
        },
        {
            "id": 0,
            "name": "Nome do Empregado",
            "departament": "Departamento"
        },
        {
            "id": 0,
            "name": "Nome do Empregado",
            "departament": "Departamento"
        }    
    ]
```

#### GET /api/employe/{id}
##### Response
```
     {
        "id": 0,
        "name": "Nome do Empregado",
        "departament": "Departamento"
    }       
```

#### POST /api/employe/
##### Request
```
     {
        "name": "Nome do Empregado",
        "departament": "Departamento"
    }       
```
##### Response
```
     {
        "id": 0,
        "name": "Nome do Empregado",
        "departament": "Departamento"
    }       
```


#### PUT /api/employe/{id}
##### Request
```
     {
        "name": "Nome do Empregado",
        "departament": "Departamento"
    }       
```
##### Response
```
     {
        "id": 0,
        "name": "Nome do Empregado",
        "departament": "Departamento"
    }       
```

#### DELETE /api/employe/{id}
##### Response
``` 
    HTTP CODE 204
```
