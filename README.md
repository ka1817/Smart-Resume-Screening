# Smart Resume Screening (FastAPI + Docker + GitHub Actions + EC2)

---

## 🚀 Problem Statement

Recruiters spend hours manually screening hundreds of resumes for a single job opening, often missing qualified candidates due to time constraints or subjective bias. Traditional Applicant Tracking Systems (ATS) rely on keyword matching, which fails to evaluate context, relevance, or candidate potential accurately.

This inefficiency leads to:

 • Delays in hiring timelines

 • Poor candidate-job fit

 • Missed opportunities for top talent

There's a need for an intelligent, automated, and explainable resume screening system that can augment the recruitment process.

---

## 🚀 Introduction

Smart Resume Screening is an AI-powered web application that intelligently evaluates resumes against job descriptions using FastAPI, LangChain, and LLM (LLaMA3 via Groq).

It extracts meaningful information (skills, education, experience) from a PDF resume, compares it to a job description, and provides:

✅ 20 keyword match scores

🔍 Relevance-based insights

📊 Final score with shortlist verdict

🌐 Intuitive web interface using HTML/CSS/Bootstrap

🐳 Containerized with Docker & deployed on AWS EC2

⚙️ CI/CD automated via GitHub Actions

This tool is designed for HR professionals, startups, and tech recruiters who want to reduce manual screening effort and make faster, data-driven hiring decisions.

---

## 📁 Folder Structure

```
Smart_Resume_Screening/
├── .github/workflows/ci-cd.yml       # CI/CD config
├── src/                              # Core logic
│   ├── resume_parser.py              # PDF text extraction
│   ├── screening.py                  # LLM-based screening logic
│   └── prompt_template.txt           # Custom prompt
├── static/css/style.css              # Styling
├── templates/index.html              # Frontend UI
├── tests/                            # Pytest test files
├── main.py                           # FastAPI app
├── Dockerfile                        # Docker image build
├── requirements.txt                  # Python dependencies
├── pytest.ini                        # Pytest config
├── .env                              # API key & secrets (not committed)
├── .dockerignore
├── .gitignore
├── README.md
```

---

## 🔧 Git Commands (Version Control)

```bash
# Clone the repo
$ git clone https://github.com/ka1817/Smart-Resume-Screening.git

# Check status
$ git status

# Add changes
$ git add .

# Commit changes
$ git commit -m "your message"

# Push to GitHub
$ git push origin main
```

---

## 🪓 Docker Commands

```bash
# Build Docker image
$ docker build -t pranavreddy123/smart-resume-screening .

# Run container with GROQ API key and port
$ docker run -d -p 8000:8000 -e GROQ_API_KEY=your_key pranavreddy123/smart-resume-screening

# Check running containers
$ docker ps

# Stop container
$ docker stop <container_id>
```

---

## ⚖️ GitHub Actions: CI/CD

**Workflow file**: `.github/workflows/ci-cd.yml`

* **CI**: Runs `pytest` for test validation
* **CD**: Builds Docker image and pushes to DockerHub

### Secrets Required:

* `GROQ_API_KEY`
* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`

Triggers on push/pull requests to `main` (except `README.md` changes)

---

## 🚧 Deployment on AWS EC2

1. Launch Ubuntu EC2 instance and open port **8000** in the security group.
2. SSH into the instance:

   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```
3. Install Docker:

   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo systemctl start docker
   sudo systemctl enable docker
   ```
4. Pull and run Docker container:

   ```bash
   docker pull pranavreddy123/smart-resume-screening:latest

   docker run -d -p 8000:8000 -e GROQ_API_KEY=your_key pranavreddy123/smart-resume-screening
   ```
5. Visit `http://<EC2-IP>:8000` to access the app.

---

## 🌟 Highlights

* End-to-end resume screening pipeline
* Fully automated CI/CD
* Lightweight frontend + scalable backend
* Easily extensible to other LLMs or job formats

---

## 📅 Author

GitHub: [@ka1817](https://github.com/ka1817)
DockerHub: [`pranavreddy123`](https://hub.docker.com/u/pranavreddy123)

---

**License**: MIT

---

*Built with FastAPI ✨, powered by Groq AI 🧪*
