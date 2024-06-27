# SandCodes Hackathon Submission

This is My sandcodes hackathon submission.

**Hackathon Theme:** Planet Hackunia Needs Your Help!

try it [here](#try-it-here).

---

# SpaceTec Survival Guide

Welcome to the SpaceTec Survival Guide project! This repository contains the source code for a responsive website designed to assist humanity in surviving an alien invasion. The project includes real-time alien detection maps, a survival guide, and a chat assistant powered by ChatGPT-3.5-turbo.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

The SpaceTec Survival Guide is a web application developed to provide essential tools and information during an alien invasion. The website is responsive across all device sizes and includes a survival guide, real-time alien detection map, and chat assistant for user support.

## Features

- **Responsive Design:** Compatible with all device sizes using HTML, CSS, JavaScript, and Bootstrap.
- **Backend:** Built with FastAPI in Python.
- **Google Maps Integration:** Displays real-time alien detection markers.
- **Chat Assistant:** Integrated with ChatGPT-3.5-turbo API endpoint using gpt4free.
- **Pages:**
  - Home Page
  - Survival Guide Page
  - Alien Detection Map Page
  - Chat Assistant Page

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap CSS
- **Backend:** Python, FastAPI
- **API Integration:** Google Maps API, ChatGPT-3.5-turbo API (gpt4free)
- **Deployment:** Vercel (Backend), GitHub Pages (Frontend)

## Project Structure

```
/project-root
│── /frontend
│   ├── index.html
│   ├── survival-guide.html
│   ├── map.html
│   ├── chat.html
│   ├── /css
│   └── /js
│── /backend
│   ├── main.py
│   └── /models
│── README.md
└── ...
```

## Endpoints

### Get Markers
```http
GET /markers
```
**Response:** List of markers.

### Add Marker
```http
POST /markers
```
**Body:** Marker object.

**Response:** Added marker object.

### Chatbot Response
```http
GET /chatbot/{message}
```
**Path Parameter:** User message.

**Response:** ChatGPT-3.5-turbo reply.

## Installation

### Prerequisites
- Python 3.7+
- Node.js and npm
- Git

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/spacetec-survival-guide.git
    cd spacetec-survival-guide/backend
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Open `index.html` in your preferred browser to view the homepage.

## Usage

- **Home Page:** Provides an overview and latest updates.
- **Survival Guide Page:** Detailed tips and strategies for surviving the alien invasion.
- **Alien Detection Map Page:** Displays real-time locations of aliens using Google Maps API.
- **Chat Assistant Page:** Offers real-time chat support using ChatGPT-3.5-turbo.

## Deployment

### Backend
- Deployed on Vercel.

### Frontend
- Hosted on GitHub Pages.

---

### Try it here

Link for the hosted site [SpaceTec Website](https://nasheethahmeda.github.io/Space-Tec-Website).
