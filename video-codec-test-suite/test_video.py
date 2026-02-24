import subprocess
import json
import pytest

def get_video_info(filepath):
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_streams", filepath
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

def get_video_stream(filepath):
    info = get_video_info(filepath)
    return next(s for s in info["streams"] if s["codec_type"] == "video")

def get_audio_stream(filepath):
    info = get_video_info(filepath)
    return next(s for s in info["streams"] if s["codec_type"] == "audio")

class TestGeneratedVideo:
    """Tests for our generated test video"""

    def test_codec_is_h264(self):
        video = get_video_stream("sample.mp4")
        assert video["codec_name"] == "h264"

    def test_resolution_is_720p(self):
        video = get_video_stream("sample.mp4")
        assert video["width"] == 1280
        assert video["height"] == 720

class TestiPhoneVideo:
    """Tests for real iPhone footage — mirrors Apple SDET work"""

    def test_iphone_uses_hevc_codec(self):
        video = get_video_stream("iphone_sample.MOV")
        assert video["codec_name"] == "hevc", \
            f"Expected HEVC, got {video['codec_name']}"

    def test_iphone_resolution_is_1080p(self):
        video = get_video_stream("iphone_sample.MOV")
        assert video["width"] == 1920
        assert video["height"] == 1080

    def test_iphone_frame_rate_is_60fps(self):
        video = get_video_stream("iphone_sample.MOV")
        assert video["r_frame_rate"] == "60/1"

    def test_iphone_has_audio_track(self):
        audio = get_audio_stream("iphone_sample.MOV")
        assert audio["codec_name"] == "aac"

    def test_iphone_audio_is_stereo(self):
        audio = get_audio_stream("iphone_sample.MOV")
        assert audio["channels"] == 2

    def test_iphone_audio_sample_rate(self):
        audio = get_audio_stream("iphone_sample.MOV")
        assert audio["sample_rate"] == "44100"

    def test_iphone_color_space(self):
        video = get_video_stream("iphone_sample.MOV")
        assert video["color_space"] == "bt709"

    def test_iphone_has_metadata_streams(self):
        info = get_video_info("iphone_sample.MOV")
        metadata_streams = [s for s in info["streams"] 
                           if s.get("codec_tag_string") == "mebx"]
        assert len(metadata_streams) > 0, \
            "iPhone video should contain Apple metadata streams"