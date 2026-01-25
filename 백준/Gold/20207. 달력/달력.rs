use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    const M: usize = 365;
    let mut arr = vec![0; M + 2];
    for _ in 0..n {
        let (s, e): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        arr[s] += 1;
        arr[e + 1] -= 1;
    }

    for i in 1..=M {
        arr[i] += arr[i - 1];
    }

    let mut res = 0;
    let mut width = 0;
    let mut height = 0;
    for i in 1..=M {
        if arr[i] == 0 {
            res += width * height;
            width = 0;
            height = 0;
        } else {
            width += 1;
            height = height.max(arr[i]);
        }
    }

    res += width * height;
    print!("{res}");
}
