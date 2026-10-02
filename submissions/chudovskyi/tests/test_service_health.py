import pytest

from datetime import datetime, timedelta, timezone

from app.services.health import build_health


STARTED_AT = datetime(2026, 1, 1, 12, 0, 0, tzinfo=timezone.utc)


class TestServiceHealth:
    def test_build_health_ok(self):
        health = build_health("prompt-manager", STARTED_AT)

        assert health["status"] == "ok"
        assert health["service"] == "prompt-manager"

    def test_build_health_uptime_seconds(self):
        now = STARTED_AT + timedelta(seconds=90)

        health = build_health("prompt-manager", STARTED_AT, now=now)

        assert health["uptime_seconds"] == 90

    def test_build_health_empty_name_raises(self):
        with pytest.raises(ValueError):
            build_health("", STARTED_AT)

    def test_build_health_blank_name_raises(self):
        with pytest.raises(ValueError):
            build_health("   ", STARTED_AT)
