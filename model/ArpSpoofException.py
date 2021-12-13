class ArpSpoofException(Exception):

    def __init__(self, msg=None):
        if msg is None:
            msg = 'Error excuting ArpSpoof'
        super(ArpSpoofException, self).__init__(msg)