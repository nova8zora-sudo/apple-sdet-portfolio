# Apple SDET Portfolio
### Software Developer in Test — Video Applications Team

Professional test automation portfolio demonstrating expertise in video codecs, 
image formats, audio testing, and CI/CD pipelines.

Built with real iPhone footage and photos as test assets — mirroring the exact 
work done on the Apple Video Applications team.

![CI](https://github.com/nova8zora-sudo/apple-sdet-portfolio/actions/workflows/tests.yml/badge.svg)

---

## Projects

### 🎬 Video Codec Test Suite
Automated tests for H.264 and HEVC (H.265) video formats using FFmpeg and Python.
- Tests codec name, resolution, frame rate, duration, color space
- Uses real iPhone 13 Pro footage as test asset
- **10 passing tests**

### 📸 Image Format Validator
Automated EXIF metadata validation for HEIC images using ExifTool.
- Tests file type, camera model, resolution, color profile, lens data
- Uses real iPhone 13 Pro photos as test assets
- Validates Apple Display P3 wide color gamut
- **10 passing tests**

### 🔊 Audio Metadata Tester
Automated audio codec and metadata validation using FFmpeg and Python.
- Tests AAC codec, sample rate, stereo channels, Core Media Audio handler
- Extracted from real iPhone 13 Pro video footage
- **10 passing tests**

### ⚙️ CI Pipeline
GitHub Actions workflow that automatically runs all tests on every push.
- Runs on macos-latest
- Installs FFmpeg and ExifTool automatically
- Generates HTML test reports as artifacts

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9 | Test automation language |
| pytest | Test framework |
| FFmpeg / FFprobe | Video and audio inspection |
| ExifTool | Image metadata extraction |
| GitHub Actions | CI/CD pipeline |

---

## How to Run
```bash
# Install dependencies
pip3 install pytest pytest-html Pillow mutagen exifread
brew install ffmpeg exiftool

# Run video tests
cd video-codec-test-suite
python3 -m pytest test_video.py -v

# Run image tests
cd image-format-validator
python3 -m pytest test_images.py -v

# Run audio tests
cd audio-metadata-tester
python3 -m pytest test_audio.py -v
```

---

## Test Results

| Suite | Tests | Status |
|-------|-------|--------|
| Video Codec | 10 | ✅ Passing |
| Image Format | 10 | ✅ Passing |
| Audio Metadata | 10 | ✅ Passing |
| **Total** | **30** | **✅ All Passing** |
