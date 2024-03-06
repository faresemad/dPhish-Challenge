# dPhish-Challenge

Get Information about IPAddress

## Description

This is a simple python script to get information about an IP Address. It uses the ipinfo.io API to get the information.

## Instructions to Run the Code

1. Clone the repository or download the code.

```bash
git clone https://github.com/faresemad/dPhish-Challenge.git
```

2. Create a virtual environment and install the requirements.

```bash
# Create and activate a virtual environment (optional)
python3 -m venv venv
# For Windows:
venv\Scripts\activate
# For Unix/macOS:
source venv/bin/activate
```

3. Install the requirements.

```bash
pip install -r requirements/local.txt
```

4. Install `make` and `docker` if not already installed.
  - install make for Windows
    - `https://gnuwin32.sourceforge.net/packages/make.htm`
  - install make for linux
    - ```bash
    sudo apt-get install make
    ```
  - install docker for Windows
    - `https://docs.docker.com/docker-for-windows/install/`
  - install docker for linux
    - `https://docs.docker.com/engine/install/ubuntu/`

5. Build Project
- Build the project using the following command:
  - With `make`:
    ```bash
    make build
    ```
  - Without `make`:
    ```bash
    docker-compose -f docker-compose.yml build
    ```


6. Run the code
- Run the code using the following command:
  - With `make`:
    ```bash
    make run
    ```
  - Without `make`:
    ```bash
    docker-compose -f docker-compose.yml up
    ```


## API Endpoints

1.  `api/scanner/ip-addresses/`

    - Method: POST
    - Description: Get information about an IP Address.
    - Request:
      - Content-Type: application/json
      - Body:
        ```json
        {
          "address": "<IP Address>, e.g."
        }
        ```
    - Response:
      - Content-Type: application/json
      - Body:
        ```json
        {
          "message": "IPs are being processed"
        }
        ```

2.  `api/scanner/ip-addresses/<id>/`

    - Method: GET
    - Description: Get information about an IP Address.
    - Request:
      - Content-Type: application/json
    - Response:
      - Content-Type: application/json
      - Body:
        ```json
        {
          "ip": "<IP Address>",
          "loc": "<Latitude, Longitude>",
          "org": "<Organization>",
          "city": "<City>",
          "readme": "<Readme>",
          "region": "<Region>",
          "country": "<Country>",
          "timezone": "<Timezone>"
        }
        ```
