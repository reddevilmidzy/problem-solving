use std::io::{stdin, read_to_string};
use std::fmt::Write;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut graph = vec![n; n];
    let mut st = vec![true; n];

    for i in 0..n {
        for j in i+1..n {
            let a = nums[i];
            let b = nums[j];

            if a*2 == b {
                graph[i] = j;
                st[j] = false;
            } else if b*2 == a {
                graph[j] = i;
                st[i] = false;
            } else if a*3 == b {
                graph[j] = i;
                st[i] = false;
            } else if b*3 == a {
                graph[i] = j;
                st[j] = false;
            }
        }
    }

    let mut res = String::new();
    for i in 0..n {
        if st[i] {

            write!(res, "{}", nums[i]).unwrap();
            let mut cur = graph[i];

            while cur != n {
                write!(res, " {}", nums[cur]).unwrap();
                cur = graph[cur];
            }
        }
    }
    print!("{res}");

}