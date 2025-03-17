from urllib.parse import urlparse
import tldextract


def has_path(url):
    """
    Check if the URL has a path component.

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
