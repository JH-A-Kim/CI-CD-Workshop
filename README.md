# GitHub Actions CI/CD in Practice

## Learning objectives
1.  Attendees will be able to **create** a basic `.yml` workflow file to automatically run unit tests on their code in GitHub Actions (CI).
2.  Attendees will be able to **configure** a `.yml` workflow file to automatically deploy their code to GitHub Pages (CD).
3.  Attendees will be able to **identify** and describe the key components of a GitHub Actions workflow file (Runner, Job, Step, Action).

## Pain, Dream, Fix

**Pain:**
Developers spend a significant amount of time debugging, testing, and ensuring code consistency across different environments. They have to manually verify code works before merging, which is tedious and error-prone. Furthermore, deploying changes is often a manual process that delays release; while one developer is deploying, another might push changes that aren't yet tested, leading to "integration hell."

**Dream:**
Imagine a world where a developer never has to manually run a test suite or SSH into a server to deploy. The moment they push a change, an automated pipeline takes over. Code is verified in a clean environment instantly. If it passes, it is deployed to production automatically. The developer focuses entirely on writing code, not plumbing.

**Fix:**
**GitHub Actions.** It allows for fully automated testing and deployment pipelines directly within the repository. We can ensure code velocity and consistency by defining "Infrastructure as Code." Testing becomes as simple as pushing a commit, and deploying becomes as simple as merging a Pull Request.

## Materials
* **Slide Deck:** https://docs.google.com/presentation/d/19q4MuYz5nqu4GSwMYKyRkUGMZO8QX8c4BrJz3M5tIck/edit?usp=sharing
* **Starter Repository:** A pre-made GitHub repo containing a simple Python application (`adder.py`, `tests/`) so students don't have to write app code from scratch.
* **GitHub Account:** Required for all attendees.
* **Laptop:** With Git installed.

## Activities

### Section 1: Introduction
**Goal:** Go over the slides and introduce the concepts

### Section 2: The CI Demo - Testing
**Goal:** Attendees create a pipeline that tests code on every Pull Request.

1.  **Setup:** Fork CI-CD-Workshop Repo
2.  **The Workflow:** Start working on the CI file `.github/workflows/ci.yml`.
    * *Live Coding:* 
4.  **Verification:**
    * create a new branch `break-code`.
    * Intentionally break the `adder.py` logic.
    * Open a Pull Request and watch the action **FAIL**.
    * Fix the code and watch the action **PASS**.

### Section 3: The CD Demo - Deployment
**Goal:** Create a pipeline that deploys the app to GitHub Pages on every push to main.

1.  **Configuration:** Show how to enable GitHub Actions in Pages
2.  **The Workflow:** Start working on the CD file `.github/workflows/deploy.yml`.
    * *Live Coding:* 
4.  **Verification:** Merge a pr into main with your name replacing the existing message in index.html

### Section 4: End
* Feedback/Questions
* Share links to documentation.
