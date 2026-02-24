def get_file_extension(filename):
    return filename.split(".")[-1].lower()

class TestVideoFormats:
    
    def test_mov_extension(self):
        assert get_file_extension("sample.mov") == "mov"
    
    def test_mp4_extension(self):
        assert get_file_extension("sample.mp4") == "mp4"
    
    def test_mxf_extension(self):
        assert get_file_extension("sample.mxf") == "mxf"
    
    def test_uppercase_extension(self):
        assert get_file_extension("sample.MOV") == "mov"
    
    def test_prores_filename(self):
        filename = "prores_422_sample.mov"
        assert "prores" in filename.lower()