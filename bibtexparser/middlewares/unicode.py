import bibtexparser
from bibtexparser.middlewares import BlockMiddleware
from unidecode import unidecode


class SafeUnicodeSanitizerMiddleware(BlockMiddleware):
    def __init__(self, skip_fields=None):
        super().__init__(allow_parallel_execution=True)
        self.skip_fields = skip_fields or ["file", "url", "doi"]

    def transform_entry(self, entry, *args, **kwargs):
        for field in entry.fields:
            if field.key in self.skip_fields:
                continue

            if isinstance(field.value, str):
                field.value = unidecode(field.value)

        return entry
