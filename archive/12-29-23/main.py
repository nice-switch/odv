import odv

odv.execute(
    service_type=odv.enum.ServiceType.DATABASE,
    launch_parameters=[
        odv.enum.DatabaseType.SQLITE,
        odv.enum.EnvironmentType.DEVELOPMENT,
        odv.enum.DebugType.SENSITIVE_OUTPUT,
    ]
)