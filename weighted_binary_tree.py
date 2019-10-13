
# DuplicateEntryOption needs to be defined before WeightedBinaryTree in order to use it in the method parameters
# InsertionResult can be defined after WeightedBinaryTree if it is not used in the parameters.
class DuplicateEntryOption:
    ADD = "Add"
    REPLACE = "Replace"
    IGNORE = "Ignore"


class WeightedBinaryTree(object):

    DEFAULT_WEIGHT = 1.0

    def __init__(self, key, weight = DEFAULT_WEIGHT):
        self.left = None #WeightedBinaryTree()
        self.right = None #WeightedBinaryTree()
        self.key = key
        self.weight = weight
        self.sub_tree_weight = 0.0

    def __str__(self):
        return f'{self.key} {self.weight} {self.sub_tree_weight} {self.get_tree_weight()}'

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

    def insert(self, key, weight=DEFAULT_WEIGHT):
        self.simple_binary_insert(key, weight)

    def simple_binary_insert(self, key, new_weight=DEFAULT_WEIGHT, duplicate_entry_option=DuplicateEntryOption.ADD):
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
            elif duplicate_entry_option == DuplicateEntryOption.ADD:
                result.previous_weight = self.weight
                self.weight += new_weight
                result.status = InsertionResultStatus.REPLACED
            else:
                # Default behavior will be the same as ignore
                # TODO: specify a default as a constant or a class or object variable, not buried in the code here!
                result.status = InsertionResultStatus.IGNORED

        elif key < self.key:
            if self.left is not None:
                result = self.left.simple_binary_insert(key, new_weight, duplicate_entry_option)
            else:
                self.left = WeightedBinaryTree(key, new_weight)
                result.inserted_node = self.left
                result.status = InsertionResultStatus.CREATED
        elif key > self.key:
            if self.right is not None:
                result = self.right.simple_binary_insert(key, new_weight, duplicate_entry_option)
            else:
                self.right = WeightedBinaryTree(key, new_weight)
                result.inserted_node = self.right
                result.status = InsertionResultStatus.CREATED
        self.update_sub_tree_weights()
        return result

    def update_sub_tree_weights(self):
        self.sub_tree_weight = self.left.get_tree_weight() if self.left is not None else 0.0
        self.sub_tree_weight += self.right.get_tree_weight() if self.right is not None else 0.0
        return self


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


