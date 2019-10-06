
#DuplicateEntryOption neews to be defined before WeightedBinaryTree in order to use it in the method parameters
#InsertionResult can be defined after WeightedBinaryTree if it is not used in the parameters.
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
            #print(f'{self.key} {self.weight} {self.sub_tree_weight} {self.get_tree_weight()}')
            print(str(self))
        else:
            #print(f'{prefix} {self.key} {self.weight} {self.sub_tree_weight} {self.get_tree_weight()}')
            print(f'{prefix} ' + str(self))
        if self.left is not None:
            self.left.display(prefix + 'l')
        if self.right is not None:
            self.right.display(prefix + 'r')

    def get_tree_weight(self):
        return self.weight + self.sub_tree_weight

    #TODO:  Make a DuplcateEntryOption class, for now just default to replace
    def insert(self, key, weight=DEFAULT_WEIGHT):
        self.simple_binary_insert(key, weight)

    def simple_binary_insert(self, key, weight=DEFAULT_WEIGHT, duplicate_entry_option=DuplicateEntryOption.ADD):
        if key is None:
            result = InsertionResult(None)
            result.status = InsertionResultStatus.FAILED
            return result

        result = InsertionResult()
        if key == self.key:
            self.weight = weight
            result.inserted_node = self
        elif key < self.key:
            if self.left is not None:
                result = self.left.simple_binary_insert(key, weight)
            else:
                self.left = WeightedBinaryTree(key, weight)
                result.inserted_node = self.left
                result.status = InsertionResultStatus.CREATED
        elif key > self.key:
            if self.right is not None:
                result = self.right.simple_binary_insert(key, weight)
            else:
                self.right = WeightedBinaryTree(key, weight)
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


class InsertionResultStatus:
    # public enum Status { CREATED, IGNORED, REPLACED, UPDATED, FAILED, UNKNOWN };
    CREATED = "Created"
    IGNORED = "Ignored"
    REPLACED = "Replaced"
    UPDATED = "Updated"
    FAILED = "Failed"
    UNKOWNN = "Unknown"


