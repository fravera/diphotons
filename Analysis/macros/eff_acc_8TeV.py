
import ROOT

points = [
    (750,0.412357 ),
    (1000,0.467164),
    (1250,0.512209),
    (1500,0.548338),
    (1750,0.589140),
    (2000,0.621876),
    (2250,0.641876),
    (2500,0.649571),
    (3000,0.659437),
]



gr = ROOT.TGraph()

for ip in points: gr.SetPoint(gr.GetN(),ip[0],ip[1])

gr.Fit("pol2")

gr.Draw()

