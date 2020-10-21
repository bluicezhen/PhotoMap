class HTTPException(Exception):
    """Rise the Exception represent return standard HTTP error like 404, 500 to client"""
    def __init__(self, status: int, msg: str):
        self.http_status = status
        self.err_msg = msg

    def __str__(self):
        return repr(self.err_msg)
