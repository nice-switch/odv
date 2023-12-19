from odv import enum, database

def start_database(database_type: str) -> None:
    # TODO Initialize whatever's necessary to make database run.
    
    match database_type:
        case enum.development_database_type:
            pass
        case enum.production_database_type:
            pass
        case default:
            raise Exception(f"Invalid arg '{str(database_type)}' valid: {enum.CLI.valid_database_first_args}")
    
    return None


def start_client() -> None:
    
    return None


def start_guard() -> None:
    
    return None


def start_web() -> None:
    
    return None