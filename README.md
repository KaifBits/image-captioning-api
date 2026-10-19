# Image Captioning API

A REST API that generates natural-language captions for uploaded images using a pretrained deep learning model.

## Features

- Upload JPG and PNG images
- Generate captions through a FastAPI endpoint
- Receive results in JSON format
- Interactive Swagger API documentation
- Original Streamlit app included

## Tech Stack

- Python 3.11
- TensorFlow / Keras
- FastAPI
- Uvicorn
- Pillow

## Project Structure

```text
image-captioning-api/
+-- api.py
+-- imageCaptioning.py
+-- main.py
+-- requirements.txt
+-- models/
    +-- encoded_test_img_features.pkl
    +-- idx_to_word.pkl
    +-- model_weights_25.h5
    +-- word_to_idx.pkl
## Installation

1. Clone this repository.
2. Create and activate a Python 3.11 virtual environment.
3. Install dependencies:

```bash
python -m pip install -r requirements.txt

```

4. Run the API:

```bash
python -m uvicorn api:app
```

5. Open http://127.0.0.1:8000/docs to test the API.

## API Endpoint

`POST /caption`

Upload a JPG or PNG image using the multipart form field named `image`.

Example JSON response:

```json
{
  "filename": "example.jpg",
  "caption": "A sample image caption"
}
```

## Credits

The original image-captioning implementation was adapted from:
https://github.com/gautamgc17/Image-Captioning

Please check the original project's license and model-weight terms before redistributing its code or assets.

## Disclaimer

This project is intended for learning and experimentation. Caption quality depends on the pretrained model.
