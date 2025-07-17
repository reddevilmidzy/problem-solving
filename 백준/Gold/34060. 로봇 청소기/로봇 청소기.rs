use std::collections::{HashMap, HashSet};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();

    let mut edges = Vec::new();
    let mut x_lines: HashMap<i32, Vec<(i32, usize)>> = HashMap::new();

    let mut x = 1;
    let y: i32 = next().parse().unwrap();
    x_lines.entry(y).or_default().push((x, 1));

    let mut pre = y;

    for i in 2..=n {
        let y: i32 = next().parse().unwrap();
        if pre + 1 == y {
            edges.push((i - 1, i));
        }
        if pre >= y {
            x += 1;
        }
        x_lines.entry(y).or_default().push((x, i));

        pre = y;
    }
    for vals in x_lines.values() {
        for i in 1..vals.len() {
            if vals[i - 1].0 + 1 == vals[i].0 {
                edges.push((vals[i - 1].1, vals[i].1));
            }
        }
    }

    // println!("{edges:?}");
    // println!("{x_lines:?}");

    let mut parent: Vec<usize> = (0..=n).collect();

    for (u, v) in edges {
        if find(&mut parent, u) != find(&mut parent, v) {
            union(&mut parent, u, v);
        }
    }

    for x in 1..=n {
        parent[x] = find(&parent, x);
    }

    let res: HashSet<usize> = parent.into_iter().collect();

    // println!("{parent:?}");
    print!("{}\n{n}", res.len() - 1);
}

fn find(parent: &Vec<usize>, x: usize) -> usize {
    if parent[x] != x {
        return find(parent, parent[x]);
    }
    x
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
