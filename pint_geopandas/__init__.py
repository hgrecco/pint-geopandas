import pprint

try:
    from importlib.metadata import version
except ImportError:
    # Backport for Python < 3.8
    from importlib_metadata import version

try:  # pragma: no cover
    __version__ = version("pint_geopandas")
except Exception:  # pragma: no cover
    # we seem to have a local copy not installed without setuptools
    # so the reported version will be unknown
    __version__ = "unknown"

__all__ = ["__version__"]


def show_versions():

    deps = [
        "pint_geopandas",
        "pint_pandas",
        "pint",
        "pandas",
        "numpy",
    ]

    versions = {dep: version(dep) for dep in deps}
    pprint.pprint(versions)
