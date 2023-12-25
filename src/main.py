import odv

# Okay, we're back at it again.

odv.cli.execute(
    service=odv.enum.ServiceType.DATABASE,
    args=[
        odv.enum.ExecutionType.DEBUG,
        odv.enum.DatabaseType.SQLITE
    ]
)