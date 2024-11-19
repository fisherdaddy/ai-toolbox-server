# AI Toolbox Server

A Flask-based API server for AI tools and services.

## Features

- RESTful API endpoints
- Blueprint-based architecture
- Ready for Vercel deployment

## Setup

1. Clone the repository:
```bash
git clone [your-repository-url]
cd ai-toolbox-server
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python api/index.py
```

## Deployment

This project is configured for deployment on Vercel. Simply push to your GitHub repository and connect it to Vercel for automatic deployments.

## Project Structure

```
.
├── api/
│   └── index.py          # Main entry point
├── app/
│   ├── routes/           # API routes
│   └── services/         # Business logic
├── requirements.txt      # Python dependencies
└── vercel.json          # Vercel configuration
```

## License

MIT
