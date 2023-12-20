import odv, sys

# Checks for available args and grabs the first one if available.
# NOTE sys.argv[0] is the file arg.
target_service: str | None = len(sys.argv) >= 1 and sys.argv[1] or None

# Validity check for target_service, this should always be something!
if (target_service is None):
    # TODO add available args list with error message.
    raise Exception("No target service to initialize...")

# Just some post processing on the string.
target_service = target_service.lower()

# Checks if more args are available after target_service then creates a list with the extra args or a empty list when none are available.
cli_args: list[str] = len(sys.argv) > 2 and sys.argv[3::] or []


# TODO Make a TOML/JSON file for all configuration.


match target_service:
    case odv.enum.ServiceType.DATABASE:
        print("Starting database service...")
        
        # TODO initialize_database_service shouldn't run everytime, will have to put into an arg.
        odv.initialize_database_service(
            database_type=odv.enum.DatabaseType.DEVELOPMENT,
            api_port=odv.enum.DatabasePort.DEVELOPMENT,
            api_host=odv.enum.DatabaseHost.MACHINE
        )
        
        # TODO add args for publish that use the config files.
        odv.publish_database_service()
        
    case odv.enum.ServiceType.CLIENT:
        print("Starting client service...")
        
    case odv.enum.ServiceType.GUARD:
        print("Starting guard service...")
    case odv.enum.ServiceType.WEB:
        print("Starting web service...")
    