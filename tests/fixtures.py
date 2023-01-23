import pytest
import io

from bobtail import BobTail
from bobtail_upload import BobtailUpload

@pytest.fixture(scope="function")
def bobtail_app():
    def inner(*, routes):
        b = BobTail(routes=routes)
        b.use(BobtailUpload())
        return b
    return inner

@pytest.fixture(scope="function")
def environ():
    def inner(*, path="/images", method="GET", data=b'{\n    "name": "joe"\n}', content="multipart/form-data"):
        return {
            "PATH_INFO": path,
            "REQUEST_METHOD": method,
            "wsgi.input": io.BytesIO(data),
            "CONTENT_TYPE": content,
        }

    return inner


@pytest.fixture(scope="function")
def Image():
    class Image:

        def get(self, req, res):
            pass

        def post(self, req, res):
            data = req.get_multipart_value("cat")
            req.upload.add(
                file_name="cat.png",
                data=data,
                mimetype="image/png"
            )
            req.upload.save(table_name="images", pk=1)
            res.set_body(None)
            res.set_status(202)

        def delete(self, req, res):
            pass

        def put(self, req, res):
            pass
    return Image
