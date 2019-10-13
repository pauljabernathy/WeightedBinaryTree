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

    def test_display(self):
        wbt = WeightedBinaryTree('root')
        wbt.left = WeightedBinaryTree('left', 2)
        wbt.right = WeightedBinaryTree('z')
        #wbt.display()


class BasicInsertionTestNoDuplication(unittest.TestCase):

    def test_simple_binary_insert_puts_items_in_the_correct_spot(self):
        #With simple_binary_insert, k will remain the root
        root = WeightedBinaryTree('k')
        root.simple_binary_insert('c')
        root.simple_binary_insert('w')
        root.simple_binary_insert('m')
        root.simple_binary_insert('x')
        root.simple_binary_insert('a')
        root.simple_binary_insert('e')

        root.display()
        self.assertEqual('c', root.left.key)
        self.assertEqual(1.0, root.left.weight)
        self.assertEqual('w', root.right.key)
        self.assertEqual(1.0, root.right.weight)
        self.assertEqual('m', root.right.left.key)
        self.assertEqual(1.0, root.right.left.weight)
        self.assertEqual('x', root.right.right.key)
        self.assertEqual(1.0, root.right.right.weight)
        self.assertEqual('a', root.left.left.key)
        self.assertEqual(1.0, root.left.loeft.weight)
        self.assertEqual('e', root.left.right.key)
        self.assertEqual(1.0, root.left.weight)

    def test_simple_binary_insert_returns_correct_insertion_result(self):
        root = WeightedBinaryTree('k')
        result = root.simple_binary_insert('c')
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('c', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)

        result = root.simple_binary_insert('w')
        self.assertTrue(isinstance(result, InsertionResult))
        self.assertEqual('w', result.inserted_node.key)
        self.assertEqual(InsertionResultStatus.CREATED, result.status)


class BasicInsertionTestWithReplacement(unittest.TestCase):

    def test_simple_binary_insert_returns_replaced_status(self):
        root = WeightedBinaryTree('k')
        root.simple_binary_insert('c', 1.0, DuplicateEntryOption)
        root.simple_binary_insert('w', 1.0, DuplicateEntryOption.REPLACE)

        result = root.simple_binary_insert('c', 3.0, DuplicateEntryOption.REPLACE)
        self.assertEqual('Replaced', result.status)
        result = root.simple_binary_insert('w', 3.0, DuplicateEntryOption.REPLACE)
        self.assertEqual('Replaced', result.status)

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


class BasicInsertionTestWithIgnore(unittest.TestCase):

    def test_simple_binary_insert_returns_ignored_status(self):
        root = WeightedBinaryTree('k')
        root.simple_binary_insert('c', 1.0, DuplicateEntryOption)
        root.simple_binary_insert('w', 1.0, DuplicateEntryOption.IGNORE)

        result = root.simple_binary_insert('c', 3.0, DuplicateEntryOption.IGNORE)
        self.assertEqual('Ignored', result.status)
        result = root.simple_binary_insert('w', 3.0, DuplicateEntryOption.IGNORE)
        self.assertEqual('Ignored', result.status)

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


class TestHandleSubTrees(unittest.TestCase):

    def test_update_sub_tree_weight(self):
        root = WeightedBinaryTree('k', 2.0)
        #simple_binary_insert() calls update_sub_tree_weights, so add the nods manually
        root.left = WeightedBinaryTree('c', 3.0)
        self.assertEqual(0.0, root.sub_tree_weight)
        root.update_sub_tree_weights()
        self.assertEqual(3.0, root.sub_tree_weight)

        root.right = WeightedBinaryTree('w', 4.0)
        self.assertEqual(3.0, root.sub_tree_weight)
        root.update_sub_tree_weights()
        self.assertEqual(7.0, root.sub_tree_weight)