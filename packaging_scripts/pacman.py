"""Module for config file helper functions."""

from pathlib import Path
from pycman.config import PacmanConfig

# ========== Constants ==========
PACMAN_CONF = Path("/etc/pacman.conf")


# ========== Functions ==========
def list_configured_repos():
    """Read /etc/pacman.conf to list all configured repositories.

    :raises FileNotFoundError: if config file does not exist
    :returns: all repos configured on the system
    :rtype: list
    """
    if not Path(PACMAN_CONF).is_file():
        raise FileNotFoundError(f"{PACMAN_CONF} does not exist")

    config = PacmanConfig()
    config.load_from_file(PACMAN_CONF)

    return list(config.repos)
