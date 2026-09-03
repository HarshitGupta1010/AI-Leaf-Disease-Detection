# Leaf Disease Detection

An AI-powered plant leaf analysis application. Upload a leaf image to identify possible diseases, estimate severity and confidence, and receive symptoms, likely causes, and treatment recommendations.

The project provides:

- A Streamlit web interface for interactive image analysis.
- A FastAPI endpoint for programmatic image uploads.
- Groq vision-model integration for leaf and disease analysis.
- Handling for healthy leaves and invalid, non-leaf images.

## Requirements

- Python 3.10 or newer
- A [Groq API key](https://console.groq.com/keys)

## Setup

1. Clone the repository and open its directory:

   ```bash
   git clone https://github.com/HarshitGupta1010/AI-Leaf-Disease-Detection.git
   cd AI-Leaf-Disease-Detection
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

   Do not commit `.env` or expose your API key publicly.

## Run the Streamlit App

```bash
streamlit run main.py
```

Open the local URL shown by Streamlit, upload a JPG, JPEG, or PNG leaf image, and select **Detect Disease**.

## Run the FastAPI Service

```bash
uvicorn app:app --reload
```

The API is available at `http://127.0.0.1:8000`.

### API Endpoints

#### `GET /`

Returns basic API information.

#### `POST /disease-detection-file`

Upload an image using `multipart/form-data` with the field name `file`.

Example with cURL:

```bash
curl -X POST "http://127.0.0.1:8000/disease-detection-file" \
  -F "file=@path/to/leaf-image.jpg"
```

The JSON response includes the detected disease status, disease name and type, severity, confidence, symptoms, possible causes, treatment recommendations, and an analysis timestamp.

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Configuration

The following environment variables are supported:

| Variable | Default | Description |
| --- | --- | --- |
| `GROQ_API_KEY` | Required | API key used to call Groq. |
| `MODEL_NAME` | `meta-llama/llama-4-scout-17b-16e-instruct` | Groq vision model used for analysis. |
| `MODEL_TEMPERATURE` | `0.3` | Response randomness setting. |
| `MAX_COMPLETION_TOKENS` | `1024` | Maximum response length. |

## Project Structure

```text
.
├── main.py                 # Streamlit user interface
├── app.py                  # FastAPI application
├── utils.py                # Image conversion and detector integration
├── Leaf Disease/
│   ├── main.py             # LeafDiseaseDetector implementation
│   └── config.py           # Environment-backed configuration
├── requirements.txt        # Python dependencies
└── vercel.json             # Deployment configuration
```

## Notes

This tool provides AI-generated guidance and is intended for informational use. Confirm diagnoses and treatment decisions with a qualified agricultural professional, especially before applying chemicals to plants.

## License

No license has been specified for this repository.