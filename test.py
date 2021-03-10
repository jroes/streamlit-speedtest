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

# gcloud builds submit --tag gcr.io/experiment-jon/streamlit-speedtest

# Deploy to instance
cmd = f"gcloud compute instances create-with-container {vm_prefix} --container-image {hosted_docker_image}"

# n2: Elapsed time: 4.697584629058838
# n2d: 