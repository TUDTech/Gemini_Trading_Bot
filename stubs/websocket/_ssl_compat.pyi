import ssl as ssl
from ssl import SSLError as SSLError  # type: ignore

HAVE_CONTEXT_CHECK_HOSTNAME: bool
HAVE_SSL: bool

class SSLError(Exception): ...  # type: ignore
