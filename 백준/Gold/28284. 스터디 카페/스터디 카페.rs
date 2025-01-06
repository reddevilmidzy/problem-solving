use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut a: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();
    let mut time: Vec<(usize, i32)> = Vec::with_capacity(2 * n);
    let mut real_time: Vec<usize> = vec![0; m * 2 + 1];
    for _ in 0..m {
        let (st, ed): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        time.push((st, 1));
        time.push((ed + 1, -1));
    }

    time.sort();
    real_time[0] = time[0].0;
    let mut pre = vec![0; m * 2 + 1];
    let mut pre_val = time[0].0;
    time[0] = (0, time[0].1);

    for i in 1..m * 2 {
        if time[i].0 == pre_val {
            pre_val = time[i].0;
            time[i] = (time[i - 1].0, time[i].1);
        } else {
            real_time[time[i - 1].0 + 1] = time[i].0;
            pre_val = time[i].0;
            time[i] = (time[i - 1].0 + 1, time[i].1);
        }
    }

    for (idx, val) in &time {
        pre[*idx] += val;
    }

    for i in 1..pre.len() {
        pre[i] += pre[i - 1];
    }
    a.sort();
    let mut max_a: Vec<u64> = vec![0; n];
    let mut min_a: Vec<u64> = vec![0; n];
    min_a[0] = a[0] as u64;
    max_a[0] = a[n - 1] as u64;
    for i in 1..n {
        min_a[i] += min_a[i - 1] + a[i] as u64;
        max_a[i] += max_a[i - 1] + a[n - i - 1] as u64;
    }

    let mut min_res: u64 = 0;
    let mut max_res: u64 = 0;
    for i in 0..pre.len() - 1 {
        if pre[i] == 0 {
            continue;
        }
        let st = real_time[i];
        let ed = real_time[i + 1];

        let diff = (ed - st) as u64;
        min_res += min_a[pre[i] as usize - 1] * diff;
        max_res += max_a[pre[i] as usize - 1] * diff;
    }
    print!("{} {}", min_res, max_res);
}
