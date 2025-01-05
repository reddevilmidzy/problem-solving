use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();

    let a: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();
    let b: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut a_pre: Vec<u64> = vec![0; n + 1];
    let mut b_pre: Vec<u64> = vec![0; n + 1];

    for i in 0..n {
        a_pre[i + 1] = a_pre[i] + a[i];
        b_pre[i + 1] = b_pre[i] + b[i];
    }

    let mut a_k = vec![a_pre[n]; k + 1];
    let mut b_k = vec![b_pre[n]; k + 1];

    for i in 1..=k {
        let mut a_tmp = u64::MAX;
        let mut b_tmp = u64::MAX;
        for j in 0..=n {
            if j + (n - i) > n {
                break;
            }
            a_tmp = a_tmp.min(a_pre[j + (n - i)] - a_pre[j]);
            b_tmp = b_tmp.min(b_pre[j + (n - i)] - b_pre[j]);
        }
        a_k[i] = a_tmp;
        b_k[i] = b_tmp;
    }
    //
    // println!("a_k = {:?}", a_k);
    // println!("b_k = {:?}", b_k);
    // println!("{:?}", a_pre);
    // println!("{:?}", b_pre);
    //
    let mut res = u64::MAX;
    for i in 0..=k {
        let aa = a_k[i].max(b_k[k - i]);
        let bb = b_k[i].max(a_k[k - i]);
        res = res.min(aa.min(bb));
    }
    print!("{res}");
}
