import odv, sys

service: str = sys.argv[1]
args: list[str] = sys.argv[2::]

if service is not None:
    service = service.lower()
    if service == "database":
        pass
    if service == "client":
        pass
    if service == "guard":
        pass
    if service == "web":
        pass