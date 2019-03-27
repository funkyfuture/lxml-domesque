from lxml_domesque import Document, TagNode, any_of, not_


def test_anyof_filter():
    def has_a_attribute(node):
        return isinstance(node, TagNode) and "a" in node.attributes

    def has_b_attribute(node):
        return isinstance(node, TagNode) and "b" in node.attributes

    document = Document('<root><x a=""/><x b=""/><x c=""/></root>')

    results = tuple(document.root.child_nodes(any_of(has_a_attribute, has_b_attribute)))

    assert len(results) == 2
    assert all("c" not in x.attributes for x in results)


def test_not_filter():
    def has_a_attribute(node):
        return isinstance(node, TagNode) and "a" in node.attributes

    def has_b_attribute(node):
        return isinstance(node, TagNode) and "b" in node.attributes

    document = Document('<root><x a=""/><x b=""/><x c=""/></root>')

    results = tuple(
        document.root.child_nodes(not_(any_of(has_a_attribute, has_b_attribute)))
    )

    assert len(results) == 1
    assert "c" in results[0].attributes
