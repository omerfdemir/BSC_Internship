import signal
import sys
from flask import Flask
from flask_restful import Api
from resources.remote_memory import RemoteMemory
#from SDMAgent.resources.vm_handler import VirtualMachineHandler, virtualMachines


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    for key,value in virtualMachines.items():
        virtualMachines.pop(key)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


app = Flask(__name__)
api = Api(app)

#api.add_resource(Memory, '/Memory/<int:computeBrickId>/<int:memSize>')
api.add_resource(RemoteMemory, '/RemoteMemory')
#api.add_resource(VirtualMachineHandler, '/VirtualMachineHandler')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
