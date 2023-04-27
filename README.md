# OpenAI Examples

1. Set the API Key by copying the `.env` and setting the values
```
cp .env.example .env
```
2. Install the dependencies
```
pip install -r requirements.txt
```

## Image Magick Processing

Install it running the following command:
```
brew install imagemagick
```

- Create white rectangle
```
convert -size 256x256 xc:"#FFFFFF" resources/white.png
```
- Resize image
```
magick img.png -resize '375x375!' output.png
```