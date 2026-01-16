microservices-db-orchestration/
│
├── services/
│   ├── user-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── api/
│   │   │   ├── core/
│   │   │   ├── models/
│   │   │   ├── db/
│   │   │   ├── events/
│   │   │   └── tests/
│   │   ├── alembic/
│   │   ├── alembic.ini
│   │   └── Dockerfile
│   │
│   ├── order-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── api/
│   │   │   ├── core/
│   │   │   ├── models/
│   │   │   ├── db/
│   │   │   ├── events/
│   │   │   └── tests/
│   │   ├── alembic/
│   │   ├── alembic.ini
│   │   └── Dockerfile
│   │
│   ├── payment-service/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── api/
│   │   │   ├── core/
│   │   │   ├── models/
│   │   │   ├── db/
│   │   │   ├── events/
│   │   │   └── tests/
│   │   ├── alembic/
│   │   ├── alembic.ini
│   │   └── Dockerfile
│
├── gateway/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── core/
│   │   └── tests/
│   └── Dockerfile
│
├── infrastructure/
│   ├── docker/
│   │   ├── docker-compose.yml
│   │   ├── kafka/
│   │   │   ├── docker-compose.kafka.yml
│   │   │   └── config/
│   │   └── postgres/
│   │       └── init.sql
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── monitoring/
│       ├── prometheus.yml
│       ├── grafana/
│       └── loki/
│
├── docs/
│   ├── architecture.md
│   ├── diagrams/
│   │   └── architecture.mmd
│   └── api/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .env.example
├── README.md
└── Makefile