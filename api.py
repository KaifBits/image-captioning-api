
from io import BytesIO

from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError

from imageCaptioning import generate_caption

app = FastAPI(title="Image Captioning API")


@app.get("/")
def home():
    return {"message": "Image Captioning API is running"}


@app.post("/caption")
def create_caption(image: UploadFile = File(...)):
    # Accept only supported image formats
    if image.content_type not in {
        "image/jpeg",
        "image/png",
    }:
        raise HTTPException(
            status_code=415,
            detail="Please upload a JPG or PNG image."
        )

    try:
        image_bytes = image.file.read()

        pil_image = Image.open(BytesIO(image_bytes))
        pil_image.load()

        caption = generate_caption(pil_image)

        return {
            "filename": image.filename,
            "caption": caption.capitalize()
        }

    except (UnidentifiedImageError, OSError):
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is not a valid image."
        )
