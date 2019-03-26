from typing import TYPE_CHECKING, Callable, Dict

from lxml import etree

if TYPE_CHECKING:
    from lxml_domesque.nodes import NodeBase, TagNode  # noqa: F401

ElementAttributes = etree._Attrib
Filter = Callable[["NodeBase"], bool]
_WrapperCache = Dict[int, "TagNode"]
