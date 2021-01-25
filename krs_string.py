import krs_photo0 as photo0,krs_photo1 as photo1,krs_photo2 as photo2,krs_photo3 as photo3,krs_photo4 as photo4,krs_photo5 as photo5
import random as r

#special message
spmsg=(
"\n"*5,
"          50 YEARS ANNIVERSARY",
'        |/AMEN  |)IDER  ("ERIES',
"        |\\      |\\      _)\n",
"  They are powerful heroes of justice,",
" the masked warriors  with unfathomable",
" power beyond the  strength of mortals,",
"   who are willing to  fight against",
"  the malevolent forces - to  protect",
"          our beautiful world!\n",
"        They are - KAMEN RIDERS.",
"\n"*5,
"Kamen Rider - Created by Shotaro Ishinomori\n(C)1971-2021 Toei Company and Ishimori Pro."
)
photo=(
photo0.source,
photo1.source,
photo2.source,
photo3.source,
photo4.source,
photo5.source
)
menu=(
"."+"-"*30+".",
"|                              |",
"|      SELECT YOUR  RIDER      |",
"|     [1] - KAMEN RIDER 1      |",
"|     [2] - KAMEN RIDER 2      |",
"|     [3] - KAMEN RIDER V3     |",
"|   [4] - KAMEN RIDER AMAZON   |",
"|    [5] - KAMEN RIDER BLACK   |",
"|  [6] - KAMEN RIDER BLACK RX  |",
"|                              |",
"'"+"-"*30+"'"
)
selected=(
"|        KAMEN RIDER  1        |",
"|        KAMEN RIDER  2        |",
"|        KAMEN RIDER V3        |",
"|      KAMEN RIDER AMAZON      |",
"|      KAMEN RIDER  BLACK      |",
"|     KAMEN RIDER BLACK RX     |",
)
select=[
"."+"-"*30+".",
"|                              |",
"|      YOU HAVE  SELECTED      |",
"|                              |",
selected[0],
"|                              |",
"|   PRESS ENTER  TO CONTINUE   |",
"|                              |",
"'"+"-"*30+"'"
]
kaijin=(
#final boss
"|   Great Demon King  of Eleven Realms   |",
#Level 2 bosses (1 - 8)
"|         Merciless  Machine Man         |",
"|           Hideous Hopper Man           |",
"|          Menacing  Monkey Man          |",
"|         Frightening Fungus Man         |",
"|           Jealousy Jelly Man           |",
"|          Shivering  Shock Man          |",
"|           Cranky  Copper Man           |",
"|            Heinous  Hog Man            |",
#Level 1 bosses (9 - 13)
"|           Professor  Turbine           |",
"|           Creepy Blender Man           |",
"|           Evil  Serpent Naga           |",
"|             Crimson Knight             |",
"|             Sleepy Peacock             |",
)
level=[
"."+"-"*40+".",
"|"+" "*40+"|",
kaijin[0],#2
"|"+" "*40+"|",
"'"+"-"*40+"'",#4
" "*20+"||",
" "*20+"||",
"."+"-"*40+".",
"|"+" "*40+"|",
kaijin[8],#9
"|"+" "*40+"|",
kaijin[8],#11
"|"+" "*40+"|",
kaijin[8],#13
"|"+" "*40+"|",
"'"+"-"*40+"'",#15
" "*20+"||",
" "*20+"||",
"."+"-"*40+".",
"|"+" "*40+"|",
kaijin[13],#20
"|"+" "*40+"|",
kaijin[13],#22
"|"+" "*40+"|",
"'"+"-"*40+"'",#24
]