def pytest_addoption(parser):
    parser.addoption(
        "--full",
        action="store_true",
        default=False,
        help="Enable slow tests",
    )


def pytest_configure(config):
    if not config.option.full and not config.option.markexpr:
        config.option.markexpr = "not slow"
