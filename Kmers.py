
class KmerNode:
    def __init__(self, level, count=1):
        self.nodes = {}
        self.count = count
        self.level = level

    def printRecursive(self):
        self.printRecursiveInternal(self, 0)

    def printRecursiveInternal(self, node, i):
        for k,v in node.nodes.iteritems():
            print "  " * i + k + "(%s)" % v.count
            self.printRecursiveInternal(v, i+1)

class KmerTree:
    def __init__(self, text, k):
        self.root = KmerNode(0)
        self.k = k
        self.mostFrequent = []
        self.mostFrequentNum = 0
        for i in xrange(len(text)-k+1):
            n = self.root
            level = 1
            for j in xrange(i, i+k):
                c = text[j]
                if c in n.nodes:
                    n.nodes[c].count += 1
                else:
                    n.nodes[c] = KmerNode(level)
                n = n.nodes[c]
                level += 1

    def printTree(self):
        self.root.printRecursive()

    def findMostFrequentKmers(self):
        self.mostFrequent = []
        self.mostFrequentNum = 0
        self.findMostFrequentKmersRecursive(self.root, "")
        return self.mostFrequent

    def findMostFrequentKmersRecursive(self, node, s):
        if node.level == self.k:
            if node.count == self.mostFrequentNum:
                self.mostFrequent.append(s)
            elif node.count > self.mostFrequentNum:
                self.mostFrequentNum = node.count
                self.mostFrequent = [s]
            return
        for k,v in node.nodes.iteritems():
            self.findMostFrequentKmersRecursive(v, s+k)

    def findMostFrequentKmersWithMismatch(self, m):
        self.mostFrequent = []
        self.mostFrequentNum = 0
        self.findMostFrequentKmersWithMismatchRecursive(self.root, "", m, 0)
        return self.mostFrequent

    def findMostFrequentKmersWithMismatchRecursive(self, node, s, m, mismatches):
        if mismatches > m:
            return
        #print "checking mismatched string: %s (mismatch: %s)" % (s, mismatches)
        if node.level == self.k:
            print "%s (%s) %s" % (s, node.count, mismatches)
            if node.count == self.mostFrequentNum:
                self.mostFrequent.append(s)
            elif node.count > self.mostFrequentNum:
                self.mostFrequentNum = node.count
                self.mostFrequent = [s]
            return
        for k,v in node.nodes.iteritems():
            self.findMostFrequentKmersWithMismatchRecursive(v, s+k, m, mismatches)
        # traverse paths that don't exist for mismatches
        for k in ["T", "A", "C", "G"]:
            if k not in node.nodes.keys():
                self.findMostFrequentKmersWithMismatchRecursive(KmerNode(node.level+1, node.count), s+k, m, mismatches+1)
            

tree = KmerTree("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
tree.printTree()
print tree.findMostFrequentKmersWithMismatch(1)
print tree.mostFrequentNum

#tree = KmerTree(text, 9)
#print tree.findMostFrequentKmers()
#print tree.mostFrequentNum


