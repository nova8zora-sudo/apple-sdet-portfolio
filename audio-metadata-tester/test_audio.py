import subprocess
import json
import pytest

def get_audio_info(filepath):
    """Extract audio stream info using FFprobe."""
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_streams", filepath
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    return next(s for s in data["streams"] if s["codec_type"] == "audio")

class TestiPhoneAudio:
    """Tests for iPhone AAC audio — mirrors Apple SDET work."""

    def test_codec_is_aac(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert audio["codec_name"] == "aac", \
            f"Expected AAC, got {audio['codec_name']}"

    def test_sample_rate_is_cd_quality(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert audio["sample_rate"] == "44100", \
            f"Expected 44100Hz, got {audio['sample_rate']}"

    def test_channels_is_stereo(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert audio["channels"] == 2, \
            f"Expected stereo (2), got {audio['channels']}"

    def test_channel_layout_is_stereo(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert audio["channel_layout"] == "stereo"

    def test_codec_profile_is_lc(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert audio["profile"] == "LC", \
            f"Expected AAC-LC profile, got {audio['profile']}"

    def test_audio_has_duration(self):
        audio = get_audio_info("iphone_audio.m4a")
        duration = float(audio["duration"])
        assert duration > 0, "Audio must have a duration"

    def test_audio_has_bitrate(self):
        audio = get_audio_info("iphone_audio.m4a")
        bitrate = int(audio["bit_rate"])
        assert bitrate > 100000, \
            f"Expected bitrate above 100kbps, got {bitrate}"

    def test_handler_is_core_media(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert "Core Media" in audio["tags"]["handler_name"], \
            "Expected Apple Core Media Audio handler"

    def test_codec_type_is_audio(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert audio["codec_type"] == "audio"

    def test_audio_starts_at_zero(self):
        audio = get_audio_info("iphone_audio.m4a")
        assert float(audio["start_time"]) == 0.0, \
            "Audio should start at 0.0 seconds"