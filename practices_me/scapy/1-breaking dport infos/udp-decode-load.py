>>> read = rdpcap('message.pcapng')
>>> read
<message.pcapng: TCP:0 UDP:1663 ICMP:0 Other:0>


>>> for list in read:
...:     print(list['UDP'])

>>> list
<Ether  dst=00:00:00:00:00:00 src=00:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=29 id=14169 flags=DF frag=0 ttl=64 proto=udp chksum=0x575 src=127.0.0.1 dst=127.0.0.1 |<UDP  sport=59990 dport=3 len=9 chksum=0xfe1c |<Raw  load='x' |>>>>


>>> for list in read:
...:     print(list['UDP'].dport,end=' , ')
...: 
40 , 41 , 78 , 210 , 134 , 83 , 218 , 175 , 26 , 165 , 74 , 166 , 187 , 161 , 101 , 191 , 156 , 117 , 105 , 82 , 235 , 152 , 240 , 158 , 67 , 7 , 100 , 224 , 75 , 141 , 5 , 162 , 216 , 28 , 180 , 239 , 155 , 141 , 142 , 121 , 41 , 143 , 110 , 27 , 137 , 15 , 101 , 17 , 164 , 232 , 246 , 88 , 99 , 98 , 252 , 27 , 99 , 23 , 22 


>>> for list in read:
...:     print(chr(list['UDP'].dport),end='')









ûp;ÈúÍÂùHð.Wý	)§nQêè0Èëç­!Ý
                             ÏPÃ>ÏëFcÎ5
ÎÆ7¢1RüqM ÓÚ#Da$(7OÍÇ3À*ÉQóSí
                             êG`
Øê.;l[­@ø.°^ÏÅ
UZ$öIÆ	:Û¿pæ¿lN;Ávôþu*À®BF0<OíºÝÀãìî¥¤
¤ñ	ÝaV;ñFTèÃÎfG{äæ®ÚÛ¡uÜá	]®²nïCD°}{½
³JpL2vú=?«Òk!æ4¶>Q®oê-6øÙÆbLº_0C³¡Îàq|B"â4ÂÕ-R»$h#NA´%YôÑ½(           Lg |û	ø4£·"&6`Uô²/	»ÞjïràÖ?õ@é#¢øg]
ý}~~þpâkPÑÒ2-uF¥NH£ùÒ¶ÓªºB234µeuÂÈ!£T'k@À©£CG	¸HÆ;S´O   ìÔ°ÅWêóÔ©Aÿï  ~FÓôñs­¥¿$Åò»k¢ÁÃ®lÈö

dã?F*û¶øº¿ö%ü¨¥Î8
GEAÚ4×ä-\5ÖøäXÎêÝÌ²)ÁCý¦ö¯ïâ®ûµÆ;ºG¤ÙòÂàÛã­GÊôùa>ªµ	
=ÍPX¯F1%ÙDkKp m3Æ¼Ïÿ=qc'MÌPCTF{53cr3t_c0d3_1n_p0rt5}/­¨7e[ïêcá/áTéQh(áSdùµVÇ ï¹ît¿ç|¬£+BÂ£Èòf#MNÇÆ³ùGºÉr1;
D
"<N!7¦^âqâ¼­ýªÇÒ¼ü$§tüØqÅGÌKí]mPMHcS§ZZ×GUú@À³»ß
                             ùx%º	üTh/ÜdYo¾¸.ÄÉ¡pâ¨6Ð6k¶üNz|¬rÆÇL½ÛÈäñ&6iõí[õÎ(l_	ºrìþ9_¥*CW@xiöH
é¤|h¼ôÌcÊR%nyñÄÕe]?×)	[	y¬º
¹V~C_ðp·
¶P=§t,Y_í]tÅv§Äp@ oUã:
                      Cí¥×Ö$Ãí¯ÕÓf cIp´Lû4M®qæ¸yFìrXî¶aÄÅo×HÖñÙi
                ¿  ª¤DÐa?Âv?ýFÚ0ªødÂH¢/KW*ié>ÿ»ßJoC2            ûÙGÇ!¹PUçg¥8\íÍ^?1c8.ÜwãÁ+	]
Jyø²¤{¸Úì¨	
Qç                        ë¶,	
¼X}ñowQO»TÐÚ»H~¢â(|ÏÈèÅ§Ë_Ò>÷ýÂ((	R
_µ`ü&Xäª´ná9»*
              >à
ÂÎó¨¹Ø&É¬Nwcò\ñ¡&F>>> 



