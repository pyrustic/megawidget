
Back to [Reference Overview](https://github.com/pyrustic/megawidget/blob/master/docs/reference/README.md)

# megawidget.tree



<br>


```python
BODY = "body"

FRAME_BOX = "frame_box"

FRAME_HEADER = "frame_header"

FRAME_NODE = "frame_node"

```

<br>

```python

class Error:
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

<br>

```python

class ExampleHook:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    def build_node(self, tree, node, frame):
        """
        
        """

    def on_collapse_node(self, tree, node):
        """
        
        """

    def on_destroy_node(self, tree, node):
        """
        
        """

    def on_expand_node(self, tree, node):
        """
        
        """

    def on_feed_node(self, tree, node, *args, **kwargs):
        """
        
        """

    def on_map_node(self, tree, node):
        """
        
        """

```

<br>

```python

class Hook:
    """
    
    """

    def on_build_node(self, tree, node, frame):
        """
        
        """

    def on_collapse_node(self, tree, node):
        """
        
        """

    def on_destroy_node(self, tree, node):
        """
        
        """

    def on_expand_node(self, tree, node):
        """
        
        """

    def on_feed_node(self, tree, node, *args, **kwargs):
        """
        
        """

    def on_map_node(self, tree, node):
        """
        
        """

```

<br>

```python

class Tree:
    """
    Tree is the megawidget to use to display the data as a tree.
    To use Tree, you need to subclass it.
    
    pyrustic.tree.SimpleTree is a nice example to study.
    
    Scroll to the bottom of this file at the top-level script
    environment to see the usage of SimpleTree
    """

    def __init__(self, master=None, indent=50, spacing=10, cnfs=None):
        """
        PARAMETERS:
        
        - master: widget parent. Example: an instance of tk.Frame
        
        - indent: left indent
        
        - spacing: space between two nodes
        
        - options: dictionary of widgets options
            The widgets keys are: BODY, NODE_FRAME, HEADER_FRAME, and BOX_FRAME.
            Example: Assume that you want to set the NODE_FRAME's background to black
            and the BODY's background to red:
                options = {BODY: {"background": "red"},
                           NODE_FRAME: {"background": "black"}}
        """

    @property
    def hook(self):
        """
        
        """

    @hook.setter
    def hook(self, val):
        """
        
        """

    @property
    def indent(self):
        """
        
        """

    @property
    def nodes(self):
        """
        Returns sequence of nodes. Check the method 'node()' to
        see how an individual node data structure looks like.
        """

    @property
    def root(self):
        """
        
        """

    @property
    def spacing(self):
        """
        
        """

    def attach(self, node_id):
        """
        Attaches (again) a detached node. Returns True if it worked, else False
        """

    def clear(self, node_id):
        """
        Deletes the descendants of this node. Returns True if all right, else False.
        """

    def collapse(self, node_id):
        """
        Collapses this node. Returns True if it worked, else returns False
        """

    def collexp(self, node_id):
        """
        Useful method to toggle the state collapsed/expanded of the node
        """

    def delete(self, node_id):
        """
        Deletes this node.
        Returns True or False
        """

    def descendants(self, node_id):
        """
        List of descendants nodes.
        [ node, node, ...]
        
        Please check the doc of the method "node()" to learn more about
        the structure of a node object (a dict in fact)
        """

    def detach(self, node_id):
        """
        Detaches an attached node. Returns True if it worked, else False.
        The detached node won't be visible anymore.
        The detached node's descendants won't be visible anymore.
        """

    def expand(self, node_id):
        """
        Expands this node. Returns True if it worked, else returns False
        """

    def expanded(self, node_id):
        """
        Returns True if this node is actually expanded, else returns False
        """

    def feed(self, node_id, *args, **kwargs):
        """
        This method will call "_on_feed(*args, **kwargs").
        Use it to feed some data to the tree
        """

    def ghost(self, node_id):
        """
        Hide the header frame of the node whose node_id is given.
        Note that the descendants nodes will still be visible.
        Use this method to give illusion that descendants nodes
        don't have a root at all (kind of floating without root).
        This method returns a boolean (True to indicate that all right, else False)
        """

    def insert(self, parent=None, title='', index='end', data=None, container=True, expand=False):
        """
        Insert a node.
        - parent: the node_id of the parent or None if this is the root node of the tree
        - title: string
        - index: an integer to indicate where to put the node between
         its parent's descendants.
            Put "end" to indicate that this node should be added at the the end
        - data: None or dictionary to contain whatever data you want. It could help later.
        - container: boolean. True, if the node should contain another node. False else.
        - expand: boolean, True if this node should be expanded from creation. False else.
        Returns:
            None if failed to insert the node, else returns the newly created node_id
        """

    def move(self, node_id, parent_id=None, index=0):
        """
        Moves a node to another index. Returns True if all right, else False.
        """

    def node(self, id_or_path):
        """
        Returns a node by its node_id or its dotted path.
        A node is a dictionary of data:
        node = {"parent": int, "node_id": int, "container": bool,
                "index": int, "expanded": bool, "data": dict, "title": str,
                "frame_node": tk.Frame, "frame_header": tk.Frame,
                "frame_box": tk.Frame, "attached": bool, "ghosted": bool}
        Example of dotted path (each number in the path is a position index):
            Hub
                Africa
                America
                Asia
                    China
            china node = "0.2.0"
        """

    def tag(self, node_id, data=None):
        """
        Edits this node's data. Data should be None or a dict
        Returns the data
        """

    def title(self, node_id, title=None):
        """
        Use this method to display or edit the title of a node.
        Returns this node's title if you don't set a title as argument
        """

    def unghost(self, node_id):
        """
        Reveals the header frame of the node whose node_id is given.
        This method returns a boolean (True to indicate that all right, else False)
        """

    def untag(self, node_id, data=None):
        """
        Edits this node's data. Data should be a sequence of keys.
        Returns the data
        """

    def walk(self, node_id):
        """
        Walks throughout the node.
        Example:
            for node_id, descendants in tree.walk(2):
                print(node_id, len(descendants))
        """

```

