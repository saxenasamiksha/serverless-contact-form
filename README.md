# Serverless Contact Form Using AWS Lambda & DynamoDB

This project demonstrates how to build a fully **serverless contact form** using **AWS Lambda**, **API Gateway**, and **DynamoDB**, without managing any backend servers

## Project Overview

**Frontend**: HTML + JavaScript (Fetch API)
**Backend**: AWS Lambda Function (Python)
**API Gateway**: REST endpoint to trigger Lambda
**Database**: DynamoDB table to store contact form submissions
**Deployment**: Fully cloud-based and scalable

---

 Technologies Used

- **HTML, CSS, JavaScript (Fetch API)**
- **AWS Lambda** (Python 3.10)
- **AWS API Gateway**
- **AWS DynamoDB**
- **IAM Roles & Policies**
- **GitHub for version control**

---

## Architecture

User (Browser)
|
v
[HTML Contact Form]
|
v
[API Gateway REST Endpoint]
|
v
[AWS Lambda Function]
|
v
[DynamoDB Table (ContactForm)]

serverless-contact-form/
├── contact.html # Frontend form with fetch() API
├── lambda_function.py # AWS Lambda backend (Python)
├── README.md # This file
├── screenshots/ # Output screenshots
└── recording.mp4 # Voice-over screen recording


---

## How It Works

1. User fills out the form and submits it
2. JavaScript `fetch()` sends the data to API Gateway
3. API Gateway triggers the Lambda function
4. Lambda stores the data into DynamoDB table
5. A response is sent back to the frontend and displayed to the user

---

## Testing

Open `contact.html` in your browser and fill the form. On submission, it will:

- Show a success message on screen
- Store the data in DynamoDB
- API URL used: `https://zduv86h97c.execute-api.ap-south-1.amazonaws.com/prod/submit`

---

##  Output Screenshots

| Screenshot                     | Description                          |
|-------------------------------|--------------------------------------|
| ![](screenshots/form.png)     | Contact form in browser              |
| ![](screenshots/dynamodb.png) | Data in DynamoDB table               |
| ![](screenshots/lambda.png)   | Lambda function showing invocation   |
| ![](screenshots/api.png)      | API Gateway configuration            |

---

##  Demo Video

 See `recording.mp4` in this repository for a full walkthrough with voice explanation.

---

##  Author

**Name**: *Your Name Here*  
**Internship**: RISE - Cloud Computing Track  
**Platform**: [https://www.tamizhanskills.com](https://www.tamizhanskills.com)

---

## Submission Info

✅ This GitHub repository contains:
- Source Code (HTML + Python)
- Output Screenshots
- Demo Screen Recording (with voice)
- Project Documentation (this README file)

