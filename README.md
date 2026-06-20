# Architecture Agent

AI-powered Architecture Governance Platform built with FastAPI, Next.js, PostgreSQL, Ollama, and Mermaid.

## Screenshots

### Assessment Page

<img src="screenshots/assessment.png" width="900"/>

### History Page

<img src="screenshots/history.png" width="900"/>

### Findings Page

<img src="screenshots/findings.png" width="900"/>

### AI Architecture Assistant Page

<img src="screenshots/assistant.png" width="900"/>

### Architecture Page

<img src="screenshots/architecture.png" width="900"/>

## Overview

Architecture Agent is an AI-powered Architecture Governance Platform that combines infrastructure analysis, architecture visualization, Retrieval-Augmented Generation (RAG), and local Large Language Models (LLMs) to provide actionable architecture insights and recommendations.

The platform analyzes infrastructure repositories, stores assessment reports, retrieves historical architecture context, and leverages AI to generate architecture redesigns, remediation guidance, and interactive architecture conversations.

The platform helps engineers and architects understand:

* Current architecture
* Security risks
* Reliability concerns
* Scalability bottlenecks
* Cost optimization opportunities
* Target architecture recommendations

---

## Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Protected APIs
* User-specific report isolation

### Architecture Assessment

Analyze infrastructure repositories and generate:

* Findings
* Overall architecture score
* Security observations
* Compliance insights
* Benchmark results
* Recommendations

### Assessment History

Store assessment reports in PostgreSQL and review them later.

Features:

* Historical reports
* User-specific report access
* Report details page
* Pagination support

### Architecture Diagrams

Generate Mermaid-based visual architecture diagrams.

Capabilities:

* Current architecture visualization
* Mermaid source view
* Interactive diagram rendering

### AI Architecture Refactoring Advisor

Generate AI-powered redesign recommendations.

Outputs:

* Current Problems
* Target Architecture
* Migration Plan
* Architecture Scorecard
* Target Architecture Diagram

Powered by Ollama.

### AI Chat Assistant

Chat with an AI assistant about a specific assessment.

Examples:

* Explain findings
* Suggest improvements
* Answer architecture questions
* Recommend best practices

### Remediation Recommendations

Generate actionable remediation guidance for:

* Security issues
* Infrastructure risks
* Misconfigurations
* Compliance concerns

### PDF Export

Export assessment reports as PDF documents.

---

## AI Capabilities

### Retrieval-Augmented Generation (RAG)

The platform uses Retrieval-Augmented Generation (RAG) to provide context-aware responses.

Assessment reports are persisted and retrieved as contextual knowledge for AI-powered features such as:

- Architecture Chat Assistant
- Architecture Redesign Advisor
- Remediation Recommendations
- Historical Assessment Analysis

### LangChain Integration

LangChain is used to orchestrate AI workflows and manage interactions with local LLMs running through Ollama.

Capabilities include:

- Prompt orchestration
- Context injection
- Retrieval workflows
- Architecture reasoning
- Recommendation generation

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* JWT Authentication
* ReportLab
* Ollama

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* Mermaid

### Database

* PostgreSQL

### AI

* Ollama
* Llama Models

---

## Project Structure

```text
backend/
├── app/
│   └── api/
├── db/
├── models/
├── services/
├── alembic/
└── main.py

frontend/
├── src/
│   ├── app/
│   ├── components/
│   ├── services/
│   └── lib/
```

## Backend Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create:

```text
backend/.env
```

Example:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/architecture_agent

JWT_SECRET=your_secret_key

JWT_ALGORITHM=HS256

OLLAMA_URL=http://localhost:11434

CORS_ORIGINS=http://localhost:3000
```

### 4. Run Database Migrations

```bash
alembic upgrade head
```

### 5. Start Backend

```bash
uvicorn backend.main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Frontend Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment Variables

Create:

```text
frontend/.env.local
```

Example:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Start Frontend

```bash
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

## Ollama Setup

Install Ollama:

https://ollama.com

Pull a model:

```bash
ollama pull llama3
```

Run Ollama:

```bash
ollama serve
```

Verify:

```bash
curl http://localhost:11434/api/tags
```

---

## Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE architecture_agent;
```

Update:

```env
DATABASE_URL
```

to match your local configuration.

---

## API Endpoints

### Authentication

```http
POST /api/v1/register
POST /api/v1/login
```

### Assessments

```http
POST /api/v1/architecture/analyze
```

### Reports

```http
GET /api/v1/reports
GET /api/v1/reports/{id}
```

### Architecture Diagrams

```http
POST /api/v1/reports/{id}/diagram
```

### Architecture Redesign

```http
POST /api/v1/reports/{id}/redesign
```

### Chat Assistant

```http
POST /api/v1/reports/{id}/chat
```

### Remediation

```http
POST /api/v1/reports/{id}/remediation
```

### PDF Export

```http
GET /api/v1/reports/{id}/export/pdf
```

### Health

```http
GET /health
```

---

## Production Readiness

Implemented:

* JWT Authentication
* Pagination
* Health Checks
* Environment Configuration
* Structured Logging
* Global Error Handling
* Docker Support
* PostgreSQL Persistence

---

## Future Enhancements

* Architecture Drift Detection
* Team Collaboration
* Role-Based Access Control
* Cloud Cost Analysis
* CI/CD Integrations
* Multi-Cloud Support
* Kubernetes Deep Analysis
* Terraform State Analysis

---

## Author

Ramuswaminaath Jeyapiragash

AI-powered Architecture Governance Platform built as a full-stack cloud architecture analysis and recommendation system.

