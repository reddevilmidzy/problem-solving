use std::io::{read_to_string, stdin};

fn back(candy: &mut Vec<Vec<usize>>, visited: &mut Vec<bool>, n: usize, cur: &mut Vec<usize>) {
    if cur.len() == n {
        candy.push(cur.clone());
    }
    for i in 0..n {
        if !visited[i] {
            visited[i] = true;
            cur.push(i);
            back(candy, visited, n, cur);
            cur.pop();
            visited[i] = false;
        }
    }
}
fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();

    let nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut candy = Vec::new();
    let mut visited = vec![false; n];

    back(&mut candy, &mut visited, n, &mut Vec::new());
    let mut res : usize = 0;
    for can in candy {
        let mut cur = 500;
        let mut flag = true;
        for i in can {
            cur += nums[i];
            cur -= k;
            if cur < 500 {
                flag = false;
                break;
            }
        }
        if flag {
            res += 1;
        }
    }
    print!("{res}")
}

