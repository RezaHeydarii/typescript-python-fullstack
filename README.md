# Typescript-Python-Fullstack

A **monorepo** built with **TurboRepo** that demonstrates a full-stack architecture combining **Python** and **TypeScript**. This Proof of Concept (POC) explores how both languages can coexist efficiently within the same project. It includes:

- A **Python backend** using [FastAPI].
- A **frontend** written in **Next.js** using **TypeScript**.
- **Cron jobs** for background tasks, written in Python.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)

## Features
- **Monorepo structure** with **TurboRepo** for easy management of multiple projects.
- **Python FastAPI/Flask** backend for serving APIs.
- **Next.js** with **TypeScript** for the frontend, providing SSR and static site generation.
- **Cron jobs** using Python for scheduled tasks.
- **Seamless integration** between **TypeScript** and **Python** for full-stack development.

## Tech Stack
- **TurboRepo** for monorepo management
- **Python** with [FastAPI] (backend) and cron jobs
- **TypeScript** with **Next.js** (frontend)
- **Docker** for containerization (optional)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/RezaHeydarii/typescript-python-fullstack.git
    ```
2. Navigate to the project directory:
    ```bash
    cd typescript-python-fullstack
    ```
3. Install dependencies:
    ```bash
    yarn install
    ```
4. Set up Python environment:
    ```bash
    yarn prepare-repo
    ```
5. Run TurboRepo to start all projects:
    ```bash
    turbo run dev
    ```

## Usage
### Running the Backend (Python)
   To start the backend API server, run:
   ```bash
   yarn dev:python-server
   ```

### Running the Frontend (Next.js)
   To start the Next.js server, run:
   ```bash
   npm run dev:web-app
   ```

### Running Python Cron Jobs
   To execute the cron jobs, run:
   ```bash
   cd apps/cronjobs
   python cronjob.py
   ```

## Folder Structure
```
typescript-python-fullstack/
├── apps/
│   ├── server/         # Python FastAPI app
│   ├── web-app/        # Next.js app with TypeScript
│   └── data-extractors/        # Python cron jobs
├── packages/            # Shared packages
│   ├── eslint-config/         # eslint configs
│   └── typescript-config/        # typescript configs
├── turbo.json           # TurboRepo configuration
├── package.json         # Dependencies and scripts
└── README.md
```

This structure should give clear instructions to anyone who wants to understand or contribute to your `typescript-python-fullstack` project. Let me know if you'd like any additional customizations!