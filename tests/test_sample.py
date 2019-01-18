import unittest

from smsframework import Gateway, OutgoingMessage
from twiliostudio import TwilioStudioProvider
from flask import Flask
from requests_mock import Mocker


import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class TwilioTest(unittest.TestCase):
    def setUp(self):
        # Gateway
        gw = self.gw = Gateway()
        gw.add_provider('main', TwilioStudioProvider, account_sid='sid', secret='secret', username='dag')

        # Flask
        app = self.app = Flask(__name__)

        # Register receivers
        gw.receiver_blueprints_register(app, prefix='/msg/')

    def test_send(self):
        """ Test send SMS """
        with Mocker() as m:
            m.post('https://studio.twilio.com/v1/Flows/sid/Executions',
                   request_headers={
                       'Authorization': 'Basic ZGFnOnNlY3JldA==',  # dag:secret
                       'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                   },
                   status_code=200,
                   headers={},
                   json={
                       'url': 'https://studio.twilio.com/v1/Flows/sid/Executions/FN0000',
                       # ... many more fields. See: https://www.twilio.com/docs/studio/rest-api/execution
                   })

            om = self.gw.send(OutgoingMessage('+1999', 'Test'))
            self.assertEqual(om.msgid, 'Flows/sid/Executions/FN0000')
