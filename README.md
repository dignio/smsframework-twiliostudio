<!--
[![Build Status](https://api.travis-ci.org/dignio/py-smsframework-twiliostudio.png?branch=master)](https://travis-ci.org/dignio/py-smsframework-twiliostudio) 
-->
[![Pythons](https://img.shields.io/badge/python-2.7%20%7C%203.4%E2%80%933.7%20%7C%20pypy-blue.svg)](.travis.yml)


SMSFramework Twilio Studio provider
===============================

version number: 0.0.6
author: Dag Høidahl

Overview
--------

Twilio Studio provider for SMSFramework

Installation / Usage
--------------------

To install use pip:

    $ pip install py-smsframework-twiliostudio


Or clone the repo:

    $ git clone git@github.com:dignio/py-smsframework-twiliostudio.git
    $ python setup.py install
    
Example:

```python
from smsframework import Gateway, OutgoingMessage
from twiliostudio import TwilioStudioProvider

gw = Gateway()
gw.add_provider('main', TwilioStudioProvider, account_sid='sid', secret='secret', username='dag')

gw.send(OutgoingMessage('+19990001122', 'Hello'))
```
    
Contributing
------------

TBD

Example
-------

TBD
