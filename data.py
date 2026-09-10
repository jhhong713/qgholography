# -*- coding: utf-8 -*-
"""All editable content for the QG & Holography site.

Edit this file, then run:  python3 build.py
"""

PI_NAME = "Junho Hong"
PI_EMAIL = "junhohong@sogang.ac.kr"
CV_URL = "https://drive.google.com/file/d/1dUrk5StndWqmRpvLeok2jnu36gyC5fmx/view"
INSPIRE_URL = "https://inspirehep.net/authors/1669906"

# ---------------------------------------------------------------- people ----
# Each group: (role label, [members])
# Member keys: name_en, name_ko (optional), term (list of lines), links (list of (label, url))

PEOPLE = [
    ("Principal Investigator", [
        dict(
            name_en="Junho Hong",
            name_ko="홍준호",
            photo="p2.jpg",
            term=["2024.03 – present: Assistant Professor, Sogang University"],
            education=[
                ("2021", "Ph.D. in Physics, University of Michigan"),
                ("2016", "B.S. in Physics, Seoul National University"),
            ],
            career=[
                ("2024.03 – present", "Assistant Professor, Sogang University"),
                ("2021.09 – 2024.02", "Postdoctoral Researcher, KU Leuven"),
            ],
            links=[
                ("INSPIRE-HEP", INSPIRE_URL),
                ("Curriculum Vitae", CV_URL),
                ("Email", "mailto:" + PI_EMAIL),
            ],
        ),
    ]),
    ("Postdoctoral Researchers", [
        dict(name_en="Sourav Roychowdhury", photo="p4.jpg",
             term=["2025.04 – present"]),
        dict(name_en="Soumya Adhikari", photo="p3.jpg",
             term=["2025.10 – present"]),
    ]),
    ("Graduate Students", [
        dict(name_en="Suhyun Lee", name_ko="이수현", photo="p6.jpg",
             degree="MS–PhD integrated",
             term=["2025.03 – present", "2024.05 – 2025.02: Undergraduate Intern"]),
        dict(name_en="Gamseung Han", name_ko="한감승", photo="p1.jpg",
             degree="MS–PhD integrated",
             term=["2025.09 – present", "2025.07 – 2025.08: Undergraduate Intern"]),
        dict(name_en="Geum Lee", name_ko="이금", photo="p5.jpg",
             degree="Master",
             term=["2026.03 – present", "2025.01 – 2026.02: Undergraduate Intern"]),
        dict(name_en="Chanyoung Joung", name_ko="정찬영", photo="p8.jpg",
             degree="Master",
             term=["2026.03 – present", "2025.01 – 2026.02: Undergraduate Intern"]),
    ]),
    ("Undergraduate Interns", [
        dict(name_en="Dane Jeon", name_ko="전세진", photo="p7.jpg",
             term=["2026.02 – present: Military Service", "2025.01 – 2026.01: Undergraduate Intern"]),
    ]),
]

# ---------------------------------------------------------- publications ----
# (year, authors, title, journal_ref, arxiv, doi)
# `authors` uses "Junho Hong" verbatim — the builder bolds it automatically.
# journal_ref = "" means preprint.

PUBLICATIONS = [
    (2026, "Soumya Adhikari, Junho Hong, Chanyoung Joung, Geum Lee, Sourav Roychowdhury",
     "Boundary-value problem in type IIB supergravity and holography",
     "", "2609.03126", ""),
    (2026, "Junho Hong",
     "Constants in sequences of M2-brane partition functions",
     "", "2608.04204", ""),
    (2026, "Nikolay Bobev, Sunjin Choi, Junho Hong, Valentin Reys",
     "Towards OSV in AdS",
     "JHEP 09 (2026) 076", "2606.23893", "10.1007/JHEP09(2026)076"),
    (2026, "Soumya Adhikari, Junho Hong, Chanyoung Joung, Geum Lee",
     "Type IIB supergravity action and holography",
     "JHEP 06 (2026) 271", "2603.18248", "10.1007/JHEP06(2026)271"),

    (2025, "Nikolay Bobev, Marina David, Vasil Dimitrov, Junho Hong",
     "AdS<sub>7</sub> black holes and holography",
     "JHEP 11 (2025) 159", "2509.02833", "10.1007/JHEP11(2025)159"),
    (2025, "Nikolay Bobev, Pieter-Jan De Smet, Junho Hong, Valentin Reys, Xuao Zhang",
     "An Airy tale at large <i>N</i>",
     "JHEP 07 (2025) 123", "2502.04606", "10.1007/JHEP07(2025)123"),
    (2025, "Junho Hong",
     "Perturbatively exact supersymmetric partition functions of ABJM theory "
     "on Seifert manifolds and holography",
     "JHEP 01 (2025) 194", "2411.09006", "10.1007/JHEP01(2025)194"),

    (2024, "Nikolay Bobev, Sunjin Choi, Junho Hong, Valentin Reys",
     "Superconformal indices of 3d <i>N</i> = 2 SCFTs and holography",
     "JHEP 10 (2024) 121", "2407.13177", "10.1007/JHEP10(2024)121"),
    (2024, "Seppe Geukens, Junho Hong",
     "Subleading analysis for <i>S</i><sup>3</sup> partition functions of "
     "<i>N</i> = 2 holographic SCFTs",
     "JHEP 06 (2024) 190", "2405.00845", "10.1007/JHEP06(2024)190"),
    (2024, "Nikolay Bobev, Marina David, Junho Hong, Valentin Reys, Xuao Zhang",
     "A compendium of logarithmic corrections in AdS/CFT",
     "JHEP 04 (2024) 020", "2312.08909", "10.1007/JHEP04(2024)020"),

    (2023, "Nikolay Bobev, Junho Hong, Valentin Reys",
     "Holographic thermal observables and M2-branes",
     "JHEP 12 (2023) 054", "2309.06469", "10.1007/JHEP12(2023)054"),
    (2023, "Nikolay Bobev, Marina David, Junho Hong, Rishi Mouland",
     "AdS<sub>7</sub> black holes from rotating M5-branes",
     "JHEP 09 (2023) 143 [Erratum: JHEP 09 (2023) 198]", "2307.06364",
     "10.1007/JHEP09(2023)143"),
    (2023, "Nikolay Bobev, Junho Hong, Valentin Reys",
     "Large <i>N</i> partition functions of 3d holographic SCFTs",
     "JHEP 08 (2023) 119", "2304.01734", "10.1007/JHEP08(2023)119"),
    (2023, "Nikolay Bobev, Thomas Hertog, Junho Hong, Joel Karlsson, Valentin Reys",
     "Microscopics of de Sitter entropy from precision holography",
     "Phys. Rev. X 13 (2023) 041056", "2211.05907", "10.1103/PhysRevX.13.041056"),
    (2023, "Nikolay Bobev, Sunjin Choi, Junho Hong, Valentin Reys",
     "Large <i>N</i> superconformal indices for 3d holographic SCFTs",
     "JHEP 02 (2023) 027", "2210.15326", "10.1007/JHEP02(2023)027"),
    (2023, "Nikolay Bobev, Junho Hong, Valentin Reys",
     "Large <i>N</i> partition functions of the ABJM theory",
     "JHEP 02 (2023) 020", "2210.09318", "10.1007/JHEP02(2023)020"),

    (2022, "Alfredo González Lezcano, Junho Hong, James T. Liu, "
           "Leopoldo A. Pando Zayas, Christoph F. Uhlemann",
     "<i>c</i>-functions in flows across dimensions",
     "JHEP 10 (2022) 083", "2207.09360", "10.1007/JHEP10(2022)083"),
    (2022, "Nikolay Bobev, Junho Hong, Valentin Reys",
     "Large <i>N</i> partition functions, holography, and black holes",
     "Phys. Rev. Lett. 129 (2022) 041602", "2203.14981",
     "10.1103/PhysRevLett.129.041602"),
    (2022, "Arash Arabi Ardehali, Junho Hong",
     "Decomposition of BPS moduli spaces and asymptotics of supersymmetric "
     "partition functions",
     "JHEP 01 (2022) 062", "2110.01538", "10.1007/JHEP01(2022)062"),

    (2021, "Junho Hong",
     "The topologically twisted index of <i>N</i> = 4 SU(<i>N</i>) super-Yang-Mills "
     "theory and a black hole Farey tail",
     "JHEP 10 (2021) 145", "2108.02355", "10.1007/JHEP10(2021)145"),
    (2021, "Junho Hong, James T. Liu",
     "Subleading corrections to the <i>S</i><sup>3</sup> free energy of "
     "necklace quiver theories dual to massive IIA",
     "JHEP 11 (2021) 183", "2103.17033", "10.1007/JHEP11(2021)183"),
    (2021, "Alfredo González Lezcano, Junho Hong, James T. Liu, Leopoldo A. Pando Zayas",
     "The Bethe-Ansatz approach to the <i>N</i> = 4 superconformal index at finite rank",
     "JHEP 06 (2021) 126", "2101.12233", "10.1007/JHEP06(2021)126"),
    (2021, "Alfredo González Lezcano, Junho Hong, James T. Liu, Leopoldo A. Pando Zayas",
     "Sub-leading structures in superconformal indices: subdominant saddles "
     "and logarithmic contributions",
     "JHEP 01 (2021) 001", "2007.12604", "10.1007/JHEP01(2021)001"),
    (2021, "Junho Hong",
     "The <i>N</i> = 4 SU(<i>N</i>) super-Yang-Mills index and dual AdS black holes",
     "Ph.D. thesis, University of Michigan", "", "10.7302/1496"),

    (2020, "Arash Arabi Ardehali, Junho Hong, James T. Liu",
     "Asymptotic growth of the 4d <i>N</i> = 4 index and partially deconfined phases",
     "JHEP 07 (2020) 073", "1912.04169", "10.1007/JHEP07(2020)073"),

    (2019, "Junho Hong, Niall T. Macpherson, Leopoldo A. Pando Zayas",
     "Aspects of AdS<sub>2</sub> classification in M-theory: solutions with "
     "mesonic and baryonic charges",
     "JHEP 11 (2019) 127", "1908.08518", "10.1007/JHEP11(2019)127"),
    (2019, "Junho Hong, Finn Larsen, James T. Liu",
     "The scales of black holes with nAdS<sub>2</sub> geometry",
     "JHEP 10 (2019) 260", "1907.08862", "10.1007/JHEP10(2019)260"),

    (2018, "Junho Hong, James T. Liu, Daniel R. Mayerson",
     "Gauged six-dimensional supergravity from warped IIB reductions",
     "JHEP 09 (2018) 140", "1808.04301", "10.1007/JHEP09(2018)140"),
    (2018, "Junho Hong, James T. Liu",
     "The topologically twisted index of <i>N</i> = 4 super-Yang-Mills on "
     "<i>T</i><sup>2</sup> × <i>S</i><sup>2</sup> and the elliptic genus",
     "JHEP 07 (2018) 018", "1804.04592", "10.1007/JHEP07(2018)018"),
]

# ------------------------------------------------------------- teaching ----
# (course title, level, [terms taught])
# Listed from introductory to advanced.

COURSES = [
    ("General Physics I", "Undergraduate", ["2025 Spring", "2026 Spring"]),
    ("General Physics II", "Undergraduate", ["2026 Fall"]),
    ("Electromagnetism I", "Undergraduate", ["2024 Spring", "2025 Spring"]),
    ("Electromagnetism II", "Undergraduate", ["2024 Fall", "2025 Fall"]),
    ("Mathematical Physics II", "Undergraduate", ["2026 Fall"]),
    ("Quantum Mechanics II", "Graduate", ["2024 Fall"]),
    ("Quantum Field Theory I", "Graduate", ["2025 Fall"]),
    ("Quantum Field Theory II", "Graduate", ["2026 Spring"]),
]

# (lecture title, host, when)
SPECIAL_LECTURES = [
    ("Precision Holography",
     "SNU&ndash;APCTP Winter School on Fundamental Physics",
     "2026 Feb 2&ndash;6"),
]
