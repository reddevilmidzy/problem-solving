use std::io;
use std::cmp::max;

fn gcd(a: i64, b: i64) -> i64 {
    let mut a = a;
    let mut b = b;
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    a
}

fn lcm(a: i64, b: i64) -> i64 {
    a / gcd(a, b) * b
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let mut iter = input.split_whitespace();
    let d: i64 = iter.next().unwrap().parse().expect("Failed to parse");
    let mut p: i64 = iter.next().unwrap().parse().expect("Failed to parse");
    let mut q: i64 = iter.next().unwrap().parse().expect("Failed to parse");

    if p < q {
        std::mem::swap(&mut p, &mut q);
    }

    let mut res = f64::INFINITY;
    let lcm_pq = lcm(p, q);

    for i in (0..=std::cmp::min(d, lcm_pq) + p).step_by(p as usize) {
        let target = max(d - i, 0);
        let mut tmp = target / q * q;

        if tmp < target {
            tmp += q;
        }
        if res > (tmp + i) as f64 {
            res = (tmp + i) as f64;
        }
    }

    println!("{}", res);
}