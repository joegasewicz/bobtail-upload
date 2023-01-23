import shutil
import pytest

from bobtail_upload.upload import BobtailUpload, BobtailUploadError, Upload
from bobtail import BobTail
from tests.fixtures import environ, bobtail_app, Image


class TestBobtailUpload:

    def teardown_method(self):
        try:
            shutil.rmtree("test1")
            shutil.rmtree("uploads")
            shutil.rmtree("../test1")
            shutil.rmtree("../uploads") # keep this last
        except:
            pass

    def test_run(self):
        upload = BobtailUpload()
        assert upload.options["UPLOAD_DIR"] == "uploads"

        upload = BobtailUpload(options={"UPLOAD_DIR": "test1"})
        assert upload.options["UPLOAD_DIR"] == "test1"


class TestUpload:

    def teardown_method(self):
        try:
            shutil.rmtree("uploads")
        except:
            pass

    @pytest.mark.skip
    def test_add(self, environ, bobtail_app, Image):
        app = bobtail_app(routes=[(Image(), "/images")])

        env = environ(path="/images", method="POST")
        data = app(env, lambda s, r: None)
        pass



    def test_save(self):
        pass
