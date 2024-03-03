# dPhish-Challenge

Get Information about IPAddress

## Description

This is a simple python script to get information about an IP Address. It uses the ipinfo.io API to get the information.

## Instructions to Run the Code

1. Clone the repository or download the code.

```bash
git clone https://github.com/faresemad/HighTech.git
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

4. Build Project

```bash
make build
```

5. Run the code

```bash
make up
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
