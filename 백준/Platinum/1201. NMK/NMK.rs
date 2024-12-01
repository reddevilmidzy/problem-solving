use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();

    if n - m + 1 < k {
        print!("-1");
        return;
    }

    let mut res: Vec<usize> = Vec::with_capacity(n);

    let mut lds = n;

    for i in (1..=m).rev() {
        res.push(i);

        let mut tmp = Vec::with_capacity(k - 1);
        for _ in 0..k - 1 {
            if lds <= m {
                break;
            }
            tmp.push(lds);
            lds -= 1;
        }
        tmp.reverse();
        res.extend(tmp);
    }
    res.reverse();
    if res.len() != n {
        print!("-1");
        return;
    }
    for val in res {
        print!("{} ", val);
    }
}
