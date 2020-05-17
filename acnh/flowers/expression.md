---
title: Gene Expression
layout: acnh
---

# Roses

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WR][]![WR][]![LR][] | ![YR][]![WR][]![LR][] | ![YR][]![YR][]![WR][] |
| R1   | ![RR][]![RR][]![RR][] | ![OR][]![RR][]![RR][] | ![OR][]![OR][]![RR][] |
| R2   | ![BR][]![BR][]![BR][] | ![OR][]![RR][]![BR][] | ![OR][]![OR][]![UR][] |

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WR][]![WR][]![LR][] | ![YR][]![WR][]![LR][] | ![YR][]![YR][]![WR][] |
| R1   | ![PR][]![PR][]![PR][] | ![YR][]![PR][]![PR][] | ![YR][]![YR][]![PR][] |
| R2   | ![RR][]![RR][]![RR][] | ![OR][]![RR][]![RR][] | ![OR][]![OR][]![RR][] |

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WR][]![WR][]![LR][] | ![YR][]![WR][]![LR][] | ![YR][]![YR][]![WR][] |
| R1   | ![WR][]![WR][]![LR][] | ![YR][]![WR][]![LR][] | ![YR][]![YR][]![WR][] |
| R2   | ![PR][]![PR][]![PR][] | ![YR][]![WR][]![LR][] | ![YR][]![YR][]![WR][] |

| Pigment |    1    |    2    |    3    |
| ------- | :-----: | :-----: | :-----: |
| Red     | ![PR][] | ![RR][] | ![BR][] |
| Yellow  | ![YR][] | ![YR][] |         |
| Purple  | ![WR][] | ![LR][] |         |

| Gene | 0    | 1         | 2                               |
| ---- | ---- | --------- | ------------------------------- |
| 1    | None | Red +2    | Red +3                          |
| 2    | None | Yellow +1 | Yellow +2                       |
| 3    | None |           | Purple +1                       |
| 4    | None | Red -1    | Y0 → Red -2<br />Y1/2 → Red = 0 |

# Tulips

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WT][]![WT][]![WT][] | ![YT][]![YT][]![WT][] | ![YT][]![YT][]![YT][] |
| R1   | ![RT][]![PT][]![WT][] | ![OT][]![YT][]![YT][] | ![OT][]![YT][]![YT][] |
| R2   | ![BT][]![RT][]![RT][] | ![BT][]![RT][]![RT][] | ![LT][]![LT][]![LT][] |

| Gene | 0    | 1                     | 2                     |
| ---- | ---- | --------------------- | --------------------- |
| 1    | None | Red +3                | Red +5                |
| 2    | None | Yellow +3             | Yellow +4             |
| 3    | None | Red -1<br />Yellow -1 | Red -2<br />Yellow -2 |

| Pigment | Yellow 0 | Yellow 1 | Yellow 2 | Yellow 3 | Yellow 4 |
| ------- | :------: | :------: | :------: | :------: | :------: |
| Red 0   | ![WT][]  | ![WT][]  | ![YT][]  | ![YT][]  | ![YT][]  |
| Red 1   | ![WT][]  | ![YT][]  | ![YT][]  |          |          |
| Red 2   | ![PT][]  |          | ![YT][]  | ![YT][]  |          |
| Red 3   | ![RT][]  | ![RT][]  | ![LT][]  | ![OT][]  | ![OT][]  |
| Red 4   | ![RT][]  |          | ![RT][]  | ![LT][]  |          |
| Red 5   | ![BT][]  |          |          | ![BT][]  | ![LT][]  |

# Pansies

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WP][]![WP][]![UP][] | ![YP][]![YP][]![UP][] | ![YP][]![YP][]![YP][] |
| R1   | ![RP][]![RP][]![UP][] | ![OP][]![OP][]![OP][] | ![YP][]![YP][]![YP][] |
| R2   | ![RP][]![RP][]![LP][] | ![RP][]![RP][]![LP][] | ![OP][]![OP][]![LP][] |

| Gene | 0    | 1         | 2         |
| ---- | ---- | --------- | --------- |
| 1    | None | Red +1    | Red +2    |
| 2    | None | Yellow +1 | Yellow +2 |
| 3    | None | None      | Blue +1   |

| Pigment |    Yellow 0    |    Yellow 1    |    Yellow 2    |
| ------- | :------------: | :------------: | :------------: |
| Red 0   | ![WP][]![UP][] | ![YP][]![UP][] | ![YP][]![YP][] |
| Red 1   | ![RP][]![UP][] | ![OP][]![OP][] | ![YP][]![YP][] |
| Red 2   | ![RP][]![LP][] | ![RP][]![LP][] | ![OP][]![LP][] |

# Cosmos

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WC][]![WC][]![WC][] | ![YC][]![YC][]![WC][] | ![YC][]![YC][]![YC][] |
| R1   | ![PC][]![PC][]![PC][] | ![OC][]![OC][]![PC][] | ![OC][]![OC][]![OC][] |
| R2   | ![RC][]![RC][]![RC][] | ![OC][]![OC][]![RC][] | ![BC][]![BC][]![RC][] |

| Gene | 0    | 1         | 2                     |
| ---- | ---- | --------- | --------------------- |
| 1    | None | Red +1    | Red +2                |
| 2    | None | Yellow +1 | Yellow +2             |
| 3    | None | None      | Red +1<br />Yellow -1 |

| Pigment | Yellow 0 | Yellow 1 | Yellow 2 |
| ------- | :------: | :------: | :------: |
| Red 0   | ![WC][]  | ![YC][]  | ![YC][]  |
| Red 1   | ![PC][]  | ![OC][]  | ![OC][]  |
| Red 2   | ![RC][]  | ![OC][]  | ![BC][]  |
| Red 3   | ![RC][]  | ![RC][]  |          |

# Lilies

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WL][]![WL][]![WL][] | ![YL][]![WL][]![WL][] | ![YL][]![YL][]![WL][] |
| R1   | ![RL][]![PL][]![WL][] | ![OL][]![YL][]![YL][] | ![OL][]![YL][]![YL][] |
| R2   | ![BL][]![RL][]![PL][] | ![BL][]![RL][]![PL][] | ![OL][]![OL][]![WL][] |

| Gene | 0    | 1                     | 2                     |
| ---- | ---- | --------------------- | --------------------- |
| 1    | None | Red +2                | Red +3                |
| 2    | None | Yellow +3             | Yellow +4             |
| 3    | None | Red -1<br />Yellow -1 | Red -2<br />Yellow -2 |

| Pigment | Yellow 0 | Yellow 1 | Yellow 2 | Yellow 3 | Yellow 4 |
| ------- | :------: | :------: | :------: | :------: | :------: |
| Red 0   | ![WL][]  | ![WL][]  | ![WL][]  | ![YL][]  | ![YL][]  |
|         |          | ![YL][]  | ![YL][]  |          |          |
| Red 1   | ![PL][]  | ![PL][]  | ![YL][]  | ![YL][]  |          |
| Red 2   | ![RL][]  |          | ![RL][]  | ![OL][]  | ![OL][]  |
| Red 3   | ![BL][]  |          |          | ![BL][]  |          |

# Hyacinths

|      |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WH][]![WH][]![UH][] | ![YH][]![YH][]![WH][] | ![YH][]![YH][]![YH][] |
| R1   | ![RH][]![PH][]![WH][] | ![OH][]![YH][]![YH][] | ![OH][]![YH][]![YH][] |
| R2   | ![RH][]![RH][]![RH][] | ![UH][]![RH][]![RH][] | ![LH][]![LH][]![LH][] |

# Windflowers

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WW][]![WW][]![UW][] | ![OW][]![OW][]![UW][] | ![OW][]![OW][]![OW][] |
| R1   | ![RW][]![RW][]![UW][] | ![PW][]![PW][]![PW][] | ![OW][]![OW][]![OW][] |
| R2   | ![RW][]![RW][]![RW][] | ![RW][]![RW][]![LW][] | ![RW][]![RW][]![LW][] |

# Mums

| Gene |          Y0           |          Y1           |          Y2           |
| ---- | :-------------------: | :-------------------: | :-------------------: |
| R0   | ![WM][]![WM][]![LM][] | ![YM][]![YM][]![WM][] | ![YM][]![YM][]![YM][] |
| R1   | ![PM][]![PM][]![PM][] | ![YM][]![RM][]![PM][] | ![LM][]![LM][]![LM][] |
| R2   | ![RM][]![RM][]![RM][] | ![LM][]![LM][]![RM][] | ![GM][]![GM][]![RM][] |

| Gene | 0    | 1         | 2         |
| ---- | ---- | --------- | --------- |
| 1    | None | Red +1    | Red +2    |
| 2    | None | Yellow +2 | Yellow +3 |
| 3    | None | Yellow -1 | Y1 → 0    |

| Pigment | Yellow 0 | Yellow 1 | Yellow 3 |
| ------- | :------: | :------: | :------: |
| Red 0   | ![WM][]  | ![YM][]  | ![YM][]  |
| Red 1   | ![PM][]  | ![YM][]  | ![LM][]  |
| Red 2   | ![RM][]  | ![LM][]  | ![GM][]  |

[WR]: ../img/icon/RW.png "White Rose"
[RR]: ../img/icon/RR.png "Red Rose"
[YR]: ../img/icon/RY.png "Yellow Rose"
[PR]: ../img/icon/RP.png "Pink Rose"
[OR]: ../img/icon/RO.png "Orange Rose"
[LR]: ../img/icon/RU.png "Purple Rose"
[BR]: ../img/icon/RK.png "Black Rose"
[UR]: ../img/icon/RB.png "Blue Rose"
[RG]: ../img/icon/RG.png "Gold Rose"
[WT]: ../img/icon/TW.png "White Tulip"
[RT]: ../img/icon/TR.png "Red Tulip"
[YT]: ../img/icon/TY.png "Yellow Tulip"
[PT]: ../img/icon/TP.png "Pink Tulip"
[OT]: ../img/icon/TO.png "Orange Tulip"
[LT]: ../img/icon/TU.png "Purple Tulip"
[BT]: ../img/icon/TK.png "Black Tulip"

[WP]: ../img/icon/PW.png "White Pansy"
[RP]: ../img/icon/PR.png "Red Pansy"
[YP]: ../img/icon/PY.png "Yellow Pansy"
[OP]: ../img/icon/PO.png "Orange Pansy"
[LP]: ../img/icon/PU.png "Purple Pansy"
[UP]: ../img/icon/PB.png "Blue Pansy"

[RC]: ../img/icon/CR.png "Red Cosmos"
[WC]: ../img/icon/CW.png "White Cosmos"
[YC]: ../img/icon/CY.png "Yellow Cosmos"
[BC]: ../img/icon/CK.png "Black Cosmos"
[OC]: ../img/icon/CO.png "Orange Cosmos"
[PC]: ../img/icon/CP.png "Pink Cosmos"

[WL]: ../img/icon/LW.png "White Lily"
[RL]: ../img/icon/LR.png "Red Lily"
[YL]: ../img/icon/LY.png "Yellow Lily"
[PL]: ../img/icon/LP.png "Pink Lily"
[OL]: ../img/icon/LO.png "Orange Lily"
[BL]: ../img/icon/LK.png "Black Lily"

[RH]: ../img/icon/HR.png "Red Hyacinth"
[WH]: ../img/icon/HW.png "White Hyacinth"
[YH]: ../img/icon/HY.png "Yellow Hyacinth"
[LH]: ../img/icon/HU.png "Purple Hyacinth"
[OH]: ../img/icon/HO.png "Orange Hyacinth"
[PH]: ../img/icon/HP.png "Pink Hyacinth"
[UH]: ../img/icon/HB.png "Blue Hyacinth"

[RW]: ../img/icon/WR.png "Red Windflower"
[WW]: ../img/icon/WW.png "White Windflower"
[UW]: ../img/icon/WB.png "Blue Windflower"
[LW]: ../img/icon/WU.png "Purple Windflower"
[PW]: ../img/icon/WP.png "Pink Windflower"
[OW]: ../img/icon/WO.png "Orange Windflower"

[RM]: ../img/icon/MR.png "Red Mum"
[WM]: ../img/icon/MW.png "White Mum"
[YM]: ../img/icon/MY.png "Yellow Mum"
[LM]: ../img/icon/MU.png "Purple Mum"
[PM]: ../img/icon/MP.png "Pink Mum"
[GM]: ../img/icon/MG.png "Green Mum"