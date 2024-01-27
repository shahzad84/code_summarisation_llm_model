# Code Summarization API

This project implements a FastAPI-based API for summarizing code using OpenAI's GPT-3.5-turbo model.

![Image description](img.png)

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/) (v3.6 or higher)

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your-api-key-here
    ```

### Running the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
