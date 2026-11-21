from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

# Step 6: Create MindMapComposite and MindMapLeaf objects to test
root = MindMapComposite("Root", "circle")
branch = MindMapComposite("Branch 1", "square")
root.add(branch)
leaf1 = MindMapLeaf("Child 1", "square")
leaf2 = MindMapLeaf("Child 2", "cloud")
branch.add(leaf1)
root.add(leaf2)

print(root)  # Should display "((Root))"
root.display()    # Should display root and its children

print("MindMapComposite tests completed!")