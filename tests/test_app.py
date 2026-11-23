import unittest

from app import health_payload


class HealthPayloadTest(unittest.TestCase):
    def test_health_payload(self) -> None:
        self.assertEqual(health_payload(), {"status": "ok"})
