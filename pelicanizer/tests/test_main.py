from mock import sentinel, call

from pelicanizer.main import main
from pelicanizer.tests.logutil import LogMockingTestCase


class main_tests (LogMockingTestCase):
    def test_typical_run(self):
        m_parse_args = self.patch('pelicanizer.clargs.parse_args')
        m_init = self.patch('pelicanizer.log.init')
        m_WebServer = self.patch('pelicanizer.web.server.WebServer')
        m_reactor = self.make_mock()

        result = main(sentinel.args, m_reactor)

        self.assertIs(result, None)

        self.assert_calls_equal(
            m_parse_args,
            [call(main.__doc__, sentinel.args)])

        self.assert_calls_equal(
            m_init,
            [call()])

        self.assert_calls_equal(
            m_WebServer,
            [call(m_reactor),
             call().listen(m_parse_args().port)])

        self.assert_calls_equal(
            m_reactor,
            [call.run()])
