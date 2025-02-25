fn find(parent: &mut Vec<usize>, x: usize) -> usize {
    if parent[x] != x {
        parent[x] = find(parent, parent[x]);
    }

    parent[x]
}

fn union(parent: &mut Vec<usize>, a: usize, b: usize) {
    let a = find(parent, a);
    let b = find(parent, b);

    if a < b {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}
