from odv import auth, data, enum



def cli(service: enum.ServiceType, args: list[str]):
    match service:
        case enum.ServiceType.DATABASE:
            print("DB")
        case enum.ServiceType.AUTHORIZATION:
            print("AUTH")