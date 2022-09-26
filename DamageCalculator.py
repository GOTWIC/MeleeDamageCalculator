def calculateMeleeDMG(w, b):
    cc = w.cc * (1 + b.br + b.ss + b.gl2)
    cd = w.cd * (1 + b.os + b.gl1)
    atkspd = w.speed * (1 + w.pf + w.bf)
    rng = w.range + w.pr + w.slb
    sc = w.sc * (1 + w.ww + w.vs + w.vf + w.cm2)
    b = w.b

    # Do Damage Calculations here
