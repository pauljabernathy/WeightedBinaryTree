import unittest
from weighted_binary_tree import *


class TestCreateTree(unittest.TestCase):

    def test_create_tree(self):
        wbt = WeightedBinaryTree('root')
        wbt.left = WeightedBinaryTree('left', 2)
        wbt.right = WeightedBinaryTree('z')
        self.assertTrue(isinstance(wbt, WeightedBinaryTree))
        self.assertTrue(isinstance(wbt.left, WeightedBinaryTree))
        self.assertTrue(isinstance(wbt.right, WeightedBinaryTree))

    @unittest.skip("don't need this to run every time")
    def test_display(self):
        wbt = WeightedBinaryTree('root')
        wbt.left = WeightedBinaryTree('left', 2)
        wbt.right = WeightedBinaryTree('z')
        # wbt.display()


class BasicInsertionTestUpdate(unittest.TestCase):

    def test_simple_binary_insert_puts_items_in_the_correct_spot(self):
        # With simple_binary_insert, k will remain the root
        root = WeightedBinaryTree('k')
        root.simple_binary_insert('c')
        root.simple_binary_insert('w')
        root.simple_binary_insert('m')
        root.simple_binary_insert('x')
        root.simple_binary_insert('a')
        root.simple_binary_insert('e')

        self.assertEqual('c', root.left.key)
        self.assertEqual(1.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(1.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(1.0, root.right.left.weight)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(1.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(1.0, root.left.left.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(1.0, root.left.weight)

    def test_simple_binary_insert_returns_correct_insertion_result(self):
        root = WeightedBinaryTree('k')
        result = root.simple_binary_insert('c', duplicate_entry_option=DuplicateEntryOption.UPDATE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        result = root.simple_binary_insert('w', duplicate_entry_option=DuplicateEntryOption.UPDATE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)


class TestSimpleBinaryInsertWithAdd(unittest.TestCase):

    def test_simple_binary_insert_updates_items_that_should_be_updated(self):
        # With simple_binary_insert, k will remain the root
        root = WeightedBinaryTree('k')
        root.simple_binary_insert('c', 1.0, DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('w', 1.0, DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('m', 1.0, DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('x', 1.0, DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('a', 1.0, DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('e', 1.0, DuplicateEntryOption.UPDATE)

        root.simple_binary_insert('c', 3.0, DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('w', 3.0, DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('m', 47.0, DuplicateEntryOption.UPDATE)

        self.assertEqual('c', root.left.key)
        self.assertEqual(4.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(4.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(48.0, root.right.left.weight)

    def test_simple_binary_insert_returns_correct_insert_result(self):
        root = WeightedBinaryTree('k')
        result = root.simple_binary_insert('c', 1.0, DuplicateEntryOption.UPDATE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        result = root.simple_binary_insert('w', 1.0, DuplicateEntryOption.UPDATE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        # from attempts to add
        result = root.simple_binary_insert('c', 3.0, DuplicateEntryOption.UPDATE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual('Updated', result.status)

        result = root.simple_binary_insert('w', 3.0, DuplicateEntryOption.UPDATE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual('Updated', result.status)

    def test_tree_weights_are_updated_correctly(self):
        # Build the tree and make sure it builds it correctly.
        root = WeightedBinaryTree('k', 5)
        root.simple_binary_insert('c', 3, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('w', 2, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('m', 8, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('x', 7, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('a', 2, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('e', 1, duplicate_entry_option=DuplicateEntryOption.UPDATE)

        self.assertEqual(5, root.weight)
        self.assertEqual('c', root.left.key)
        self.assertEqual(3.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(2.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(8.0, root.right.left.weight)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(7.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(2.0, root.left.left.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(1.0, root.left.right.weight)

        self.assertEqual(23, root.sub_tree_weight)
        self.assertEqual(3, root.left.sub_tree_weight)
        self.assertEqual(15, root.right.sub_tree_weight)
        self.assertEqual(0, root.right.left.sub_tree_weight)
        self.assertEqual(0, root.right.right.sub_tree_weight)
        self.assertEqual(0, root.left.left.sub_tree_weight)
        self.assertEqual(0, root.left.right.sub_tree_weight)

        # Now, "insert" some.
        root.simple_binary_insert('x', 3, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('a', 5, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        root.simple_binary_insert('e', 11, duplicate_entry_option=DuplicateEntryOption.UPDATE)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(10.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(7.0, root.left.left.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(12.0, root.left.right.weight)

        self.assertEqual(42, root.sub_tree_weight)
        self.assertEqual(19, root.left.sub_tree_weight)
        self.assertEqual(18, root.right.sub_tree_weight)
        self.assertEqual(0, root.right.left.sub_tree_weight)
        self.assertEqual(0, root.right.right.sub_tree_weight)
        self.assertEqual(0, root.left.left.sub_tree_weight)
        self.assertEqual(0, root.left.right.sub_tree_weight)

        # TODO: test with with negative numbers (should not be allowed)


class TestSimpleBinaryInsertWithReplacement(unittest.TestCase):

    def test_simple_binary_insert_replaces_items_that_should_be_replaced(self):
        # With simple_binary_insert, k will remain the root
        root = WeightedBinaryTree('k')
        root.simple_binary_insert('c', 1.0, DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('w', 1.0, DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('m', 1.0, DuplicateEntryOption.REPLACE)

        result = root.simple_binary_insert('c', 3.0, DuplicateEntryOption.REPLACE)
        self.assertEqual('Replaced', result.status)
        root.simple_binary_insert('w', 3.0, DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('m', 47.0, DuplicateEntryOption.REPLACE)

        self.assertEqual('c', root.left.key)
        self.assertEqual(3.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(3.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(47.0, root.right.left.weight)

    def test_simple_binary_insert_returns_correct_insertion_result(self):
        root = WeightedBinaryTree('k')
        result = root.simple_binary_insert('c', 1.0, DuplicateEntryOption)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        result = root.simple_binary_insert('w', 1.0, DuplicateEntryOption.REPLACE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        #now replacing
        result = root.simple_binary_insert('c', 3.0, DuplicateEntryOption.REPLACE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual('Replaced', result.status)

        result = root.simple_binary_insert('w', 3.0, DuplicateEntryOption.REPLACE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual('Replaced', result.status)

    def test_tree_weights_are_updated_correctly(self):
        # First, build the tree and make sure it builds it correctly with with REPLACE.
        root = WeightedBinaryTree('k', 5)
        root.simple_binary_insert('c', 3, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('w', 2, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('m', 8, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('x', 7, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('a', 2, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('e', 1, duplicate_entry_option=DuplicateEntryOption.REPLACE)

        self.assertEqual(5, root.weight)
        self.assertEqual('c', root.left.key)
        self.assertEqual(3.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(2.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(8.0, root.right.left.weight)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(7.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(2.0, root.left.left.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(1.0, root.left.right.weight)

        self.assertEqual(23, root.sub_tree_weight)
        self.assertEqual(3, root.left.sub_tree_weight)
        self.assertEqual(15, root.right.sub_tree_weight)
        self.assertEqual(0, root.right.left.sub_tree_weight)
        self.assertEqual(0, root.right.right.sub_tree_weight)
        self.assertEqual(0, root.left.left.sub_tree_weight)
        self.assertEqual(0, root.left.right.sub_tree_weight)

        # Now, replace some.
        root.simple_binary_insert('x', 3, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('a', 5, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        root.simple_binary_insert('e', 11, duplicate_entry_option=DuplicateEntryOption.REPLACE)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(3.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(5.0, root.left.left.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(11.0, root.left.right.weight)

        self.assertEqual(32, root.sub_tree_weight)
        self.assertEqual(16, root.left.sub_tree_weight)
        self.assertEqual(11, root.right.sub_tree_weight)
        self.assertEqual(0, root.right.left.sub_tree_weight)
        self.assertEqual(0, root.right.right.sub_tree_weight)
        self.assertEqual(0, root.left.left.sub_tree_weight)
        self.assertEqual(0, root.left.right.sub_tree_weight)


class TestSimpleBinaryInsertionWithIgnore(unittest.TestCase):

    def test_simple_binary_insert_ignores_items_that_should_be_ignored(self):
        # With simple_binary_insert, k will remain the root
        root = WeightedBinaryTree('k')
        root.simple_binary_insert('c', 1.0, DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('w', 1.0, DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('m', 1.0, DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('x', 1.0, DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('a', 1.0, DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('e', 1.0, DuplicateEntryOption.IGNORE)

        root.simple_binary_insert('c', 3.0, DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('w', 3.0, DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('m', 47.0, DuplicateEntryOption.IGNORE)

        self.assertEqual('c', root.left.key)
        self.assertEqual(1.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(1.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(1.0, root.right.left.weight)

    def test_simple_binary_insert_returns_correct_insert_result(self):
        root = WeightedBinaryTree('k')
        result = root.simple_binary_insert('c', 1.0, DuplicateEntryOption)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        result = root.simple_binary_insert('w', 1.0, DuplicateEntryOption.IGNORE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        # from attempts to add
        result = root.simple_binary_insert('c', 3.0, DuplicateEntryOption.IGNORE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual('Ignored', result.status)

        result = root.simple_binary_insert('w', 3.0, DuplicateEntryOption.IGNORE)
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual('Ignored', result.status)

    def test_tree_weights_are_updated_correctly(self):
        # First, build the tree and make sure it builds it correctly with with IGNORE.
        root = WeightedBinaryTree('k', 5)
        root.simple_binary_insert('c', 3, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('w', 2, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('m', 8, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('x', 7, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('a', 2, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('e', 1, duplicate_entry_option=DuplicateEntryOption.IGNORE)

        self.assertEqual(5, root.weight)
        self.assertEqual('c', root.left.key)
        self.assertEqual(3.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(2.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(8.0, root.right.left.weight)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(7.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(2.0, root.left.left.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(1.0, root.left.right.weight)

        self.assertEqual(23, root.sub_tree_weight)
        self.assertEqual(3, root.left.sub_tree_weight)
        self.assertEqual(15, root.right.sub_tree_weight)
        self.assertEqual(0, root.right.left.sub_tree_weight)
        self.assertEqual(0, root.right.right.sub_tree_weight)
        self.assertEqual(0, root.left.left.sub_tree_weight)
        self.assertEqual(0, root.left.right.sub_tree_weight)

        # Now, "insert" some.
        root.simple_binary_insert('x', 3, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('a', 5, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        root.simple_binary_insert('e', 11, duplicate_entry_option=DuplicateEntryOption.IGNORE)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(7.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(2.0, root.left.left.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(1.0, root.left.right.weight)

        self.assertEqual(23, root.sub_tree_weight)
        self.assertEqual(3, root.left.sub_tree_weight)
        self.assertEqual(15, root.right.sub_tree_weight)
        self.assertEqual(0, root.right.left.sub_tree_weight)
        self.assertEqual(0, root.right.right.sub_tree_weight)
        self.assertEqual(0, root.left.left.sub_tree_weight)
        self.assertEqual(0, root.left.right.sub_tree_weight)


class TestHandleSubTrees(unittest.TestCase):

    def test_update_sub_tree_weight(self):
        root = WeightedBinaryTree('k', 2.0)

        # Simple_binary_insert() calls update_sub_tree_weights, so add the nods manually.
        root.left = WeightedBinaryTree('c', 3.0)
        self.assertEqual(0.0, root.sub_tree_weight)
        root.update_sub_tree_weights()
        self.assertEqual(3.0, root.sub_tree_weight)

        root.right = WeightedBinaryTree('w', 4.0)
        self.assertEqual(3.0, root.sub_tree_weight)
        root.update_sub_tree_weights()
        self.assertEqual(7.0, root.sub_tree_weight)


class TestPlaceInTree(unittest.TestCase):

    def test_is_root(self):
        m = WeightedBinaryTree('m', 1)
        j = WeightedBinaryTree('j', 10, parent=m)
        self.assertTrue(m.is_root())
        self.assertFalse(j.is_root())

    def test_is_root_and_get_parent_with_simple_binary_insert(self):
        m = WeightedBinaryTree('m', 1)
        j = m.simple_binary_insert('j', 10).inserted_node
        l = m.simple_binary_insert('l', 1).inserted_node
        i = m.simple_binary_insert('i', 1).inserted_node
        n = m.simple_binary_insert('n', 1).inserted_node
        self.assertTrue(m.is_root())
        self.assertFalse(j.is_root())
        self.assertFalse(l.is_root())
        self.assertFalse(i.is_root())
        self.assertFalse(n.is_root())

        self.assertEqual(None, m.parent)
        self.assertEqual(m, j.parent)
        self.assertEqual(j, l.parent)
        self.assertEqual(j, i.parent)
        self.assertEqual(m, n.parent)

    def test_is_left_or_right_child_simple_binary_insert(self):
        m = WeightedBinaryTree('m', 1)
        j = m.simple_binary_insert('j', 10).inserted_node
        l = m.simple_binary_insert('l', 1).inserted_node
        i = m.simple_binary_insert('i', 1).inserted_node
        n = m.simple_binary_insert('n', 1).inserted_node

        self.assertFalse(m.is_left_child())
        self.assertFalse(m.is_right_child())
        self.assertTrue(j.is_left_child())
        self.assertFalse(j.is_right_child())
        self.assertFalse(l.is_left_child())
        self.assertTrue(l.is_right_child())
        self.assertTrue(i.is_left_child())
        self.assertFalse(i.is_right_child())
        self.assertFalse(n.is_left_child())
        self.assertTrue(n.is_right_child())


class TestRebalanceOneLevel(unittest.TestCase):

    def test_when_self_is_root(self):
        m = WeightedBinaryTree('m', 1)
        j = m.simple_binary_insert('j', 10).inserted_node
        l = m.simple_binary_insert('l', 1).inserted_node
        i = m.simple_binary_insert('i', 1).inserted_node
        n = m.simple_binary_insert('n', 1).inserted_node

        self.assertTrue(m.is_root())
        self.assertFalse(j.is_root())
        self.assertFalse(n.is_root())
        self.assertEqual(j, m.left)
        self.assertEqual(n, m.right)

        #should not through an error in the following line
        m.rebalance_one_level()

        #Now, the tree should be...exactly the same as before.
        self.assertTrue(m.is_root())
        self.assertFalse(j.is_root())
        self.assertFalse(n.is_root())
        self.assertEqual(j, m.left)
        self.assertEqual(n, m.right)

    def test_when_parent_is_root_and_self_is_left(self):
        m = WeightedBinaryTree('m', 1)
        j = m.simple_binary_insert('j', 10).inserted_node
        l = m.simple_binary_insert('l', 1).inserted_node
        i = m.simple_binary_insert('i', 1).inserted_node
        n = m.simple_binary_insert('n', 1).inserted_node

        self.assertTrue(m.is_root())
        self.assertFalse(j.is_root())

        j.rebalance_one_level()
        self.assertTrue(j.is_root())
        self.assertFalse(m.is_root())
        self.assertIsNone(j.parent)
        self.assertEqual(i, j.left)
        self.assertEqual(m, j.right)
        self.assertEqual(l, m.left)
        self.assertEqual(n, m.right)

    def test_when_parent_is_root_and_this_is_right(self):
        m = WeightedBinaryTree('m', 1)
        l = m.simple_binary_insert('l').inserted_node
        o = m.simple_binary_insert('o', 10).inserted_node
        n = m.simple_binary_insert('n', 1).inserted_node
        p = m.simple_binary_insert('p', 1).inserted_node

        self.assertTrue(m.is_root())
        self.assertFalse(o.is_root())
        self.assertEqual(l, m.left)
        self.assertEqual(o, m.right)
        self.assertEqual(n, m.right.left)
        self.assertEqual(p, m.right.right)

        o.rebalance_one_level()
        self.assertFalse(m.is_root())
        self.assertTrue(o.is_root())
        self.assertEqual(m, o.left)
        self.assertEqual(l, m.left)
        self.assertEqual(p, o.right)
        self.assertEqual(n, m.right)

    def test_when_parent_is_left_and_self_is_left(self):
        m = WeightedBinaryTree('m', 1)
        n = m.simple_binary_insert('n', 1).inserted_node
        k = m.simple_binary_insert('k', 1).inserted_node
        i = m.simple_binary_insert('i', 10).inserted_node
        h = m.simple_binary_insert('h', 1).inserted_node
        j = m.simple_binary_insert('j', 1).inserted_node
        l = m.simple_binary_insert('l', 1).inserted_node

        self.assertTrue(m.is_root())
        self.assertEqual(k, m.left)
        self.assertEqual(n, m.right)
        self.assertEqual(i, m.left.left)
        self.assertEqual(h, m.left.left.left)
        self.assertEqual(j, m.left.left.right)
        self.assertEqual(l, m.left.right)

        i.rebalance_one_level()
        self.assertTrue(m.is_root())
        self.assertEqual(i, m.left)
        self.assertEqual(h, m.left.left)
        self.assertEqual(k, m.left.right)
        self.assertEqual(j, m.left.right.left)
        self.assertEqual(l, m.left.right.right)
        self.assertEqual(n, m.right)

    def test_when_parent_is_left_and_self_is_right(self):
        '''o = WeightedBinaryTree('o', 1)
        m = o.simple_binary_insert('m', 1).inserted_node
        j = o.simple_binary_insert('j', 1).inserted_node
        n = o.simple_binary_insert('n', 1).inserted_node
        i = o.simple_binary_insert('i', 1).inserted_node
        k = o.simple_binary_insert('k', 10).inserted_node
        l = o.simple_binary_insert('l', 1).inserted_node
        h = o.simple_binary_insert('h', 1).inserted_node
        p = o.simple_binary_insert('p', 1).inserted_node
        m.display()

        self.assertTrue(o.is_root())
        self.assertEqual(m, o.left)
        self.assertEqual(j, m.left)
        self.assertEqual(i, j.left)
        self.assertEqual(h, i.left)
        self.assertEqual(k, j.right)
        self.assertEqual(l, k.right)
        self.assertEqual(n, m.right)
        self.assertEqual(p, o.right)
        self.assertEqual()
        '''
        h = WeightedBinaryTree('h', 1)
        d = h.simple_binary_insert('d', 1).inserted_node
        b = h.simple_binary_insert('b', 1).inserted_node
        f = h.simple_binary_insert('f', 1).inserted_node
        e = h.simple_binary_insert('e', 10).inserted_node
        g = h.simple_binary_insert('g', 1).inserted_node
        i = h.simple_binary_insert('i', 1).inserted_node

        self.assertTrue(h.is_root())
        self.assertEqual(d, h.left)
        self.assertEqual(b, d.left)
        self.assertEqual(f, d.right)
        self.assertEqual(e, f.left)
        self.assertEqual(g, f.right)
        self.assertEqual(i, h.right)

        f.rebalance_one_level()
        self.assertTrue(h.is_root())
        self.assertEqual(f, h.left)
        self.assertEqual(d, f.left)
        self.assertEqual(b, d.left)
        self.assertEqual(e, d.right)
        self.assertEqual(g, f.right)
        self.assertEqual(i, h.right)

    def test_when_parent_is_right_and_self_is_left(self):
        m = WeightedBinaryTree('m', 1)
        l = m.simple_binary_insert('l', 1).inserted_node
        r = m.simple_binary_insert('r', 1).inserted_node
        p = m.simple_binary_insert('p', 10).inserted_node
        n = m.simple_binary_insert('n', 1).inserted_node
        q = m.simple_binary_insert('q', 1).inserted_node
        s = m.simple_binary_insert('s', 1).inserted_node

        self.assertTrue(m.is_root())
        self.assertEqual(l, m.left)
        self.assertEqual(r, m.right)
        self.assertEqual(p, r.left)
        self.assertEqual(n, p.left)
        self.assertEqual(q, p.right)
        self.assertEqual(s, r.right)

        p.rebalance_one_level()
        self.assertTrue(m.is_root())
        self.assertEqual(l, m.left)
        self.assertEqual(p, m.right)
        self.assertEqual(n, p.left)
        self.assertEqual(r, p.right)
        self.assertEqual(q, r.left)
        self.assertEqual(s, r.right)

    def test_when_parent_is_right_and_self_is_right(self):
        m = WeightedBinaryTree('m', 1)
        l = m.simple_binary_insert('l', 1).inserted_node
        o = m.simple_binary_insert('o', 1).inserted_node
        n = m.simple_binary_insert('n', 1).inserted_node
        q = m.simple_binary_insert('q', 10).inserted_node
        p = m.simple_binary_insert('p', 1).inserted_node
        r = m.simple_binary_insert('r', 1).inserted_node

        self.assertTrue(m.is_root())
        self.assertEqual(l, m.left)
        self.assertEqual(o, m.right)
        self.assertEqual(n, o.left)
        self.assertEqual(q, o.right)
        self.assertEqual(p, q.left)
        self.assertEqual(r, q.right)

        q.rebalance_one_level()
        self.assertTrue(m.is_root())
        self.assertEqual(l, m.left)
        self.assertEqual(q, m.right)
        self.assertEqual(o, q.left)
        self.assertEqual(n, o.left)
        self.assertEqual(p, o.right)
        self.assertEqual(r, q.right)