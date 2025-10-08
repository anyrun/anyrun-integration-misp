<p align="center">
    <a href="#readme">
        <img alt="ANY.RUN logo" src="https://raw.githubusercontent.com/anyrun/anyrun-sdk/b3dfde1d3aa018d0a1c3b5d0fa8aaa652e80d883/static/logo.svg">
    </a>
</p>

______________________________________________________________________

# ANY.RUN Threat Intelligence Feeds Connector for MISP

Connector delivers fresh, high-confidence IOCs directly from ANY.RUN’s interactive malware sandbox into MISP Events, empowering faster detection and response.

### Setup Python script

#### Clone this project
```console
$ git clone git@github.com:anyrun/anyrun-integration-misp.git
```

#### Jump into the project directory
```console
$ cd anyrun-integration-misp/anyrun-integration-ti-feeds
```

#### Create and fill the .env config. See "Setup secrets" and "Generate Basic Authentication token" sections below
```console
$ cp .env_example .env
```

#### Run the script using two of the following ways:
```console
$ docker-compose up --build
```
```console
$ python3 -m venv venv
$ source venv/bin/scripts/activate
$ pip install -r requirements.txt
$ python3 connector-anyrun-feed.py
```

#  Setup secrets

#### Click Administration, List Auth Keys
![img.png](static/img.png)

#### Click Add authentication key
![img_1.png](static/img_1.png)

#### Use API-KEY as the value for the environment variable: MISP_API_KEY

## Generate Basic Authentication token

To obtain your Basic Authentication token, please contact your ANY.RUN account manager directly or fill out the request [form](https://any.run/demo/?utm_source=opencti_marketplace&utm_medium=integration&utm_campaign=opencti_form).

Use Basic Authentication token as the value for the environment variable: ANYRUN_BASIC_TOKEN

## Support
This is an ANY.RUN supported connector. If you need help, contact <support@any.run>