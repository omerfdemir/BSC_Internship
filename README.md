TESTING THE API
---------------

For exmaple test of the dBMC-API, please, check http://repo.nitlab.inf.uth.gr/dredbox/dBMC-API/wikis/Test-script-for-the-dBMC-API
File `test_dBMC_API.sh` implements shell commands that test in fast way dBMC-API. To test the API, the script first launches http servers for the dBMC_API and the SDMAgents modules. Each server listens to a different port and is launched in a different terminal.

Then using the script executes API calls via the `curl` tool with each API that is implemented by the dBMC-API.

For the SDMAgent's `api/memory/addremotememory` and `api/memory/removeremotememor` calls subsequently forwarded from the dBMC_API to the SDMAgent module.

Below is a screenshot of the execution of the `test_dBMC_API.sh` script.

![image](/uploads/7485315ab04e3a14b63f3b1bef9d8dae/image.png)
