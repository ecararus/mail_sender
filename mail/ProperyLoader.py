from ConfigParser import SafeConfigParser

class EmailConnection:
    def __init__(self):
        try:
            config = SafeConfigParser()
            config.read('owk.cfg')
            self.fromEmail = config.get('email', 'fromEmail')
            self.password = config.get('email', 'password')
            self.server = config.get('email', 'server')
            self.port = config.get('email', 'port')
        except SafeConfigParser.Error, err:
            print "Failed to load properties" + str(err)
