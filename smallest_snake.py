# OOP - it has a class!
import re;e=' '
k={'?':'\n'+e*8,'|':'if ','&':'import ','B':'def ','S':e*4,
'$':'\n'+e*16,'^':'\n'+e*12,'L':'w.','@':' in ','Y':'u(0,h,l)',
'P':'y,(k,k','O':'()','K':'e.type==','V':'[1]', 'X':'x.','Q':'x.display'}
r=re.compile("|".join(map(re.escape,k.keys())))
exec(r.sub(lambda x:k[x.group(0)],"""
&pygame as x;&sys;from collections &deque as g;from random &randrange as u
b=bool;r=Xdraw.rect;k=255;h=512;l=16;v=[16]*2;
class MO:
SB__init__(w):XinitO;Lz=Xtime.ClockO;Ly=Q.set_mode((h,h));Lp=[0,0];La=[64]*2;Ld={
S275:[l,0],276:[-l,0],274:[l,1],273:[-l,1],1:275};Lc=gO;Ll=0;L_mO
SBm(w):?k = LdV?|k not@Ld:return?Lc.append(Lp[:]);s,d=Ld[k];Lp[d]=(Lp[d]+s)%h
S?|Lp==La:Ll+=1;La=[Y,Y]?|Lp@Lc:Lp,Ll=[0,0],b(Lc.clearO)?|len(Lc)>Ll:Lc.popleftO
SBq(w,e):?k=LdV?|e@Ld and Ld[e]V!=Ld[k]V:LdV=e
SB_m(w):?t=0?while 1:^Ly.fill((0)*3)^for e@Xevent.getO:$|K12:XquitO;sys.exitO$elif K2:Lq(e.key)
S^t+=Lz.tickO/1000.0^|t>.2:t=b(LmO)^r(LP,0),Lp+v);r(LP,k),La+v)^for c@Lc:r(LP,99),c+v)^Q.flipO
MO
"""))
