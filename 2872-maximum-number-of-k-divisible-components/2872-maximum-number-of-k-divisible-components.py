class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Pick root = 0 (you tried to find real root, but in a tree ANY root works)
        root = 0

        # DFS: returns (components_in_subtree, remainder_of_subtree)
        def dfs(node, parent):
            total_components = 0
            remainder_sum = values[node] % k

            for child in g[node]:
                if child == parent:
                    continue

                child_components, child_remainder = dfs(child, node)

                total_components += child_components

                if child_remainder == 0:
                    # child subtree is divisible → CUT IT
                    total_components += 1
                else:
                    # must merge child's remainder into parent
                    remainder_sum = (remainder_sum + child_remainder) % k

            # If after merging all children, the parent's sum is divisible:
            # The entire subtree becomes a new component
            if remainder_sum == 0:
                return total_components, 0

            return total_components, remainder_sum

        components, rem = dfs(root, -1)

        # If root also becomes divisible, count it
        if rem == 0:
            components += 1

        return components
        