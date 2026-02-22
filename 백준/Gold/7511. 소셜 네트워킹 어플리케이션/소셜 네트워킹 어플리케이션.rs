use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn find(x: usize, parent: &mut Vec<usize>) -> usize {
    if parent[x] != x {
        parent[x] = find(parent[x], parent);
    }
    parent[x]
}

fn union(a: usize, b: usize, parent: &mut Vec<usize>) {
    let a = find(a, parent);
    let b = find(b, parent);

    if a < b {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let t = next().parse::<u32>().unwrap();

    let mut res = String::new();

    for i in 1..=t {
        writeln!(res, "Scenario {i}:").unwrap();
        let n: usize = next().parse().unwrap();
        let k: u32 = next().parse().unwrap();
        let mut parent = (0..=n).collect::<Vec<_>>();
        for _ in 0..k {
            let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
            union(u, v, &mut parent);
        }
        let m: u32 = next().parse().unwrap();
        for _ in 0..m {
            let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
            let u = find(u, &mut parent);
            let v = find(v, &mut parent);

            if u != v {
                writeln!(res, "0").unwrap();
            } else {
                writeln!(res, "1").unwrap();
            }
        }
        writeln!(res, "").unwrap();
    }
    print!("{res}");
}
