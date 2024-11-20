use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();
    let t: usize = input.next().unwrap().unwrap().parse().unwrap();

    let mut res = String::with_capacity(t);
    for _ in 0..t {
        let n = input.next().unwrap().unwrap();
        res.push_str(&n);
        res.push('\n');
    }
    print!("{res}")
}
