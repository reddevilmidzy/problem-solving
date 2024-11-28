use std::collections::HashMap;
use std::io::{read_to_string, stdin};

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

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let pis: Vec<usize> = (0..3).map(|_| next().parse().unwrap()).collect();
    let mut idx = HashMap::new();

    for i in 0..3 {
        idx.insert(pis[i], i);
    }

    let mut edges: Vec<Vec<usize>> = Vec::with_capacity(m);

    for _ in 0..m {
        let u: usize = next().parse().unwrap();
        let v: usize = next().parse().unwrap();
        let w: usize = next().parse().unwrap();
        let k: usize = next().parse().unwrap();
        edges.push(vec![w, idx[&k], u, v]);
    }
    edges.sort();
    let mut parent: Vec<usize> = (0..=n).collect();

    let mut cnt = n - 1;
    let mut ans: Vec<usize> = vec![0; 3];
    let mut cost: Vec<usize> = vec![0; 3];

    for edge in edges {
        if find(&mut parent, edge[2]) != find(&mut parent, edge[3]) {
            union(&mut parent, edge[2], edge[3]);
            cnt -= 1;
            ans[pis[edge[1]]] += 1;
            cost[pis[edge[1]]] += edge[0];

            if cnt == 0 {
                break;
            }
        }
    }
    println!("{}", cost.iter().sum::<usize>());

    for i in 0..3 {
        println!("{} {}", ans[i], cost[i]);
    }
}
