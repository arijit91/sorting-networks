import halver

class Separator():
  def __init__(self, a, f, eps_b, eps_f):
    self.a = a
    self.f = f
    self.eps_b = eps_b
    self.eps_f = eps_f
    self.line_wire_map = {}

    if self.f != 0:
        self.t = 0
        while 2**(self.t) * f < self.a :
            self.t += 1
        self.eps = min(self.eps_b, self.eps_f / (self.t + 1))
    else :
        self.eps = self.eps_b

    assert self.a % 2 == 0
    assert self.f % 2 == 0

    self.inputs = []

  def separate(self, inputs):
      h0 = halver.create_halver(self.a, self.eps)
      b0 = h0.sort([y for x, y in inputs])

      par, lc, rc = [], [], []

      assert(len(b0) % 2 == 0)
      bl0 = b0[:len(b0)/2]
      br0 = b0[len(b0)/2:]

      if self.f == 0 :
          flr = []
          bl = bl0
          br = br0

      elif self.t == 0 :
          assert self.f == self.a 
          flr = [y for x, y in inputs]
          bl = []
          br = []

      else :

        sz = self.a - (2**(self.t-1) * self.f)

        assert 0 <= sz <= (self.a / 2)
        assert sz % 2 == 0
        assert sz <= (len(b0) / 2)

        h1 = halver.create_halver(sz, self.eps)

        blr1 = h1.sort(bl0[:sz])[sz/2:]
        brl1 = h1.sort(br0[:sz])[:sz/2]

        bll, brr = bl0[:], br0[:]
        for elem in blr1:
            bll.remove(elem)

        for elem in brl1:
            brr.remove(elem)

        sz = 2**(self.t - 2) * self.f

        assert(len(bll) == sz and len(brr) == sz)

        for stage in range(self.t - 1):
            assert sz % 2 == 0
            h = halver.create_halver(sz, self.eps)
            bll = h.sort(bll)[:sz/2]
            brr = h.sort(brr)[sz/2:]
            sz /= 2

        assert len(brr) == sz and len(bll) == sz and sz * 2 == self.f

        bl, br = bl0[:], br0[:]
        for elem in bll:
            bl.remove(elem)

        for elem in brr:
            br.remove(elem)

        flr = bll
        flr.extend(brr)

        assert(len(flr) == self.f)

      for index in range(self.a):
          if 0 <= index < self.f : 
              par.append((inputs[index][0], flr[index]))
          elif self.f <= index < self.f + (self.a - self.f) / 2:
              lc.append((inputs[index][0], bl[index - self.f]))
          else:
              rc.append((inputs[index][0], br[index - self.f/2 - self.a/2]))

      #print par
      #print
      #print lc
      #print
      #print rc
      #pause = raw_input()
      return (par, lc, rc)
