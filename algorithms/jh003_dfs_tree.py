# Need to have a dictionary to index the nodes
# Otherwise the created nodes will be gone

from collections import defaultdict

def build_org_chart(data):
    tree_map = {}
    for (a,b) in data:
        if a not in tree_map:
            tree_map[a] = []
        if b not in tree_map:
            tree_map[b] = []
        tree_map[b].append(a)
    return tree_map

def get_reports(p, tree_map):
    reports = [p]
    for c in tree_map[p]:
        reports += get_reports(c, tree_map)
    return reports

def get_reports_by_depth(p, tree_map, depth):
    reports = defaultdict(list)
    reports[depth].append(p)
    for c in tree_map[p]:
        for key, val in get_reports(c, tree_map, depth+1).iteritems():
            reports[key] += val
    return reports

def main():
    tests = [('a','b'), ('b','c'), ('d','b'), ('e','b'),\
             ('b','f'), ('g','c'), ('c','h')]
    org = build_org_chart(tests)
    print org
    # print get_reports_by_depth('c',org,0)
    print get_reports('c', org)

if __name__ == '__main__':
    main()
