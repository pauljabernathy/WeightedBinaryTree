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