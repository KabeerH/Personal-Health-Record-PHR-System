# Personal-Health-Record-PHR-System - Using python HTTP.Server

# Development Process

## System Architecture (design) used: 

For this project I decided to use a microservice architecture style approach the reason why I chose this approach is because this type of architecture can have many benefits:

- Scalability: The microservices can be scaled on an independent level based on the demand. If one of the services scales with a lot of traffic then that service will be scaled up without touching the other parts of my application
- Maintenance: These microservices are independent and loosely coupled. This allows easy maintenance with the application
- Agility: Each microservice is small and can focus on a specific function allowing for easier management
- Many aspects: In a microservice style each microservice is referred to a different aspect of the overall application: In a PHR system we can have one service responsible for the (user auth, user registration, etc (frontend)) and other for the creation, retrieving, updating and deleting records (CRUD).

## Vision Statement

`FOR` individuals `WHO` need to view, add and send personal health records securely to healthcare providers, THE PHR system application is a tool to achieve these tasks `THAT` allow the user to make new records, view any record that is related to them or even send them to other people or providers, these features can be accessed by the user at anytime via APIS. `UNLIKE` traditional PHR systems, this system focuses on the needs of the users through personas and user stories. It uses a microservice approach to get the best results. `OUR` product lets the user manage their health information and records in a secure environment with the proper security measures to ensure that no sensitive information gets leaked to anyone beside them or the trusted people they send the data to.

FORMAT USED: (Moore’s vision template)

- FOR (target customer)
- WHO (statement of the need or opportunity)
- THE (Product name) is a (product category)
- THAT (key benefit, compelling reason to buy)
- UNLIKE (primary competitive alternative)
- OUR PRODUCT (statement of primary differentiation

## Personas

Persona one: Mike Cull, Freelancer (patient) 

- Age: 57
- Occupation: Freelancer
- Current Health: Diabetic with low blood sugar levels
- Currently needs: Needs monthly checkups, so needs to send those results to his healthcare provider
- What the PHR system does for him: The PHR system allows Mike to send his test results to his healthcare provider in a secure way. This allows communication between the two parties only and no one else.

Persona two: Sam Buck, Doctor 

- Age: 34
- Occupation: Doctor
- Current Health: Healthy
- Currently needs: Needs a way to receive patient records so he can make the appropriate assessment to his patients.
- What the PHR system does for him: The PHR system allows Sam to receive records from the system securely so he can follow up with his patients keeping confidentiality between the two parties.

Persona three: Billy Meek, professional football player (patient)

- Age: 23
- Occupation: Professional football player
- Currently needs: Since Billy needs to stay fit and healthy to play his football matches he needs to get regular tests done to see if any issues occur with his health, and get the appropriate treatment.
- What the PHR system does for him: The PHR system allows Billy to view his records of his tests done for reference so if he has any concerns he can take up with his healthcare provider. 

## Scenarios and user stories:

- `Name`: Mike Cull
- Scenario: While doing his monthly checkup, after getting the results he needs to send those records to his healthcare provider
- User Story: As Mike a diabetic with low blood sugar, I want to share my test results with my healthcare provider so he can consult with me.


- `Name`: Sam Buck
- Scenario: On a normal day as a doctor, Sam needs to access records of different patients to make the correct assessments but doesn’t want to keep hardcopy of the records in his office 
- User Story: As Sam a healthcare professional, I want to access patients records so I can make assessments with them

- `Name`: Billy Meek
- Scenario: Billy during a game feels dizzy and nauseous and faints. He doesn’t understand why, so goes to check his records on the PHR system to see what could have caused this.
- User Story: As Billy a professional football player, I want to view my health records, so I know what caused me to faint during my game.

# PHR System Documentation

## Overview of Application

This application is a system that uses the built-in package `http.server`  to handle HTTP requests that allow the user to create, recieve, update and delete requests. For data storage I am using a SQlite database that is implemented inside my code where if the database is not presented then make one.

## Tools and Technology Used
- Programming Language: Python 
- Database: SQlite 
- Version Control: Git 
- Containerization: Docker 
- API Testing: Postman

## Getting Started

1. Clone the repository using the command in cmd
```bash
git clone https://github.com/KabeerH/Personal-Health-Record-PHR-System
```
2. Change to the directory where you have cloned the project
```bash
cd directory
```
3. To build the project using docker
```bash 
docker-compose up --build
```
4. To start the project if not started
```bash 
docker-compose up 
```
5. To Stop the application and delete the container
```bash
docker-compose down
```

Once the application is started, you can go to http://localhost:8000/ to access the application

## METHODS Functions

### GET (ALL) /

This endpoint retrieves all notes from the database.

- Method: `GET`
- URL: `/`

**Usage with Postman:**
1. Set the HTTP method to `GET`.
2. Enter the request URL as `http://localhost:8000/`.
3. Click on `Send` to make the request.

![Screenshot 2024-03-06 164025](https://github.com/KabeerH/Personal-Health-Record-PHR-System/assets/122492914/49256844-32b6-4e16-9199-e23b06cb6ee0)

### GET (record by record_id) /records/:record_id

This endpoint retrieves records by the record_id in the database

- Method: `GET`
- URL: `/records/:record_id`

**Usage with Postman:**
1. Set the HTTP method to `GET`.
2. Enter the request URL as `http://localhost:8000/records/record_id`.
3. Click on `Send` to make the request.

![Screenshot 2024-03-06 164249](https://github.com/KabeerH/Personal-Health-Record-PHR-System/assets/122492914/fe64d259-daa0-4692-8618-a915747823bf)

### POST /records

This endpoint creates a new record in the database.

- Method: `POST`
- URL: `/records`
- Request Body: A JSON object containing 'record_id', 'full_name', 'dob', 'sex', 'allegries', ''medications', 'diagnosis', 'treatment', and 'notes'
  
**Usage with Postman:**
1. Set the HTTP method to `POST`.
2. Enter the request URL as `http://localhost:8000/records`.
3. Click on `Body`, then select `raw` and `JSON`.
4. In the text field, enter your note in the format: 'record_id', 'full_name', 'dob', 'sex', 'allegries', ''medications', 'diagnosis', 'treatment', and 'notes'
5. Click on `Send` to make the request.

![Screenshot 2024-03-06 163724](https://github.com/KabeerH/Personal-Health-Record-PHR-System/assets/122492914/f57c0b2e-772e-410c-9dbc-32d1798e49c6)


### PUT /notes

This endpoint updates an existing note in the database.

- Method: `PUT`
- URL: `/records`
- Request Body: A JSON object containing record_id', 'full_name', 'dob', 'sex', 'allegries', ''medications', 'diagnosis', 'treatment', and 'notes'

**Usage with Postman:**
1. Set the HTTP method to `PUT`.
2. Enter the request URL as `http://localhost:8000/records`.
3. Click on `Body`, then select `raw` and `JSON`.
4. In the text field, enter your note in the following format: record_id', 'full_name', 'dob', 'sex', 'allegries', ''medications', 'diagnosis', 'treatment', and 'notes'
5. Click on `Send` to make the request.

![image](https://github.com/KabeerH/Personal-Health-Record-PHR-System/assets/122492914/a824b598-9ef4-48a3-b475-5851163222c5)

### DELETE /records/:record_id

This endpoint deletes a note from the database.

- Method: `DELETE`
- URL: `/records/:record_id`

**Usage with Postman:**
1. Set the HTTP method to `DELETE`.
2. Enter the request URL as `http://localhost:8000/records/record_id`.
3. change record_id with the id you trying to delete
4. Click on `Send` to make the request

![image](https://github.com/KabeerH/Personal-Health-Record-PHR-System/assets/122492914/cff7144d-2ca2-4e66-84f0-74adcbdbc222)

## Security precautions made: 

- User Authentication: Using Basic Authentication the system first verifies the identity of the user. When making any request to the system it checks the user’s credentials.

- Password Hashing: Whenever a new user is added to the system, their data is hashed using the SHA-256 before storing the data into the SQlite database, if someone gets access to the users table then the data won’t show their password but instead hashed values.

- Access Control: The records are associated with the user, the system will check which user is trying to access what data and only return the data associated with that user ensuring data security. 


## Contributors 

- Kabeer Harjani | https://github.com/KabeerH
