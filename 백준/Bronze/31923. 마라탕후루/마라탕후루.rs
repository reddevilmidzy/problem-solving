use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let p: u32 = next().parse().unwrap();
    let q: u32 = next().parse().unwrap();

    let mut a: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    let mut b: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut res = vec![0; n];

    let mut cnt = 0;
    for i in 0..n {
        let mut tmp = 0;
        while a[i] != b[i] {
            tmp += 1;
            cnt += 1;
            if cnt > 10_000 {
                print!("NO");
                return;
            }
            a[i] += p;
            b[i] += q;
        }
        res[i] = tmp;
    }

    println!("YES");
    for i in 0..n {
        print!("{} ", res[i]);
    }
}
