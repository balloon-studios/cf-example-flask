# Example Flask app running on Cloud Foundry

This repo contains the bare bones of a flask app which runs inside Cloud
Foundry (CF).

## Steps To A Running App

1. Install the `cf` CLI tool
  - Download an *"INSTALLER"* from https://github.com/cloudfoundry/cli/releases
    - On OSX, right-click and open it once it's downloaded
      - Otherwise it'll complain about code signing
1. Get `cf` authenticated and working against the CF API
  - Open the terminal (we'll be using it for the entire session ...)
  - Run `cf login -a https://api.eu-gb.bluemix.net`
    - Follow the prompts to get to the `cf-training` space
1. Copy `manifest-template.yml` to `manifest.yml`
1. Edit `manifest.yml` as indicated inside the file
1. `cf push -f manifest.yml`
  - The `-f` is optional iff using this exact filename, but it's a good habit
    to get into
1. Browse to the FQDN the `cf push` tells you it's registered
