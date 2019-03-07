"""Module for config file helper functions."""

import configparser
import pathlib

# ========== Constants ==========
PACMAN_CONF = pathlib.Path("/etc/pacman.conf")


# ========== Functions ==========
def parse_configfile(filepath):
    """Parse a config file given its path and return
    a ConfigParser object.

    :param path: path to config file to parse
    :type path: str, bytes, or path-like object
    :returns: object used to parse config file
    :rtype: ConfigParser object
    :raises: FileNotFoundError if path does not exist
    """
    if not pathlib.Path(filepath).is_file():
        raise FileNotFoundError(f"{filepath} does not exist")

    config_reader = configparser.ConfigParser(strict=False, allow_no_value=True)
    config_reader.read(filepath)

    return config_reader


def list_configured_repos():
    """Read /etc/pacman.conf to list all configured repositories.

    :raises FileNotFoundError: if config file does not exist
    :returns: all repos configured on the system
    :rtype: list
    """
    parsed_config = parse_configfile(PACMAN_CONF)

    repos = parsed_config.sections()
    # remove the 'option' entry from the list
    del repos[0]

    repos.sort()

    return repos
