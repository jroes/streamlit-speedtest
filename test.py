# TODO: Probably better off using the GCE API instead of exec'ing everywhere.

import subprocess

def run_with_stdout(cmd):
    subprocess.run(cmd.split(), capture_output=True, text=True).stdout

# TODO: argify
test_file = "prophet/streamlit_app.py"

# Get authenticated to the right project & configure docker:
# https://cloud.google.com/container-registry/docs/advanced-authentication

project_id = "experiment-jon"
vm_prefix = "speedtest-vm"
local_docker_image = "streamlit-speedtest"
hosted_docker_image = f"gcr.io/{project_id}/{local_docker_image}"

# Have GCP build the container and put it into the registry
cmd = "gcloud builds submit --tag gcr.io/experiment-jon/streamlit-speedtest"
run_with_stdout(cmd)

for instance_type in ["n2", "n2d", "c2", "a1"]:
    # Deploy to instance
    cmd = f"gcloud compute instances create-with-container {vm_prefix} --container-image {hosted_docker_image}"
    run_with_stdout(cmd)

# TODO: How do we collect the data from all of the instances?

# n2: Elapsed time: 4.697584629058838
# n2d: Elapsed time: 2.876523733139038
# c2: Elapsed time: 3.544968366622925
