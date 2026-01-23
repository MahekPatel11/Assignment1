# Git, Linux Shell, Docker & Streamlit – Practical Assignments Portfolio 🚀

## 🔍 Project Summary

This repository showcases a complete hands-on implementation of foundational DevOps and application development concepts using Git, Linux Shell Scripting, Docker, and Streamlit.

Each task is organized into its own directory to ensure clean separation of concerns and to follow best practices commonly used in professional software development environments.

Through these assignments, practical experience was gained in:
- Linux command-line usage and automation
- Version control workflows with Git and GitHub
- Containerization using Docker
- Building interactive web applications with Streamlit
- Managing an end-to-end project lifecycle using Git

---

## ⚙️ Technologies & Environment

- **Operating System:** Ubuntu (Linux)
- **Version Control:** Git, GitHub
- **Scripting Language:** Bash (Shell)
- **Programming Language:** Python 3.10
- **Web Framework:** Streamlit
- **Container Platform:** Docker

---

## 📁 Directory Layout
```text
Assignments/

├── git_assignment/
│   ├── README.md

├── shell_assignment/
│   ├── welcome.sh
│   ├── machine_details.sh
│   ├── intro.sh
│   ├── check_file.sh
│   ├── even_numbers.sh
│   ├── valide_function.sh
│   ├── users.sh
│   ├── safe_read.sh
│   └── server.log

├── docker_assignment/
│   ├── app.py
│   └── Dockerfile

└── streamlit_assignment/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    └── README.md
```
## 📗 Git Version Control Assignment

### Concepts Implemented
- Initializing local Git repositories  
- Tracking file changes and committing updates  
- Creating and switching between branches  
- Merging feature branches into the main branch  
- Connecting local repositories with GitHub  
- Resolving merge conflicts manually  
- Reverting and resetting commits  
- Cleaning commit history using interactive rebase  

## Git Commands Used

1. **Initialize and Track Changes**
   - `git init` → Initialize a new Git repository
   - `git add` → Stage changes for commit
   - `git commit` → Commit staged changes to the repository

2. **Branching and Switching**
   - `git branch` → List or create branches
   - `git checkout` → Switch between branches
   - `git merge` → Merge one branch into another

3. **Remote Repositories**
   - `git remote` → Manage remote repository connections
   - `git push` → Push local commits to a remote repository
   - `git pull` → Fetch and merge changes from a remote repository

4. **Undoing Changes and History Manipulation**
   - `git revert` → Revert a commit by creating a new commit
   - `git reset` → Undo commits or staging
   - `git rebase -i` → Interactively rebase commits for cleanup or reordering

### Key Concepts Covered in Git

- **Repository initialization** → Setting up a new Git repository using `git init`
- **Branching and merging** → Creating branches, switching between them, and merging changes
- **Working with remote repositories** → Connecting to remote repositories and syncing changes using `git push` and `git pull`
- **Handling merge conflicts** → Resolving conflicts that occur during merges
- **Undoing changes** → Reverting commits, resetting changes, and cleaning commit history

---

## 📘 2. Shell Scripting Assignment

### Topics Practiced
1. Navigating the Linux file system and using core terminal commands  
2. Creating basic shell scripts such as welcome messages and system detail scripts  
3. Declaring variables and accepting user input from the terminal  
4. Applying conditional logic using if–else statements  
5. Implementing loops for repetitive tasks  
6. Defining and using functions within shell scripts  
7. Performing text manipulation using tools like grep, sed, and awk  
8. Working with arrays in shell scripts  
9. Managing errors and debugging shell scripts  

### Practical Skills Developed
- Developing and executing Bash scripts  
- Automating routine command-line tasks  
- Analyzing and processing log and text files  
- Handling errors and improving script reliability

---

## 📘 3. Docker Assignment

### Work Performed
- Studied Docker fundamentals and compared containerization with virtual machines  
- Installed Docker on a Linux system and validated the setup  
- Downloaded official images from Docker Hub  
- Executed, stopped, and removed Docker containers  
- Created a Dockerfile for a Python-based application  
- Built Docker images and ran them locally  

### Files Provided
- `app.py` – Basic Python program for Docker execution  
- `Dockerfile` – Configuration file used to build the Docker image  

---

## 📘 4. Streamlit + Docker + Git Capstone Project

### Project Overview
A basic Streamlit web application displaying a Hello World message along with user interaction. The application is containerized using Docker and managed through Git and GitHub.

### Key Highlights
- Interactive user interface built using Streamlit  
- Docker-based setup for consistent application deployment  
- Use of Git branches for separate development and Docker workflows  
- Version tagging to manage project releases  

### Implementation Steps
1. Initialized a dedicated Git repository for the project  
2. Developed a Streamlit application with interactive components  
3. Executed and tested the application locally  
4. Created a `requirements.txt` file to manage dependencies  
5. Dockerized the Streamlit application using a Dockerfile  
6. Built and ran the Docker container with the required port mapping  
7. Accessed the application through a web browser  
8. Managed development using separate Git branches  
9. Merged branches and resolved conflicts where necessary  
10. Tagged the final release version and pushed the code to GitHub  

---

## ▶️ Running the Capstone Project

### Local Execution

pip install -r requirements.txt
streamlit run app.py
Access the application at:

http://localhost:8501
Docker-Based Execution
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
Access the application at:

http://localhost:8501
🔖 Release & Version Management
A stable project version was created using Git tags:

git tag v1.0,
git push origin v1.0

## 🌟 Key Learnings
- Improved proficiency in Git and GitHub version control workflows  
- Gained practical experience with Linux commands and shell scripting  
- Developed hands-on knowledge of Docker containerization  
- Successfully built and deployed an interactive Streamlit application  
- Followed industry-relevant development and deployment standards  

---

## 👤 Contributor
**Mahek Patel**  
AI/ML Trainee

---

## 📌 Final Summary
This repository showcases hands-on experience with core development and DevOps tools, highlighting the ability to follow structured workflows, write maintainable code, and deploy applications using modern technologies.






