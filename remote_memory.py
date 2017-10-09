from flask import request
from flask_restful import Resource, reqparse
from subprocess import call
import json


class RemoteMemory(Resource):
    def get(self):
        pass
    def post(self):
        jsonData = request.get_json(force=True)
        state = 0

        for segment in jsonData['segments']:
            localaddr = int(segment['startA'],16)
            locaddr = segment['startA']
            if (localaddr >= int("0x400000000",16)) and (localaddr < int("0x500000000",16)):
                if jsonData["action"] == "Add":
                    print "echo %d,1 > memory/probe"%localaddr
                    print "echo online"
                    state = 1
                else:
                    print "echo offline"
                    print "echo %d > memory/remove"%localaddr
                    state = 2
            else:
                if jsonData["action"] == "Add":
                    print "echo %d,1 > memory/probe"%localaddr
                    print "echo online"
                    state = 3
                else:
                    print "echo offline"
                    print "echo %d > memory/remove"%localaddr
                    state = 4
        #Glue Logic config
        #for chunk in memoryChunks:
            #call("echo '$((" + str(chunk['startAddress']) + ")) > /sys/sdmc/netport" + str(chunk['id']) + "/startAddress")
            #call("echo '$((" + str(chunk['endAddress']) + ")) > /sys/sdmc/netport" + str(chunk['id']) + "/endAddress")
            #call("echo '$((" + str(chunk['offset']) + ")) > /sys/sdmc/netport" + str(chunk['id']) + "/offset")
            #call("echo '$((" + str(transceiverPort) + ")) > /sys/sdmc/netport" + str(chunk['id']) + "/outId")
            #call("echo activate > /sys/sdmc/netport" + str(chunk['id']) + "/set")


        #Memory hotplug
        #for chunk in memoryChunks:
            #call("echo '" + str(chunk['startAddress']) + "' > /sys/devices/system/memory/probe")
            #call("echo online > /sys/devices/system/memory/memoryXXX/state")
        status={}
        status['status']="Success"
        return json.dumps([locaddr,state,status,localaddr,jsonData["action"]])
