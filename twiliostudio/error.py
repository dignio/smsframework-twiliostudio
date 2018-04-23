from smsframework.exc import *


class TwilioStudioProviderError(ProviderError):
    """ The errors """
    code = None

    def __init__(self, code, message=''):
        self.code = code
        super(TwilioStudioProviderError, self).__init__(
            '#{}: {}'.format(self.code, message)
        )
