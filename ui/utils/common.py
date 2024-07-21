import json


def get_post_data(request) -> dict:
  return json.loads(request.body.decode('utf-8'))
