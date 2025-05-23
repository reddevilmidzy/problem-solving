use std::collections::BinaryHeap;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split("\n");
    let mut next = || token.next();

    let mut res = String::new();
    while let Some(input) = next() {
        if input.is_empty() {
            break;
        }
        let nums: Vec<i32> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();
        let n = nums.len();
        writeln!(res, "{}", solve(n, nums)).unwrap();
    }
    print!("{res}");
}

fn solve(n: usize, nums: Vec<i32>) -> String {
    let mut res = String::new();
    let mut hq = BinaryHeap::with_capacity(n);

    let mut even = 0;
    for i in 0..n {
        even += nums[i];
        if nums[i] > 0 {
            hq.push((nums[i], i));
        }
    }
    // 총합이 짝수여야 한다.
    if even % 2 != 0 {
        writeln!(res, "fail").unwrap();
        return res;
    }

    let mut graph = vec![vec![0; n]; n];

    while let Some((cur, i)) = hq.pop() {
        // 현재 차수만큼 젤 큰놈 끄집어냄
        if hq.len() < cur as usize {
            writeln!(res, "fail").unwrap();
            return res;
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

    for i in 0..n {
        for j in 0..n {
            write!(res, "{} ", graph[i][j]).unwrap();
        }
        writeln!(res, "").unwrap();
    }
    res
}
