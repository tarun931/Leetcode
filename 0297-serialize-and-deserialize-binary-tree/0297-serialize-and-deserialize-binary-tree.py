# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def helper(root):
            if not root:
                res.append("N")
                return 
            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)       
        return ",".join(res)      

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def helper():
            if vals[self.i]=="N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node

        root = helper()
        return root




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))