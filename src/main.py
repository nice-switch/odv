import odv, sys

# TODO Make a TOML/JSON file for all configuration.

service: str = sys.argv[1]
args: list[str] = sys.argv[2::]

if service != None and odv.enum.CLI.valid_first_args.count(str(service)) != 0:
    
    service = service.lower()
    
    match service:
        case "database":
            if len(args) > 0:
                database_environment_arg = args[0]
                match database_environment_arg:
                    case "production":
                        odv.start_database(
                            database_type=odv.enum.development_database_type
                        )
                    case "development":
                        pass
                    case default:
                        print(f"Invalid database arg '{database_environment_arg}' valid: ")
                    
                #Qodv.start_database()
        case "client":
            odv.start_client()
        case "guard":
            odv.start_guard()
        case "web":
            odv.start_web()
        case default:
            print(f"Invalid arg '{str(service)}' valid: f{odv.enum.CLI.valid_first_args}")
