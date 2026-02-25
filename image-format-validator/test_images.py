import subprocess
import json
import pytest

def get_exif(filepath):
    """Extract metadata using ExifTool."""
    result = subprocess.run(
        ["exiftool", "-json", filepath],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)[0]

class TestHEICFormat:
    """Tests for iPhone HEIC image format."""

    def test_file_type_is_heic(self):
        data = get_exif("IMG_4651.HEIC")
        assert data["FileType"] == "HEIC", \
            f"Expected HEIC, got {data['FileType']}"

    def test_camera_is_iphone(self):
        data = get_exif("IMG_4651.HEIC")
        assert "iPhone" in data["Model"], \
            f"Expected iPhone, got {data['Model']}"

    def test_resolution_is_12mp(self):
        data = get_exif("IMG_4651.HEIC")
        assert data["ImageWidth"] == 4032
        assert data["ImageHeight"] == 3024

    def test_has_date_taken(self):
        data = get_exif("IMG_4651.HEIC")
        assert "DateTimeOriginal" in data, \
            "Photo must have DateTimeOriginal metadata"

    def test_color_profile_is_p3(self):
        data = get_exif("IMG_4651.HEIC")
        assert "P3" in data["ProfileDescription"], \
            f"Expected Display P3, got {data['ProfileDescription']}"

    def test_has_aperture_data(self):
        data = get_exif("IMG_4651.HEIC")
        assert "FNumber" in data, \
            "Photo must contain aperture (FNumber) metadata"

    def test_has_iso_data(self):
        data = get_exif("IMG_4651.HEIC")
        assert "ISO" in data, \
            "Photo must contain ISO metadata"

    def test_has_lens_info(self):
        data = get_exif("IMG_4651.HEIC")
        assert "LensModel" in data, \
            "Photo must contain lens model metadata"

    def test_make_is_apple(self):
        data = get_exif("IMG_4651.HEIC")
        assert data["Make"] == "Apple"

    def test_second_photo_also_valid(self):
        data = get_exif("IMG_4618.HEIC")
        assert data["FileType"] == "HEIC"
        assert data["Make"] == "Apple"
        assert "DateTimeOriginal" in data