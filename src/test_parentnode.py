from htmlnode import LeafNode, ParentNode

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

def test_to_html_with_no_children(self):
    parent_node = ParentNode("div", None)
    with self.assertRaises(ValueError):
            parent_node.to_html()

def test_to_html_with_missing_tag(self):
      child_node = LeafNode("span", "child")
      parent_node = ParentNode(None, [child_node])
      with self.assertRaises(ValueError):
            parent_node.to_html()

def test_to_html_with_deep_nesting(self):
     great_grandchild_node = LeafNode("i", "great-grandchild")
     grandchild_node = ParentNode("b", [great_grandchild_node])
     child_node = ParentNode("span", [grandchild_node])
     parent_node = ParentNode("div", [child_node])
     self.assertEqual(
          parent_node.to_html(),
          "<div><span><b><i>great-grandchild</i></b></span></div>",
     )