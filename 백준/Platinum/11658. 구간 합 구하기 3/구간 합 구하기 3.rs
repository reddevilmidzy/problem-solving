use std::fmt::Write;
use std::io::{read_to_string, stdin};

#[derive(Debug)]
struct Seg2D {
    n: usize,
    a: Vec<Vec<u32>>,
}

impl Seg2D {
    fn new(n: usize) -> Self {
        let a = vec![vec![0; n * 2]; n * 2];
        Self { n, a }
    }

    fn init(&mut self, val: Vec<Vec<u32>>) {
        for i in 0..self.n {
            for j in 0..self.n {
                self.a[i + self.n][j + self.n] = val[i][j];
            }
        }

        for i in self.n..self.n * 2 {
            for j in (1..self.n).rev() {
                self.a[i][j] = self.a[i][j << 1] + self.a[i][j << 1 | 1];
            }
        }

        for i in (1..self.n).rev() {
            for j in 1..self.n * 2 {
                self.a[i][j] = self.a[i << 1][j] + self.a[i << 1 | 1][j];
            }
        }
    }

    fn update(&mut self, x: usize, y: usize, val: u32) {
        self.a[x + self.n][y + self.n] = val;

        let mut i = y + self.n;

        while i > 1 {
            self.a[x + self.n][i >> 1] = self.a[x + self.n][i] + self.a[x + self.n][i ^ 1];
            i >>= 1;
        }

        let mut x = x + self.n;
        while x > 1 {
            let mut i = y + self.n;
            while i >= 1 {
                self.a[x >> 1][i] = self.a[x][i] + self.a[x ^ 1][i];
                i >>= 1;
            }
            x >>= 1;
        }
    }

    fn query1d(&self, x: usize, mut y1: usize, mut y2: usize) -> u32 {
        let mut res = 0;
        y1 += self.n;
        y2 += self.n + 1;

        while y1 < y2 {
            if (y1 & 1) != 0 {
                res += self.a[x][y1];
                y1 += 1;
            }
            if (y2 & 1) != 0 {
                y2 -= 1;
                res += self.a[x][y2];
            }
            y1 >>= 1;
            y2 >>= 1;
        }

        res
    }

    pub fn query(&self, mut x1: usize, y1: usize, mut x2: usize, y2: usize) -> u32 {
        let mut res = 0;
        x1 += self.n;
        x2 += self.n + 1;
        while x1 < x2 {
            if (x1 & 1) != 0 {
                res += Self::query1d(&self, x1, y1, y2);
                x1 += 1;
            }
            if (x2 & 1) != 0 {
                x2 -= 1;
                res += Self::query1d(&self, x2, y1, y2);
            }
            x1 >>= 1;
            x2 >>= 1;
        }

        res
    }
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let val: Vec<Vec<u32>> = (0..n)
        .map(|_| (0..n).map(|_| next().parse::<u32>().unwrap()).collect())
        .collect();
    let mut seg = Seg2D::new(n);

    seg.init(val);

    // println!("{:?}", &seg);

    for _ in 0..m {
        let cmd: u8 = next().parse().unwrap();
        if cmd == 0 {
            let (x, y, c): (usize, usize, u32) = (
                next().parse().unwrap(),
                next().parse().unwrap(),
                next().parse().unwrap(),
            );
            seg.update(x - 1, y - 1, c);
        } else {
            let (x1, y1, x2, y2): (usize, usize, usize, usize) = (
                next().parse().unwrap(),
                next().parse().unwrap(),
                next().parse().unwrap(),
                next().parse().unwrap(),
            );
            writeln!(res, "{}", seg.query(x1 - 1, y1 - 1, x2 - 1, y2 - 1)).unwrap();
        }
    }

    print!("{res}");
}
