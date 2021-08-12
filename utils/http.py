def response_body(data, status, message, status_code):
    try:
        return {"data": data,
                "meta": {
                    "status": status,
                    "message": message,
                    "status_code": status_code
                    }
                }
    except:
        return {"data": "",
                "meta": {
                    "status": "error",
                    "message": "fail to return response",
                    "status_code": 400
                    }
                }
