// 0-index
// ref: https://infossm.github.io/blog/2019/11/15/2D-segment-tree/

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
