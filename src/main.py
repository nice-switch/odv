import odv

odv.execute(
    service_type=odv.enum.ServiceType.DATABASE,
    launch_parameters=[
        odv.enum.LaunchParameter.SQLITE_DATABASE,
        odv.enum.LaunchParameter.DEVELOPMENT_ENVIRONMENT,
        odv.enum.LaunchParameter.SENSITIVE_DEBUG_OUTPUT,
    ]
)