import halver

class Separator():
  def __init__(self, a, f, eps_b, eps_f):
    self.a = a
    self.f = f
    self.eps_b = eps_b
    self.eps_f = eps_f
    self.line_wire_map = {}

    self.t = 0
    while 2**(self.t) * f < self.a :
        self.t += 1

    assert self.a % 2 == 0
    assert self.f % 2 == 0
    assert self.t >= 2

    self.eps = min(self.eps_b, self.eps_f / (self.t + 1))

    self.inputs = []

  def separate(self, inputs):
      h0 = halver.create_halver(self.a, self.eps)
      b0 = h0.sort([y for x, y in inputs])

      assert(len(b0) % 2 == 0)
      bl0 = b0[:len(b0)/2]
      br0 = b0[len(b0)/2:]

      sz = self.a - (2**(self.t-1) * self.f)

      assert 0 <= sz <= (self.a / 2)
      assert sz % 2 == 0
      assert sz <= (len(b0) / 2)

      h1 = halver.create_halver(sz, self.eps)

      blr1 = h1.sort(bl0[:sz])[sz/2:]
      bll = [elem for elem in bl0 if elem not in blr1]

      brl1 = h1.sort(br0[:sz])[:sz/2]
      brr = [elem for elem in br0 if elem not in brl1]

      sz = 2**(self.t - 2) * self.f
      assert(len(bll) == sz and len(brr) == sz)

      for stage in range(self.t - 1):
          assert sz % 2 == 0
          h = halver.create_halver(sz, self.eps)
          bll = h.sort(bll)[:sz/2]
          brr = h.sort(brr)[sz/2:]
          sz /= 2

      assert len(brr) == sz and len(bll) == sz and sz * 2 == self.f

      bl = [elem for elem in bl0 if elem not in bll]
      br = [elem for elem in br0 if elem not in brr]

      flr = bll
      flr.extend(brr)

      assert(len(flr) == self.f)

      lc, rc, par = [], [], []

      for index in range(self.a):
          if 0 <= index < self.f : 
              par.append((inputs[index][0], flr[index]))
          elif self.f <= index < self.f + (self.a - self.f) / 2:
              lc.append((inputs[index][0], bl[index - self.f]))
          else:
              rc.append((inputs[index][0], br[index - self.f/2 - self.a/2]))

      return (par, lc, rc)
