# Edge TTS API

Edge TTS API is a FastAPI-based service that provides text-to-speech (TTS) functionality using Microsoft's Edge TTS service.

## Project Structure

```
.gitignore
.idea/
    .gitignore
    edge-tts-api.iml
    inspectionProfiles/
        profiles_settings.xml
        Project_Default.xml
    misc.xml
    modules.xml
    vcs.xml
    workspace.xml
api.py
docker-compose.yml
Dockerfile
edgettsapi/
    __init__.py
    model/
        __init__.py
        TtsRequest.py
        Voice.py
LICENSE
README.md
requirements.txt
```

## Installation
Clone the repository: 

```bash
$ git clone <repository-url> cd edge-tts-api
```

Build and run the Docker container: 

```bash
$ docker-compose up --build
```

## API Endpoints

### POST /tts

Converts text to speech.

#### Request Body: 

TtsRequest (defined in edgettsapi/model/TtsRequest.py)

#### Response: 

FileResponse containing the audio file.


### GET /voices

Retrieves a list of available voices.

#### Response: 

List of Voice (defined in edgettsapi/model/Voice.py)

#### Environment Variables

- EDGE_TTS_BASE_URL: Base URL for the API (default: http://localhost:8000)

## Dependencies

The project dependencies are listed in the requirements.txt file and include:

- fastapi
- uvicorn
- edge-tts
- pydantic
- python-dotenv

## Development

Running Locally

Install dependencies: 

```bash
$ pip install -r requirements.txt
```

Run the application: 

```bash
$ python api.py
```

## Using Docker

Build the Docker image: 

```bash
$ docker build -t edge-tts-api .
```

Run the Docker container: 

```bash
$ docker run -p 8000:8000 edge-tts-api
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.