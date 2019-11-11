
# DuplicateEntryOption needs to be defined before WeightedBinaryTree in order to use it in the method parameters
# InsertionResult can be defined after WeightedBinaryTree if it is not used in the parameters.
class DuplicateEntryOption:
    UPDATE = "Update"
    REPLACE = "Replace"
    IGNORE = "Ignore"


class WeightedBinaryTree(object):

    DEFAULT_WEIGHT = 1.0

    def __init__(self, key, weight = DEFAULT_WEIGHT, parent=None, left=None, right=None):
        self.left = None #WeightedBinaryTree()
        self.right = None #WeightedBinaryTree()
        self.key = key
        self.weight = weight
        self.sub_tree_weight = 0.0
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.key} {self.weight} {self.sub_tree_weight} {self.get_tree_weight()}]'

    def display(self, prefix=None):
        if prefix is None:
            self.display('')
            return
        if prefix == '':
            print(str(self))
        else:
            print(f'{prefix} ' + str(self))
        if self.left is not None:
            self.left.display(prefix + 'l')
        if self.right is not None:
            self.right.display(prefix + 'r')

    def get_tree_weight(self):
        return self.weight + self.sub_tree_weight

    def get_weights_list(self):
        """
        created to help in unit testing
        :return: a list of weights in the form [self.weight, sub tree weight, total tree weight (self.weight + sub tree weight)]
        """
        return [self.weight, self.sub_tree_weight, self.get_tree_weight()]

    def insert(self, key, weight=DEFAULT_WEIGHT):
        self.simple_binary_insert(key, weight)

    # TODO: deal with with negative numbers (should not be allowed)
    def simple_binary_insert(self, key, new_weight=DEFAULT_WEIGHT, duplicate_entry_option=DuplicateEntryOption.UPDATE):
        if key is None:
            result = InsertionResult(None)
            result.status = InsertionResultStatus.FAILED
            return result

        result = InsertionResult()
        if key == self.key:
            result.inserted_node = self
            if duplicate_entry_option == DuplicateEntryOption.IGNORE:
                result.status = InsertionResultStatus.IGNORED
            elif duplicate_entry_option == DuplicateEntryOption.REPLACE:
                result.previous_weight = self.weight
                self.weight = new_weight
                result.status = InsertionResultStatus.REPLACED
            elif duplicate_entry_option == DuplicateEntryOption.UPDATE:
                result.previous_weight = self.weight
                self.weight += new_weight
                result.status = InsertionResultStatus.UPDATED
            else:
                # Default behavior will be the same as ignore
                # TODO: specify a default as a constant or a class or object variable, not buried in the code here!
                result.status = InsertionResultStatus.IGNORED

        elif key < self.key:
            if self.left is not None:
                result = self.left.simple_binary_insert(key, new_weight, duplicate_entry_option)
            else:
                self.left = WeightedBinaryTree(key, new_weight, parent=self)
                result.inserted_node = self.left
                result.status = InsertionResultStatus.CREATED
        elif key > self.key:
            if self.right is not None:
                result = self.right.simple_binary_insert(key, new_weight, duplicate_entry_option)
            else:
                self.right = WeightedBinaryTree(key, new_weight, parent=self)
                result.inserted_node = self.right
                result.status = InsertionResultStatus.CREATED
        self.update_sub_tree_weights()
        return result

    def update_sub_tree_weights(self):
        self.sub_tree_weight = self.left.get_tree_weight() if self.left is not None else 0.0
        self.sub_tree_weight += self.right.get_tree_weight() if self.right is not None else 0.0
        return self

    def is_root(self):
        return self.parent is None

    def is_left_child(self):
        if self.parent is None:
            return False
        if self.parent.left is not None and self.parent.left is self:
            return True
        else:
            return False

    def is_right_child(self):
        if self.parent is None:
            return False
        if self.parent.right is not None and self.parent.right is self:
            return True
        else:
            return False

    # TODO: return a RebalanceResult
    def rebalance_one_level(self):
        """
        Moves the current node up or down, and shifts parent, left and right, and parent's left or right, accordingly.
        Does not rebalance the entire tree.
        :return: nothing at the moment; will return a RebalanceResult when that is implemented.
        """
        if self.is_root():
            return

        old_parent = self.parent

        if self.parent.is_root() and self.is_left_child():
            old_right = self.right
            self.right = old_parent
            old_parent.parent = self
            self.parent = None  #TODO: set_parent() method like in Java version if needed
            old_parent.left = old_right
            if old_right is not None:
                old_right.parent = old_parent

        elif self.parent.is_root() and self.is_right_child():
            old_left = self.left
            self.left = old_parent
            old_parent.parent = self
            self.parent = None
            old_parent.right = old_left
            if old_left is not None:
                old_left.parent = old_parent

        elif self.parent.is_left_child() and self.is_left_child():
            old_right = self.right
            old_grand_parent = old_parent.parent
            self.right = old_parent
            old_parent.parent = self
            old_grand_parent.left = self
            self.parent = old_grand_parent
            old_parent.left = old_right
            if old_right is not None:
                old_right.parent = old_parent

        elif self.parent.is_left_child() and self.is_right_child():
            old_left = self.left
            old_grand_parent = old_parent.parent
            self.left = old_parent
            old_parent.parent = self
            old_grand_parent.left = self
            self.parent = old_grand_parent
            old_parent.right = old_left
            if old_left is not None:
                old_left.parent = old_parent

        elif self.parent.is_right_child() and self.is_left_child():
            old_right = self.right
            old_grand_parent = old_parent.parent
            self.right = old_parent
            old_parent.parent = self
            old_grand_parent.right = self
            self.parent = old_grand_parent
            old_parent.left = old_right
            if old_right is not None:
                old_right.parent = old_parent

        elif self.parent.is_right_child() and self.is_right_child():
            old_left = self.left
            old_grand_parent = old_parent.parent
            self.left = old_parent
            old_parent.parent = self
            old_grand_parent.right = self
            self.parent = old_grand_parent
            old_parent.right = old_left
            if old_left is not None:
                old_left.parent = old_parent

        old_parent.update_sub_tree_weights()
        self.update_sub_tree_weights()
        if self.parent is not None:
            self.parent.update_sub_tree_weights()


class InsertionResult:
    def __init__(self, inserted_node:WeightedBinaryTree=None):
        self.inserted_node = inserted_node
        self.status = InsertionResultStatus.UNKOWNN
        self.previous_weight = 0.0

    # TODO: @property attributes?


class InsertionResultStatus:
    # public enum Status { CREATED, IGNORED, REPLACED, UPDATED, FAILED, UNKNOWN };
    CREATED = "Created"
    IGNORED = "Ignored"
    REPLACED = "Replaced"
    UPDATED = "Updated"
    FAILED = "Failed"
    UNKOWNN = "Unknown"


