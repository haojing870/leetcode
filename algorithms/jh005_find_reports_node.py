# Need to have a dictionary to index the nodes
# Otherwise the created nodes will be gone

# Check if one person reports to multiple managers when building train
# Check if a->b, b->a circular reporting by reading from root


from collections import defaultdict

class person(object):
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.reports = []

def build_org_chart(pairs):
    ppl_dict = {}
    for a,b in pairs:
        if b not in ppl_dict:
            ppl_dict[b] = person(b,None)
        if a not in ppl_dict:
            ppl_dict[a] = person(a,b)
        elif ppl_dict[a].manager is not None and ppl_dict[a].manager != b:
            raise Exception('One person %s reoprts to >1 manager' % a)
            print 'Error: %s reports to >1 manager' % a
        ppl_dict[b].reports.append(a)
    return ppl_dict

def get_reports(p, org, mgmt_chain):
    if p in mgmt_chain:
        mgmt_chain.append(p)
        raise Exception('circular reporting %s' % '->'.join(mgmt_chain))
    
    reports = [p]
    mgmt_chain.append(p)
    for i in org[p].reports:
        reports += get_reports(org[i].name, org, mgmt_chain)
    mgmt_chain.remove(p)
    return reports

def get_reports_by_depth(p, org, depth):
    reports = defaultdict(list)
    reports[depth] = [p]
    for i in org[p].reports:
        for k,v in get_reports_by_depth(org[i].name, org, depth+1).iteritems():
            reports[k] += v
    return reports

def main():
    tests = [('a','b'), ('ab','c'), ('d','b'), ('e','b'),\
             ('g','c'), ('c','h'), ('b','e')]
    #tests = [('jh','cz'),('cz','ab'),('jh','bh')]
    ppl_dict = build_org_chart(tests)
    #print get_reports_by_depth('c', ppl_dict, 0)
    print get_reports('e', ppl_dict, [])

if __name__ == '__main__':
    main()
