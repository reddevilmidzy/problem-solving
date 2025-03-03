use std::collections::VecDeque;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let nums: Vec<Vec<i32>> = (0..n)
        .map(|_| (0..m).map(|_| next().parse().unwrap()).collect())
        .collect();
    let mut visited = vec![vec![false; m]; n];

    let d = vec![(1, 0), (0, 1), (-1, 0), (0, -1)];
    let mut res = 0;

    for y in 0..n {
        for x in 0..m {
            if nums[y][x] > 0 && !visited[y][x] {
                let tmp = bfs(n,m,&nums, &mut visited, y, x);
                if tmp >= 0{
                    res += tmp;
                } else {
                    print!("-1");
                    return;
                }
            }
        }
    }
    print!("{res}");
}

fn bfs(
    n: usize,
    m: usize,
    nums: &Vec<Vec<i32>>,
    visited: &mut Vec<Vec<bool>>,
    r: usize,
    c: usize,
) -> i32 {
    let d = vec![(1, 0), (0, 1), (-1, 0), (0, -1)];

    let mut queue = VecDeque::new();
    visited[r][c] = true;
    queue.push_back((r, c));
    while let Some((y, x)) = queue.pop_front() {
        for &(dy, dx) in &d {
            let ny = y as i32 + dy;
            let nx = x as i32 + dx;

            if ny < 0 || nx < 0 || ny as usize >= n || nx as usize >= m {
                continue;
            }
            let ny = ny as usize;
            let nx = nx as usize;

            if nums[ny][nx] == -1 {
                continue;
            }
            if !visited[ny][nx] && nums[y][x].abs_diff(nums[ny][nx]) > 1 {
                return -1;
            }
            if !visited[ny][nx] && nums[ny][nx] > 0 && nums[y][x] - nums[ny][nx] == 1 {
                visited[ny][nx] = true;
                queue.push_back((ny, nx));
            }
        }
    }

    for &(dy, dx) in &d {
        let ny = r as i32 + dy;
        let nx = c as i32 + dx;

        if ny < 0 || nx < 0 || ny as usize >= n || nx as usize >= m {
            continue;
        }
        let ny = ny as usize;
        let nx = nx as usize;
        if nums[ny][nx] == -1 {
            continue;
        }
        if nums[ny][nx] - nums[r][c] == 1 {
            return 0;
        }
    }

    1

}
