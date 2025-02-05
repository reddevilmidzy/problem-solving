use std::collections::BinaryHeap;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut hq = BinaryHeap::with_capacity(n);

    let mut even = 0;
    for i in 0..n {
        let num: i32 = next().parse().unwrap();
        even += num;
        if num > 0 {
            hq.push((num, i));
        }
    }
    // 총합이 짝수여야 한다.
    if even % 2 != 0 {
        print!("-1");
        return;
    }

    let mut graph = vec![vec![0; n]; n];

    while let Some((cur, i)) = hq.pop() {
        // 현재 차수만큼 젤 큰놈 끄집어냄
        if hq.len() < cur as usize {
            print!("-1");
            return;
        }

        let mut tmp = BinaryHeap::with_capacity(cur as usize);
        for _ in 0..cur {
            let (nxt, j) = hq.pop().unwrap();
            graph[i][j] = 1;
            graph[j][i] = 1;
            if nxt > 1 {
                tmp.push((nxt - 1, j));
            }
        }
        hq.append(&mut tmp);
    }

    let mut res = String::new();
    for i in 0..n {
        for j in 0..n {
            write!(res, "{} ", graph[i][j]).unwrap();
        }
        writeln!(res, "").unwrap();
    }
    print!("{res}");
}
