use std::collections::HashMap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut real_time = HashMap::new();
    let mut mos = Vec::with_capacity(n * 2);

    for i in 0..n {
        let (st, ed): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        mos.push((st, i, 1));
        mos.push((ed, i, -1));
    }

    mos.sort();
    let mut pre_val = mos[0].0;
    real_time.insert(0, mos[0].0);
    mos[0] = (0, mos[0].1, mos[0].2);

    for i in 1..n * 2 {
        if mos[i].0 == pre_val {
            pre_val = mos[i].0;
            mos[i] = (mos[i - 1].0, mos[i].1, mos[i].2);
        } else {
            real_time.insert(mos[i - 1].0 + 1, mos[i].0);
            pre_val = mos[i].0;
            mos[i] = (mos[i - 1].0 + 1, mos[i].1, mos[i].2);
        }
    }

    let mut pre = vec![0; n * 2 + 1];

    for (idx, _, val) in &mos {
        pre[*idx] += val;
    }
    let mut max_cnt = pre[0];
    for i in 1..pre.len() {
        pre[i] += pre[i - 1];
        max_cnt = max_cnt.max(pre[i]);
    }

    let mut idx = 0;
    while pre[idx] < max_cnt {
        idx += 1;
    }
    print!("{}\n{} ", max_cnt, real_time.get(&idx).unwrap());
    while pre[idx] == max_cnt {
        idx += 1;
    }
    print!("{}", real_time.get(&idx).unwrap());
}
