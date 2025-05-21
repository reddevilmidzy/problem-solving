use std::collections::{HashMap, VecDeque};
use std::io::{read_to_string, stdin};

fn calc(c: char) -> u8 {
    1 << (c as u8 - 'a' as u8)
}

fn partner(c: usize) -> usize {
    if c == 0 {
        return 3;
    }
    if c == 1 {
        return 5;
    }
    if c == 2 {
        return 4;
    }
    if c == 3 {
        return 0;
    }
    if c == 4 {
        return 2;
    }
    if c == 5 {
        return 1;
    }
    unreachable!()
}

fn nxt_pos(c: usize) -> (i32, i32) {
    if c == 0 {
        return (-1, 0);
    }
    if c == 1 {
        return (0, 1);
    }
    if c == 2 {
        return (0, 1);
    }
    if c == 3 {
        return (1, 0);
    }
    if c == 4 {
        return (0, -1);
    }
    if c == 5 {
        return (0, -1);
    }
    unreachable!()
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let board: Vec<Vec<usize>> = (0..n)
        .map(|_| {
            next()
                .chars()
                .map(|c| c.to_digit(10).unwrap() as usize)
                .collect()
        })
        .collect();

    let mut nums = vec![0; 10];

    // a=0, b=1, c=2, d=3, e=4, f=5, g=6
    nums[0] |= calc('a');
    nums[0] |= calc('b');
    nums[0] |= calc('c');
    nums[0] |= calc('d');
    nums[0] |= calc('e');
    nums[0] |= calc('f');

    nums[1] |= calc('b');
    nums[1] |= calc('c');

    nums[2] |= calc('a');
    nums[2] |= calc('b');
    nums[2] |= calc('g');
    nums[2] |= calc('e');
    nums[2] |= calc('d');

    nums[3] |= calc('a');
    nums[3] |= calc('b');
    nums[3] |= calc('g');
    nums[3] |= calc('c');
    nums[3] |= calc('d');

    nums[4] |= calc('f');
    nums[4] |= calc('b');
    nums[4] |= calc('g');
    nums[4] |= calc('c');

    nums[5] |= calc('a');
    nums[5] |= calc('f');
    nums[5] |= calc('g');
    nums[5] |= calc('c');
    nums[5] |= calc('d');

    nums[6] |= calc('a');
    nums[6] |= calc('f');
    nums[6] |= calc('g');
    nums[6] |= calc('e');
    nums[6] |= calc('d');
    nums[6] |= calc('c');

    nums[7] |= calc('a');
    nums[7] |= calc('b');
    nums[7] |= calc('c');

    nums[8] |= calc('a');
    nums[8] |= calc('b');
    nums[8] |= calc('c');
    nums[8] |= calc('d');
    nums[8] |= calc('e');
    nums[8] |= calc('f');
    nums[8] |= calc('g');

    nums[9] |= calc('a');
    nums[9] |= calc('b');
    nums[9] |= calc('c');
    nums[9] |= calc('d');
    nums[9] |= calc('f');
    nums[9] |= calc('g');

    let mut graph: HashMap<(usize, usize), Vec<(usize, usize)>> = HashMap::new();

    let nn = n as i32;
    let mm = m as i32;

    for y in 0..nn {
        for x in 0..mm {
            // a,b,c,d,e,f
            for k in 0..6 {
                let nxt = nxt_pos(k);
                // 상대 위치
                let ny = y + nxt.0;
                let nx = x + nxt.1;

                if ny < 0 || nx < 0 || ny >= nn || nx >= mm {
                    continue;
                }
                let ny = ny as usize;
                let nx = nx as usize;

                // 상대꺼
                let p = partner(k);
                let y = y as usize;
                let x = x as usize;
                let cur = nums[board[y][x]];
                let nxt = nums[board[ny][nx]];
                let k = k as u8;

                if ((cur >> k) & 1) != 0 && ((nxt >> p) & 1) != 0 {
                    graph.entry((y, x)).or_default().push((ny, nx));
                    graph.entry((ny, nx)).or_default().push((y, x));
                }
            }
        }
    }

    let mut visited = vec![vec![false; m]; n];
    let mut queue = VecDeque::new();
    queue.push_back((0usize, 0usize));
    visited[0][0] = true;

    while let Some((y, x)) = queue.pop_front() {
        for &(ny, nx) in graph.get(&(y, x)).unwrap_or(&vec![]) {
            if !visited[ny][nx] {
                visited[ny][nx] = true;
                queue.push_back((ny, nx));
            }
        }
    }

    for i in 0..n {
        for j in 0..m {
            if !visited[i][j] {
                print!("NO");
                return;
            }
        }
    }

    print!("YES");
}
