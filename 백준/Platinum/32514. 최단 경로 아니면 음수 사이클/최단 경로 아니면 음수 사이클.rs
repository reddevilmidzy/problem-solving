use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let st: usize = next().parse().unwrap();

    let mut edges = Vec::new();

    for _ in 0..m {
        let (u, v, w): (usize, usize, i32) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );

        edges.push((u, v, w));
    }

    print!("{}", solve(n, st, edges));
}

fn solve(n: usize, st: usize, edges: Vec<(usize, usize, i32)>) -> String {
    let inf = i32::MAX;
    let mut dist = vec![inf; n];
    dist[st] = 0;
    let mut parent = vec![-1; n];
    let mut last_update = -1;
    for _ in 0..n {
        last_update = -1;
        for &(u, v, w) in &edges {
            if dist[u] != inf && dist[u] + w < dist[v] {
                dist[v] = dist[u] + w;
                parent[v] = u as i32;
                last_update = v as i32;
            }
        }
    }

    let mut res = String::new();

    if last_update == -1 {
        writeln!(res, "PATH").unwrap();
        for i in 0..n {
            write!(res, "{} ", dist[i]).unwrap();
        }
        return res;
    }
    let mut cycle = Vec::new();
    let mut cur = last_update;
    for _ in 0..n {
        cur = parent[cur as usize];
    }

    let start = cur;
    cycle.push(start);
    cur = parent[start as usize];

    while cur != start {
        cycle.push(cur);
        cur = parent[cur as usize];
    }

    cycle.push(start);
    cycle.reverse();

    writeln!(res, "CYCLE").unwrap();
    writeln!(res, "{}", cycle.len() - 1).unwrap();
    for node in cycle {
        write!(res, "{node} ").unwrap();
    }

    res
}

#[test]
fn tmp() {
    let n = 4;
    // let edges = vec![(0, 1, -3), (1, 2, -8), (1, 3, 3), (2, 0, 11), (3, 0, 0)];
    // let edges = vec![(0,1,-1), (1,2,-2), (2,0,-3),(1,0,0)];
    // let edges = vec![
    //     (2, 1, 1),
    //     (0, 1, -1),
    //     (1, 2, -2),
    //     (2, 3, 5),
    //     (3, 4, 0),
    //     (4, 0, -3),
    //     (3, 0, 8),
    // ];
    let edges = vec![(1, 0, 4), (2, 3, 5), (3, 1, -2), (1, 2, -6)];
    // let edges = vec![(0,1,5), (1,2,1), (1,3,2), (4,3,-1), (3,5,2), (5,4,-3), (2,4,1)];

    print!("{}", solve(n, 1, edges));
}
