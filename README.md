\# CI/CD Demo App



A Flask app with a fully automated CI/CD pipeline: push to `main` →

tests run → Docker image builds and pushes to Docker Hub → 

auto-deploys to a live AWS EC2 instance.



\## Architecture

GitHub Push → GitHub Actions (test → build → push image) → 

Docker Hub → SSH deploy → AWS EC2 (Ubuntu, Docker) → Live app



\## Tech Stack

Python, Flask, Docker, GitHub Actions, AWS EC2



\## Live demo

http://YOUR\_EC2\_IP:5000



\## Run locally

\\`\\`\\`

pip install -r requirements.txt

python app.py

\\`\\`\\`

