from prov.model import ProvDocument


def get_prov():
    doc = ProvDocument()
    doc.set_default_namespace('http://roocs.org/')
    doc.get_provn()
