# Bobtail File Upload
Middleware to upload files for [Bobtail](https://github.com/joegasewicz/bobtail)

### Install
```bash
pip install bobtail-upload
```

### Usage
```python
from bobtail_upload import BobtailUpload

app = Bobtail(routes=routes)

app.use(BobtailUpload(options={}))
```

### Saving files
Bobtail Upload will attach the an Upload API to the request object
There are 2 methods now available:

- `add(self, *, file_name: str, data: bytes, mimetype: str) -> None`
- `save(self, *, table_name: str = None, pk: Union[int, str] = None) -> None`

```python
def post(self, req: Request, res: Response):
    data = req.get_multipart_data()
    req.upload.add(
        file_name=data["logo"]["value"]["filename"],
        data=data["logo"]["value"]["file_data"],
        mimetype=data["logo"]["value"]["mimetype"],
    )
    
    req.upload.save()
```

### Mapping file saves to your database tables
To save files based on a table name & primary key. 

The default upload directory path is `/uploads`
```
- uploads
  - images
    - 2
```
For example
```python
def post(self, req: Request, res: Response):
    data = req.get_multipart_data()
    req.upload.add(
        file_name=data["logo"]["value"]["filename"],
        data=data["logo"]["value"]["file_data"],
        mimetype=data["logo"]["value"]["mimetype"],
    )
    
    # Use your ORM to save the file to your db & obtain the returned primary key (pk)
    req.upload.save(table_name="images", pk=pk)
```

### Options
- UPLOAD_DIR - the directory path where files will be saved (defaults to `uploads`).
```python
options = {
    "UPLOAD_DIR": "uploads",
}
```