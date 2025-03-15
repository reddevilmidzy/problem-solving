use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();

    let mut lions: Vec<u32> = Vec::with_capacity(k);
    let mut min_lion = u32::MAX;
    let mut max_lion = 0;

    for _ in 0..k {
        let num = next().parse().unwrap();
        min_lion = min_lion.min(num);
        max_lion = max_lion.max(num);
        lions.push(num);
    }

    let mut res = 0;
    for i in 0..k - 1 {
        res += lions[i].abs_diff(lions[i + 1]);
    }

    let mut min_human = u32::MAX;
    let mut max_human = 0;
    for _ in 0..n - k {
        let num = next().parse().unwrap();
        min_human = min_human.min(num);
        max_human = max_human.max(num);
    }

    if min_human < min_lion {
        let l = lions[0].abs_diff(min_human);
        let r = lions[k - 1].abs_diff(min_human);
        let m = min_lion.abs_diff(min_human) * 2;
        res += l.min(r).min(m);
    }
    if max_human > max_lion {
        let l = lions[0].abs_diff(max_human);
        let r = lions[k - 1].abs_diff(max_human);
        let m = max_lion.abs_diff(max_human) * 2;
        res += l.min(r).min(m);
    }

    println!("{}", res);
}
