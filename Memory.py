from flask_restful import fields, marshal_with, reqparse, Resource, request
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser
import json
import requests
post_parser = reqparse.RequestParser()
post_parser2 = reqparse.RequestParser()

post_parser2.add_argument(
    'memoryAddress',
    required=True,
    help='memoryAddress', )
post_parser.add_argument(
    'startA',
    required=True,
    help='Start Address', )
post_parser.add_argument(
    'endA',
    required=True,
    help='End Address', )
post_parser.add_argument(
    'port',
    required=True,
    help='Port', )
post_parser.add_argument(
    'offset',
    required=True,
    help='Memory Offset', )
post_parser.add_argument(
    'action',
    required=True,
    help='Action', )


class MemoryTest(Resource):
    def post(self):
        memoryAddress = []
        memoryAddress2 = []
        result = []
        jsonData = request.get_json(force=True)
        for memAddr in jsonData["memoryAddress"]:
            action = memAddr["action"]
            startA = memAddr["startA"]
            endA = memAddr["endA"]
            port = memAddr["port"]
            offset = memAddr["offset"]
            url = "http://0.0.0.0:5000/RemoteMemory"
            payload = {
                "segments": [{
                    "startA": startA,
                    "endA": endA,
                    "port": port,
                    "offset": offset
                }],
                "action":
                action
            }
            if (action == "Add"):
                memoryAddress.append(memAddr)
                r = requests.post(url, data=json.dumps(payload))
                resp = r.json()
                # print(r.text)

                result.append(json.loads(resp))
            elif (action == "Remove"):
                memoryAddress2.append(memAddr)
                r = requests.post(url, data=json.dumps(payload))
                resp = r.json()
                # print(r.text)

                result.append(json.loads(resp))
            else:
                pass
        """startA = args.startA
        endA = args.endA
        port = args.port
        offset = args.offset
        action = "Add"
        url = "http://0.0.0.0:5000/RemoteMemory"
        payload = {
            "segments": [{
                "startA": startA,
                "endA": endA,
                "port": port,
                "offset": offset
            }],
            "action":
            action
        }

        r = requests.post(url, data=json.dumps(payload))
        resp = r.json()
        # print(r.text)"""

        return result


class AddRemoteMemory(Resource):
    def post(self):
        memoryAddress = []
        result = []
        jsonData = request.get_json(force=True)
        for memAddr in jsonData["memoryAddress"]:
            action = memAddr["action"]
            startA = memAddr["startA"]
            endA = memAddr["endA"]
            port = memAddr["port"]
            offset = memAddr["offset"]
            url = "http://0.0.0.0:5000/RemoteMemory"
            payload = {
                "segments": [{
                    "startA": startA,
                    "endA": endA,
                    "port": port,
                    "offset": offset
                }],
                "action":
                action
            }

            memoryAddress.append(memAddr)
            r = requests.post(url, data=json.dumps(payload))
            resp = r.json()
            # print(r.text)

            result.append(json.loads(resp))

        return result, r.status_code


class RemoveRemoteMemory(Resource):
    def post(self):
        memoryAddress = []
        result = []
        jsonData = request.get_json(force=True)
        for memAddr in jsonData["memoryAddress"]:
            action = memAddr["action"]
            startA = memAddr["startA"]
            endA = memAddr["endA"]
            port = memAddr["port"]
            offset = memAddr["offset"]
            url = "http://0.0.0.0:5000/RemoteMemory"
            payload = {
                "segments": [{
                    "startA": startA,
                    "endA": endA,
                    "port": port,
                    "offset": offset
                }],
                "action":
                action
            }

            memoryAddress.append(memAddr)
            r = requests.post(url, data=json.dumps(payload))
            resp = r.json()
            # print(r.text)

            result.append(json.loads(resp))

        return result, r.status_code
