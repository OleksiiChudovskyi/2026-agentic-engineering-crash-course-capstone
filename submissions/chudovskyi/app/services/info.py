import time

STARTED_AT = time.monotonic()


def build_info(
    service_name: str,
    version: str,
    api_version: str,
    started_at: float,
    now: float,
) -> dict:
    """Info payload: status, service name, versions and uptime in seconds."""

    raise NotImplementedError
