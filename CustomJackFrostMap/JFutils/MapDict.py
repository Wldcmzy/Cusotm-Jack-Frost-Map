prj = '''
1 178977703c66276066a776a56de3c1a1.xml
2 4f9410119d8e6ba4898cc6d56ab9eccb.xml
3 81d3d295a180f7309cb3ae5c35dc25b6.xml
4 aa5e1aab44b3a8d2ad03ce3772bf8834.xml
5 d6cd27a071357cc4df1ac79a4bd9d268.xml
6 f395cf63edbc9aea96c82bf326fe68ac.xml
7 c712f2336df850e2fa326e091b61040c.xml
8 f88a41582e95b14a42372c0aaa4bed45.xml
9 9f532a138d80956ceff12f2cac5d21a8.xml
10 4cefaeec1a05ba68bcefc8ebe6355f18.xml
11 daf53a1d555887a99bc71aea2ae90935.xml
12 64c5d8b3769a1cc33f8920b371c7282e.xml
13 da2c58df20cb4eb3f2be5ed330b596fd.xml
14 6c6f9e3647881c9d2fd0dfca2202f329.xml
15 990a588a3350934dcc6e52c3492881b0.xml
16 66a5a27abb1e128be447f89bdc27d5ae.xml
17 f1a31f872eae2e1dcd1463c34e882741.xml
18 feb8e98038b2c26c7db532f2b594aaf0.xml
19 454750d80ae2b0a21c06759f9a5e0caa.xml
20 01712286e17752c6436a9854bca38e54.xml
21 b80570407a04fbd976545fa1675b0097.xml
22 2fb74059c98719c7cff859b10a3d595b.xml
23 7651d3ef552f38f0439d9ec3e4fb1ff5.xml
24 6530a5be1fb446a713b649834553bd2e.xml
25 6a6edededfbe4e49a1c8e21e158aa5e9.xml
26 66a5a27abb1e128be447f89bdc27d5ae.xml
27 3431973cee84e7ec5f9aa389a76bfb67.xml
28 32482fc4666cce514102f5da3ba424b2.xml
29 9f9dafb169788fd274274ccddf47bf12.xml
30 32d770098dc9dbec9520f3727062298e.xml
31 58bb48058a2d858513cd5bbc4ea4952f.xml
32 2f3bd076c409c63d9b8cef1a74eaab4a.xml
33 e8619f515a53ac7a70aa6fcd46b1a711.xml
34 9adf686d461f08f58261f84ea6f74fda.xml
35 03863d9b6c97ddf3c2ad8f1235a6f1ea.xml
36 3431973cee84e7ec5f9aa389a76bfb67.xml
37 4fab476e906c1e6f49b46b9f3662056a.xml
38 a7e6bbe95fc85417fcaa01f51d00e33f.xml
39 116fe93a6230a699f2b64569ab5077a0.xml
40 6c6f9e3647881c9d2fd0dfca2202f329.xml
'''.strip()

mapdict = {}

for each in prj.split('\n'):
    x, y = each.split()
    x = int(x)
    mapdict[x] = y
    mapdict[y] = x

