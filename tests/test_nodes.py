from lxml_domesque import is_tag_node, Document, TagNode, TextNode


def test_add_previous():
    document = Document("<root><e1/></root>")
    document.root[0].add_previous(
        document.new_tag_node("e2"), document.new_tag_node("e3")
    )

    assert str(document) == "<root><e3/><e2/><e1/></root>"


def test_add_next():
    document = Document("<root><e1/></root>")
    document.root[0].add_next(document.new_tag_node("e2"), document.new_tag_node("e3"))

    assert str(document) == "<root><e1/><e2/><e3/></root>"


def test_siblings_filter():
    document = Document("<root><e1/>ham<e2/>spam<e3/></root>")
    e2 = document.root[2]

    assert isinstance(e2.previous_node(), TextNode)
    assert isinstance(e2.next_node(), TextNode)

    assert isinstance(e2.previous_node(is_tag_node), TagNode)
    assert isinstance(e2.next_node(is_tag_node), TagNode)
