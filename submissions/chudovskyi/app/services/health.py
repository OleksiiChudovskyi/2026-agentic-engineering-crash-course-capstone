from datetime import datetime, timezone


def build_health(
    service_name: str,
    started_at: datetime,
    now: datetime | None = None,
) -> dict:
    """Health payload: status, service name and uptime in whole seconds."""

    if not service_name or not service_name.strip():
        raise ValueError("service_name must not be empty")

    now = now or datetime.now(timezone.utc)
    uptime = (now - started_at).total_seconds()

    return {
        "status": "ok",
        "service": service_name,
        "uptime_seconds": max(int(uptime), 0),
    }
