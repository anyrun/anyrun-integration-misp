<p align="center">
    <a href="#readme">
        <img alt="ANY.RUN logo" src="https://raw.githubusercontent.com/anyrun/anyrun-sdk/b3dfde1d3aa018d0a1c3b5d0fa8aaa652e80d883/static/logo.svg">
    </a>
</p>

______________________________________________________________________

# ANY.RUN Threat Intelligence Feeds connector for MISP

The [TI Feeds](https://any.run/threat-intelligence-feeds/?utm_source=anyrungithub_misp_feeds&utm_medium=integration&utm_content=ti_feeds_landing) connector delivers fresh, high-confidence Indicators of Compromise (IPs, domains, URLs) directly from ANY.RUN’s Interactive Sandbox into MISP events, empowering faster detection and response for SOC teams. Over 15,000 companies fortify their security with TI Feeds' filtered, high-fidelity IOCs. The solution integrates seamlessly with SIEMs/XDRs/firewalls and other security systems for enhanced monitoring, detection, and blocking of malware and phishing threats.

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
![static/img.png](static/img.png)

#### Click Add authentication key
![static/img_1.png](static/img_1.png)

#### Use API-KEY as the value for the environment variable: MISP_API_KEY

## Generate Basic Authentication token

To obtain your Basic Authentication token, please contact your ANY.RUN account manager directly or fill out the [request form](https://any.run/demo/?utm_source=anyrungithub_misp_feeds&utm_medium=integration&utm_content=demopage).

Use Basic Authentication token as the value for the environment variable: ANYRUN_BASIC_TOKEN

## Support
This connector is supported by ANY.RUN. If you need help, contact <support@any.run>.
