import os
from typing import Union

from bobtail import AbstractMiddleware, Request, Response, Tail


class BobtailUploadError(Exception):
    pass


class Upload:

    def __init__(self, options):
        self.options = options

    def add(self, *, file_name: str, data: bytes, mimetype: str) -> None:
        """
        Add a single file to
        :param file_name:
        :param data:
        :param mimetype:
        :return:
        """
        self.file_name = file_name
        self.data = data
        self.mimetype = mimetype

    def _create_path(self, table_name: str, id: Union[int, str]) -> str:
        base_path = self.options['UPLOAD_DIR']
        if table_name and id:
            dir_path = f"{base_path}/{table_name}/{id}/"
            os.makedirs(os.path.dirname(dir_path), exist_ok=True)
            return f"{dir_path}{self.file_name}"
        else:
            return f"{base_path}/{self.file_name}"

    def save(self, *, table_name: str = None, id: Union[int, str] = None) -> None:
        """
        Saves the file with optional table name & id path
        :param table_name:
        :param id:
        :return:
        """
        try:
            with open(self._create_path(table_name, id), "wb") as f:
                f.write(self.data)
            self._clean_up()
        except Exception as exc:
            self._clean_up()
            raise BobtailUploadError(str(exc)) from exc

    def _clean_up(self):
        self.file_name = None
        self.data = None
        self.mimetype = None


class BobtailUpload(AbstractMiddleware):

    options = {
        "UPLOAD_DIR": "uploads",
    }

    def __init__(self, options=None):
        if options:
            self.options = options
        # Create upload directory if one doesn't exit
        if not os.path.isdir(self.options["UPLOAD_DIR"]):
            os.makedirs(self.options["UPLOAD_DIR"])

    def run(self, req: Request, res: Response, tail: Tail) -> None:
        """
        :param req:
        :param res:
        :param tail:
        :return:
        """
        setattr(req, "upload", Upload(self.options))
        tail(req, res)
