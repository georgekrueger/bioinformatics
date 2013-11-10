
import DnaReverseComplement

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
        self.mostFrequentMap = {}
        self.findMostFrequentKmersWithMismatchRecursive(self.root, "", m, 0)
        #print self.mostFrequentMap
        for k,v in self.mostFrequentMap.iteritems():
            if v == self.mostFrequentNum:
                self.mostFrequent.append(k)
            elif v > self.mostFrequentNum:
                self.mostFrequentNum = v
                self.mostFrequent = [k]
        return self.mostFrequent

    def findMostFrequentKmersWithMismatchRecursive(self, node, s, m, mismatches):
        if mismatches > m:
            return
        
        if node.level == self.k:
            if s in self.mostFrequentMap:
                self.mostFrequentMap[s] += node.count
            else:
                self.mostFrequentMap[s] = node.count
                
            revComp = DnaReverseComplement.dnaReverseComplement(s)
            if revComp in self.mostFrequentMap:
                self.mostFrequentMap[revComp] += node.count
            else:
                self.mostFrequentMap[revComp] = node.count
                
            return
        for k,v in node.nodes.iteritems():
            self.findMostFrequentKmersWithMismatchRecursive(v, s+k, m, mismatches)

        # traverse paths that don't exist for mismatches
        for k in ["T", "A", "C", "G"]:
                for k2,v2 in node.nodes.iteritems():
                    if k2 != k:
                        self.findMostFrequentKmersWithMismatchRecursive(v2, s+k, m, mismatches+1)
            

if __name__ == "__main__":
    f = open("stepic_dataset.txt")
    buff = f.readline().split(' ')
    text = buff[0]
    k = int(buff[1])
    d = int(buff[2])
    tree = KmerTree(text, k)
    #tree = KmerTree("ACGTTGCATGTCGCATGATGCATGAGAGCT", 5)
    #tree.printTree()
    mostFreq = tree.findMostFrequentKmersWithMismatch(d)
    print " ".join(mostFreq)



