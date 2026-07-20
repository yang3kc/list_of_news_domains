from urllib.parse import urlparse
import re
import tldextract


def normalize_domain(raw):
    """
    Normalize a raw domain or URL string to a bare lowercase domain name.

    Handles:
    - Bare domains: 'example.com' → 'example.com'
    - Full URLs: 'http://example.com' → 'example.com'
    - Malformed schemes (missing //): 'http:example.com' → 'example.com'
    """
    raw = raw.strip().lower()
    # Fix missing // after http: or https: (e.g., "http:example.com")
    raw = re.sub(r"^(https?):(?!//)", r"\1://", raw)
    if raw.startswith("http://") or raw.startswith("https://"):
        return extract_domain(raw)
    return raw


COSMETIC_PREFIX = re.compile(r"^(?:www\d*|m|amp|beta|mobile|qa-www)\.")


def canonicalize_domain(raw):
    """Canonicalize a bare domain: lowercase, drop stray-space prefixes,
    leading dots, and cosmetic host labels (www, www2, m, amp, beta, qa-www).
    Does NOT reduce to eTLD+1 — subdomain granularity is preserved.
    Returns '' for empty/invalid input."""
    if not isinstance(raw, str):
        return ""
    raw = raw.strip().lower()
    raw = re.split(r"\s+", raw)[-1]      # "com wsavcw.com" -> "wsavcw.com"
    raw = raw.lstrip(".")                # ".ljworld.com"   -> "ljworld.com"
    # strip cosmetic prefix labels only while a registrable tail (with a dot) remains
    while COSMETIC_PREFIX.match(raw) and "." in COSMETIC_PREFIX.sub("", raw):
        raw = COSMETIC_PREFIX.sub("", raw)
    return raw


def has_path(url):
    """
    Check if the URL has a path component.
    NOTE: only works for URLs; does not work for domain names

    Returns:
        bool: True if URL has a non-empty path, False otherwise
    """
    parsed_url = urlparse(url)
    path = parsed_url.path.replace("/", "")
    return path != ""


def extract_suffix(url):
    """
    Extract the top-level domain suffix from the URL.

    Returns:
        str: The top-level domain suffix (e.g. 'com', 'org', 'co.uk')
    """
    extracted = tldextract.extract(url)
    suffix = extracted.suffix
    return suffix


def extract_domain(url):
    """
    Extract the domain from the URL.

    Returns:
        str: The domain (e.g. 'example.com')
    """
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    return domain
