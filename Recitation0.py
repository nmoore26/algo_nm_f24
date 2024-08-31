#Recitation0


'''In this recitation, you will complete the Knuth-Morris-Pratt string matching algorithm.
I wrote the function compute_table, which tells you how much to shift the gene when a mismatch is found.
You must complete the algorithm by completing the function, kmp.
'''
def compute_table(gene):
    '''Expect that gene is a string.
    returns a list of indices. The jth index in the list indicates how many places to move the pattern if a mismatch occurs at position j.
    This is not the most efficient way to do this. This is an O(m^3) algorithm, where m is the length of gene.
    I've written it this way because this is the most direct way to describe how the table is defined.
    A better implementation can run in linear time, O(m).
    '''
    table = []
    for j,g in enumerate(gene):
        shift_when_mismatch_at_j = min([s for s in range(j+1) if gene[:j-s]==gene[s:j] and gene[j]!= gene[j-s]], default = j+1)
        table.append(shift_when_mismatch_at_j)
    return table

def test_compute_table():
    gene = "abcabcacab"
    print(compute_table(gene))
    ideal_answer=  [ j - i +1 for j,i in enumerate([0,1,1,0,1,1,0,5,0,1])] #See Knuth's paper, keep in mind he starts indexing at 1 instead of 0.
    assert compute_table(gene)== ideal_answer
test_compute_table()
#print( compute_table("abcabcacab"))

def kmp(gene,genome): 
    ''' Your code here.
        Implement the Knuth-Morris-Pratt algorithm: On input gene and genome, it should return True if gene in genome and False otherwise.
        Your code should not use string comparison to compare strings of length 2 or more.
        This is because we are pretending to code in C, where we must compare each element of an array, individually.
    '''
    if len(gene) == 0:
        return True

    if len(gene) > len(genome):
        return False  # No match possible if gene is longer than genome

    table = compute_table(gene)
    i = 0  # index for genome
    m_id = 0  # index for gene
    for i in range(len(genome)):
        if genome[i] == gene[m_id]:
            i += 1
            m_id += 1
            print(i,m_id)
            if m_id == len(gene):
                return True  # Found the gene in genome
        else:
            if m_id != 0:
                shift = table[m_id -1]  # Use the table to find the shift value
                i  = shift
                m_id =0
            else:
                i += 1
    return False  # Gene not found in genome
    


def test_kmp():
    '''
    Do not modify this code. Make sure that this test passes before pushing your code to github.
    '''
    genes = ["", "a","t", "att", "cat", "catacatttcat", "ggggaa", "atatatatat", "aaaat", "aaaa"]
    genomes = ["", "a", "catacattaccattacgaccag", "atgcacattatatatatatgcatat", "gggggggaaaaaaaa", "aaa", "taaa"]

    for gene in genes:
        for genome in genomes: #tests every pair of gene and genome.
            # You can uncomment out this to help you debug.
            # print("gene, genome", gene, genome)
            # print(kmp(gene, genome))
            # print(gene in genome)
            assert(kmp(gene, genome) == (gene in genome) ) #asserts that the kmp function returns the same value as the builtin 'in' function.
test_kmp()
