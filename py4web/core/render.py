import renoir
import renoir.constants
import renoir.writers

from .utils import safely, Cache


class RenoirXMLEscapeMixin:
    def _escape_data(self, data):
        """Allows Renoir to convert yatl helpers to strings"""
        return safely(
            lambda: data.xml(), default=lambda: self._to_html(self._to_unicode(data))
        )


class RenoirCustomWriter(RenoirXMLEscapeMixin, renoir.writers.Writer):
    ...


class RenoirCustomEscapeAllWriter(RenoirXMLEscapeMixin, renoir.writers.EscapeAllWriter):
    ...


class Renoir(renoir.Renoir):
    """Custom Renoir Engine that understands yatl helpers"""
    _writers = {
        renoir.constants.ESCAPES.common: RenoirCustomWriter,
        renoir.constants.ESCAPES.all: RenoirCustomEscapeAllWriter,
    }


def render(
    content=None,
    filename=None,
    path=".",
    context={},
    delimiters="[[ ]]",
    cached_renoir_engines=Cache(100),
):
    """
    renders the template using renoire, same API as yatl.render, does caching of
    both Renoire engine and source files
    """
    engine = cached_renoir_engines.get(
        (path, delimiters),
        lambda: Renoir(path=path, delimiters=delimiters.split(" "), reload=True),
    )
    if content is not None:
        return engine._render(content, context=context)
    return engine.render(filename, context=context)
