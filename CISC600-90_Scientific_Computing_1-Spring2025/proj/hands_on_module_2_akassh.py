# Hands on module 2
# - Course: CISC600-90-O
# - Semester: Spring 2025
# - Student Name: Akassh Shah

# Pick and solve one (1) problem from the set { 2.18, 2.26, 2.27 } pages 53-55, using Python or another programming language. Analyze your results and upload your solution as either a Jupyter notebook (.ipynb) file with generated program output, OR as a text or word file with your solution including generated program output and a separate source code file, if applicable.

# (Note: make sure to use the official textbook Chapra and Canale, 8th edition - don't use an earlier or newer edition)

# Problem chosen: 2.18

# 2.18

# 2.18 Piecewise functions are sometimes useful when the relationship between a dependent and an independent variable cannot be adequately represented by a single equation. For example, the velocity of a rocket might be described by
# υ(t) =
#         11t^2 - 5t         when 0 ≤ t ≤ 10
#         1100 - 5t           when 10 ≤ t ≤ 20
#         50t + 2(t - 20)^2   when 20 ≤ t ≤ 30
#         1520e^(0.2(t - 30))     when t > 30
#         0                   otherwise
# Develop a well-structured function to compute v as a function of t. Then use this function to generate a table of v versus t for t = -5 to 50 at increments of 0.5.

from math import e


def velocity_of_rocket(t: float):
    return {
        0.0 <= t <= 10: (11 * (t**2)) - (5 * t),
        10.0 <= t <= 20.0: 1100 - (5 * t),
        20.0 <= t <= 30.0: (50 * t) + (2 * ((t - 20) ** 2)),
        30.0 < t: 1520 * (e ** (0.2 * (t - 30))),
    }.get(True, 0.0)


if __name__ == "__main__":
    for i in range(-1, 101, 1):
        t = i / 2.0
        print(f"velocity of rocket at time {t=}: {velocity_of_rocket(t)}")

# Output
# velocity of rocket at time t=-0.5: 0.0
# velocity of rocket at time t=0.0: 0.0
# velocity of rocket at time t=0.5: 0.25
# velocity of rocket at time t=1.0: 6.0
# velocity of rocket at time t=1.5: 17.25
# velocity of rocket at time t=2.0: 34.0
# velocity of rocket at time t=2.5: 56.25
# velocity of rocket at time t=3.0: 84.0
# velocity of rocket at time t=3.5: 117.25
# velocity of rocket at time t=4.0: 156.0
# velocity of rocket at time t=4.5: 200.25
# velocity of rocket at time t=5.0: 250.0
# velocity of rocket at time t=5.5: 305.25
# velocity of rocket at time t=6.0: 366.0
# velocity of rocket at time t=6.5: 432.25
# velocity of rocket at time t=7.0: 504.0
# velocity of rocket at time t=7.5: 581.25
# velocity of rocket at time t=8.0: 664.0
# velocity of rocket at time t=8.5: 752.25
# velocity of rocket at time t=9.0: 846.0
# velocity of rocket at time t=9.5: 945.25
# velocity of rocket at time t=10.0: 1050.0
# velocity of rocket at time t=10.5: 1047.5
# velocity of rocket at time t=11.0: 1045.0
# velocity of rocket at time t=11.5: 1042.5
# velocity of rocket at time t=12.0: 1040.0
# velocity of rocket at time t=12.5: 1037.5
# velocity of rocket at time t=13.0: 1035.0
# velocity of rocket at time t=13.5: 1032.5
# velocity of rocket at time t=14.0: 1030.0
# velocity of rocket at time t=14.5: 1027.5
# velocity of rocket at time t=15.0: 1025.0
# velocity of rocket at time t=15.5: 1022.5
# velocity of rocket at time t=16.0: 1020.0
# velocity of rocket at time t=16.5: 1017.5
# velocity of rocket at time t=17.0: 1015.0
# velocity of rocket at time t=17.5: 1012.5
# velocity of rocket at time t=18.0: 1010.0
# velocity of rocket at time t=18.5: 1007.5
# velocity of rocket at time t=19.0: 1005.0
# velocity of rocket at time t=19.5: 1002.5
# velocity of rocket at time t=20.0: 1000.0
# velocity of rocket at time t=20.5: 1025.5
# velocity of rocket at time t=21.0: 1052.0
# velocity of rocket at time t=21.5: 1079.5
# velocity of rocket at time t=22.0: 1108.0
# velocity of rocket at time t=22.5: 1137.5
# velocity of rocket at time t=23.0: 1168.0
# velocity of rocket at time t=23.5: 1199.5
# velocity of rocket at time t=24.0: 1232.0
# velocity of rocket at time t=24.5: 1265.5
# velocity of rocket at time t=25.0: 1300.0
# velocity of rocket at time t=25.5: 1335.5
# velocity of rocket at time t=26.0: 1372.0
# velocity of rocket at time t=26.5: 1409.5
# velocity of rocket at time t=27.0: 1448.0
# velocity of rocket at time t=27.5: 1487.5
# velocity of rocket at time t=28.0: 1528.0
# velocity of rocket at time t=28.5: 1569.5
# velocity of rocket at time t=29.0: 1612.0
# velocity of rocket at time t=29.5: 1655.5
# velocity of rocket at time t=30.0: 1700.0
# velocity of rocket at time t=30.5: 1679.8597954749846
# velocity of rocket at time t=31.0: 1856.532192403458
# velocity of rocket at time t=31.5: 2051.7853875155247
# velocity of rocket at time t=32.0: 2267.573540414731
# velocity of rocket at time t=32.5: 2506.056331464195
# velocity of rocket at time t=33.0: 2769.620576593574
# velocity of rocket at time t=33.5: 3060.9041153551243
# velocity of rocket at time t=34.0: 3382.8222113085503
# velocity of rocket at time t=34.5: 3738.5967289585633
# velocity of rocket at time t=35.0: 4131.788379257749
# velocity of rocket at time t=35.5: 4566.332356398579
# velocity of rocket at time t=36.0: 5046.577722559552
# velocity of rocket at time t=36.5: 5577.330934781251
# velocity of rocket at time t=37.0: 6163.903949603905
# velocity of rocket at time t=37.5: 6812.167386913858
# velocity of rocket at time t=38.0: 7528.609285080574
# velocity of rocket at time t=38.5: 8320.400035425344
# velocity of rocket at time t=39.0: 9195.464145907677
# velocity of rocket at time t=39.5: 10162.559552264489
# velocity of rocket at time t=40.0: 11231.365270374587
# velocity of rocket at time t=40.5: 12412.578267102828
# velocity of rocket at time t=41.0: 13718.020519139865
# velocity of rocket at time t=41.5: 15160.757331318377
# velocity of rocket at time t=42.0: 16755.22809857524
# velocity of rocket at time t=42.5: 18517.390820269276
# velocity of rocket at time t=43.0: 20464.88181320257
# velocity of rocket at time t=43.5: 22617.19222180671
# velocity of rocket at time t=44.0: 24995.863092067517
# velocity of rocket at time t=44.5: 27624.70096155346
# velocity of rocket at time t=45.0: 30530.01612324525
# velocity of rocket at time t=45.5: 33740.885947791285
# velocity of rocket at time t=46.0: 37289.44589960621
# velocity of rocket at time t=46.5: 41211.211159399994
# velocity of rocket at time t=47.0: 45545.43207204347
# velocity of rocket at time t=47.5: 50335.486977212306
# velocity of rocket at time t=48.0: 55629.31635439053
# velocity of rocket at time t=48.5: 61479.902627302436
# velocity of rocket at time t=49.0: 67945.80042981726
# velocity of rocket at time t=49.5: 75091.72264040587
# velocity of rocket at time t=50.0: 82989.18805037923
