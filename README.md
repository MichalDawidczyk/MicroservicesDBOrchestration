# Microservices Database Orchestration Platform

A production-grade microservices architecture built with **Python**, **FastAPI**, **SQLModel**, **PostgreSQL**, and **Kafka**.  
Each service owns its **own database**, communicates asynchronously through an **event bus**, and is deployed using **Docker**.

## Architecture Overview

The platform consists of several independent microservices:

### **User Service**
- User registration, login, JWT authentication  
- Own PostgreSQL database  
- SQLModel models + Alembic migrations  

### **Order Service**
- Order creation, status updates, history  
- Publishes events: `order_created`  
- Consumes events: `payment_success`, `payment_failed`  

### **Payment Service**
- Mock payment processor (success/failure simulation)  
- Consumes `order_created`  
- Publishes `payment_success` / `payment_failed`  

### **API Gateway**
- Unified entrypoint for all services  
- JWT validation  
- Routing to internal services  
- Optional Traefik/Nginx reverse proxy  

### **Event Bus**
- Kafka 
- Asynchronous communication  
- DLQ (Dead Letter Queue) support  
  
---

## 🧱 Tech Stack

| Area | Technology |
|------|------------|
| Backend | Python, FastAPI |
| ORM | SQLModel |
| Databases | PostgreSQL |
| Messaging | Kafka |
| Auth | JWT |
| Infrastructure | Docker, Docker Compose |