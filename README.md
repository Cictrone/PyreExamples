# PyreExamples

## Overview
There are four sub projects in here to show off some pyre static anlysis :)
- Flask RCE
- Flask Secret Logging
- Flask XSS
- Flask XSS Sanitized

## Run
Make sure to be in the base dir in the project and have pyre already installed (read [here](https://pyre-check.org/docs/installation.html) to set pyre up). Next you will want to run `pyre analyze` and boom, your done.

## Output
The output should be the following:
```
 ƛ Fixpoint iterations: 2
[
  {
    "line": 18,
    "column": 8,
    "path": "FlaskSecretsLogging/server.py",
    "code": 3,
    "name": "Possible cookies logged",
    "description":
      "Possible cookies logged [3]: Data from [Cookies] source(s) may reach [Logging] sink(s)",
    "long_description":
      "Possible cookies logged [3]: Data from [Cookies] source(s) may reach [Logging] sink(s)",
    "concise_description":
      "Possible cookies logged [3]: Data from [Cookies] source(s) may reach [Logging] sink(s)",
    "inference": null,
    "define": "FlaskSecretsLogging.server.index"
  },
  {
    "line": 12,
    "column": 48,
    "path": "FlaskXSS/server.py",
    "code": 2,
    "name": "Possible cross site scripting",
    "description":
      "Possible cross site scripting [2]: Data from [UserSpecified] source(s) may reach [CrossSiteScripting] sink(s)",
    "long_description":
      "Possible cross site scripting [2]: Data from [UserSpecified] source(s) may reach [CrossSiteScripting] sink(s)",
    "concise_description":
      "Possible cross site scripting [2]: Data from [UserSpecified] source(s) may reach [CrossSiteScripting] sink(s)",
    "inference": null,
    "define": "FlaskXSS.server.index"
  },
  {
    "line": 15,
    "column": 54,
    "path": "FlaskRCE/server.py",
    "code": 1,
    "name": "Possible shell injection",
    "description":
      "Possible shell injection [1]: Data from [UserSpecified] source(s) may reach [RemoteCodeExecution] sink(s)",
    "long_description":
      "Possible shell injection [1]: Data from [UserSpecified] source(s) may reach [RemoteCodeExecution] sink(s)",
    "concise_description":
      "Possible shell injection [1]: Data from [UserSpecified] source(s) may reach [RemoteCodeExecution] sink(s)",
    "inference": null,
    "define": "FlaskRCE.server.index"
  }
]
```